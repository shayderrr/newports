# define d = Character("Disk")
# define q = Character("Quinn")
# define yi = Character("Yinhui")
# define ya = Character("Yangyi")
# define sp = Character("Spark")
# define tm = Character("Temero NEO")
# define n = Character("Nox Cesso")
# define j = Character("Jex")
# define k = Character("Koa") # owned by blaze1953 on toyhouse
# define m = Character("Mia") # owned by Felow_thetherianYT
# define py = Character("Python")
# define ca = Character("Carmen")
# define ja = Character("Jam")
# define ma = Character("Matte")
# define jac = Character("Jacob")
# define no = Character("Notive")
# define or = Character("Orchid")

label ocmonday:
    stop music
    pause 2.0
    scene mcroom with dissolve
    pause 1.0
    scene black with dissolve
    pause 1.0
    play music "audio/home.mp3" fadein 0.5
    scene mcroom with dissolve
    " Ouhhgg... What time is it? Why'd you have to wake up so early again...? "
    " You sit up from your bed and you look at your phone. "
    " It's 5:30 AM. You then look at your calendar app and - oh right, today's your first day of school... "
    " ...Your first day of school at one of the most prestigious private highschools ever, {b}Everleaf High{/b}. "
    " You don't even know how you managed to get into this school, you're pretty dumb in your opinion. "
    " Might be just out of pure luck. "
    " You have a whole lot of time to get yourself ready for the day, too. Since school starts at 7:30 AM. "
    " Let's get started with taking a bath. You stink. "
    scene black with dissolve
    " After a whole lot of getting ready for school... "
    " ...And a bit of gaming here and there... "
    scene mcroom with dissolve
    " You're finally done with getting yourself ready for school. "
    " It's 6:50 AM, you'd better be going. It's best to be early rather than late. "
    " You get out of your home and you start walking to your school. "
    scene black with dissolve
    stop music fadeout 0.5
    pause 2.0
    play music "audio/paperhigh.mp3" fadein 0.5
    scene paperschoolfront with dissolve
    " You finally arrive at Everleaf High, and now that you think about it... "
    " ...This school looks similar to another school that you've heard of before, but can't quite put a name on it... "
    " Oh well. Fancy schools have low quality rip offs. In this case, Everleaf is the fancy school. "
    " Shouldn't be a big deal at all... "
    " But twitter would make it into a big deal. "
    " Alright, that's enough thinking. You're staring at the school like a weirdo. "
    " Let's go inside... "
    scene black with dissolve
    pause 2.0
    scene hallway with dissolve
    " Wow, it's just as fancy as it looks like on the outside. "
    " Why does this look like the same Paper School you go to in the other route? we didn't want the background artist to suffer more. "
    " Everyone was just chilling doing their own things nearby the lockers, "
    " Looking at their phones, talking to their friends...average school stuff. "
    if persistent.ocplayed == True:
        " You were just walking around until you bumped into someone. (Geez, how many times are you gonna bump into someone in this game?) "
    else:
        " You were just walking around until you bumped into someone. (Geez, this is like, the second time already...) "
    x " Owie...! "
    " The other person landed on the floor, and so you looked down and lended them a hand to help them up. "
    show disksad at center with easeinbottom
    x " That hurt a bit... "
    hide disksad at bottom
    show diskneutral at center
    x " Thank you for helping me up, though! "
    " ...Judging from his looks, he looks like a huge extrovert. How can you tell? I don't know. "
    " Do you wanna keep talking with this guy or are you gonna be an introvert and skedaddle the hell away? "
    menu:
        " Let's keep talking. ":
            x " Actually, I've never seen you here before...are you new? "
            x " I'm gonna assume that you are! Since I haven't seen you here at all until now! "
            x " Wait... am I forgetting something...? "
            hide diskneutral at bottom
            show diskhappy at center
            x " Oh, right! I should introduce myself! It would be rude not to! "
            " ...Wow, he's a real ball of sunshine. "
            hide diskhappy at bottom
            show diskneutral at center
            $ diskknow = True
            d " I'm Disk! Yes, that's really my name, hehe... "
            d " Nice to meet you! Um... "
            " He pauses for you to tell him your name. "
            " You told him that it was nice to meet him aswell and that your name was [name]. "
            d " Ooooohh!! Nice name, [name]! I like the sound of it! "
            d " I'm the guy that throws parties every friday night! That's how I'm so popular in this school! "
            d " I also like to give people gifts because I feel nice and I think that they need them! "
            d " Though, when they open up their present they act all surprised because it's an 'expensive' thing... "
            d " It's only just 2k! It's not that expensive... But, I suppose to them it is... "
            " Wow, rich boy speaking. "
            d " I also have this brother named Quinn! He's in drama club! "
            play sound "audio/bellring.mp3"
            " The bell rang, but Disk didn't stop talking. "
            d " He's got a real knack for acting! Like, he's really really good at it! "
            d " You should go and talk to him sometime!{nw} "
            if kind == True:
                " You cut Disk off and you kindly told him that it was time to go to class. "
            elif calm == True:
                " You cut Disk off and you calmly told him that it was time to go to class. "
            elif mean == True:
                " You cut Disk off rudely and you told him that it was time to go to class. "
            hide diskneutral at bottom
            show disksad at center
            d " Awh, already? I was hoping to get more time to talk to you... "
            hide disksad at bottom
            show diskneutral at center
            d " Well, I'll see you later in class then! "
            d " Bye, [name]! "
            hide diskneutral at right with easeoutright
            scene black with dissolve
            " You then went off to look for your classroom. "
            pause 2.0
            jump ochistory1
        " Nah, I'll go to class early. ":
            hide diskneutral at left with easeoutleft
            " You said a quick 'your welcome' to him before you went off to find your classroom. "
            " Being early is better than being late to class, right? "
            scene black with dissolve
            pause 2.0
            jump ochistory1
    label ochistory1:
        scene classroom with dissolve
        " You entered your classroom that you were assigned to and you see all of your classmates doing basic student stuff. "
        " Some were being chill and being by themselves, whilst others were socializing and having fun. "
        " You then hear the classroom quiet down and everyone getting back to their proper seats... You don't see any teacher coming in though-{nw} "
        " Oh. He's there. He's just really short...about 5'1, you think? "
        " There's no way a teacher can be THAT short. But then again, there's people who are like that, so... "
        " You can't make fun of this teacher otherwise you'll get cancelled by twitter. And everyone else. "
        show mrclioneutral at center with easeinright
        x " Good morning, class. "
        " You hear the class greet him with a nice and cozy good morning. "
        x " As you might have heard, we have a new student. "
        x " Please, [name]. Go up front and introduce yourself to your new classmates. "
        " Well, here goes nothing. "
        " You go up and start introducing yourself... "
        if kind == True:
            menu:
                " Hello everyone, nice to meet you! I'm [name]! ":
                    " What things do you like to do? "
                    menu:
                        " I like to dance! ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that this will be a fun class, and that we will all be friends! ":
                                    jump ocintrodone
                                " I expect for everyone to be kind, and that we will all be nice to eachother! ":
                                    jump ocintrodone
                        " I like to sing! ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that this will be a fun class, and that we will all be friends! ":
                                    jump ocintrodone
                                " I expect for everyone to be kind, and that we will all be nice to eachother! ":
                                    jump ocintrodone
                        " I like to draw! ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that this will be a fun class, and that we will all be friends! ":
                                    jump ocintrodone
                                " I expect for everyone to be kind, and that we will all be nice to eachother! ":
                                    jump ocintrodone
                        " I like to chill around! ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that this will be a fun class, and that we will all be friends! ":
                                    jump ocintrodone
                                " I expect for everyone to be kind, and that we will all be nice to eachother! ":
                                    jump ocintrodone
                " Hi hi!! I'm [name]! ":
                    " What things do you like to do? "
                    menu:
                        " I like to dance! ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that this will be a fun class, and that we will all be friends! ":
                                    jump ocintrodone
                                " I expect for everyone to be kind, and that we will all be nice to eachother! ":
                                    jump ocintrodone
                        " I like to sing! ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that this will be a fun class, and that we will all be friends! ":
                                    jump ocintrodone
                                " I expect for everyone to be kind, and that we will all be nice to eachother! ":
                                    jump ocintrodone
                        " I like to draw! ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that this will be a fun class, and that we will all be friends! ":
                                    jump ocintrodone
                                " I expect for everyone to be kind, and that we will all be nice to eachother! ":
                                    jump ocintrodone
                        " I like to chill around! ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that this will be a fun class, and that we will all be friends! ":
                                    jump ocintrodone
                                " I expect for everyone to be kind, and that we will all be nice to eachother! ":
                                    jump ocintrodone
                " Haiiii! The name's [name]! ":
                    " What things do you like to do? "
                    menu:
                        " I like to dance! ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that this will be a fun class, and that we will all be friends! ":
                                    jump ocintrodone
                                " I expect for everyone to be kind, and that we will all be nice to eachother! ":
                                    jump ocintrodone
                        " I like to sing! ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that this will be a fun class, and that we will all be friends! ":
                                    jump ocintrodone
                                " I expect for everyone to be kind, and that we will all be nice to eachother! ":
                                    jump ocintrodone
                        " I like to draw! ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that this will be a fun class, and that we will all be friends! ":
                                    jump ocintrodone
                                " I expect for everyone to be kind, and that we will all be nice to eachother! ":
                                    jump ocintrodone
                        " I like to dance, sing, draw, and chill around! ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that this will be a fun class, and that we will all be friends! ":
                                    jump ocintrodone
                                " I expect for everyone to be kind, and that we will all be nice to eachother! ":
                                    jump ocintrodone
                        " I like to chill around! ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that this will be a fun class, and that we will all be friends! ":
                                    jump ocintrodone
                                " I expect for everyone to be kind, and that we will all be nice to eachother! ":
                                    jump ocintrodone
        elif calm == True:
            menu:
                " Sup everyone, I'm [name]. ":
                    " What are the things you like to do? "
                    menu:
                        " I like to draw. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
                        " I like to sing. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
                        " I like to dance. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
                        " I like to be a chill guy. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
                        " I like to dance, sing, draw, and be a chill guy. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
                " Suhhh y'all, the name's [name]. ":
                    " What are the things you like to do? "
                    menu:
                        " I like to draw. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
                        " I like to sing. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
                        " I like to dance. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
                        " I like to be a chill guy. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
                        " I like to dance, sing, draw, and be a chill guy. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
                " Suppp guys gals and everyone else, I'm [name]. ":
                    " What are the things you like to do? "
                    menu:
                        " I like to draw. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
                        " I like to sing. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
                        " I like to dance. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
                        " I like to be a chill guy. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
                        " I like to dance, sing, draw, and be a chill guy. ":
                            " What are your expectations for this class? "
                            menu:
                                " I expect that everyone will be chill and that we can all be homies. ":
                                    jump ocintrodone
                                " I expect that everyone will be all friendly and that we can all chillax together. ":
                                    jump ocintrodone
        elif mean == True:
            menu:
                " Hi. I'm [name]. ":
                    " What are the things that you like to do? "
                    menu:
                        " I like to draw sometimes. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
                        " I like to sing sometimes. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
                        " I like to dance sometimes. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
                        " I like to do all of the above sometimes. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
                        " I'm not good at anything. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
                " ...I'm [name]. ":
                    " What are the things that you like to do? "
                    menu:
                        " I like to draw sometimes. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
                        " I like to sing sometimes. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
                        " I like to dance sometimes. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
                        " I like to do all of the above sometimes. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
                        " I'm not good at anything. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
                " My name is [name]. ":
                    " What are the things that you like to do? "
                    menu:
                        " I like to draw sometimes. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
                        " I like to sing sometimes. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
                        " I like to dance sometimes. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
                        " I like to do all of the above sometimes. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
                        " I'm not good at anything. ":
                            " What are your expectations for this class? "
                            menu:
                                " I don't know. ":
                                    jump ocintrodone
                                " I guess I expect to be friends with everyone here. ":
                                    jump ocintrodone
        label ocintrodone:
            " You then finished introducing yourself and waited for the teachers next instruction. "
            if kind == True:
                " Almost everyone seemed to like your introduction, and looks like they're starting to like your positivity! "
            elif calm == True:
                " Everyone liked how relaxed you were, and were starting to like you! "
            elif mean == True:
                " You could tell that everyone thought you were scary, but you could see some who thought that you could change. "
            x " Thank you for introducing yourself, [name]. "
            mscl " I am Mister Clio, your history teacher. "
            mscl " I'm pretty sure that the principal already gave you the schedule, so... "
            mscl " You can now pick who to sit with. Feel free to sit with anyone, I don't mind. "
            hide mrclioneutral at left with easeoutleft
            " You nod, and then look at your options infront of you. "
            " Who do you want to sit with? (Who you sit with can't be changed in the future.) "
            if diskknow == True:
                menu:
                    " Disk, a guy with a mask, and a girl that's drawing. ":
                        $ diqutte = True
                        jump diqutte
                    " A guy with antennas, a girl with a butterfly bow, and a sleepy guy. ":
                        $ spatemnox = True
                        jump spatemnox
                    " A girl that looks mean, A scene kid, and a kid with a guitar. ":
                        $ jamorcar = True
                        jump jamorcar
                    " An emo looking kid, a girl with a flower on her head, and a tall guy. ":
                        $ koamiajex = True
                        jump koamiajex
                    " A guy with goggles, a chill nonbinary person, and two kids that look like twins. ":
                        $ jacnotyinyang = True
                        jump jacnotyinyang
                    " I'll sit alone. ":
                        $ alone = True
                        jump ocalone
            else:
                menu:
                    " A extroverted guy, a guy with a mask, and a girl that's drawing. ":
                        $ diqutte = True
                        jump diqutte
                    " A guy with antennas, a girl with a butterfly bow, and a sleepy guy. ":
                        $ spatemnox = True
                        jump spatemnox
                    " A girl that looks mean, A scene kid, and a kid with a guitar. ":
                        $ jamorcar = True
                        jump jamorcar
                    " An emo looking kid, a girl with a flower on her head, and a tall guy. ":
                        $ koamiajex = True
                        jump koamiajex
                    " A guy with goggles, a chill nonbinary person, and two kids that look like twins. ":
                        $ jacnotyinyang = True
                        jump jacnotyinyang
                    " I'll sit alone. ":
                        $ alone = True
                        jump ocalone
            label diqutte:
                " You decided who to sit with, and grabbed a chair in the corner before you sat next to them. "
                show diskneutral at right with easeinleft
                show quinnneutral at center with easeinleft
                show matteneutral at left with easeinleft
                if diskknow == True:
                    d " And then I said: No way! and then she said-{nw} "
                    d " [name]!! Hi!! "
                    x " ...She said the new kid's name? "
                    d " No, no! I'm just greeting my new good friend! "
                    x " They're your friend already, Disk? Hmhm, growing more and more popular day by day... "
                    d " What, you jealous? "
                    " The other girl didn't speak and continued to draw in her sketchbook. "
                    hide quinnneutral at bottom
                    show quinnhappy at center
                    x " Heh, I'd never get jealous of you, brother. We're equally popular. "
                    hide diskneutral at bottom
                    show diskjoyous at right
                    d " Right you are, dear brother! "
                    hide diskjoyous at bottom
                    show diskneutral at right
                    hide quinnhappy at bottom
                    show quinnneutral at center
                    d " Anywho! I'd like to introduce my friends to you, [name]! "
                    $ quinnknow = True
                    $ matteknow = True
                    d " The guy I was talking to, is Quinn! This is my younger brother, the one I talked about! "
                    q " You told them about me, huh? "
                    d " How could I not? You're literally the coolest brother that I could ever have! "
                    q " Awh, you're sweet, Disk. "
                    d " I know, hehe! "
                    d " Anywho... that girl drawing over there? Her name is Matte! "
                    ma " Oh, huh? Sorry, I was busy drawing. "
                    ma " But yeah, it's me. Matte. I'm Disk's cousin. "
                    d " My super cool cousin! "
                    hide matteneutral at bottom
                    show mattehappy at left
                    ma " You sure do love calling people cool, Disk. "
                    d " It's true though! All of you are cool! I think everyone is cool! "
                    q " Even the bad people, Disk? "
                    d " ...They're uncool. "
                    ma " That's good. "
                    hide mattehappy at bottom
                    show matteneutral at left
                    mscl " Alright, that's enough talking. Let's get started with our lecture for today... "
                    " Time to pay attention. Or not. Who cares? "
                    " What do you do? "
                    menu:
                        " Actually pay attention to class ":
                            " Nerd. "
                            scene black with dissolve
                            " You paid attention to the lesson the history teacher was teaching to you all. "
                            " It was pretty boring, but atleast you had something to put in your notes. "
                            if persistent.ocroute == True:
                                " While listening to class, you heard some strange noises coming from the ceiling... "
                                " ...More like coming from the vents. "
                                " You thought that it was nothing though, and continued to write down notes. "
                                pause 2.0
                                play sound "audio/bellring.mp3"
                                " The bell ends, meaning that class has ended. "
                                " You put all of your stuff in your bag and you headed out into the hallways. "
                                pause 2.0
                                jump ocbreak1
                            else:
                                pause 2.0
                                play sound "audio/bellring.mp3"
                                " The bell ends, meaning that class has ended. "
                                " You put all of your stuff in your bag and you headed out into the hallways. "
                                pause 2.0
                                jump ocbreak1
                        " Don't pay attention in class, and talk with your seatmates. ":
                            " Just like me fr! "
                            scene black with dissolve
                            " You talked with your seatmates throughout the class. "
                            " Though they were actually trying to learn, you managed to get their attention. "
                            " ...Sometimes. "
                            " But you caught Disk talking to you a lot though. "
                            " You eventually got a bit scolded by Mister Clio and started paying attention. "
                            " Boring. "
                            play sound "audio/bellring.mp3"
                            " The bell ends, meaning that class has ended. "
                            " You put all of your stuff in your bag and you headed out into the hallways. "
                            pause 2.0
                            jump ocbreak1
                else:
                    x " And then I said: No way! and then she said-{nw} "
                    x " [name]!! Hi!! "
                    x " ...She said the new kid's name? "
                    x " No, no! I'm just greeting our new friend! "
                    x " They're your friend already, Disk? Hmhm, growing more and more popular day by day... "
                    x " What, you jealous? "
                    " The other girl didn't speak and continued to draw in her sketchbook. "
                    hide quinnneutral at bottom
                    show quinnhappy at center
                    x " Heh, I'd never get jealous of you, brother. We're equally popular. "
                    hide diskneutral at bottom
                    show diskjoyous at right
                    d " Right you are, dear brother! "
                    hide diskjoyous at bottom
                    show diskneutral at right
                    hide quinnhappy at bottom
                    show quinnneutral at center
                    x " Anywho! I'd like to introduce myself and my friends to you, [name]! "
                    $ diskknow = True
                    $ quinnknow = True
                    $ matteknow = True
                    d " I'm Disk! I'm kinda popular here, as my brother said, heh... "
                    d " The guy I was talking to, is Quinn! This is my younger brother! "
                    q " You told them about me, huh? "
                    d " How could I not? You're literally the coolest brother that I could ever have! "
                    q " Awh, you're sweet, Disk. "
                    d " I know, hehe! "
                    d " Anywho... that girl drawing over there? Her name is Matte! "
                    ma " Oh, huh? Sorry, I was busy drawing. "
                    ma " But yeah, it's me. Matte. I'm Disk's cousin. "
                    d " My super cool cousin! "
                    hide matteneutral at bottom
                    show mattehappy at left
                    ma " You sure do love calling people cool, Disk. "
                    d " It's true though! All of you are cool! I think everyone is cool! "
                    q " Even the bad people, Disk? "
                    d " ...They're uncool. "
                    ma " That's good. "
                    hide mattehappy at bottom
                    show matteneutral at left
                    mscl " Alright, that's enough talking. Let's get started with our lecture for today... "
                    " Time to pay attention. Or not. Who cares? "
                    " What do you do? "
                    menu:
                        " Actually pay attention to class ":
                            " Nerd. "
                            scene black with dissolve
                            " You paid attention to the lesson the history teacher was teaching to you all. "
                            " It was pretty boring, but atleast you had something to put in your notes. "
                            if persistent.ocroute == True:
                                " While listening to class, you heard some strange noises coming from the ceiling... "
                                " ...More like coming from the vents. "
                                " You thought that it was nothing though, and continued to write down notes. "
                                pause 2.0
                                play sound "audio/bellring.mp3"
                                " The bell ends, meaning that class has ended. "
                                " You put all of your stuff in your bag and you headed out into the hallways. "
                                pause 2.0
                                jump ocbreak1
                            else:
                                pause 2.0
                                play sound "audio/bellring.mp3"
                                " The bell ends, meaning that class has ended. "
                                " You put all of your stuff in your bag and you headed out into the hallways. "
                                pause 2.0
                                jump ocbreak1
                        " Don't pay attention in class, and talk with your seatmates. ":
                            " Just like me fr! "
                            scene black with dissolve
                            " You talked with your seatmates throughout the class. "
                            " Though they were actually trying to learn, you managed to get their attention. "
                            " ...Sometimes. "
                            " But you caught Disk talking to you a lot though. "
                            " You eventually got a bit scolded by Mister Clio and started paying attention. "
                            " Boring. "
                            play sound "audio/bellring.mp3"
                            " The bell ends, meaning that class has ended. "
                            " You put all of your stuff in your bag and you headed out into the hallways. "
                            pause 2.0
                            jump ocbreak1
            label spatemnox:
                show sparkneutral at left with easeinright
                show noxsleepy at center with easeinright
                show temeroneutral at right with easeinright
                x " Remember that time we had to stop by to a different school because of {i}the incident{/i}? "
                x " Yep. I remember very clearly. "
                x " ...h...so sleepy... "
                hide temeroneutral at bottom
                show temerohappy at right
                x " Well, I saw this really cute girl! She was so hot! "
                x " And I know what you're gonna say, Spark, 'the guy with her was better'! "
                hide sparkneutral at bottom
                show sparkshit at left
                x " Hey, don't call me out like that... "
                x " HAH, gayass. "
                x " Don't call me out while the new guy is here. "
                hide temerohappy at bottom
                show temeroneutral at right
                x " Oh shit, the new kid's sitting with us? for real? "
                hide sparkshit at bottom
                show sparkneutral at left
                x " Yeah. You didn't notice them? Blind ass. "
                x " Oh come on. We gotta put a good impression on the newbie! "
                x " Yeah, yeah...Whatever. "
                x " zzzz... "
                x " Hey, new kid! You're [name], right? "
                $ temeroknow = True
                $ sparkknow = True
                $ noxknow = True
                tm " Nice name there. I'm Temero Neo! You can call me Temero, Neo, whatever you'd like. "
                sp " I'm Spark. Sleepy guy over there is Nox. He's normally like that. "
                n " Spark, when do we get to go home...? "
                sp " We go home at 5:45 pm, but if you have clubs then you'll go home at 6 pm. "
                n " That's so long... "
                sp " You can sleep, don't worry. Mister Clio lets you sleep in his class, but not too much. "
                n " Oh, that's right... "
                " Nox then went straight to sleeping after Spark said that. "
                sp " ...You know, he's sometimes adorable. "
                hide temeroneutral at bottom
                show temerohappy at right
                tm " Thought you said the guy form that other school was better. "
                hide sparkneutral at bottom
                show sparkshit at left
                sp " Hey, that guy's still my number 1. His name is Edward. "
                sp " Did I ever mention that I like Nox better than Edward? No. I only said that he's cute. "
                sp " Plus, I see Nox as a younger brother. "
                hide temerohappy at bottom
                show temeroneutral at right
                tm " ...Yeah, alright. Fine. "
                mscl " Alright, that's enough talking. Let's get started with our lecture for today... "
                " Time to pay attention. Or not. Who cares? "
                " What do you do? "
                menu:
                    " Actually pay attention to class ":
                        " Nerd. "
                        scene black with dissolve
                        " You paid attention to the lesson the history teacher was teaching to you all. "
                        " It was pretty boring, but atleast you had something to put in your notes. "
                        if persistent.ocroute == True:
                            " While listening to class, you heard some strange noises coming from the ceiling... "
                            " ...More like coming from the vents. "
                            " You thought that it was nothing though, and continued to write down notes. "
                            pause 2.0
                            play sound "audio/bellring.mp3"
                            " The bell ends, meaning that class has ended. "
                            " You put all of your stuff in your bag and you headed out into the hallways. "
                            pause 2.0
                            jump ocbreak1
                        else:
                            pause 2.0
                            play sound "audio/bellring.mp3"
                            " The bell ends, meaning that class has ended. "
                            " You put all of your stuff in your bag and you headed out into the hallways. "
                            pause 2.0
                            jump ocbreak1
                    " Don't pay attention in class, and talk with your seatmates. ":
                        " Just like me fr! "
                        scene black with dissolve
                        " You talked with your seatmates throughout the class. "
                        " Spark and Temero actually talked a lot with you, while they had Nox sleeping. "
                        " You eventually got a bit scolded by Mister Clio and started paying attention. "
                        " Boring. "
                        play sound "audio/bellring.mp3"
                        " The bell ends, meaning that class has ended. "
                        " You put all of your stuff in your bag and you headed out into the hallways. "
                        pause 2.0
                        jump ocbreak1
            label jamorcar:
                show jamneutral at right with easeinleft
                show orchidneutral at center with easeinleft
                show carmenneutral at left with easeinleft
                x " You know, I really like your guitar skills, Carmen! "
                x " ...!! "
                x " I think it's a bit annoying. "
                x " You think everything's annoying, Jam... "
                x " So? It's just my opinion. I'd rather have peace and quiet while gaming rather than having guitar noises in the background. "
                " And you just noticed that she was playing with her expensive looking phone. "
                " Damn. There's a lot of rich kids in this school. Yuo're not used to this. "
                hide orchidneutral at bottom
                show orchidangry at center
                x " Jam, you should act more nicer since the new kid's sitting with us. "
                x " ...[name] is sitting with us? "
                x " ... "
                x " ...Ergh...alright, fine. "
                hide orchidangry at bottom
                show orchidneutral at center
                x " That's much better. "
                x " Anywho, um... Let's introduce ourselves to them! "
                hide carmenneutral at bottom
                show carmenconfused at left
                x " ??? "
                x " Don't worry, I'll speak for you, Carmen. "
                hide carmenconfused at bottom
                show carmenneutral at left
                $ orchidknow = True
                $ carmenknow = True
                $ jamknow = True
                oc " I'm Orchid! I don't have a gender, so... you can call me by any pronouns! "
                oc " He/him or They/them is preferred, though. I'm also filipino! "
                " Orchid looks over to Jam, waiting for her to introduce herself to you. "
                x " ...Sigh. "
                ja " I'm Jam. I guess...I like to game a lot. That's pretty much it. "
                oc " And the guy with a guitar over there is Carmen! He's mute. "
                oc " He sometimes likes to speak with his guitar somehow, and he does know sign language! He mostly likes to use his guitar, though. "
                hide carmenneutral at bottom
                show carmenhappy at left
                ca " !!! "
                oc " We are all happy to meet you, [name]!!! "
                ja " Yeah, whatever. "
                hide carmenhappy at bottom
                show carmenneutral at left
                mscl " Alright, that's enough talking. Let's get started with our lecture for today... "
                " Time to pay attention. Or not. Who cares? "
                " What do you do? "
                menu:
                    " Actually pay attention to class ":
                        " Nerd. "
                        scene black with dissolve
                        " You paid attention to the lesson the history teacher was teaching to you all. "
                        " It was pretty boring, but atleast you had something to put in your notes. "
                        if persistent.ocroute == True:
                            " While listening to class, you heard some strange noises coming from the ceiling... "
                            " ...More like coming from the vents. "
                            " You thought that it was nothing though, and continued to write down notes. "
                            pause 2.0
                            play sound "audio/bellring.mp3"
                            " The bell ends, meaning that class has ended. "
                            " You put all of your stuff in your bag and you headed out into the hallways. "
                            pause 2.0
                            jump ocbreak1
                        else:
                            pause 2.0
                            play sound "audio/bellring.mp3"
                            " The bell ends, meaning that class has ended. "
                            " You put all of your stuff in your bag and you headed out into the hallways. "
                            pause 2.0
                            jump ocbreak1
                    " Don't pay attention in class, and talk with your seatmates. ":
                        " Just like me fr! "
                        scene black with dissolve
                        " You talked with your seatmates throughout the class. "
                        " Carmen was the one talking to you for the most part, but with sign language. "
                        " You were lucky enough that you knew sign language. Those lessons paid off. "
                        " You eventually got a bit scolded by Mister Clio and started paying attention. "
                        " Boring. "
                        play sound "audio/bellring.mp3"
                        " The bell ends, meaning that class has ended. "
                        " You put all of your stuff in your bag and you headed out into the hallways. "
                        pause 2.0
                        jump ocbreak1
            label koamiajex:
                show koaneutral at left with easeinright
                show jexneutral at center with easeinright
                show mianeutral at right with easeoutright
                x " Hehe... Jex, do you think I should plant some more flowers in the school? "
                x " Well, I'm sure that Miss Wisteria is going to love those. So, yes. You should. "
                x " Yahoo! "
                x " You really do like to plant things, do you, Mia? "
                x " Yep! "
                " The other guy with an eyepatch seems to be just reading a book and not paying attention to the conversation. "
                x " Oooh, lookie! It's the new kid! "
                " The attention is now shifted to you,even the guy who was reading started looking at you. "
                x " We should all introduce ourselves! "
                x " Indeed we should, Mia. "
                x " ... "
                $ jexknow = True
                $ miaknow = True
                $ koaknow = True
                hide mianeutral at bottom
                show miahappy at right
                m " I'm Mia! I like to plant things around the school, like flowers! "
                j " I'm Jex. I just like to chill around, I suppose. "
                " The other two looked at the guy with the eyepatch to see if he would introduce himself. "
                hide miahappy at bottom
                show mianeutral at right
                k " ...I'm Koa. It's nice to meet you. "
                m " Wow, you finally spoke! And here I thought you were a case like Carmen over there! "
                k " ... "
                mscl " Alright, that's enough talking. Let's get started with our lecture for today... "
                " Time to pay attention. Or not. Who cares? "
                " What do you do? "
                menu:
                    " Actually pay attention to class ":
                        " Nerd. "
                        scene black with dissolve
                        " You paid attention to the lesson the history teacher was teaching to you all. "
                        " It was pretty boring, but atleast you had something to put in your notes. "
                        if persistent.ocroute == True:
                            " While listening to class, you heard some strange noises coming from the ceiling... "
                            " ...More like coming from the vents. "
                            " You thought that it was nothing though, and continued to write down notes. "
                            pause 2.0
                            play sound "audio/bellring.mp3"
                            " The bell ends, meaning that class has ended. "
                            " You put all of your stuff in your bag and you headed out into the hallways. "
                            pause 2.0
                            jump ocbreak1
                        else:
                            pause 2.0
                            play sound "audio/bellring.mp3"
                            " The bell ends, meaning that class has ended. "
                            " You put all of your stuff in your bag and you headed out into the hallways. "
                            pause 2.0
                            jump ocbreak1
                    " Don't pay attention in class, and talk with your seatmates. ":
                        " Just like me fr! "
                        scene black with dissolve
                        " You talked with your seatmates throughout the class. "
                        " Mia was talking to you the most, but she was mostly just talking about her favorite plants. To which you didn't mind. "
                        " You eventually got a bit scolded by Mister Clio and started paying attention. "
                        " Boring. "
                        play sound "audio/bellring.mp3"
                        " The bell ends, meaning that class has ended. "
                        " You put all of your stuff in your bag and you headed out into the hallways. "
                        pause 2.0
                        jump ocbreak1
            label jacnotyinyang:
                show jacobneutral at right with easeinleft
                show notiveneutral at center with easeinleft
                show yangyineutral at left with easeinleft
                x " ... "
                x " ... "
                x " ... "
                hide yangyineutral at left with easeoutleft
                show yinhuineutral at left with easeinleft
                x " ... "
                " Jesus, this group is quiet. "
                " You could almost hear those crickets that would make noise in cartoons whenever it's really quiet and awkward. "
                hide yinhuineutral at left with easeoutleft
                show yangyineutral at left with easeinleft
                x " So... "
                x " How about we introduce ourselves to the new guy over there? "
                x " It would be rude not to, don't you guys think? "
                x " ...I suppose it would. "
                $ yinhuiknow = True
                $ yangyiknow = True
                $ jacobknow = True
                $ notiveknow = True
                hide yangyineutral at bottom
                show yangyihappy at left
                ya " I'll start! I'm Yangyi, it's nice to meet you! "
                no " Then I'll go next. I'm Notive. "
                x " ... "
                no " The guy next to me is Jacob. He's just like that, wanna be bad boy ish... "
                hide yangyihappy at bottom
                show yangyineutral at left
                ya " ... "
                " Yangyi turns to look at who you would assume to be his brother, as if asking him to introduce himself. "
                " The other guy seems very distrustful of you, but he decided to do it for his brother. "
                hide yangyineutral at left with easeoutleft
                show yinhuineutral at left with easeinleft
                yi " ...I'm Yinhui. I'm Yangyi's brother. "
                " Pretty simple, but it does the job. "
                " Yangyi seems happy that he got his brother to introduce himself to you. "
                " Yinhui just gives you a nasty look as if saying 'dont touch my brother' but it quickly faded away when the teacher spoke up. "
                hide yinhuineutral at left with easeoutleft
                show yangyineutral at left with easeinleft
                mscl " Alright, that's enough talking. Let's get started with our lecture for today... "
                " Time to pay attention. Or not. Who cares? "
                " What do you do? "
                menu:
                    " Actually pay attention to class ":
                        " Nerd. "
                        scene black with dissolve
                        " You paid attention to the lesson the history teacher was teaching to you all. "
                        " It was pretty boring, but atleast you had something to put in your notes. "
                        if persistent.ocroute == True:
                            " While listening to class, you heard some strange noises coming from the ceiling... "
                            " ...More like coming from the vents. "
                            " You thought that it was nothing though, and continued to write down notes. "
                            pause 2.0
                            play sound "audio/bellring.mp3"
                            " The bell ends, meaning that class has ended. "
                            " You put all of your stuff in your bag and you headed out into the hallways. "
                            pause 2.0
                            jump ocbreak1
                        else:
                            pause 2.0
                            play sound "audio/bellring.mp3"
                            " The bell ends, meaning that class has ended. "
                            " You put all of your stuff in your bag and you headed out into the hallways. "
                            pause 2.0
                            jump ocbreak1
                    " Don't pay attention in class, and talk with your seatmates. ":
                        " Just like me fr! "
                        scene black with dissolve
                        " You talked with your seatmates throughout the class. "
                        " Yangyi was talking to you the most though, since he was the only extroverted one there. "
                        " You eventually got a bit scolded by his brother and got told off to pay attention to class. "
                        " Boring. "
                        play sound "audio/bellring.mp3"
                        " The bell ends, meaning that class has ended. "
                        " You put all of your stuff in your bag and you headed out into the hallways. "
                        pause 2.0
                        jump ocbreak1
            label ocalone:
                " You sat alone, and saw all the other students having fun. "
                mscl " Alright, that's enough talking. Let's get started with our lecture for today... "
                " Time to pay attention. Or not. Who cares? "
                " What do you do? "
                menu:
                    " Actually pay attention to class ":
                        " Nerd. "
                        scene black with dissolve
                        " You paid attention to the lesson the history teacher was teaching to you all. "
                        " It was pretty boring, but atleast you had something to put in your notes. "
                        if persistent.ocroute == True:
                            " While listening to class, you heard some strange noises coming from the ceiling... "
                            " ...More like coming from the vents. "
                            " You thought that it was nothing though, and continued to write down notes. "
                            pause 2.0
                            play sound "audio/bellring.mp3"
                            " The bell ends, meaning that class has ended. "
                            " You put all of your stuff in your bag and you headed out into the hallways. "
                            pause 2.0
                            jump ocbreak1
                        else:
                            pause 2.0
                            play sound "audio/bellring.mp3"
                            " The bell ends, meaning that class has ended. "
                            " You put all of your stuff in your bag and you headed out into the hallways. "
                            pause 2.0
                            jump ocbreak1
                    " Don't pay attention in class and draw ":
                        " Just like me fr! "
                        scene black with dissolve
                        " Since you had no seatmates, you could only draw to cure your boredom. "
                        " You eventually got told by the teacher to pay attention, and you did. "
                        " Boring. "
                        play sound "audio/bellring.mp3"
                        " The bell ends, meaning that class has ended. "
                        " You put all of your stuff in your bag and you headed out into the hallways. "
                        pause 2.0
                        jump ocbreak1
    label ocbreak1:
        scene hallway with dissolve
        " It's the first break of the day. Where do you want to go? "
        if persistent.ocplayed == True:
            " Just as you were deciding on where to go, a little card flew right into your face. "
            " It read... "
            " 'If you manage to find me, I'll give you a sweet reward. If you're interested, look at the back of the card.' "
            " There's no name written on it, so you don't know who this is. "
            " Do you take the challenge though? "
            menu:
                " Yeah it would be fun ":
                    $ pythonchallenge = True
                    " Alright. You checked the back of the card to see the hint. "
                    " 'Finding me is no easy task, for you have to look around the entire school for clues.' "
                    " 'But all you have to do for me is to find 3 numbers hidden around this area.' "
                    " 'I'll give you a hint on where the first one is...' "
                    " 'Where echoes bounce and footsteps race, victory shines in this wide-open place.' "
                    " 'On jerseys worn or banners high, Find the digit where champions fly.' "
                    " It was a little confusing, but you think you have an idea on where the first number is. "
                    " (Quick thing here, but there will be an indicator if you found the code or not.) "
                    " (Of course you can cheat a little bit and press the back button to check other spaces.) "
                    " (If you find this number, then you'll have to wait for the next day for the next code.) "
                    " Where do you go to look? "
                    menu:
                        " {image=diskicon} The front of the school {image=diskicon} ":
                            jump ocfrontschool1
                        " {image=jamicon} The back of the school {image=jamicon} ":
                            jump ocbackschool1
                        " {image=yinyangicon} The gym {image=yinyangicon} ":
                            jump ocgym1
                        " The cafeteria ":
                            jump occafe1
                        " {image=quinnicon} The rooftop {image=matteicon} ":
                            jump ocroof1
                        " {image=noxicon} The library {image=noxicon} ":
                            jump oclibrary1
                " No thanks ":
                    $ pythonchallenge = False
                    " Alright. Where do you want to hang out for the break instead? "
                    menu:
                        " {image=diskicon} The front of the school {image=diskicon} ":
                            jump ocfrontschool1
                        " {image=jamicon} The back of the school {image=jamicon} ":
                            jump ocbackschool1
                        " {image=yinyangicon} The gym {image=yinyangicon} ":
                            jump ocgym1
                        " The cafeteria ":
                            jump occafe1
                        " {image=quinnicon} The rooftop {image=matteicon} ":
                            jump ocroof1
                        " {image=noxicon} The library {image=noxicon} ":
                            jump oclibrary1
        else:
            menu:
                " {image=diskicon} The front of the school {image=diskicon} ":
                    jump ocfrontschool1
                " {image=jamicon} The back of the school {image=jamicon} ":
                    jump ocbackschool1
                " {image=yinyangicon} The gym {image=yinyangicon} ":
                    jump ocgym1
                " The cafeteria ":
                    jump occafe1
                " {image=quinnicon} The rooftop {image=matteicon} ":
                    jump ocroof1
                " {image=noxicon} The library {image=noxicon} ":
                    jump oclibrary1
        label ocfrontschool1:
            scene black with dissolve
            pause 2.0
            scene paperschoolfront with dissolve
            # disk
            " You walked outside the paper school, taking in the fresh air. "
            " Everything seems a bit more calmer when you're out of the school. Like when you're at home and you just wanna nap. "
            " You looked around and spotted a fellow classmate of yours just chilling around... "
            " Approach him? "
            menu:
                " Yeah sure ":
                    " You walked up to him and saw that he was sitting on the ground, doodling something. "
                    show diskneutral at center with easeinbottom
                    " You sat down next to him and tried to talk with him. "
                    if diskknow == True:
                        d " Hmmm...hm... "
                        " You tapped his shoulder to get his attention. "
                        hide diskneutral at bottom
                        show diskhappy at center
                        d " Huh? Oh, [name]!! Hiiiii!! It's so nice to see you!! "
                        hide diskhappy at bottom
                        show diskneutral at center
                        d " I'm just doodling a little something, heheh... "
                        d " My art skills aren't that good, so please don't judge me! "
                        " Disk then showed you what he was drawing and his drawing skills aren't that bad actually. "
                        " It looked pretty good in your opinion. "
                        " It was a drawing of him and his little puppy named Matcha. "
                        d " That's the puppy I have! Her name is Matcha! "
                        d " I have another one called Bacon, she likes to hang around with Matcha a lot! "
                        " ...You feel as if that was a reference to something {a=https://www.roblox.com/games/9342644342/Flavor-Frenzy-Tower-Defense}flavorful{/a}, but you can't put a finger on what he's referencing to. "
                        d " Hehe, they're the cutest... "
                        d " Oh, right! I'm having another party this friday after school, do you wanna come with? "
                        " Come to Disk's party? "
                        menu:
                            " Yeah sure ":
                                $ diskparty = True
                                hide diskneutral at bottom
                                show diskjoyous at center
                                d " Yayay!! I'm glad that you're going! "
                                hide diskjoyous at bottom
                                show diskneutral at center
                                d " You're gonna have so much fun, trust me! We're gonna have all sorts of games and stuff! "
                                d " Oh, and also, we're gonna have... "
                                scene black with dissolve
                                " You spent the rest of the break talking to Disk about what's gonna happen in the party. "
                                " It honestly got you a little excited, even thuogh friday is just a bit away. "
                                play sound "audio/bellring.mp3"
                                " The bell eventually rang, and you both get up to go to the next class. "
                                pause 2.0
                                jump ochealthclass1
                            " No thanks, I'm busy ":
                                $ diskparty = False
                                hide diskneutral at bottom
                                show disksad at center
                                d " Awh, sad that you can't go... "
                                hide disksad at bottom
                                show diskneutral at center
                                d " But! I can talk to you about the party if you want me to! "
                                scene black with dissolve
                                " You spent the rest of the break talking to Disk about what's gonna happen in the party. "
                                " You thought it was cool despite the fact that you're not even going. "
                                play sound "audio/bellring.mp3"
                                " The bell eventually rang, and you both get up to go to the next class. "
                                pause 2.0
                                jump ochealthclass1
                    else:
                        x " Hmmm...hm... "
                        " You tapped his shoulder to get his attention. "
                        hide diskneutral at bottom
                        show diskhappy at center
                        x " Huh? Oh, [name]!! Hiiiii!! It's so nice to see you!! "
                        hide diskhappy at bottom
                        show diskneutral at center
                        x " Waitwait, I don't think I got myself to be able to introduce myself to you! "
                        $ diskknow = True
                        d " I'm Disk! I'm sort of popular here...heheh... "
                        d " I'm just doodling a little something, heheh... "
                        d " My art skills aren't that good, so please don't judge me! "
                        " Disk then showed you what he was drawing and his drawing skills aren't that bad actually. "
                        " It looked pretty good in your opinion. "
                        " It was a drawing of him and his little puppy named Matcha. "
                        d " That's the puppy I have! Her name is Matcha! "
                        d " I have another one called Bacon, she likes to hang around with Matcha a lot! "
                        " ...You feel as if that was a reference to something {a=https://www.roblox.com/games/9342644342/Flavor-Frenzy-Tower-Defense}flavorful{/a}, but you can't put a finger on what he's referencing to. "
                        d " Hehe, they're the cutest... "
                        d " Oh, right! I'm having another party this friday after school, do you wanna come with? "
                        " Come to Disk's party? "
                        menu:
                            " Yeah sure ":
                                $ diskparty = True
                                hide diskneutral at bottom
                                show diskjoyous at center
                                d " Yayay!! I'm glad that you're going! "
                                hide diskjoyous at bottom
                                show diskneutral at center
                                d " You're gonna have so much fun, trust me! We're gonna have all sorts of games and stuff! "
                                d " Oh, and also, we're gonna have... "
                                scene black with dissolve
                                " You spent the rest of the break talking to Disk about what's gonna happen in the party. "
                                " It honestly got you a little excited, even thuogh friday is just a bit away. "
                                play sound "audio/bellring.mp3"
                                " The bell eventually rang, and you both get up to go to the next class. "
                                pause 2.0
                                jump ochealthclass1
                            " No thanks, I'm busy ":
                                $ diskparty = False
                                hide diskneutral at bottom
                                show disksad at center
                                d " Awh, sad that you can't go... "
                                hide disksad at bottom
                                show diskneutral at center
                                d " But! I can talk to you about the party if you want me to! "
                                scene black with dissolve
                                " You spent the rest of the break talking to Disk about what's gonna happen in the party. "
                                " You thought it was cool despite the fact that you're not even going. "
                                play sound "audio/bellring.mp3"
                                " The bell eventually rang, and you both get up to go to the next class. "
                                pause 2.0
                                jump ochealthclass1
                " No, I don't want to disturb him. ":
                    " You decided not to talk to him and you just sat on a nearby bench. "
                    " You looked at the clouds, the scenery, and your phone to pass the time. "
                    " It's nothing interesting, but atlest you had something to do. And this is a nice break from hearing your classmates yelling. "
                    " You just sort of chillaxed there. Like a chill guy. "
                    scene black with dissolve
                    " You chillaxed outside the school for the rest of the break. "
                    " Your chillness increased by 5 points, which is pretty cool. "
                    " You wanna know what's not chill though? "
                    play sound "audio/bellring.mp3"
                    " The bell ringing. It's time to go to class already. You've chilled too much. "
                    " But you honestly didn't care. You got up and walked back into your classroom. "
                    pause 2.0
                    jump ochealthclass1
        label ocbackschool1:
            # jam
            scene black with dissolve
            pause 2.0
            scene paperschoolback with dissolve
            " You walked to the back of the school, taking in the fresh air. "
            " You walked for a bit and spotted one of your fellow classmates playing a game on her phone. "
            " Sit next to her? "
            menu:
                " Yeah sure ":
                    " You sat down next to her and looked at the game she was playing. "
                    show jamgame at center with easeinbottom
                    if jamknow == True:
                        ja " ... "
                        " She seems pretty concentrated. Even though she's just playing bird crossing. "
                        " Bird crossing is just a chill game, so there's no need for you to try hard...except try harding at making your island look good. "
                        " You wait for her to notice you. Which took about 10 minutes until she did. "
                        ja " ...Oh, it's you. "
                        ja " Could you not? I'm trying to play a game here. "
                        " You told her that you weren't gonna do anything and were just gonna watch her play. "
                        " ...But you won't if she really didn't want you to watch her. "
                        ja " ... "
                        ja " You'd really want to watch me play a game that looks like it was made for kids? "
                        ja " Well, if you really want to then I guess I'll let you watch me. "
                        " She then moved her switch so that you could see better. "
                        " With a closer look, her island actually looks pretty neat. You complimented her for that. "
                        hide jamgame at bottom
                        show jamsurprised at center
                        ja " ... "
                        hide jamsurprised at bottom
                        show jamgame at center
                        ja " ...No one's really said that to me before. Excluding my online friends. "
                        ja " Thanks though. I appreciate it. "
                        ja " I put a lot of effort into it... I also have references to my favorite games in here. "
                        ja " Like, a lot of them. Especially in my room. "
                        ja " Let me just show you real quick... "
                        scene black with dissolve
                        " You spent the entire break with Jam, with her showing her island off to you. "
                        " It was really well built, and really well decorated. "
                        " You had a feeling that this would go popular on the internet, but Jam insisted that it sucked. "
                        " You thought that it didn't look that bad though. You've seen worse. "
                        play sound "audio/bellring.mp3"
                        " The bell rang, indicating that it was time for the next class. "
                        " You both got up and went back to the classroom. "
                        pause 2.0
                        jump ochealthclass1
                    else:
                        x " ... "
                        " She seems pretty concentrated. Even though she's just playing bird crossing. "
                        " Bird crossing is just a chill game, so there's no need for you to try hard...except try harding at making your island look good. "
                        " You wait for her to notice you. Which took about 10 minutes until she did. "
                        x " ...Oh, it's you. "
                        x " Could you not? I'm trying to play a game here. "
                        " You told her that you weren't gonna do anything and were just gonna watch her play. "
                        " ...But you won't if she really didn't want you to watch her. "
                        x " ... "
                        x " You'd really want to watch me play a game that looks like it was made for kids? "
                        x " Well, if you really want to then I guess I'll let you watch me. "
                        " She then moved her switch so that you could see better. "
                        " With a closer look, her island actually looks pretty neat. You complimented her for that. "
                        hide jamgame at bottom
                        show jamsurprised at center
                        x " ... "
                        hide jamsurprised at bottom
                        show jamgame at center
                        x " ...No one's really said that to me before. Excluding my online friends. "
                        x " Thanks though. I appreciate it. "
                        x " I put a lot of effort into it... I also have references to my favorite games in here. "
                        x " Like, a lot of them. Especially in my room. "
                        x " Let me just show you real quick... "
                        x " ...I don't think I've introduced myself before yet to you. "
                        $ jamknow = True
                        ja " I'm Jam. You must be the new student, from what I remember."
                        ja " Now, let's get back to playing... "
                        scene black with dissolve
                        " You spent the entire break with Jam, with her showing her island off to you. "
                        " It was really well built, and really well decorated. "
                        " You had a feeling that this would go popular on the internet, but Jam insisted that it sucked. "
                        " You thought that it didn't look that bad though. You've seen worse. "
                        play sound "audio/bellring.mp3"
                        " The bell rang, indicating that it was time for the next class. "
                        " You both got up and went back to the classroom. "
                        pause 2.0
                        jump ochealthclass1
                " No thanks, I don't want to disturb her ":
                    " You decided not to sit next to her and continued roaming around the back of the school. "
                    scene black with dissolve
                    " You spent the rest of the break exploring the back of the school. "
                    " You eventually tired yourself out from walking somehow and you rested underneath a tree. "
                    " You looked around at your surroundings before you looked at your phone to have some entertainment. "
                    " Nothing really interesting going on the internet, but atleast you had something to do. "
                    play sound "audio/bellring.mp3"
                    " The bell then rings. Time to go back inside for the next class. "
                    pause 2.0
                    jump ochealthclass1
        label ocgym1:
            # yinhui and yangyi
            scene black with dissolve
            pause 2.0
            scene gym with dissolve
            " You walk into the gym, only to hear an argument happening in the corner. "
            " You decided to go to where the noise was coming from and listen to what was going on. "
            if persistent.ocplayed == True and pythonchallenge == True:
                $ pythoncode4 = True
                " Before you could though, you spotted a little card on the ground... "
                " You flipped it over and it had a number on it, number 4. You found the first number for the code you need! "
                " Best to keep this in your pocket then... "
                pass
            else:
                pass
            show yangyisad at right with easeinleft
            show yinhuiangry at left with easeinleft
            if yinhuiknow and yangyiknow == True:
                ya " But, brother...! I want to spend time with the new kid! "
                if they == "she","he":
                    yi " And what if [they] hurts you? "
                elif they == "they":
                    yi " And what if [they] hurt you? "
                ya " I promise, I'll be fine! I can take care of myself, you know... I'm not a baby anymore... "
                if kind == True:
                    ya " Plus, I bet that [they] [are] very nice! "
                    ya " Didn't you hear [their] introduction earlier...? "
                elif calm == True:
                    ya " Plus, [they] sound very nice and chill! "
                    ya " Didn't you hear [their] introduction earlier...? "
                elif mean == True:
                    ya " I know [they] look a little mean, but I know that [they] [are] nice on the inside! "
                yi " ... Well, I think you just summoned [them]. "
                ya " Huh...? "
                " Yinhui then points to you, who has been watching and listening to their conversation. "
                hide yangyisad at bottom
                show yangyihappy at right
                show yangyihappy at center with move
                ya " [name]! "
                hide yangyihappy at bottom
                show yangyisad at center
                hide yinhuiangry at bottom
                show yinhuineutral at right
                " Yangyi was happy to see you, so he tried to go up to you but Yinhui stopped him. "
                ya " Yin...! "
                yi " Sorry, Yang isn't available to talk right now. "
                yi " It's best to leave for now. "
                scene black with dissolve
                " You were about to say something, until Yinhui pushed you out of the gym. "
                " You get it, overprotective brother. It's only for Yangyi's safety, you guess? "
                " Seems like you won't be able to interact with Yinhui unless if you gain Yinhui's trust. "
                " ...Wonder how you'll achieve that. "
                " You spent the entire break roaming around the school instead of hanging with the two brothers. "
                play sound "audio/bellring.mp3"
                " The bell rings eventually, and you go back to your classroom. "
                pause 2.0
                jump ochealthclass1
            else:
                x " But, brother...! I want to spend time with the new kid! "
                if they == "she","he":
                    x " And what if [they] hurts you? "
                elif they == "they":
                    x " And what if [they] hurt you? "
                x " I promise, I'll be fine! I can take care of myself, you know... I'm not a baby anymore... "
                if kind == True:
                    x " Plus, I bet that [they] [are] very nice! "
                    x " Didn't you hear [their] introduction earlier...? "
                elif calm == True:
                    x " Plus, [they] sound very nice and chill! "
                    x " Didn't you hear [their] introduction earlier...? "
                elif mean == True:
                    x " I know [they] look a little mean, but I know that [they] [are] nice on the inside! "
                x " ... Well, I think you just summoned [them]. "
                x " Huh...? "
                " The annoyed twin then points to you, who had been watching and listening to their conversation. "
                hide yangyisad at bottom
                show yangyihappy at right
                show yangyihappy at center with move
                x " [name]! "
                hide yangyihappy at bottom
                show yangyisurprised at center
                hide yinhuiangry at bottom
                show yinhuineutral at right
                " The other twin was happy to see you, so he tried to go up to you but the grumpy one stopped him. "
                x " Yang...! "
                x " Sorry, Yin isn't available to talk right now. "
                x " It's best to leave for now. "
                scene black with dissolve
                " You were about to say something, until the other guy pushed you out of the gym. "
                " You get it, overprotective brother. It's only for his safety, you guess? "
                " Seems like you won't be able to interact with the twins unless if you gain the grumpy one's trust. "
                " ...Wonder how you'll achieve that. "
                " You spent the entire break roaming around the school instead of hanging with the two brothers. "
                play sound "audio/bellring.mp3"
                " The bell rings eventually, and you go back to your classroom. "
                pause 2.0
                jump ochealthclass1
        label occafe1:
            # Spark, Temero // Carmen, Jacob // Orchid, koa
            scene black with dissolve
            pause 2.0
            scene cafeteria with dissolve
            " There's a lot of people in the cafeteria, but you spot a few of your classmates just chilling. "
            " You're thinking of sitting next to them, but who do you sit next to? "
            if sparkknow,temeroknow == True and carmenknow,jacobknow,orchidknow,koaknow == False:
                menu:
                    " {image=sparkicon} Spark and Temero {image=temeroicon} ":
                        jump sparktemcafeint
                    " {image=carmenicon} A kid with a guitar, and a guy with goggles. {image=jacobicon} ":
                        jump carmenjacobint
                    " {image=orchidicon} A scene kid and an emo looking kid. {image=koaicon} ":
                        jump orchidkoaint
                    " On second thought, I don't want to sit next to anyone. ":
                        jump cafealonesit
            elif carmenknow == True and orchidknow == True:
                menu:
                    " {image=sparkicon} A guy with antennas and a girl with a butterfly bow. {image=temeroicon} ":
                        jump sparktemcafeint
                    " {image=carmenicon} Carmen, and a guy with goggles. {image=jacobicon} ":
                        jump carmenjacobint
                    " {image=orchidicon} Orchid, and an emo looking kid. {image=koaicon} ":
                        jump orchidkoaint
                    " On second thought, I don't want to sit next to anyone. ":
                        jump cafealonesit
            elif jacobknow == True and koaknow == True:
                menu:
                    " {image=sparkicon} A guy with antennas and a girl with a butterfly bow. {image=temeroicon} ":
                        jump sparktemcafeint
                    " {image=carmenicon} A kid with a guitar, and Jacob. {image=jacobicon} ":
                        jump carmenjacobint
                    " {image=orchidicon} A scene kid and Koa. {image=koaicon} ":
                        jump orchidkoaint
                    " On second thought, I don't want to sit next to anyone. ":
                        jump cafealonesit
            else:
                menu:
                    " {image=sparkicon} A guy with antennas and a girl with a butterfly bow. {image=temeroicon} ":
                        jump sparktemcafeint
                    " {image=carmenicon} A kid with a guitar, and a guy with goggles. {image=jacobicon} ":
                        jump carmenjacobint
                    " {image=orchidicon} A scene kid and an emo looking kid. {image=koaicon} ":
                        jump orchidkoaint
                    " On second thought, I don't want to sit next to anyone. ":
                        jump cafealonesit
            label sparktemcafeint:
                show sparkneutral at right with easeinleft
                show temeroneutral at left with easeinleft
                if sparkknow and temeroknow == True:
                    sp " Argh, my antennas are acting up again. "
                    tm " And by that, you mean...? "
                    sp " The same thing I keep asking you to help me with otherwise I would go feral. "
                    tm " I'll send you some of the potions I made to help you then. "
                    tm " Geez, it's so hard to be a half-{nw} "
                    sp " The new kid's here. "
                    hide temeroneutral at bottom
                    show temerowhenzip at left
                    tm " Whoopsie! Almost dropped a secret infront of you, sorry. "
                    " You asked what Temero was going to say. "
                    hide temerowhenzip at bottom
                    show temeroneutral at left
                    tm " That's the secret. You're not supposed to know that! "
                    sp " Uh huh. It's a secret that we both have to keep. That means only us and not anyone else knows about it. "
                    tm " But anyway, I may or may not have accidentally unleashed a big butterfly made out of acid. "
                    hide sparkneutral at bottom
                    show sparksad at right
                    sp " ...Okay, how is that even possible? "
                    hide temeroneutral at bottom
                    show temerohappy at left
                    tm " My great experiments of course. How else would you think a butterfly made out of acid would appear? "
                    sp " Yeah, yeah... "
                    hide sparksad at bottom
                    show sparkneutral at right
                    sp " Wait, is that the reason why that one mansion got melted down? "
                    tm " ...{cps=5}Noooooooooooooo?{/cps} "
                    hide temerohappy at bottom
                    show temeroneutral at center
                    sp " ...Alright. Atleast they don't know that it's you who unleashed that thing. "
                    sp " You should really take more care about your experiments n stuff, otherwise they'd skedaddle from you and wreck havoc. "
                    tm " They're not that bad! "
                    sp " Yeah, they aren't that bad until they burn this town down. "
                    tm " Pshh, you're no fun. "
                    scene black with dissolve
                    " You spent the entire break talking with Spark and Temero. "
                    " You were still curious about what their secret was, but you didn't question them further. "
                    " You knew damn well that they're not spitting that secret out at all. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, you and everyone else gets up from their seats to go to the next class. "
                    pause 2.0
                    jump ochealthclass1
                else:
                    x " Argh, my antennas are acting up again. "
                    x " And by that, you mean...? "
                    x " The same thing I keep asking you to help me with otherwise I would go feral. "
                    x " I'll send you some of the potions I made to help you then. "
                    x " Geez, it's so hard to be a half-{nw} "
                    x " The new kid's here. "
                    hide temeroneutral at bottom
                    show temerowhenzip at left
                    x " Whoopsie! Almost dropped a secret infront of you, sorry. "
                    " You asked what Temero was going to say. "
                    hide temerowhenzip at bottom
                    show temeroneutral at left
                    x " That's the secret. You're not supposed to know that! "
                    x " Uh huh. It's a secret that we both have to keep. That means only us and not anyone else knows about it. "
                    x " Wait, right, right. We haven't introduced ourselves yet! "
                    x " Oh. Forgive us. "
                    $ temeroknow = True
                    $ sparkknow = True
                    sp " I'm Spark. "
                    tm " And I'm Temero Neo! You can call me Temero, Neo, whatever you'd like! "
                    tm " But anyway, I may or may not have accidentally unleashed a big butterfly made out of acid. "
                    hide sparkneutral at bottom
                    show sparksad at right
                    sp " ...Okay, how is that even possible? "
                    hide temeroneutral at bottom
                    show temerohappy at left
                    tm " My great experiments of course. How else would you think a butterfly made out of acid would appear? "
                    sp " Yeah, yeah... "
                    hide sparksad at bottom
                    show sparkneutral at right
                    sp " Wait, is that the reason why that one mansion got melted down? "
                    tm " ...{cps=5}Noooooooooooooo?{/cps} "
                    hide temerohappy at bottom
                    show temeroneutral at center
                    sp " ...Alright. Atleast they don't know that it's you who unleashed that thing. "
                    sp " You should really take more care about your experiments n stuff, otherwise they'd skedaddle from you and wreck havoc. "
                    tm " They're not that bad! "
                    sp " Yeah, they aren't that bad until they burn this town down. "
                    tm " Pshh, you're no fun. "
                    scene black with dissolve
                    " You spent the entire break talking with Spark and Temero. "
                    " You were still curious about what their secret was, but you didn't question them further. "
                    " You knew damn well that they're not spitting that secret out at all. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, you and everyone else gets up from their seats to go to the next class. "
                    pause 2.0
                    jump ochealthclass1
            label carmenjacobint:
                show carmenneutral at left with easeinright
                show jacobneutral at right with easeinright
                if carmenknow == True and jacobknow == False:
                    " You sat down to hear Carmen playing a nice tune. "
                    " The other guy seems to really enjoy Carmen's guitar playing skills. "
                    " You're thinking about just staying here and relaxing while Carmen plays. "
                    " Should you? "
                    scene black with dissolve
                    " Before you could even make a choice, you already fell asleep on the table right then and there. "
                    " Damn, atleast tell me that you're feeling sleepy before you do that. "
                    " But uh, good dreams, I guess? "
                    pause 1.0
                    play sound "audio/bellring.mp3"
                    " The bell rings, waking you up from your little nap. "
                    " You get up from your seat and go to your classroom for the next class. "
                    pause 2.0
                    jump ochealthclass1
                elif jacobknow == True and carmenknow == False:
                    " You sat down to hear a guy with a guitar playing a nice tune. "
                    " Jacob seems to really enjoy the other guys guitar playing skills. "
                    " You're thinking about just staying here and relaxing while the guy with the guitar plays. "
                    " Should you? "
                    scene black with dissolve
                    " Before you could even make a choice, you already fell asleep on the table right then and there. "
                    " Damn, atleast tell me that you're feeling sleepy before you do that. "
                    " But uh, good dreams, I guess? "
                    pause 1.0
                    play sound "audio/bellring.mp3"
                    " The bell rings, waking you up from your little nap. "
                    " You get up from your seat and go to your classroom for the next class. "
                    pause 2.0
                    jump ochealthclass1
                else:
                    " You sat down to hear a guy with a guitar playing a nice tune. "
                    " The other guy seems to really enjoy the other other guy's guitar playing skills. "
                    " You're thinking about just staying here and relaxing while the guy with the guitar plays. "
                    " Should you? "
                    scene black with dissolve
                    " Before you could even make a choice, you already fell asleep on the table right then and there. "
                    " Damn, atleast tell me that you're feeling sleepy before you do that. "
                    " But uh, good dreams, I guess? "
                    pause 1.0
                    play sound "audio/bellring.mp3"
                    " The bell rings, waking you up from your little nap. "
                    " You get up from your seat and go to your classroom for the next class. "
                    pause 2.0
                    jump ochealthclass1
            label orchidkoaint:
                show orchidneutral at right with easeinleft
                show koaneutral at left with easeinleft
                if orchidknow == True and koaknow == False:
                    oc " Hey, hey Koa! "
                    x " What is it now... "
                    oc " Do you wanna know a few compliments in my language? "
                    x " ...You know what, sure. Why not. "
                    oc " Okay, okay! To tell someone that they're pretty... Just say: Bayot ka! "
                    oc " And to tell someone that they're kind...Yawa kaayo ka! "
                    x " Alrighty... "
                    oc " So if you ever meet someone from my country, you could just say those things to them! "
                    oc " Just incase, hehe. "
                    oc " Oh, lookie! It's [name]! Hi [name]! "
                    x " Isn't this the new kid? "
                    oc " Yes [they] [are]! "
                    oc " Actually, I don't think Koa has introduced himself to you yet, so... "
                    $ koaknow = True
                    oc " This is Koa! My friend! He's really cool, but he's also a big nerd. "
                    k " Hey, I'm not THAT much of a nerd. "
                    k " Just because I read books doesn't mean that I'm a big fat nerd. "
                    oc " See? pure nerd energy! "
                    k " Eugh... It's no use arguing with you. "
                    oc " Heheh. I know! "
                    scene black with dissolve
                    " You spent the entire break talking to Orchid and Koa. "
                    " Now that you think about it... "
                    " Koa and Orchid have a somewhat father and child relationship. "
                    " It's cute. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, you and everyone else gets up from their seat to go to the next class. "
                    pause 2.0
                    jump ochealthclass1
                elif koaknow == True and orchidknow == False:
                    x " Hey, hey Koa! "
                    k " What is it now... "
                    x " Do you wanna know a few compliments in my language? "
                    k " ...You know what, sure. Why not. "
                    x " Okay, okay! To tell someone that they're pretty... Just say: Bayot ka! "
                    x " And to tell someone that they're kind...Yawa kaayo ka! "
                    k " Alrighty... "
                    x " So if you ever meet someone from my country, you could just say those things to them! "
                    x " Just incase, hehe. "
                    x " Oh, lookie! It's [name]! Hi [name]! "
                    k " Isn't this the new kid? "
                    x " Yes [they] [are]! "
                    x " Actually, I don't think I've introduced myself to you before, so... "
                    $ orchidknow = True
                    oc " I'm Orchid! I'm Koa's friend, but I'm not as big of a nerd as he is! "
                    k " Hey, I'm not THAT much of a nerd. "
                    k " Just because I read books doesn't mean that I'm a big fat nerd. "
                    oc " See? pure nerd energy! "
                    k " Eugh... It's no use arguing with you. "
                    oc " Heheh. I know! "
                    scene black with dissolve
                    " You spent the entire break talking to Orchid and Koa. "
                    " Now that you think about it... "
                    " Koa and Orchid have a somewhat father and child relationship. "
                    " It's cute. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, you and everyone else gets up from their seat to go to the next class. "
                    pause 2.0
                    jump ochealthclass1
                else:
                    x " Hey, hey Koa! "
                    x " What is it now... "
                    x " Do you wanna know a few compliments in my language? "
                    x " ...You know what, sure. Why not. "
                    x " Okay, okay! To tell someone that they're pretty... Just say: Bayot ka! "
                    x " And to tell someone that they're kind...Yawa kaayo ka! "
                    x " Alrighty... "
                    x " So if you ever meet someone from my country, you could just say those things to them! "
                    x " Just incase, hehe. "
                    x " Oh, lookie! It's [name]! Hi [name]! "
                    x " Isn't this the new kid? "
                    x " Yes [they] [are]! "
                    x " Actually, I don't think I've introduced myself to you before, so... "
                    $ orchidknow = True
                    $ koaknow = True
                    oc " I'm Orchid! I'm Koa's friend, but I'm not as big of a nerd as he is! "
                    oc " Wait, uh... You haven't met Koa yet, have you? Well, he's a nerd! That's all you need to know! "
                    k " Hey, I'm not THAT much of a nerd. "
                    k " Just because I read books doesn't mean that I'm a big fat nerd. "
                    oc " See? pure nerd energy! "
                    k " Eugh... It's no use arguing with you. "
                    oc " Heheh. I know! "
                    scene black with dissolve
                    " You spent the entire break talking to Orchid and Koa. "
                    " Now that you think about it... "
                    " Koa and Orchid have a somewhat father and child relationship. "
                    " It's cute. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, you and everyone else gets up from their seat to go to the next class. "
                    pause 2.0
                    jump ochealthclass1
            label cafealonesit:
                " Alright, lonely guy. "
                scene black with dissolve
                " You spent the entire break just chilling around in the cafeteria, all alone. "
                " You honestly didn't mind being alone. Infact, you even took a nap to show how comfortable you were. "
                " Though you wished that you slept for longer, you knew damn well that the bell was gonna ring whether you liked it or not. "
                play sound "audio/bellring.mp3"
                " Infact, the bell had just rung. "
                " Time to get back up and go to your next class! "
                pause 2.0
                jump ochealthclass1
        label ocroof1:
            # quinn, matte
            scene black with dissolve
            pause 2.0
            scene rooftop with dissolve
            " You walked up to the rooftop and spotted two of your classmates doing their own thing. "
            " You're thinking of talking to them... but who do you talk to? They both seem pretty concentrated. "
            if quinnknow == True and matteknow == True:
                menu:
                    "{image=quinnicon} Quinn {image=quinnicon}":
                        jump quinnroofint
                    "{image=matteicon} Matte {image=matteicon}":
                        jump matteroofint
            else:
                menu:
                    "{image=quinnicon} A guy that's practicing his acting skills {image=quinnicon}":
                        jump quinnroofint
                    "{image=matteicon} A girl that's painting {image=matteicon}":
                        jump matteroofint
            label quinnroofint:
                show quinnneutral at center with easeinleft
                if quinnknow == True:
                    " He seems to be really busy acting... "
                    " Maybe you should wait for him to be finished before you go up to him. "
                    " After all, you don't want to accidentally upset him by disturbing him. "
                    " It took about 5 minutes until he noticed you standing there. "
                    q " Oh, [name]! I apologize for not noticing you. Scusa. "
                    q " I was just practicing my acting for a little acting thingy my club is doing. "
                    q " Actually, since you watched me act for just a bit... "
                    q " How was my acting? And be completely honest with me. I need to know so that I can improve! "
                    " You thought about how he acted... "
                    if kind == True:
                        " ...You then told him that his acting was great! It was just that he needed some work on the expressions. "
                        " You told him that it was good but there were just some parts that needed improvement. "
                    elif calm == True:
                        " ...You then told him that his acting was great! It was just that he needed some work on the expressions. "
                        " You told him that it was good but there were just some parts that needed improvement. "
                    elif mean == True:
                        " You told him bluntly that he lacked emotion on some parts. "
                    q " Hmm... so, I'm lacking a bit on my expressions? "
                    hide quinnneutral at bottom
                    show quinnhappy at center
                    q " Well, I'll get to work on that then! "
                    hide quinnhappy at bottom
                    show quinnneutral at center
                    q " Actually, [name]... "
                    q " Could you do me a favor and watch me again? "
                    q " Just so I know that I'm improving with my expressions! "
                    " Well, you had nothing else to do anyway. "
                    " Why not? "
                    hide quinnneutral at bottom
                    show quinnhappy at center
                    q " Okay! Thanks, [name]! "
                    q " Alright, here I go... "
                    scene black with dissolve
                    " You spent the rest of the break watching Quinn practice his acting. "
                    " Surprisingly, he was a bit bad at expressing emotions on his face. He was good with his voice, but his face? nope. "
                    " And just when he got his acting right, the bell rang. "
                    play sound "audio/bellring.mp3"
                    " Oops. Was a little early at that. Sorry. "
                    " But anyway, you get down from the rooftop so that youcould go to your next class. "
                    pause 2.0
                    jump ochealthclass1
                else:
                    " He seems to be really busy acting... "
                    " Maybe you should wait for him to be finished before you go up to him. "
                    " After all, you don't want to accidentally upset him by disturbing him. "
                    " It took about 5 minutes until he noticed you standing there. "
                    x " Oh, [name]! I apologize for not noticing you. Scusa. "
                    x " Wait, right. I haven't introduced myself to you yet. Forgive me. "
                    $ quinnknow = True
                    q " I'm Quinn. I do acting around here. As for what I'm doing... "
                    q " I was just practicing my acting for a little acting thingy my club is doing. "
                    q " Actually, since you watched me act for just a bit... "
                    q " How was my acting? And be completely honest with me. I need to know so that I can improve! "
                    " You thought about how he acted... "
                    if kind == True:
                        " ...You then told him that his acting was great! It was just that he needed some work on the expressions. "
                        " You told him that it was good but there were just some parts that needed improvement. "
                    elif calm == True:
                        " ...You then told him that his acting was great! It was just that he needed some work on the expressions. "
                        " You told him that it was good but there were just some parts that needed improvement. "
                    elif mean == True:
                        " You told him bluntly that he lacked emotion on some parts. "
                    q " Hmm... so, I'm lacking a bit on my expressions? "
                    hide quinnneutral at bottom
                    show quinnhappy at center
                    q " Well, I'll get to work on that then! "
                    hide quinnhappy at bottom
                    show quinnneutral at center
                    q " Actually, [name]... "
                    q " Could you do me a favor and watch me again? "
                    q " Just so I know that I'm improving with my expressions! "
                    " Well, you had nothing else to do anyway. "
                    " Why not? "
                    hide quinnneutral at bottom
                    show quinnhappy at center
                    q " Okay! Thanks, [name]! "
                    q " Alright, here I go... "
                    scene black with dissolve
                    " You spent the rest of the break watching Quinn practice his acting. "
                    " Surprisingly, he was a bit bad at expressing emotions on his face. He was good with his voice, but his face? nope. "
                    " And just when he got his acting right, the bell rang. "
                    play sound "audio/bellring.mp3"
                    " Oops. Was a little early at that. Sorry. "
                    " But anyway, you get down from the rooftop so that youcould go to your next class. "
                    pause 2.0
                    jump ochealthclass1
            label matteroofint:
                show matteneutral at center with easeinright
                if matteknow == True:
                    " She seems pretty busy with painting... "
                    " Maybe you should just wait for her to notice you. "
                    " ...That worked, she only noticed you when we was grabbing her water bottle to drink. "
                    ma " Oh, sup [name]. "
                    ma " What I'm painting? It's for the drama club's thing they're having. "
                    ma " They specifically referred it to me as a thing. "
                    ma " They just need to use my painting as a prop, and I'm happy to help. "
                    ma " Yes, I did tell them that they could just print something and put it in a frame but they insisted. "
                    ma " Because my art was just the 'greatest' they said. "
                    ma " I was originally gonna refuse, but they paid me to paint this for 1K, so... "
                    ma " Here I am, painting for them. "
                    ma " ...Actually, I know that you probably don't draw much, but I don't want you to just stand there and look all bored while watching me, so... "
                    ma " Do you want to know some art tips? I usually give Disk some art tips since he wants to learn how to paint like me. "
                    ma " It's fine if you don't want any art tips, though. "
                    " ...You had already pulled out your notes app for this. Of course you said yes. "
                    " You had nothing else to do for the rest of the break anyway. "
                    ma " ...I actually thought you'd find art tips boring. "
                    ma " I suppose I was proven wrong, hmhm... "
                    ma " Very well then. So, my first art tip is to... "
                    scene black with dissolve
                    " You spent some time with Matte on the rooftop. "
                    " Watching her paint and give you art tips at the same time... You actually started drawing her on Ibispaint while she was talking. "
                    " She eventually caught you drawing her and she told you that she got reminded of that one 'hyperpigmentation' meme... "
                    " Wonder what that means, but she told you that it looked nice. "
                    play sound "audio/bellring.mp3"
                    " The bell then rings, and Matte stopped painting. "
                    " You both then went down the rooftop so that you two could go to the next class. "
                    pause 2.0
                    jump ochealthclass1
                else:
                    " She seems pretty busy with painting... "
                    " Maybe you should just wait for her to notice you. "
                    " ...That worked, she only noticed you when we was grabbing her water bottle to drink. "
                    x " Oh, sup [name]. "
                    x " I don't think I've got to introduce myself to you... You're the new kid, right? "
                    x " Welll... "
                    $ matteknow = True
                    ma " I'm Matte. It's good to meet you. "
                    " You told her that it was nice to meet her too, and then you asked her what she was painting. "
                    ma " What I'm painting? It's for the drama club's thing they're having. "
                    ma " They specifically referred it to me as a thing. "
                    ma " They just need to use my painting as a prop, and I'm happy to help. "
                    ma " Yes, I did tell them that they could just print something and put it in a frame but they insisted. "
                    ma " Because my art was just the 'greatest' they said. "
                    ma " I was originally gonna refuse, but they paid me to paint this for 1K, so... "
                    ma " Here I am, painting for them. "
                    ma " ...Actually, I know that you probably don't draw much, but I don't want you to just stand there and look all bored while watching me, so... "
                    ma " Do you want to know some art tips? I usually give Disk some art tips since he wants to learn how to paint like me. "
                    ma " It's fine if you don't want any art tips, though. "
                    " ...You had already pulled out your notes app for this. Of course you said yes. "
                    " You had nothing else to do for the rest of the break anyway. "
                    ma " ...I actually thought you'd find art tips boring. "
                    ma " I suppose I was proven wrong, hmhm... "
                    ma " Very well then. So, my first art tip is to... "
                    scene black with dissolve
                    " You spent some time with Matte on the rooftop. "
                    " Watching her paint and give you art tips at the same time... You actually started drawing her on Ibispaint while she was talking. "
                    " She eventually caught you drawing her and she told you that she got reminded of that one 'hyperpigmentation' meme... "
                    " Wonder what that means, but she told you that it looked nice. "
                    play sound "audio/bellring.mp3"
                    " The bell then rings, and Matte stopped painting. "
                    " You both then went down the rooftop so that you two could go to the next class. "
                    pause 2.0
                    jump ochealthclass1
        label oclibrary1:
            # Nox
            scene black with dissolve
            pause 2.0
            scene library with dissolve
            " You enter the library. Now you feel like a nerd. Well, not really. "
            " You walk around the library, looking around at the amount of books on the shelves... "
            " Until you spot one of your fellow classmates sleeping. "
            " Should you wake them up? Or should you let them continue sleeping? "
            menu:
                " Let's wake them up ":
                    " You decided to sit next to them. You put your hand on their shoulder and lightly shook them to wake them up. "
                    show noxsleepy at center with dissolve
                    if noxknow == True:
                        n " Hhhh... what is it...? "
                        n " Did class start already...? "
                        " You told him no, but you were just there to ask him why he fell asleep in the library of all places. "
                        n " Well... I'm always sleepy. "
                        n " I just chose to sleep here for now. "
                        " You then asked him if he gets enough sleep. "
                        n " No. I don't ever...*yawn*...get enough sleep... "
                        n " No matter how many naps I take... "
                        n " It's a bit frustrating... Since I have to stay awake in the morning... "
                        n " But it's a little hard for me to do that... Since my sleepiness always gets to the best of me... "
                        n " Could you actually do something to try and make me stay awake...? "
                        " You thought about how to make Nox stay awake for a bit longer... "
                        " ...Then asked him if he could tell you about his dream that he probably had. "
                        n " My dream...? I think I can remember it clearly... "
                        n " In my dream... "
                        scene black with dissolve
                        " You spent the entire break trying to make sure that Nox stays awake as he told you his dream. "
                        " And everytime he almost falls asleep, you whack him on the head to make sure he stays awake. "
                        " And it worked, surprisingly. "
                        " He had a pretty interesting dream to say the least. I have a feeling if I told you what he dreamt of you'd be weirded out. "
                        play sound "audio/bellring.mp3"
                        " The bell eventually rang, and that seemed to get Nox to wake up more. "
                        " Though he seemed fine with walking at first, you had to help him walk to the classroom because he felt like collapsing due to how sleepy he was at one point. "
                        " What a sleepy guy... "
                        pause 2.0
                        jump ochealthclass1
                    else:
                        x " Hhhh... what is it...? "
                        x " Oh... it's you... You're the new kid.... "
                        x " I remember you...I saw you and heard your introduction right before I fell asleep... "
                        x " I didn't introduce myself yet to you...did I...? I can't remember... "
                        x " If I did, might as well do it again then... "
                        $ noxknow = True
                        n " I'm Nox... Nox cesso... "
                        n " Did class start already...? "
                        " You told him no, but you were just there to ask him why he fell asleep in the library of all places. "
                        n " Well... I'm always sleepy. "
                        n " I just chose to sleep here for now. "
                        " You then asked him if he gets enough sleep. "
                        n " No. I don't ever...*yawn*...get enough sleep... "
                        n " No matter how many naps I take... "
                        n " It's a bit frustrating... Since I have to stay awake in the morning... "
                        n " But it's a little hard for me to do that... Since my sleepiness always gets to the best of me... "
                        n " Could you actually do something to try and make me stay awake...? "
                        " You thought about how to make Nox stay awake for a bit longer... "
                        " ...Then asked him if he could tell you about his dream that he probably had. "
                        n " My dream...? I think I can remember it clearly... "
                        n " In my dream... "
                        scene black with dissolve
                        " You spent the entire break trying to make sure that Nox stays awake as he told you his dream. "
                        " And everytime he almost falls asleep, you whack him on the head to make sure he stays awake. "
                        " And it worked, surprisingly. "
                        " He had a pretty interesting dream to say the least. I have a feeling if I told you what he dreamt of you'd be weirded out. "
                        play sound "audio/bellring.mp3"
                        " The bell eventually rang, and that seemed to get Nox to wake up more. "
                        " Though he seemed fine with walking at first, you had to help him walk to the classroom because he felt like collapsing due to how sleepy he was at one point. "
                        " What a sleepy guy... "
                        pause 2.0
                        jump ochealthclass1
                " No, let them continue sleeping ":
                    " You decided to let them continue sleeping peacefully. "
                    " You went on to look at all the cool books the library has.{w=0.5} Like a random BL book-{nw} "
                    " Wait. Who left this book here? "
                    " You should probably try to find the owner of this later, but then again... "
                    " ...The owner might come back here and try to find it again. "
                    " You just decided to put it near the librarian and tell them that someone lost this and leave the library. "
                    scene black with dissolve
                    " You left the library, and just roamed around the school for a bit. "
                    " You eavesdropped on a few people gossiping about some juicy drama, and boy you loved it. You loved the drama you just figured out. "
                    play sound "audio/bellring.mp3"
                    " Though, of course, the bell rang. Time to go back to class then. "
                    pause 2.0
                    jump ochealthclass1
    label ochealthclass1:
        scene classroom with dissolve
        " You walk into the classroom and saw everyone else already there. "
        " You take a quick look around before you sat down in your seat, waiting for the next teacher. "
        " Just a few minutes later, you heard the door open. "
        show altrixneutral at center with easeinright
        x " Ah- Hello and good morning, class! "
        " Everyone greets him a good morning. You decided to greet him a good morning too because it would be rude not to. "
        x " I um...I heard we had a new student here, am I correct...? "
        show diskjoyous at left with easeinleft
        if diskknow == True:
            d " Yes, sir! "
            if they == "she","he":
                d " [their] name is [name] and [they]'s very cool! "
            elif they == "they":
                d " [their] name is [name] and [they] are very cool! "
        else:
            x " Yes, sir! "
            if they == "she","he":
                x " [their] name is [name] and [they]'s very cool! "
            elif they == "they":
                x " [their] name is [name] and [they] are very cool! "
        hide diskjoyous at left with easeoutleft
        x " Eheh... thank you Disk. "
        " The teacher looks around the classroom to find where you were and eventually sees you. "
        x " Oh! You must be [name]! Hi! "
        hide altrixneutral at bottom
        show altrixhappy at center
        msa " I'm Mister Altrix, the health teacher! "
        msa " It's a pleasure to have you in our class, [name]. "
        hide altrixhappy at bottom
        show altrixneutral at center
        msa " Now, how about we get into our lesson? "
        scene black with dissolve
        " Mister Altrix then started teaching the class about the topic he was gonna talk about today. "
        " You probably thought that Altrix was a girl at first, didn't you? "
        " Well, if not, cngratulations. You get a gold star for that. "
        " That empty space on the other half of Altrix's face is actually kinda creeping you out. You wonder if it's a void of some sort... "
        " ...Aaaaannndd he just pulled out a medkit out of that half of his face. "
        " He actually gave you some context on that part of his face. it's like his personal storage thingy. "
        " It's endless, and he can put anything in there. Just not other humans. "
        " Boring... You could've put dead bodies in there. But oh well, I suppose... "
        play sound "audio/bellring.mp3"
        " The bell rings after a long while of being in class, meaning that class is over and it's time for another break. "
        " You wait for everyone else to get out of the classroom before you did. "
        pause 2.0
        jump ocbreak2
    label ocbreak2:
        scene hallway with dissolve
        " It's breaktime, and you're thinking about exploring the school some more. "
        " Where do you go? "
        menu:
            " {image=matteicon} The front of the school {image=jamicon} ":
                jump ocfrontschool2
            " {image=miaicon} The back of the school {image=temeroicon} ":
                jump ocbackschool2
            " {image=jacobicon} The gym {image=koaicon} ":
                jump ocgym2
            " The cafeteria ":
                jump occafe2
            " {image=sparkicon} The rooftop {image=noxicon} ":
                jump ocrooftop2
            " {image=carmenicon} The library {image=quinnicon} ":
                jump oclibrary2
        label ocfrontschool2:
            # Matte + Jam
            scene black with dissolve
            pause 2.0
            scene paperschoolfront with dissolve
            " You walk out of the school to get some fresh air, "
            " And you hear two of your classmates talking about something. "
            " You see them and walk up to them to see what they're doing. "
            show matteneutral at right with easeinleft
            show jamgame at left with easeinleft
            if matteknow == True and jamknow == True:
                ma " Come on, Jam. I'm just gonna draw you real quick... "
                ja " No. Besides, I don't look good enough to be drawn. "
                ma " But you are!! "
                ja " Even if you say that I am, I don't believe you. "
                ja " Now let me game, please. Matte. "
                hide matteneutral at bottom
                show mattesad at right
                ma " ...(It's so sad that she thinks that she's not good looking...) "
                ma " (I mean, she looks good enough to me! She looks hot, even!) "
                " Woah there, Matte. {i}Scissor{/i} me timbers. "
                hide mattesad at bottom
                show matteneutral at right
                ma " (psst... you there... could you help me real quick?) "
                ma " (I want to give Jam a drawing of herself as a gift, but she wont stay still if I tell her to.) "
                ma " (Could you maybe distract her for me so that she would'nt notice me drawing her?) "
                ma " (Pretty please?) "
                " Well, you didn't have anything else to do, so... "
                " You gave Matte a thumbs up and sat down next to Jam. "
                " You then start asking Jam questions about what she's doing in the game she's playing right now. "
                ja " Killing some enemies for some EXP. "
                " Matte then quietly grabs her sketchbook and she starts to draw Jam... "
                ja " Just some easy kills here and there... "
                scene black with dissolve
                " You spent the rest of the break distracting Jam just so that Matte could draw her. "
                " It actually worked pretty well since Jam was busy talking to you and gaming at the same time. So, she didn't notice Matte. "
                " Matte could've just waited a few minutes until Jam was a bit distracted more on her game, and then she could've drawn her right then and there. "
                " But oh well, here we are. Distracting Jam for Matte. "
                " You better get paid for this. "
                play sound "audio/bellring.mp3"
                " When the bell rings, Matte was done with her drawing and she showed it to Jam. "
                " Jam saw it and she said that it really captured how ugly she herself was, and she said that she didn't like it. "
                " Though, while you were walking back to your classroom, you could see Jam look at the drawing one more time and paused, before she put the drawing in her pocket. "
                " Turns out she really did like it. "
                pause 2.0
                jump ocpeclass1
            elif matteknow == True and jamknow == False:
                ma " Come on, Jam. I'm just gonna draw you real quick... "
                x " No. Besides, I don't look good enough to be drawn. "
                ma " But you are!! "
                x " Even if you say that I am, I don't believe you. "
                x " Now let me game, please. Matte. "
                hide matteneutral at bottom
                show mattesad at right
                ma " ...(It's so sad that she thinks that she's not good looking...) "
                ma " (I mean, she looks good enough to me! She looks hot, even!) "
                " Woah there, Matte. {i}Scissor{/i} me timbers. "
                hide mattesad at bottom
                show matteneutral at right
                ma " (psst... you there... could you help me real quick?) "
                $ jamknow = True
                ma " (You see the girl over there that's gaming? That's my friend, Jam.) "
                ma " (I want to give Jam a drawing of herself as a gift, but she wont stay still if I tell her to.) "
                ma " (Could you maybe distract her for me so that she would'nt notice me drawing her?) "
                ma " (Pretty please?) "
                " Well, you didn't have anything else to do, so... "
                " You gave Matte a thumbs up and sat down next to Jam. "
                " You then start asking Jam questions about what she's doing in the game she's playing right now. "
                ja " Killing some enemies for some EXP. "
                " Matte then quietly grabs her sketchbook and she starts to draw Jam... "
                ja " Just some easy kills here and there... "
                scene black with dissolve
                " You spent the rest of the break distracting Jam just so that Matte could draw her. "
                " It actually worked pretty well since Jam was busy talking to you and gaming at the same time. So, she didn't notice Matte. "
                " Matte could've just waited a few minutes until Jam was a bit distracted more on her game, and then she could've drawn her right then and there. "
                " But oh well, here we are. Distracting Jam for Matte. "
                " You better get paid for this. "
                play sound "audio/bellring.mp3"
                " When the bell rings, Matte was done with her drawing and she showed it to Jam. "
                " Jam saw it and she said that it really captured how ugly she herself was, and she said that she didn't like it. "
                " Though, while you were walking back to your classroom, you could see Jam look at the drawing one more time and paused, before she put the drawing in her pocket. "
                " Turns out she really did like it. "
                pause 2.0
                jump ocpeclass1
            elif matteknow == False and jamknow == True:
                x " Come on, Jam. I'm just gonna draw you real quick... "
                ja " No. Besides, I don't look good enough to be drawn. "
                x " But you are!! "
                ja " Even if you say that I am, I don't believe you. "
                ja " Now let me game, please. Matte. "
                hide matteneutral at bottom
                show mattesad at right
                x " ...(It's so sad that she thinks that she's not good looking...) "
                x " (I mean, she looks good enough to me! She looks hot, even!) "
                " Woah there, girlie. {i}Scissor{/i} me timbers. "
                hide mattesad at bottom
                show matteneutral at right
                x " (psst... you there... could you help me real quick?) "
                $ matteknow = True
                ma " (I haven't introduced myself to you yet, but I'm Matte. I'm Jam's friend.) "
                ma " (I want to give Jam a drawing of herself as a gift, but she wont stay still if I tell her to.) "
                ma " (Could you maybe distract her for me so that she would'nt notice me drawing her?) "
                ma " (Pretty please?) "
                " Well, you didn't have anything else to do, so... "
                " You gave Matte a thumbs up and sat down next to Jam. "
                " You then start asking Jam questions about what she's doing in the game she's playing right now. "
                ja " Killing some enemies for some EXP. "
                " Matte then quietly grabs her sketchbook and she starts to draw Jam... "
                ja " Just some easy kills here and there... "
                scene black with dissolve
                " You spent the rest of the break distracting Jam just so that Matte could draw her. "
                " It actually worked pretty well since Jam was busy talking to you and gaming at the same time. So, she didn't notice Matte. "
                " Matte could've just waited a few minutes until Jam was a bit distracted more on her game, and then she could've drawn her right then and there. "
                " But oh well, here we are. Distracting Jam for Matte. "
                " You better get paid for this. "
                play sound "audio/bellring.mp3"
                " When the bell rings, Matte was done with her drawing and she showed it to Jam. "
                " Jam saw it and she said that it really captured how ugly she herself was, and she said that she didn't like it. "
                " Though, while you were walking back to your classroom, you could see Jam look at the drawing one more time and paused, before she put the drawing in her pocket. "
                " Turns out she really did like it. "
                pause 2.0
                jump ocpeclass1
            else:
                x " Come on, Jam. I'm just gonna draw you real quick... "
                x " No. Besides, I don't look good enough to be drawn. "
                x " But you are!! "
                x " Even if you say that I am, I don't believe you. "
                x " Now let me game, please. Matte. "
                hide matteneutral at bottom
                show mattesad at right
                x " ...(It's so sad that she thinks that she's not good looking...) "
                x " (I mean, she looks good enough to me! She looks hot, even!) "
                " Woah there, girlie. {i}Scissor{/i} me timbers. "
                hide mattesad at bottom
                show matteneutral at right
                x " (psst... you there... could you help me real quick?) "
                $ matteknow = True
                $ jamknow = True
                x " (You see the girl over there that's gaming? That's my friend, Jam.) "
                ma " (I haven't introduced myself yet, but uh... I'm Matte.) "
                ma " (I want to give Jam a drawing of herself as a gift, but she wont stay still if I tell her to.) "
                ma " (Could you maybe distract her for me so that she would'nt notice me drawing her?) "
                ma " (Pretty please?) "
                " Well, you didn't have anything else to do, so... "
                " You gave Matte a thumbs up and sat down next to Jam. "
                " You then start asking Jam questions about what she's doing in the game she's playing right now. "
                ja " Killing some enemies for some EXP. "
                " Matte then quietly grabs her sketchbook and she starts to draw Jam... "
                ja " Just some easy kills here and there... "
                scene black with dissolve
                " You spent the rest of the break distracting Jam just so that Matte could draw her. "
                " It actually worked pretty well since Jam was busy talking to you and gaming at the same time. So, she didn't notice Matte. "
                " Matte could've just waited a few minutes until Jam was a bit distracted more on her game, and then she could've drawn her right then and there. "
                " But oh well, here we are. Distracting Jam for Matte. "
                " You better get paid for this. "
                play sound "audio/bellring.mp3"
                " When the bell rings, Matte was done with her drawing and she showed it to Jam. "
                " Jam saw it and she said that it really captured how ugly she herself was, and she said that she didn't like it. "
                " Though, while you were walking back to your classroom, you could see Jam look at the drawing one more time and paused, before she put the drawing in her pocket. "
                " Turns out she really did like it. "
                pause 2.0
                jump ocpeclass1
        label ocbackschool2:
            # Mia + Temero
            scene black with dissolve
            pause 2.0
            scene paperschoolback with dissolve
            " You walk into the back of the school, and you could hear some very insane sounding laughter. "
            " You were a little bit concerned so you checked out what was going on. "
            show miaworried at left with easeinright
            show temerohappy at right with easeinright
            if miaknow == True and temeroknow == True:
                m " No!! What are you doing to my precious flowers?! "
                tm " Your flowers? Heheh... I'm just giving them a little touch up! "
                tm " You know, they need to be more interesting! Besides, I need to test my new potions on something! "
                tm " Potions just dont fix themselves, you know. So I decided to test my potions on your flowers! "
                m " You atleast could've told me that you were going to do this earlier! "
                tm " Yeaahh, but I saw that you were busy talking with someone else, and I didn't want to interrupt. "
                m " But still! "
                tm " Oh well, it's too late now! Watch what this potion does! "
                " Wow, such chaos. "
                " You watch Temero pour a purple potion onto a plant while holding Mia off from disturbing her experiment with her other hand. "
                hide miaworried at bottom
                show mianeutral at left
                " The plant then grew large, larger than the school building itself. " with vpunch
                " Geez, now you're wondering what else Temero could do with those potions of hers. "
                " She can definitely destroy an entire city with these potions that she comes up with every day. "
                m " Oooh...! "
                tm " Pretty, isn't it? "
                tm " I told you that this would be a good idea! "
                hide mianeutral at bottom
                show miahappy at left
                m " Could you try to make some of my flowers glow? "
                show miahappy at center with move
                m " Pretty please, oh great Temero Neo? "
                tm " Oooh, I could DEFINITELY get used to this. "
                tm " Well, as long as you pay me about 20$ per 10 flowers. "
                m " Deal! "
                m " I'm planning to put flowers infront of the school so that it would look nice and pretty, but it would look much cooler if you made them glow at night! "
                hide temerohappy at bottom
                show temeroneutral at right
                tm " Yeah, sure. Just call me when you're gonna plant them and I'll get my potions. "
                tm " I'll see you again sometime then~ "
                m " Yeah! See you! "
                hide miahappy at left with easeoutleft
                show temeroneutral at center with move
                " Mia skedaddles away into the forest somewhere... "
                " Temero then finally spots you. "
                tm " Oh. Didn't notice that you were here. "
                tm " So, how'd you like it? My 'mad scientist side'? "
                " You thought about what you saw while Temero was acting as if she was a mad scientist of some sorts... "
                if kind == True:
                    " You told her that she'd make a great villain! "
                elif calm == True:
                    " You told her that she'd make a great villain. "
                elif mean == True:
                    " You told her that her evil scientist thing needed a little bit of work, but she'd still make a great villain. "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " Hell yes I would! "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " I'm gonna work on doing more evil things, heheh... "
                tm " Like torturing people who like kids in a romantic way... those people are disgusting... "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " So I'm gonna test all sorts of potions on them when I get my hands on one! "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " Well, technically, I'm doing the world by doing a favor. "
                tm " But I'd love to hear their cries of pain! "
                play sound "audio/bellring.mp3"
                pause 1.0
                hide temeroneutral at bottom
                show temeroangry at center
                tm " Oh, eugh. I almost forgot that we still had class. "
                hide temeroangry at bottom
                show temeroneutral at center
                tm " Whatever! We can still talk later, [name]. "
                tm " See you in class! "
                hide temeroneutral at left with easeoutleft
                scene black with dissolve
                " You went to your classroom right after Temero left. "
                pause 2.0
                jump ocpeclass1
            elif miaknow == True and temeroknow == False:
                m " No!! What are you doing to my precious flowers?! "
                x " Your flowers? Heheh... I'm just giving them a little touch up! "
                x " You know, they need to be more interesting! Besides, I need to test my new potions on something! "
                x " Potions just dont fix themselves, you know. So I decided to test my potions on your flowers! "
                m " You atleast could've told me that you were going to do this earlier! "
                x " Yeaahh, but I saw that you were busy talking with someone else, and I didn't want to interrupt. "
                m " But still! "
                x " Oh well, it's too late now! Watch what this potion does! "
                " Wow, such chaos. "
                " You watch the girl pour a purple potion onto a plant while holding Mia off from disturbing her experiment with her other hand. "
                hide miaworried at bottom
                show mianeutral at left
                " The plant then grew large, larger than the school building itself. " with vpunch
                " Geez, now you're wondering what else that girl could do with those potions of hers. "
                " She can definitely destroy an entire city with these potions that she comes up with every day. "
                m " Oooh...! "
                x " Pretty, isn't it? "
                x " I told you that this would be a good idea! "
                hide mianeutral at bottom
                show miahappy at left
                m " Could you try to make some of my flowers glow? "
                show miahappy at center with move
                m " Pretty please, oh great Temero Neo? "
                x " Oooh, I could DEFINITELY get used to this. "
                x " Well, as long as you pay me about 20$ per 10 flowers. "
                m " Deal! "
                m " I'm planning to put flowers infront of the school so that it would look nice and pretty, but it would look much cooler if you made them glow at night! "
                hide temerohappy at bottom
                show temeroneutral at right
                x " Yeah, sure. Just call me when you're gonna plant them and I'll get my potions. "
                x " I'll see you again sometime then~ "
                m " Yeah! See you! "
                hide miahappy at left with easeoutleft
                show temeroneutral at center with move
                " Mia skedaddles away into the forest somewhere... "
                " The girl then finally spots you. "
                x " Oh. Didn't notice that you were here. "
                x " You're that new kid in my class, yeah?  That's interesting. You look interesting! "
                x " Wait, sorry. I haven't introduced myself yet. "
                $ temeroknow = True
                tm " I'm Temero Neo! Call me Temero or Neo, I don't mind. "
                tm " So, how'd you like it? My 'mad scientist side'? "
                " You thought about what you saw while Temero was acting as if she was a mad scientist of some sorts... "
                if kind == True:
                    " You told her that she'd make a great villain! "
                elif calm == True:
                    " You told her that she'd make a great villain. "
                elif mean == True:
                    " You told her that her evil scientist thing needed a little bit of work, but she'd still make a great villain. "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " Hell yes I would! "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " I'm gonna work on doing more evil things, heheh... "
                tm " Like torturing people who like kids in a romantic way... those people are disgusting... "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " So I'm gonna test all sorts of potions on them when I get my hands on one! "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " Well, technically, I'm doing the world by doing a favor. "
                tm " But I'd love to hear their cries of pain! "
                play sound "audio/bellring.mp3"
                pause 1.0
                hide temeroneutral at bottom
                show temeroangry at center
                tm " Oh, eugh. I almost forgot that we still had class. "
                hide temeroangry at bottom
                show temeroneutral at center
                tm " Whatever! We can still talk later, [name]. "
                tm " See you in class! "
                hide temeroneutral at left with easeoutleft
                scene black with dissolve
                " You went to your classroom right after Temero left. "
                pause 2.0
                jump ocpeclass1
            elif miaknow == False and temeroknow == True:
                x " No!! What are you doing to my precious flowers?! "
                tm " Your flowers? Heheh... I'm just giving them a little touch up! "
                tm " You know, they need to be more interesting! Besides, I need to test my new potions on something! "
                tm " Potions just dont fix themselves, you know. So I decided to test my potions on your flowers! "
                x " You atleast could've told me that you were going to do this earlier! "
                tm " Yeaahh, but I saw that you were busy talking with someone else, and I didn't want to interrupt. "
                x " But still! "
                tm " Oh well, it's too late now! Watch what this potion does! "
                " Wow, such chaos. "
                " You watch Temero pour a purple potion onto a plant while holding the other girl off from disturbing her experiment with her other hand. "
                hide miaworried at bottom
                show mianeutral at left
                " The plant then grew large, larger than the school building itself. " with vpunch
                " Geez, now you're wondering what else Temero could do with those potions of hers. "
                " She can definitely destroy an entire city with these potions that she comes up with every day. "
                x " Oooh...! "
                tm " Pretty, isn't it? "
                tm " I told you that this would be a good idea! "
                hide mianeutral at bottom
                show miahappy at left
                x " Could you try to make some of my flowers glow? "
                show miahappy at center with move
                x " Pretty please, oh great Temero Neo? "
                tm " Oooh, I could DEFINITELY get used to this. "
                tm " Well, as long as you pay me about 20$ per 10 flowers. "
                x " Deal! "
                x " I'm planning to put flowers infront of the school so that it would look nice and pretty, but it would look much cooler if you made them glow at night! "
                hide temerohappy at bottom
                show temeroneutral at right
                tm " Yeah, sure. Just call me when you're gonna plant them and I'll get my potions. "
                tm " I'll see you again sometime then~ "
                x " Yeah! See you! "
                hide miahappy at left with easeoutleft
                show temeroneutral at center with move
                " The girl skedaddles away into the forest somewhere... "
                " Temero then finally spots you. "
                tm " Oh. Didn't notice that you were here. "
                tm " So, how'd you like it? My 'mad scientist side'? "
                " You thought about what you saw while Temero was acting as if she was a mad scientist of some sorts... "
                if kind == True:
                    " You told her that she'd make a great villain! "
                elif calm == True:
                    " You told her that she'd make a great villain. "
                elif mean == True:
                    " You told her that her evil scientist thing needed a little bit of work, but she'd still make a great villain. "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " Hell yes I would! "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " I'm gonna work on doing more evil things, heheh... "
                tm " Like torturing people who like kids in a romantic way... those people are disgusting... "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " So I'm gonna test all sorts of potions on them when I get my hands on one! "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " Well, technically, I'm doing the world by doing a favor. "
                tm " But I'd love to hear their cries of pain! "
                play sound "audio/bellring.mp3"
                pause 1.0
                hide temeroneutral at bottom
                show temeroangry at center
                tm " Oh, eugh. I almost forgot that we still had class. "
                hide temeroangry at bottom
                show temeroneutral at center
                tm " Whatever! We can still talk later, [name]. "
                tm " See you in class! "
                hide temeroneutral at left with easeoutleft
                scene black with dissolve
                " You went to your classroom right after Temero left. "
                pause 2.0
                jump ocpeclass1
            else:
                x " No!! What are you doing to my precious flowers?! "
                x " Your flowers? Heheh... I'm just giving them a little touch up! "
                x " You know, they need to be more interesting! Besides, I need to test my new potions on something! "
                x " Potions just dont fix themselves, you know. So I decided to test my potions on your flowers! "
                x " You atleast could've told me that you were going to do this earlier! "
                x " Yeaahh, but I saw that you were busy talking with someone else, and I didn't want to interrupt. "
                x " But still! "
                x " Oh well, it's too late now! Watch what this potion does! "
                " Wow, such chaos. "
                " You watch the girl pour a purple potion onto a plant while holding the other girl off from disturbing her experiment with her other hand. "
                hide miaworried at bottom
                show mianeutral at left
                " The plant then grew large, larger than the school building itself. " with vpunch
                " Geez, now you're wondering what else that girl could do with those potions of hers. "
                " She can definitely destroy an entire city with these potions that she comes up with every day. "
                x " Oooh...! "
                x " Pretty, isn't it? "
                x " I told you that this would be a good idea! "
                hide mianeutral at bottom
                show miahappy at left
                x " Could you try to make some of my flowers glow? "
                show miahappy at center with move
                x " Pretty please, oh great Temero Neo? "
                x " Oooh, I could DEFINITELY get used to this. "
                x " Well, as long as you pay me about 20$ per 10 flowers. "
                x " Deal! "
                x " I'm planning to put flowers infront of the school so that it would look nice and pretty, but it would look much cooler if you made them glow at night! "
                hide temerohappy at bottom
                show temeroneutral at right
                x " Yeah, sure. Just call me when you're gonna plant them and I'll get my potions. "
                x " I'll see you again sometime then~ "
                x " Yeah! See you! "
                hide miahappy at left with easeoutleft
                show temeroneutral at center with move
                " The other girl then skedaddles away into the forest somewhere... "
                " The girl who made the crazy potions then finally spots you. "
                x " Oh. Didn't notice that you were here. "
                x " You're that new kid in my class, yeah?  That's interesting. You look interesting! "
                x " Wait, sorry. I haven't introduced myself yet. "
                $ temeroknow = True
                tm " I'm Temero Neo! Call me Temero or Neo, I don't mind. "
                tm " So, how'd you like it? My 'mad scientist side'? "
                " You thought about what you saw while Temero was acting as if she was a mad scientist of some sorts... "
                if kind == True:
                    " You told her that she'd make a great villain! "
                elif calm == True:
                    " You told her that she'd make a great villain. "
                elif mean == True:
                    " You told her that her evil scientist thing needed a little bit of work, but she'd still make a great villain. "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " Hell yes I would! "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " I'm gonna work on doing more evil things, heheh... "
                tm " Like torturing people who like kids in a romantic way... those people are disgusting... "
                hide temeroneutral at bottom
                show temerohappy at center
                tm " So I'm gonna test all sorts of potions on them when I get my hands on one! "
                hide temerohappy at bottom
                show temeroneutral at center
                tm " Well, technically, I'm doing the world by doing a favor. "
                tm " But I'd love to hear their cries of pain! "
                play sound "audio/bellring.mp3"
                pause 1.0
                hide temeroneutral at bottom
                show temeroangry at center
                tm " Oh, eugh. I almost forgot that we still had class. "
                hide temeroangry at bottom
                show temeroneutral at center
                tm " Whatever! We can still talk later, [name]. "
                tm " See you in class! "
                hide temeroneutral at left with easeoutleft
                scene black with dissolve
                " You went to your classroom right after Temero left. "
                pause 2.0
                jump ocpeclass1
        label ocgym2:
            # Jacob + Koa
            scene black with dissolve
            pause 2.0
            scene gym with dissolve
            " You walk into the gym. I'm honestly liking the quietness in here! "
            " Oh wait, there's those two emo bad boy kids from your class that's here. "
            " You wanna approach them? "
            menu:
                " Hell nah, I don't wanna get the emo virus ":
                    " Yeah, no... that sounds a bit offensive. "
                    " Sorry if this offended anyone btw I didn't mean it/srs :sob: "
                    " Anyway, you just decided to sit near the corner of the bleachers and looked at your phone for anything interesting. "
                    scene black with dissolve
                    " You spent the entire break scrolling on tiktok out of pure boredom. "
                    " Nothing was interesting happening on tiktok, yet you didn't have anything else to do, so... "
                    " You just stayed scrolling instead of actually socializing. "
                    play sound "audio/bellring.mp3"
                    " But alas, one can't scroll on tiktok for the entire school day. The bell rang so your scrolling session is over. "
                    " Time to get up and go back to your next cla-{nw} "
                    " Wait, you're already here for your next class. You don't have to go anywhere. "
                    " Uh, let's just make you walk around the school for a bit and uhhh "
                    jump ocpeclass1
                " yk what let's talk to them ":
                    " Alright...let's go talk to the gacha life bad boys. "
                    show jacobneutral at left with easeinright
                    show koaneutral at right with easeinright
                    if jacobknow == True and koaknow == True:
                        k " You know, dude... "
                        jac " ...??? "
                        k " Sometimes I wonder what your eyes look like. Since you have those goggles on all the time. "
                        jac " ...You don't want to know what I look like underneath my goggles. "
                        k " It can't be that bad. But I mean, if you are uncomfortable with it then I won't talk about it anymore. "
                        jac " Yeah, I'm not really comfortable talking about my goggles. I don't like people touching them either. And my bandana. "
                        k " ...I'll try my best to avoid touching those, then. "
                        " And then there's awkward silence. "
                        " Maybe you should just go on your phone... "
                        " You pulled your phone out of your pocket and started to watch random ass tiktok videos. "
                        scene black with dissolve
                        " You spent the entire break scrolling on tiktok out of pure boredom. "
                        " Nothing was interesting happening on tiktok, yet you didn't have anything else to do, so... "
                        " You just stayed scrolling instead of actually socializing. "
                        play sound "audio/bellring.mp3"
                        " But alas, one can't scroll on tiktok for the entire school day. The bell rang so your scrolling session is over. "
                        " Time to get up and go back to your next cla-{nw} "
                        " Wait, you're already here for your next class. You don't have to go anywhere. "
                        " Uh, let's just make you walk around the school for a bit and uhhh "
                        jump ocpeclass1
                    elif jacobknow == True and koaknow == False:
                        x " You know, dude... "
                        jac " ...??? "
                        x " Sometimes I wonder what your eyes look like. Since you have those goggles on all the time. "
                        jac " ...You don't want to know what I look like underneath my goggles. "
                        x " It can't be that bad. But I mean, if you are uncomfortable with it then I won't talk about it anymore. "
                        jac " Yeah, I'm not really comfortable talking about my goggles. I don't like people touching them either. And my bandana. "
                        x " ...I'll try my best to avoid touching those, then. "
                        " And then there's awkward silence. "
                        " Maybe you should just go on your phone... "
                        " You pulled your phone out of your pocket and started to watch random ass tiktok videos. "
                        scene black with dissolve
                        " You spent the entire break scrolling on tiktok out of pure boredom. "
                        " Nothing was interesting happening on tiktok, yet you didn't have anything else to do, so... "
                        " You just stayed scrolling instead of actually socializing. "
                        play sound "audio/bellring.mp3"
                        " But alas, one can't scroll on tiktok for the entire school day. The bell rang so your scrolling session is over. "
                        " Time to get up and go back to your next cla-{nw} "
                        " Wait, you're already here for your next class. You don't have to go anywhere. "
                        " Uh, let's just make you walk around the school for a bit and uhhh "
                        jump ocpeclass1
                    elif jacobknow == False and koaknow == True:
                        k " You know, dude... "
                        x " ...??? "
                        k " Sometimes I wonder what your eyes look like. Since you have those goggles on all the time. "
                        x " ...You don't want to know what I look like underneath my goggles. "
                        k " It can't be that bad. But I mean, if you are uncomfortable with it then I won't talk about it anymore. "
                        x " Yeah, I'm not really comfortable talking about my goggles. I don't like people touching them either. And my bandana. "
                        k " ...I'll try my best to avoid touching those, then. "
                        " And then there's awkward silence. "
                        " Maybe you should just go on your phone... "
                        " You pulled your phone out of your pocket and started to watch random ass tiktok videos. "
                        scene black with dissolve
                        " You spent the entire break scrolling on tiktok out of pure boredom. "
                        " Nothing was interesting happening on tiktok, yet you didn't have anything else to do, so... "
                        " You just stayed scrolling instead of actually socializing. "
                        play sound "audio/bellring.mp3"
                        " But alas, one can't scroll on tiktok for the entire school day. The bell rang so your scrolling session is over. "
                        " Time to get up and go back to your next cla-{nw} "
                        " Wait, you're already here for your next class. You don't have to go anywhere. "
                        " Uh, let's just make you walk around the school for a bit and uhhh "
                        jump ocpeclass1
                    else:
                        x " You know, dude... "
                        x " ...??? "
                        x " Sometimes I wonder what your eyes look like. Since you have those goggles on all the time. "
                        x " ...You don't want to know what I look like underneath my goggles. "
                        x " It can't be that bad. But I mean, if you are uncomfortable with it then I won't talk about it anymore. "
                        x " Yeah, I'm not really comfortable talking about my goggles. I don't like people touching them either. And my bandana. "
                        x " ...I'll try my best to avoid touching those, then. "
                        " And then there's awkward silence. "
                        " Maybe you should just go on your phone... "
                        " You pulled your phone out of your pocket and started to watch random ass tiktok videos. "
                        scene black with dissolve
                        " You spent the entire break scrolling on tiktok out of pure boredom. "
                        " Nothing was interesting happening on tiktok, yet you didn't have anything else to do, so... "
                        " You just stayed scrolling instead of actually socializing. "
                        play sound "audio/bellring.mp3"
                        " But alas, one can't scroll on tiktok for the entire school day. The bell rang so your scrolling session is over. "
                        " Time to get up and go back to your next cla-{nw} "
                        " Wait, you're already here for your next class. You don't have to go anywhere. "
                        " Uh, let's just make you walk around the school for a bit and uhhh "
                        jump ocpeclass1
        label occafe2:
            # Notive, orchid, disk
            scene black with dissolve
            pause 2.0
            scene cafeteria with dissolve
            " You walked into the cafeteria and spotted some of your classmates just hanging around. "
            " You're thinking about talking to them, but who do you talk to? "
            if notiveknow,orchidknow,jexknow == True:
                menu:
                    "{image=notiveicon} Notive {image=notiveicon}":
                        jump notivecafeint
                    " {image=orchidicon} Orchid {image=orchidicon} ":
                        jump orchidcafeint
                    "{image=jexicon} Jex {image=jexicon} ":
                        jump jexcafeint
                    " I'll sit alone. ":
                        jump aloneagain
            elif notiveknow,orchidknow == True and jexknow == False:
                menu:
                    "{image=notiveicon} Notive {image=notiveicon}":
                        jump notivecafeint
                    " {image=orchidicon} Orchid {image=orchidicon} ":
                        jump orchidcafeint
                    "{image=jexicon} A tall guy {image=jexicon} ":
                        jump jexcafeint
                    " I'll sit alone. ":
                        jump aloneagain
            elif notiveknow,jexknow == True and orchidknow == False:
                menu:
                    "{image=notiveicon} Notive {image=notiveicon}":
                        jump notivecafeint
                    " {image=orchidicon} A scene kid {image=orchidicon} ":
                        jump orchidcafeint
                    "{image=jexicon} Jex {image=jexicon} ":
                        jump jexcafeint
                    " I'll sit alone. ":
                        jump aloneagain
            elif orchidkow,jexknow == True and notiveknow == False:
                menu:
                    "{image=notiveicon} A nonbinary looking fellow {image=notiveicon}":
                        jump notivecafeint
                    " {image=orchidicon} Orchid {image=orchidicon} ":
                        jump orchidcafeint
                    "{image=jexicon} Jex {image=jexicon} ":
                        jump jexcafeint
                    " I'll sit alone. ":
                        jump aloneagain
            elif notiveknow == True and orchidknow,jexknow == False:
                menu:
                    "{image=notiveicon} Notive {image=notiveicon}":
                        jump notivecafeint
                    " {image=orchidicon} A scene kid {image=orchidicon} ":
                        jump orchidcafeint
                    "{image=jexicon} A tall guy {image=jexicon} ":
                        jump jexcafeint
                    " I'll sit alone. ":
                        jump aloneagain
            elif orchidknow == True and notiveknow,jexknow == False:
                menu:
                    "{image=notiveicon} A nonbinary looking fellow {image=notiveicon}":
                        jump notivecafeint
                    " {image=orchidicon} Orchid {image=orchidicon} ":
                        jump orchidcafeint
                    "{image=jexicon} A tall guy {image=jexicon} ":
                        jump jexcafeint
                    " I'll sit alone. ":
                        jump aloneagain
            elif jexknow == True and notiveknow,orchidknow == False:
                menu:
                    "{image=notiveicon} A nonbinary looking fellow {image=notiveicon}":
                        jump notivecafeint
                    " {image=orchidicon} A scene kid {image=orchidicon} ":
                        jump orchidcafeint
                    "{image=jexicon} Jex {image=jexicon} ":
                        jump jexcafeint
                    " I'll sit alone. ":
                        jump aloneagain
            else:
                menu:
                    "{image=notiveicon} A nonbinary looking fellow {image=notiveicon}":
                        jump notivecafeint
                    " {image=orchidicon} A scene kid {image=orchidicon} ":
                        jump orchidcafeint
                    "{image=jexicon} A tall guy {image=jexicon} ":
                        jump jexcafeint
                    " I'll sit alone. ":
                        jump aloneagain
            label notivecafeint:
                show notiveneutral at center with easeinright
                if notiveknow == True:
                    " Notive seems to be just staring off into space. "
                    " You tried to get their attention by shaking them a bit, and it worked. "
                    no " Oh! Hey there, [name]! "
                    no " I was kinda just...thinking about my life choices. "
                    no " It's a fun thing to do, actually. I like to do it whenever I'm bored! "
                    no " Do you want to think about our life choices together? "
                    " Yeah, sounds like a fun thing to do! "
                    no " Okay! "
                    no " All you have to do is think of the embarrassing things you've done in life so far and think about why you did those things! "
                    no " Ready? I'll go first! "
                    no " ... "
                    hide notiveneutral at bottom
                    show notivestare at center
                    no " ... "
                    " You start rethinking your life decisions... "
                    " Yeah, Notive is right. This IS a good idea. "
                    scene black with dissolve
                    " You spent the entire break rethinking your life decisions with Notive in the cafeteria. "
                    " Very fun thing to do, made you cringe at all of the embarrassing memories you just remembered. "
                    " You should do this more often! "
                    play sound "audio/bellring.mp3"
                    " The bell then rings, and you go back to your classroom for the next class. "
                    pause 2.0
                    jump ocpeclass1
                else:
                    " They to be just staring off into space. "
                    " You tried to get their attention by shaking them a bit, and it worked. "
                    x " Oh! Hey there, [name]! "
                    x " I don't think I got to introduce myself to you, so... "
                    $ notiveknow = True
                    no " I'm Notive!! "
                    no " I was kinda just...thinking about my life choices. "
                    no " It's a fun thing to do, actually. I like to do it whenever I'm bored! "
                    no " Do you want to think about our life choices together? "
                    " Yeah, sounds like a fun thing to do! "
                    no " Okay! "
                    no " All you have to do is think of the embarrassing things you've done in life so far and think about why you did those things! "
                    no " Ready? I'll go first! "
                    no " ... "
                    hide notiveneutral at bottom
                    show notivestare at center
                    no " ... "
                    " You start rethinking your life decisions... "
                    " Yeah, Notive is right. This IS a good idea. "
                    scene black with dissolve
                    " You spent the entire break rethinking your life decisions with Notive in the cafeteria. "
                    " Very fun thing to do, made you cringe at all of the embarrassing memories you just remembered. "
                    " You should do this more often! "
                    play sound "audio/bellring.mp3"
                    " The bell then rings, and you go back to your classroom for the next class. "
                    pause 2.0
                    jump ocpeclass1
            label orchidcafeint:
                show orchidneutral at center with easeinleft
                if orchidknow == True:
                    oc " Eugh, it's so boring in here without Koa... "
                    oc " He's literally one of the only friends I have in here. "
                    oc " ...Oh! [name]! Sup! "
                    oc " How're you doing? "
                    if kind == True:
                        " You told them that you were doing great! "
                    elif calm == True:
                        " You told him that you were doing fine. "
                    elif mean == True:
                        " You told her that you were doing okay. "
                    oc " That's good to hear! "
                    oc " I'm feeling a little bored myself. The guy I usually hang with is out with someone else. "
                    oc " Why not talk to someone else you ask? "
                    oc " ... "
                    oc " I hate socializing. "
                    oc " The only reason why me and Koa became friends was because of a group project we had to do! "
                    oc " We somewhat shared the same interests. "
                    oc " At first I was like, 'oh ew a group project'! But if that group project never had happened, I wouldn't get to have another friend to add to my tiny list of friends! "
                    oc " Heheh... I say tiny because I was mostly the kid who got ignored in elementary. "
                    oc " I never really interacted with anyone, and I would only speak when I was spoken to. "
                    oc " And I would speak to people who are my friends, like, a lot. "
                    oc " A reason why I don't interact with anyone other than my friends is because I'm afraid that I'm gonna make a mistake and they won't like me. "
                    oc " Plus, I don't share the same interest as them, so.. "
                    oc " Even if I tried to pretend that I knew what they're talking about, it would feel weird to me. As in: this doesn't feel right type of weird. "
                    oc " You get what I'm saying? "
                    oc " Probably not, but oh well. "
                    scene black with dissolve
                    " You spent the entire day listening to Orchid yap about different things. "
                    " Geez, whenever you're with them the way they switch topics is so fast. "
                    " You don't mind it at all though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings eventually, stopping Orchid from their yapping session. "
                    " You then go up so that you could go to the next class. "
                    pause 2.0
                    jump ocpeclass1
                else:
                    x " Eugh, it's so boring in here without Koa... "
                    x " He's literally one of the only friends I have in here. "
                    x " ...Oh! [name]! Sup! "
                    x " You're that new kid, yeah? I don't think I got to introduce myself to you yet. "
                    $ orchidknow = True
                    oc " I'm Orchid. I'm Agender and I use any pronouns! "
                    if koaknow == True:
                        oc " Koa talked to me about you earlier, actually! "
                        if kind == True:
                            oc " He said that you're very nice. "
                        elif calm == True:
                            oc " He said that you're very chill. "
                        elif mean == True:
                            oc " He said that you look mean, but you're really just chill. "
                        oc " Well, he really wasn't wrong about that! "
                    else:
                        pass
                    oc " Anyway... "
                    oc " How're you doing? "
                    if kind == True:
                        " You told them that you were doing great! "
                    elif calm == True:
                        " You told him that you were doing fine. "
                    elif mean == True:
                        " You told her that you were doing okay. "
                    oc " That's good to hear! "
                    oc " I'm feeling a little bored myself. The guy I usually hang with is out with someone else. "
                    oc " Why not talk to someone else you ask? "
                    oc " ... "
                    oc " I hate socializing. "
                    oc " The only reason why me and Koa became friends was because of a group project we had to do! "
                    oc " We somewhat shared the same interests. "
                    oc " At first I was like, 'oh ew a group project'! But if that group project never had happened, I wouldn't get to have another friend to add to my tiny list of friends! "
                    oc " Heheh... I say tiny because I was mostly the kid who got ignored in elementary. "
                    oc " I never really interacted with anyone, and I would only speak when I was spoken to. "
                    oc " And I would speak to people who are my friends, like, a lot. "
                    oc " A reason why I don't interact with anyone other than my friends is because I'm afraid that I'm gonna make a mistake and they won't like me. "
                    oc " Plus, I don't share the same interest as them, so.. "
                    oc " Even if I tried to pretend that I knew what they're talking about, it would feel weird to me. As in: this doesn't feel right type of weird. "
                    oc " You get what I'm saying? "
                    oc " Probably not, but oh well. "
                    scene black with dissolve
                    " You spent the entire day listening to Orchid yap about different things. "
                    " Geez, whenever you're with them the way they switch topics is so fast. "
                    " You don't mind it at all though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings eventually, stopping Orchid from their yapping session. "
                    " You then go up so that you could go to the next class. "
                    pause 2.0
                    jump ocpeclass1
            label jexcafeint:
                show jexneutral at center with easeinright
                if jexknow == True:
                    " Jex seems to be busy studying. "
                    " Time to disturb him. "
                    j " ...[name]. I didn't notice you there. "
                    j " Do you want to study with me? "
                    " ...You nod your head at first. "
                    j " Okay, so-{nw} "
                    scene black with dissolve
                    " You fell asleep the moment he spoke up. "
                    " Wonder how his reaction was like when he saw you fall asleep like that. "
                    " Probably flabbergasted. Mad, even. "
                    " Atleast you get to take a nap though. Sleeping in school hits different. "
                    play sound "audio/bellring.mp3"
                    " ...Until the bell rings. "
                    " Time to get up and runnning for the next class, [name]! "
                    " No more slacking off! "
                    pause 2.0
                    jump ocpeclass1
                else:
                    " He seems to be busy studying. "
                    " Time to disturb him. "
                    x " ...[name]. I didn't notice you there. "
                    x " Do you want to study with me? "
                    " ...You nod your head at first. "
                    x " Okay, so-{nw} "
                    scene black with dissolve
                    " You fell asleep the moment he spoke up. "
                    " Wonder how his reaction was like when he saw you fall asleep like that. "
                    " Probably flabbergasted. Mad, even. "
                    " Atleast you get to take a nap though. Sleeping in school hits different. "
                    play sound "audio/bellring.mp3"
                    " ...Until the bell rings. "
                    " Time to get up and runnning for the next class, [name]! "
                    " No more slacking off! "
                    pause 2.0
                    jump ocpeclass1
            label aloneagain:
                " Alright, time to sit alone again. "
                " You decided to put on your earphones that randomly spawned in your pockets and listen to some music. "
                scene black with dissolve
                " You chose some random frutiger aero playlist and you sort of just sat there and stared into space for a bit. "
                " You stared, and stared, and stared... "
                " Until you fell asleep in your seat. "
                " You weren't really planning to take a nap here, but uh... "
                " Atleast you get to take a little break, for now. Sleeping in school hits different. "
                play sound "audio/bellring.mp3"
                " ...Until the bell rings. "
                " Time to get up and runnning for the next class, [name]! "
                " No more slacking off! "
                pause 2.0
                jump ocpeclass1
        label ocrooftop2:
            # spark + nox
            scene black with dissolve
            pause 2.0
            scene rooftop with dissolve
            " You walk up to the rooftop, taking in the fresh air. "
            " You then spot two of your classmates talking with eachother. "
            " Curious, you walk up to them to see what they're talking about. "
            show sparkneutral at right with easeinleft
            show noxsleepy at left with easeinleft
            if sparkknow == True and noxknow == True:
                sp " You know, dude. I'm starting to get really concerned about your sleeping issues. "
                n " I know... I've been trying to take my meds, but it seems like I keep forgetting..."
                sp " Geez, man. Alright, I'm gonna have to remind you to take your meds the next time you need them. "
                n " Thank youuu... "
                sp " Anything to make you feel better, man. "
                sp " I just hope your sleeping thingy doesn't get worse. "
                n " Uh huh... "
                stop music fadeout 0.5
                sp " ...Wait. Hey, stay up. "
                n " I'm just feeling lightheaded...It's no big deal... "
                sp " No, just stay up for me real quick. "
                n " I just gotta... Close my eyes for a bit... "
                sp " Nox-{nw} "
                hide noxsleepy at bottom with easeoutbottom
                hide sparkneutral at bottom
                show sparksad at right
                sp " Fuck. "
                show sparksad at center with move
                sp " Come on, buddy...Let's get you to Mister Altrix. "
                " Spark then notices that you're there. "
                sp " [name], help me carry Nox down real quick. "
                sp " Please. "
                " You looked around and saw that there was no one else to help. "
                " So, you went over and you helped out Spark with carrying Nox. "
                " geez nox was heavy {nw} "
                scene black with dissolve
                " You helped Spark carry down Nox to Mister Altrix's classroom. "
                " Mister Altrix said that he'll take care of Nox for now once you and Spark arrived to his classroom. "
                play sound "audio/bellring.mp3"
                " The bell rang, indicating that it was time for another class. "
                " You went out to go back to your classroom, wondering if Nox was going to be okay. "
                pause 2.0
                play music "audio/paperhigh.mp3" fadein 0.5
                jump ocpeclass1
            elif sparkknow == True and noxknow == False:
                sp " You know, dude. I'm starting to get really concerned about your sleeping issues. "
                x " I know... I've been trying to take my meds, but it seems like I keep forgetting..."
                sp " Geez, man. Alright, I'm gonna have to remind you to take your meds the next time you need them. "
                x " Thank youuu... "
                sp " Anything to make you feel better, man. "
                sp " I just hope your sleeping thingy doesn't get worse. "
                x " Uh huh... "
                stop music fadeout 0.5
                sp " ...Wait. Hey, stay up. "
                x " I'm just feeling lightheaded...It's no big deal... "
                sp " No, just stay up for me real quick. "
                x " I just gotta... Close my eyes for a bit... "
                sp " Nox-{nw} "
                hide noxsleepy at bottom with easeoutbottom
                hide sparkneutral at bottom
                show sparksad at right
                sp " Fuck. "
                show sparksad at center with move
                sp " Come on, buddy...Let's get you to Mister Altrix. "
                " Spark then notices that you're there. "
                sp " [name], help me carry Nox down real quick. "
                sp " Please. "
                " You looked around and saw that there was no one else to help. "
                " So, you went over and you helped out Spark with carrying the other guy. "
                " geez nox was heavy {nw} "
                scene black with dissolve
                " You helped Spark carry down the guy to Mister Altrix's classroom. "
                " Mister Altrix said that he'll take care of the guy for now once you and Spark arrived to his classroom. "
                play sound "audio/bellring.mp3"
                " The bell rang, indicating that it was time for another class. "
                " You went out to go back to your classroom, wondering if that guy was going to be okay. "
                pause 2.0
                play music "audio/paperhigh.mp3" fadein 0.5
                jump ocpeclass1
            elif sparkknow == False and noxknow == True:
                x " You know, dude. I'm starting to get really concerned about your sleeping issues. "
                n " I know... I've been trying to take my meds, but it seems like I keep forgetting..."
                x " Geez, man. Alright, I'm gonna have to remind you to take your meds the next time you need them. "
                n " Thank youuu... "
                x " Anything to make you feel better, man. "
                x " I just hope your sleeping thingy doesn't get worse. "
                n " Uh huh... "
                stop music fadeout 0.5
                x " ...Wait. Hey, stay up. "
                n " I'm just feeling lightheaded...It's no big deal... "
                x " No, just stay up for me real quick. "
                n " I just gotta... Close my eyes for a bit... "
                x " Nox-{nw} "
                hide noxsleepy at bottom with easeoutbottom
                hide sparkneutral at bottom
                show sparksad at right
                x " Fuck. "
                show sparksad at center with move
                x " Come on, buddy...Let's get you to Mister Altrix. "
                " He then notices that you're there. "
                x " [name], help me carry Nox down real quick. "
                x " Please. "
                " You looked around and saw that there was no one else to help. "
                " So, you went over and you helped him out with carrying Nox. "
                " geez nox was heavy {nw} "
                scene black with dissolve
                " You helped The other guy carry down Nox to Mister Altrix's classroom. "
                " Mister Altrix said that he'll take care of Nox for now once you and the other guy arrived to his classroom. "
                play sound "audio/bellring.mp3"
                " The bell rang, indicating that it was time for another class. "
                " You went out to go back to your classroom, wondering if Nox was going to be okay. "
                pause 2.0
                play music "audio/paperhigh.mp3" fadein 0.5
                jump ocpeclass1
            else:
                x " You know, dude. I'm starting to get really concerned about your sleeping issues. "
                x " I know... I've been trying to take my meds, but it seems like I keep forgetting..."
                x " Geez, man. Alright, I'm gonna have to remind you to take your meds the next time you need them. "
                x " Thank youuu... "
                x " Anything to make you feel better, man. "
                x " I just hope your sleeping thingy doesn't get worse. "
                x " Uh huh... "
                stop music fadeout 0.5
                x " ...Wait. Hey, stay up. "
                x " I'm just feeling lightheaded...It's no big deal... "
                x " No, just stay up for me real quick. "
                x " I just gotta... Close my eyes for a bit... "
                x " Nox-{nw} "
                hide noxsleepy at bottom with easeoutbottom
                hide sparkneutral at bottom
                show sparksad at right
                x " Fuck. "
                show sparksad at center with move
                x " Come on, buddy...Let's get you to Mister Altrix. "
                " He then notices that you're there. "
                x " [name], help me carry Nox down real quick. "
                x " Please. "
                " You looked around and saw that there was no one else to help. "
                " So, you went over and you helped him out with carrying the other guy. "
                " geez this guy was heavy {nw} "
                scene black with dissolve
                " You helped The other guy carry down the sleepy guy to Mister Altrix's classroom. "
                " Mister Altrix said that he'll take care of the sleepy guy for now once you and the other guy arrived to his classroom. "
                play sound "audio/bellring.mp3"
                " The bell rang, indicating that it was time for another class. "
                " You went out to go back to your classroom, wondering if the sleepy guy was going to be okay. "
                pause 2.0
                play music "audio/paperhigh.mp3" fadein 0.5
                jump ocpeclass1
        label oclibrary2:
            # Carmen + Quinn
            scene black with dissolve
            pause 2.0
            scene library with dissolve
            " You walk into the library, looking at some of the books that were there. "
            " Some were interesting, some weren't. "
            " You were just walking around until you spotted two of your classmates talking about something. "
            " Curious, you decided to walk up to them to see what they were talking about. "
            show carmenneutral at right with easeinleft
            show quinnneutral at left with easeinleft
            if quinnknow == True and carmenknow == True:
                q " So, Carmen... I was thinking that you could maybe be our background musician? "
                ca " ...? "
                q " Yeah, you! You're the best guitar player here, I know that you'd do great! "
                ca " ... "
                hide carmenneutral at bottom
                show carmenhappy at right
                ca " ...! "
                hide quinnneutral at bottom
                show quinnhappy at left
                q " You'll do it? That's awesome! "
                q " I'll tell the others then! Thank you, Carmen! "
                ca " !! "
                hide quinnhappy at bottom
                show quinnneutral at left
                hide carmenhappy at bottom
                show carmenneutral at right
                " Carmen and Quinn then notice that you're there. "
                q " Oh, [name]! We were just talking about what we're going to be doing for the play my club is doing! "
                ca " !! :D "
                q " Carmen's gonna be the one that's gonna make the background music for us! "
                q " Isn't that going to be cool? "
                ca " :D "
                q " It's gonna be real fun! People are gonna LOVE you Carmen! "
                ca " :O "
                q " Yeah, you! People are gonna really like your guitar skills! "
                q " I already like them a lot, but I'm gonna love them when we actually do the real thing! "
                q " This is your chance to show off your talent to the world, Carmen! "
                hide carmenneutral at bottom
                show carmenhappy at right
                ca " !! "
                scene black with dissolve
                " You spent the entire break talking with Quinn and Carmen about what was going to happen in the play. "
                " You're not even apart of the play but it was interesting getting to know some things that's gonna happen in there. "
                " You feel pretty happy about Carmen getting to show off his guitar skills. "
                " Atleast you're gonna have a bit of spoilers of what's going to happen. Heheh... "
                play sound "audio/bellring.mp3"
                " The bell rings, meaning that it was time for another class. "
                " You then get up from your seat and you went outside the library to go back to your classroom. "
                pause 2.0
                jump ocpeclass1
            elif quinnknow == True and carmenknow == False:
                q " So, Carmen... I was thinking that you could maybe be our background musician? "
                x " ...? "
                q " Yeah, you! You're the best guitar player here, I know that you'd do great! "
                x " ... "
                hide carmenneutral at bottom
                show carmenhappy at right
                x " ...! "
                hide quinnneutral at bottom
                show quinnhappy at left
                q " You'll do it? That's awesome! "
                q " I'll tell the others then! Thank you, Carmen! "
                x " !! "
                hide quinnhappy at bottom
                show quinnneutral at left
                hide carmenhappy at bottom
                show carmenneutral at right
                " The guitar guy and Quinn then notice that you're there. "
                q " Oh, [name]! We were just talking about what we're going to be doing for the play my club is doing! "
                q " Wait, you and Carmen haven't met before, yes? "
                q " Well, let me introduce him to you! "
                $ carmenknow = True
                q " This is Carmen, he likes to play the guitar a lot! And he's mute. He knows sign language. "
                ca " !! :D "
                q " Anywho... "
                q " Carmen's gonna be the one that's gonna make the background music for us! "
                q " Isn't that going to be cool? "
                ca " :D "
                q " It's gonna be real fun! People are gonna LOVE you Carmen! "
                ca " :O "
                q " Yeah, you! People are gonna really like your guitar skills! "
                q " I already like them a lot, but I'm gonna love them when we actually do the real thing! "
                q " This is your chance to show off your talent to the world, Carmen! "
                hide carmenneutral at bottom
                show carmenhappy at right
                ca " !! "
                scene black with dissolve
                " You spent the entire break talking with Quinn and Carmen about what was going to happen in the play. "
                " You're not even apart of the play but it was interesting getting to know some things that's gonna happen in there. "
                " You feel pretty happy about Carmen getting to show off his guitar skills. "
                " Atleast you're gonna have a bit of spoilers of what's going to happen. Heheh... "
                play sound "audio/bellring.mp3"
                " The bell rings, meaning that it was time for another class. "
                " You then get up from your seat and you went outside the library to go back to your classroom. "
                pause 2.0
                jump ocpeclass1
            elif quinnknow == False and carmenknow == True:
                x " So, Carmen... I was thinking that you could maybe be our background musician? "
                ca " ...? "
                x " Yeah, you! You're the best guitar player here, I know that you'd do great! "
                ca " ... "
                hide carmenneutral at bottom
                show carmenhappy at right
                ca " ...! "
                hide quinnneutral at bottom
                show quinnhappy at left
                x " You'll do it? That's awesome! "
                x " I'll tell the others then! Thank you, Carmen! "
                ca " !! "
                hide quinnhappy at bottom
                show quinnneutral at left
                hide carmenhappy at bottom
                show carmenneutral at right
                " Carmen and The other guy then notice that you're there. "
                x " Oh, [name]! We were just talking about what we're going to be doing for the play my club is doing! "
                ca " !! :D "
                x " Wait, I don't believe that I've gotten to introduce myself to you. My apologies. "
                $ quinnknow = True
                q " I'm Quinn! I'm in the drama club, and Carmen's one of my dearest friends! "
                q " Anywho, Carmen's gonna be the one that's gonna make the background music for us in the play! "
                q " Isn't that going to be cool? "
                ca " :D "
                q " It's gonna be real fun! People are gonna LOVE you Carmen! "
                ca " :O "
                q " Yeah, you! People are gonna really like your guitar skills! "
                q " I already like them a lot, but I'm gonna love them when we actually do the real thing! "
                q " This is your chance to show off your talent to the world, Carmen! "
                hide carmenneutral at bottom
                show carmenhappy at right
                ca " !! "
                scene black with dissolve
                " You spent the entire break talking with Quinn and Carmen about what was going to happen in the play. "
                " You're not even apart of the play but it was interesting getting to know some things that's gonna happen in there. "
                " You feel pretty happy about Carmen getting to show off his guitar skills. "
                " Atleast you're gonna have a bit of spoilers of what's going to happen. Heheh... "
                play sound "audio/bellring.mp3"
                " The bell rings, meaning that it was time for another class. "
                " You then get up from your seat and you went outside the library to go back to your classroom. "
                pause 2.0
                jump ocpeclass1
            else:
                x " So, Carmen... I was thinking that you could maybe be our background musician? "
                x " ...? "
                x " Yeah, you! You're the best guitar player here, I know that you'd do great! "
                x " ... "
                hide carmenneutral at bottom
                show carmenhappy at right
                x " ...! "
                hide quinnneutral at bottom
                show quinnhappy at left
                x " You'll do it? That's awesome! "
                x " I'll tell the others then! Thank you, Carmen! "
                x " !! "
                hide quinnhappy at bottom
                show quinnneutral at left
                hide carmenhappy at bottom
                show carmenneutral at right
                " The two guys then notice that you're there. "
                x " Oh, [name]! We were just talking about what we're going to be doing for the play my club is doing! "
                x " !! :D "
                x " Wait, I don't believe that I've gotten to introduce myself to you. My apologies. "
                $ quinnknow = True
                q " I'm Quinn! I'm in the drama club, and Carmen's one of my dearest friends! "
                q " And, I don't think you've met Carmen yet, no? "
                q " I'll do the introducing for him, then. "
                $ carmenknow = True
                q " This is Carmen! He likes to play the guitar, and he's mute. He's a nice guy!! "
                ca " !! :3 "
                q " Anywho, Carmen's gonna be the one that's gonna make the background music for us in the play! "
                q " Isn't that going to be cool? "
                ca " :D "
                q " It's gonna be real fun! People are gonna LOVE you Carmen! "
                ca " :O "
                q " Yeah, you! People are gonna really like your guitar skills! "
                q " I already like them a lot, but I'm gonna love them when we actually do the real thing! "
                q " This is your chance to show off your talent to the world, Carmen! "
                hide carmenneutral at bottom
                show carmenhappy at right
                ca " !! "
                scene black with dissolve
                " You spent the entire break talking with Quinn and Carmen about what was going to happen in the play. "
                " You're not even apart of the play but it was interesting getting to know some things that's gonna happen in there. "
                " You feel pretty happy about Carmen getting to show off his guitar skills. "
                " Atleast you're gonna have a bit of spoilers of what's going to happen. Heheh... "
                play sound "audio/bellring.mp3"
                " The bell rings, meaning that it was time for another class. "
                " You then get up from your seat and you went outside the library to go back to your classroom. "
                pause 2.0
                jump ocpeclass1
        label ocpeclass1:
            " So, turns out that you're having class in the gym. "
            " Great, you can already guess that this was going to be PE class. "
            " Time to suffer going to the gym. "
            pause 2.0
            scene gym with dissolve
            " You walk into the gym to see that all of your classmates were already there. "
            " But, you couldn't see where the teacher was. "
            " You were somewhat praying that the teacher wouldn't be there, but lo and behold... "
            " BOOM! someone kicked the door to the gym open! " with vpunch
            " And then a loud and energetic voic started talking as they walked right up infront of all of you. "
            show solneutral at center with easeinleft
            x " HEY HEY HEY!! You all better be energized and awake for this class! No sleeping! No acting all gloomy! Get some smiles on those faces! "
            show diskjoyous at left with easeinleft
            if diskknow == True:
                d " Hi uncle!!! "
            else:
                x " Hi uncle!!! "
            hide diskjoyous at left with easeoutleft
            show quinnhappy at left with easeinleft
            if quinnknow == True:
                q " Hi, uncle. "
            else:
                x " Hi, uncle. "
            hide quinnhappy at left with easeoutleft
            show mattehappy at right with easeinright
            if matteknow == True:
                ma " Hi, dad. "
            else:
                x " Hi, dad. "
            hide mattehappy at right with easeoutright
            hide solneutral at bottom
            show solhappy at center
            x " HELLO MY LITTLE BALLS OF SUNSHINE!! "
            hide solhappy at bottom
            show solneutral at center
            x " So, I have two things that I'd like to say before we start our class! "
            x " Number one is that Nox is going to be skipping again because he had a slight problem. He's going to be with Mister Altrix for now. "
            x " Number two is that I heard that we have a new family member! "
            if they == "she","he":
                x " Now, could someone tell me where [they] is? "
            elif they == "they":
                x " Now, could someone tell me where [they] are? "
            show yangyihappy at right with easeinright
            if yinhuiknow == True:
                ya " [they] [are] right here, sir! "
                " Yangyi pointed to where you were. "
            else:
                ya " [they] [are] right here, sir! "
                " The guy pointed to where you were. "
            hide yangyihappy at right with easeoutright
            " The teacher then looked over to where you were and brought you up next to him. "
            x " This is going to be our new family member! "
            x " Now, kid. Tell me what's your name? Don't be shy, I don't bite! "
            " You told him that your name was [name]. Geez, this class was energetic. In a good way. "
            hide solneutral at bottom
            show solhappy at center
            x " [name]! Lovely name there! I like it! "
            msso " I am Mister Sol! Your PE teacher! "
            msso " Welcome to the family! "
            " You could hear your classmates cheering. Wowzers... "
            " He then put you back to where you were standing earlier. "
            hide solhappy at bottom
            show solneutral at center
            msso " Now that we're done with the little introduction, let's get started with our lesson! "
            scene black with dissolve
            " For once, you actually had fun in gym class. "
            " How could you not with everyone being this energetic and happy? Even the teacher is acting real energetic. "
            " Maybe this school isn't so bad... "
            pause 1.0
            play sound "audio/bellring.mp3"
            " The bell rang after awhile, meaning that it was time for another break. "
            " You waited for everyone else to get out of the gym before you could. "
            pause 2.0
            jump ocbreak3
    label ocbreak3:
        scene hallway with dissolve
        " It's the third break of the day, and you're thinking about exploring the school more. "
        " Where do you want to go? "
        menu:
            " {image=sparkicon} The front of the school {image=miaicon} ":
                jump ocfrontschool3
            " {image=jamicon} The back of the school {image=carmenicon} ":
                jump ocbackschool3
            " {image=matteicon} The gym {image=diskicon} ":
                jump ocgym3
            " The cafeteria ":
                jump occafe3
            " {image=jacobicon} The rooftop {image=temeroicon} ":
                jump ocrooftop3
            " The library ":
                jump oclibrary3
        label ocfrontschool3:
            # Spark + Mia
            # mia touches spark's antennas
            scene black with dissolve
            pause 2.0
            scene paperschoolfront with dissolve
            " You walked outside the school to get some more fresh air, when ofcourse... "
            " You hear two of your classmates talking with eachother. "
            " Do you want to approach them, or do you just want to relax for a bit? "
            menu:
                " Walk up to them ":
                    " Let's go. "
                    show sparkangry at right with easeinleft
                    show miahappy at left with easeinleft
                    if sparkknow == True and miaknow == True:
                        sp " I told you Mia, not to touch my antennas. "
                        m " Can I touch your tail then? "
                        sp " No. Touching my tail is worse than touching my antennas. "
                        m " Then let me touch your antennas! "
                        sp " Sigh...just because touching my tail is worse, doesn't mean that touching my antennas is okay. "
                        hide miahappy at bottom
                        show miasad at left
                        m " Awhhh... "
                        sp " That look is not going to work on me, Mia. "
                        sp " This is the 4th time you've tried to touch my antennas and tail already... "
                        hide sparkangry at bottom
                        show sparkneutral at right
                        sp " If you touch my tail and antennas, then you'd get electrocuted to death. "
                        sp " And I don't want to get your parents to yell at me for killing their child. "
                        sp " (I also don't want to get fired for killing someone innocent.) "
                        sp " Now, how about you go, um... water your plants? "
                        hide miasad at bottom
                        show mianeutral at left
                        m " Oh, right! I had forgotten to water them! Thanks for reminding me, Spark! "
                        hide mianeutral at right with easeoutright
                        " Mia then skedaddled away to go water her plants. "
                        show sparkneutral at center with move
                        sp " Sigh... how many times do I gotta tell that girl to stop trying to touch... "
                        sp " ...Hi, [name]. I was too focused on talking to Mia to figure out that you were standing there. "
                        " You asked him what he meant by being 'fired'. "
                        sp " That's nothing important. "
                        " For a split moment, you could see Spark's antennas glow yellow for a bit before turning back into their normal color. "
                        sp " I also have to go now. I'll see you later. "
                        hide sparkneutral at left with easeoutleft
                        " Spark's acting weird. We should probably follow him. "
                        scene black with dissolve
                        " You tried to follow Spark, but got distracted when you accidentally bumped into someone and made them drop all of their things. "
                        " Feeling bad, you helped them get all of their things back and even helping them put their things into their locker. "
                        " Successfully making you forget about Spark. For now. "
                        play sound "audio/bellring.mp3"
                        " After you helped that person out, the bell rang, meaning that it was time for the next class. "
                        " You then made your way to your classroom after a minute of thinking about something you had forgotten. "
                        pause 2.0
                        jump ocgardeningclass1
                    elif sparkknow == True and miaknow == False:
                        sp " I told you Mia, not to touch my antennas. "
                        x " Can I touch your tail then? "
                        sp " No. Touching my tail is worse than touching my antennas. "
                        x " Then let me touch your antennas! "
                        sp " Sigh...just because touching my tail is worse, doesn't mean that touching my antennas is okay. "
                        hide miahappy at bottom
                        show miasad at left
                        x " Awhhh... "
                        sp " That look is not going to work on me, Mia. "
                        sp " This is the 4th time you've tried to touch my antennas and tail already... "
                        hide sparkangry at bottom
                        show sparkneutral at right
                        sp " If you touch my tail and antennas, then you'd get electrocuted to death. "
                        sp " And I don't want to get your parents to yell at me for killing their child. "
                        sp " (I also don't want to get fired for killing someone innocent.) "
                        sp " Now, how about you go, um... water your plants? "
                        hide miasad at bottom
                        show mianeutral at left
                        x " Oh, right! I had forgotten to water them! Thanks for reminding me, Spark! "
                        hide mianeutral at right with easeoutright
                        " The girl then skedaddled away to go water her plants. "
                        show sparkneutral at center with move
                        sp " Sigh... how many times do I gotta tell that girl to stop trying to touch... "
                        sp " ...Hi, [name]. I was too focused on talking to Mia to figure out that you were standing there. "
                        " You asked him what he meant by being 'fired'. "
                        sp " That's nothing important. "
                        " For a split moment, you could see Spark's antennas glow yellow for a bit before turning back into their normal color. "
                        sp " I also have to go now. I'll see you later. "
                        hide sparkneutral at left with easeoutleft
                        " Spark's acting weird. We should probably follow him. "
                        scene black with dissolve
                        " You tried to follow Spark, but got distracted when you accidentally bumped into someone and made them drop all of their things. "
                        " Feeling bad, you helped them get all of their things back and even helping them put their things into their locker. "
                        " Successfully making you forget about Spark. For now. "
                        play sound "audio/bellring.mp3"
                        " After you helped that person out, the bell rang, meaning that it was time for the next class. "
                        " You then made your way to your classroom after a minute of thinking about something you had forgotten. "
                        pause 2.0
                        jump ocgardeningclass1
                    elif sparkknow == False and miaknow == True:
                        x " I told you Mia, not to touch my antennas. "
                        m " Can I touch your tail then? "
                        x " No. Touching my tail is worse than touching my antennas. "
                        m " Then let me touch your antennas! "
                        x " Sigh...just because touching my tail is worse, doesn't mean that touching my antennas is okay. "
                        hide miahappy at bottom
                        show miasad at left
                        m " Awhhh... "
                        x " That look is not going to work on me, Mia. "
                        x " This is the 4th time you've tried to touch my antennas and tail already... "
                        hide sparkangry at bottom
                        show sparkneutral at right
                        x " If you touch my tail and antennas, then you'd get electrocuted to death. "
                        x " And I don't want to get your parents to yell at me for killing their child. "
                        x " (I also don't want to get fired for killing someone innocent.) "
                        x " Now, how about you go, um... water your plants? "
                        hide miasad at bottom
                        show mianeutral at left
                        m " Oh, right! I had forgotten to water them! Thanks for reminding me, Spark! "
                        hide mianeutral at right with easeoutright
                        " Mia then skedaddled away to go water her plants. "
                        show sparkneutral at center with move
                        x " Sigh... how many times do I gotta tell that girl to stop trying to touch... "
                        x " ...Hi, [name]. I was too focused on talking to Mia to figure out that you were standing there. "
                        $ sparkknow = True
                        sp " I'm Spark, by the way. Don't think I ever told you my name. "
                        " You told him that it was nice to meet him, and then you asked him what he meant by being 'fired'. "
                        sp " That's nothing important. "
                        " For a split moment, you could see Spark's antennas glow yellow for a bit before turning back into their normal color. "
                        sp " I also have to go now. I'll see you later. "
                        hide sparkneutral at left with easeoutleft
                        " Spark's acting weird. We should probably follow him. "
                        scene black with dissolve
                        " You tried to follow Spark, but got distracted when you accidentally bumped into someone and made them drop all of their things. "
                        " Feeling bad, you helped them get all of their things back and even helping them put their things into their locker. "
                        " Successfully making you forget about Spark. For now. "
                        play sound "audio/bellring.mp3"
                        " After you helped that person out, the bell rang, meaning that it was time for the next class. "
                        " You then made your way to your classroom after a minute of thinking about something you had forgotten. "
                        pause 2.0
                        jump ocgardeningclass1
                    else:
                        x " I told you Mia, not to touch my antennas. "
                        x " Can I touch your tail then? "
                        x " No. Touching my tail is worse than touching my antennas. "
                        x " Then let me touch your antennas! "
                        x " Sigh...just because touching my tail is worse, doesn't mean that touching my antennas is okay. "
                        hide miahappy at bottom
                        show miasad at left
                        x " Awhhh... "
                        x " That look is not going to work on me, Mia. "
                        x " This is the 4th time you've tried to touch my antennas and tail already... "
                        hide sparkangry at bottom
                        show sparkneutral at right
                        x " If you touch my tail and antennas, then you'd get electrocuted to death. "
                        x " And I don't want to get your parents to yell at me for killing their child. "
                        x " (I also don't want to get fired for killing someone innocent.) "
                        x " Now, how about you go, um... water your plants? "
                        hide miasad at bottom
                        show mianeutral at left
                        x " Oh, right! I had forgotten to water them! Thanks for reminding me, Spark! "
                        hide mianeutral at right with easeoutright
                        " The girl then skedaddled away to go water her plants. "
                        show sparkneutral at center with move
                        x " Sigh... how many times do I gotta tell that girl to stop trying to touch... "
                        x " ...Hi, [name]. I was too focused on talking to Mia to figure out that you were standing there. "
                        $ sparkknow = True
                        sp " I'm Spark, by the way. Don't think I ever told you my name. "
                        " You told him that it was nice to meet him, and then you asked him what he meant by being 'fired'. "
                        sp " That's nothing important. "
                        " For a split moment, you could see Spark's antennas glow yellow for a bit before turning back into their normal color. "
                        sp " I also have to go now. I'll see you later. "
                        hide sparkneutral at left with easeoutleft
                        " Spark's acting weird. We should probably follow him. "
                        scene black with dissolve
                        " You tried to follow Spark, but got distracted when you accidentally bumped into someone and made them drop all of their things. "
                        " Feeling bad, you helped them get all of their things back and even helping them put their things into their locker. "
                        " Successfully making you forget about Spark. For now. "
                        play sound "audio/bellring.mp3"
                        " After you helped that person out, the bell rang, meaning that it was time for the next class. "
                        " You then made your way to your classroom after a minute of thinking about something you had forgotten. "
                        pause 2.0
                        jump ocgardeningclass1
                " No thanks ":
                    " Yeah, alright. You just came here for a tiny little break anyway. "
                    " You sat down somewhere and you pulled out your phone so that you could atleast be somewhat entertained. "
                    " Time to scroll through social media for the entire break... "
                    scene black with dissolve
                    " You spent the entire break scrolling through social media. "
                    " Finally, something interesting caught your attention. "
                    " Apparently there was going to be a play sometime this week. The play is going to take place in this school. "
                    " Not too interesting, but it's something, at least. "
                    play sound "audio/bellring.mp3"
                    " The bell then rang after about 30 minutes of scrolling on social media. "
                    " You got up from where you were sitting, and you went to the next class. "
                    pause 2.0
                    jump ocgardeningclass1
        label ocbackschool3:
            # Jam + Carmen
            scene black with dissolve
            pause 2.0
            scene paperschoolback with dissolve
            " You walk into the back of the school to listen to some music. "
            " You walked aorund to find a good place to sit and you find two of your classmates doing their own things. "
            " You're thinking about talking to one of them...who do you talk to? "
            if jamknow == True and carmenknow == True:
                menu:
                    " {image=jamicon} Jam {image=jamicon} ":
                        jump jambackschoolint
                    " {image=carmenicon} Carmen {image=carmenicon} ":
                        jump carmenbackschoolint
                    " Nah, I'd rather be alone ":
                        jump alonebackschool
            elif jamknow == True and carmenknow == False:
                menu:
                    " {image=jamicon} Jam {image=jamicon} ":
                        jump jambackschoolint
                    " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                        jump carmenbackschoolint
                    " Nah, I'd rather be alone ":
                        jump alonebackschool
            elif jamknow == False and carmenknow == True:
                menu:
                    " {image=jamicon} A girl that's gaming {image=jamicon} ":
                        jump jambackschoolint
                    " {image=carmenicon} Carmen {image=carmenicon} ":
                        jump carmenbackschoolint
                    " Nah, I'd rather be alone ":
                        jump alonebackschool
            else:
                menu:
                    " {image=jamicon} A girl that's gaming {image=jamicon} ":
                        jump jambackschoolint
                    " {image=carmenicon} A guy with a guitar {image=carmenicon} ":
                        jump carmenbackschoolint
                    " Nah, I'd rather be alone ":
                        jump alonebackschool
            label jambackschoolint:
                # gaming and ranting
                " You walked up to the girl that's gaming and you sat down next to her. "
                show jamgame at center with easeinbottom
                if jamknow == True:
                    " You watched what she was playing before you noticed that she was whispering something to herself. "
                    " You asked her if she was okay. "
                    ja " ...'M fine. Just... been having some thoughts on a fandom. "
                    hide jamgame at bottom
                    show jamneutral at center
                    ja " Uh, are you comfortable with me ranting for a bit? I just need to let some steam out. "
                    " You told her that it was fine. "
                    ja " Okay... "
                    hide jamneutral at bottom
                    show jamgame at center
                    ja " So, I'm in a certain fandom and there's been some drama lately... "
                    ja " Specifically shipping drama. You know, where people make a character and another character to be in a relationship? "
                    ja " Of course, there's people that won't like the ships you ship. And sometimes, those people hate you so much that they'll do mean things to you. "
                    ja " Well, the creator of the game just confirmed a popular ship to be canon and everyone went haywire. "
                    ja " They started attacking those shippers and they also started to harass the creator. "
                    ja " All because they didn't like it. "
                    ja " What happened to just scroll by whenever you see something you don't like? "
                    ja " If you don't like something, then just ignore it. Making a huge fuss about it won't solve anything. "
                    ja " Even if I don't like the relationship, I don't make a huge mess about it. "
                    ja " Jeez, sometimes I wonder why people act this way. "
                    ja " Like....making a huge fuss about something as stupid as this is insane. Childish, even. "
                    ja " Ship wars are stupid. Making drama about the tiniest things are stupid. "
                    ja " How are people like this? I have no idea. But I don't like it. "
                    ja " I heard people dox other people just for some stupid drama...How idiotic can humans get? "
                    ja " We're just devolving at this point. We're going backwards. "
                    ja " Where did we go wrong? No idea. Everything was so peaceful back then, what happened? "
                    ja " Geez. "
                    scene black with dissolve
                    " You listened to Jam rant for the entire break. "
                    " And honestly, she was spitting out facts with the fandom shipping part. "
                    " Sometimes people are just too dramatic. And it's mad annoying. "
                    " Sometimes you wish that everything would just go back to the good old days. "
                    " Compared to now, it feels like everyone was more respectful back in the days. "
                    " Rather than today. Everything and every fandom is a mess just because of people starting drama on the smallest things. "
                    " Gonna be for real here, but people need to {b}grow up{/b} about these things. "
                    " I know I can't really do much here, but atleast there's a few people that will atleast see this message. "
                    " Back to the game... "
                    play sound "audio/bellring.mp3"
                    " The bell rings, stopping Jam from ranting any further. "
                    " You then get up and walk back into the school to go to your next class. "
                    pause 2.0
                    jump ocgardeningclass1
                else:
                    " You watched what she was playing before you noticed that she was whispering something to herself. "
                    " You asked her if she was okay. "
                    x " ...'M fine. Just... been having some thoughts on a fandom. "
                    hide jamgame at bottom
                    show jamneutral at center
                    x " Wait, hey... You're the new kid, right? "
                    x " Sorry, I can't really remember that well. I don't think I've introduced myself yet to you though... "
                    $ jamknow = True
                    ja " I'm Jam. I uh...like to game. You can probably tell. "
                    ja " Uh, are you comfortable with me ranting for a bit? I just need to let some steam out. "
                    " You told her that it was fine. "
                    ja " Okay... "
                    hide jamneutral at bottom
                    show jamgame at center
                    ja " So, I'm in a certain fandom and there's been some drama lately... "
                    ja " Specifically shipping drama. You know, where people make a character and another character to be in a relationship? "
                    ja " Of course, there's people that won't like the ships you ship. And sometimes, those people hate you so much that they'll do mean things to you. "
                    ja " Well, the creator of the game just confirmed a popular ship to be canon and everyone went haywire. "
                    ja " They started attacking those shippers and they also started to harass the creator. "
                    ja " All because they didn't like it. "
                    ja " What happened to just scroll by whenever you see something you don't like? "
                    ja " If you don't like something, then just ignore it. Making a huge fuss about it won't solve anything. "
                    ja " Even if I don't like the relationship, I don't make a huge mess about it. "
                    ja " Jeez, sometimes I wonder why people act this way. "
                    ja " Like....making a huge fuss about something as stupid as this is insane. Childish, even. "
                    ja " Ship wars are stupid. Making drama about the tiniest things are stupid. "
                    ja " How are people like this? I have no idea. But I don't like it. "
                    ja " I heard people dox other people just for some stupid drama...How idiotic can humans get? "
                    ja " We're just devolving at this point. We're going backwards. "
                    ja " Where did we go wrong? No idea. Everything was so peaceful back then, what happened? "
                    ja " Geez. "
                    scene black with dissolve
                    " You listened to Jam rant for the entire break. "
                    " And honestly, she was spitting out facts with the fandom shipping part. "
                    " Sometimes people are just too dramatic. And it's mad annoying. "
                    " Sometimes you wish that everything would just go back to the good old days. "
                    " Compared to now, it feels like everyone was more respectful back in the days. "
                    " Rather than today. Everything and every fandom is a mess just because of people starting drama on the smallest things. "
                    " Gonna be for real here, but people need to {b}grow up{/b} about these things. "
                    " I know I can't really do much here, but atleast there's a few people that will atleast see this message. "
                    " Back to the game... "
                    play sound "audio/bellring.mp3"
                    " The bell rings, stopping Jam from ranting any further. "
                    " You then get up and walk back into the school to go to your next class. "
                    pause 2.0
                    jump ocgardeningclass1
            label carmenbackschoolint:
                # playing nice music
                " You walked up to the boy that has a guitar and you sat down next to him. "
                show carmenneutral at center with easeinbottom
                if carmenknow == True:
                    " He was playing some nice tunes on his guitar... "
                    " You pretty much just wanted to hear more of those nice tunes come out. "
                    " You got upset when he stopped playing. "
                    ca " ...? "
                    " You gave him a look that basically said 'pls keep playing I like your guitar skills'. "
                    ca " ... "
                    hide carmenneutral at bottom
                    show carmenhappy at center
                    ca " ...!! "
                    " He then started playing again. "
                    " His guitar skills were so good.... "
                    scene black with dissolve
                    " So good that you fell asleep. Damn, you fall asleep that easily? Lucky ass bitch... "
                    " You rested your head on his shoulder so that adds to the comfortability meter. "
                    " This honestly just feels like a nice dream, and you wish that you never woke up... "
                    play sound "audio/bellring.mp3"
                    " WELL TOO BAD YOU HAVE TO GET UP!!11!!! "
                    " You still have school buddy, don't get yourself distracted now. "
                    " Carmen was the one that woke you up, and you both get up to go to the next class. "
                    pause 2.0
                    jump ocgardeningclass1
                else:
                    " He was playing some nice tunes on his guitar... "
                    " You pretty much just wanted to hear more of those nice tunes come out. "
                    " You got upset when he stopped playing. "
                    x " ...? "
                    " You gave him a look that basically said 'pls keep playing I like your guitar skills'. "
                    x " ... "
                    hide carmenneutral at bottom
                    show carmenhappy at center
                    x " ...!! "
                    " He then started playing again. "
                    " His guitar skills were so good.... "
                    scene black with dissolve
                    " So good that you fell asleep. Damn, you fall asleep that easily? Lucky ass bitch... "
                    " You rested your head on his shoulder so that adds to the comfortability meter. "
                    " This honestly just feels like a nice dream, and you wish that you never woke up... "
                    play sound "audio/bellring.mp3"
                    " WELL TOO BAD YOU HAVE TO GET UP!!11!!! "
                    " You still have school buddy, don't get yourself distracted now. "
                    " The guy was the one that woke you up, and you both get up to go to the next class. "
                    pause 2.0
                    jump ocgardeningclass1
            label alonebackschool:
                " You decided not to sit next to any of the two and you just sat down near a tree. "
                " You then pulled out your phone and started listening to some tunes with your earphones that somehow just popped into existence out of nowhere. "
                " Game logic. "
                scene black with dissolve
                " You spent the entire break just chillaxing out in the back of the school. "
                " At one point, you even fell asleep because of how relaxed you were. "
                " I mean, it was pretty comfortable out here in the back... "
                play sound "audio/bellring.mp3"
                " The bell then rang not too long after you took your nap, waking you up successfully. "
                " You then got up from where you were sitting and you started walking to your next class. "
                pause 2.0
                jump ocgardeningclass1
        label ocgym3:
            # Matte, Disk
            scene black with dissolve
            pause 2.0
            scene gym with dissolve
            " You walk into the gym to find two of your classmates just hanging out. "
            " Do you talk to them? "
            menu:
                " {image=matteicon} Let's talk to them {image=diskicon} ":
                    # disk is learning how to draw
                    " You walk up to them and sat next to them on the bleachers. "
                    show matteneutral at left with easeinright
                    show diskneutral at right with easeinright
                    if matteknow == True and diskknow == True:
                        ma " Now, remember! Don't chicken scratch. You're gonna piss me and multiple artists off if you do that. "
                        d " Okay!...what's chicken scratching? "
                        ma " It's when you do this! "
                        " Matte draws an example on her sketchbook before she shows it to Disk. "
                        d " Ooooh, okay! "
                        " You then greeted them with a nice 'hi' and asked them what they were doing. "
                        ma " Hi, [name]! "
                        d " Hellooo!! "
                        d " Matte is teaching me how to draw better! "
                        d " I really want to improve my art skills, hehe... "
                        ma " It's for that one guy from that paper school, isn't it? "
                        hide diskneutral at bottom
                        show diskjoyous at right
                        d " EEEKK!! How did you know?!?!? "
                        ma " Heh, Quinn told me about it. You're real madly inlove with that guy, you know? "
                        d " Mhm, mhm! He's just so cuteeeee!! "
                        ma " Now hold on, did you even interact with that guy and do you even know his name? "
                        hide diskjoyous at bottom
                        show diskneutral at right
                        d " Yes! His name is Abbie, and I helped him out with a lot of things back when we were in Paper School! "
                        " You asked Disk what he meant by 'when we were in paper school'. "
                        d " Oh! right, you don't know? "
                        d " Everyone in this school had to temporarily be in Paper School because of an 'incident' that happened... "
                        d " We don't know what happened, though! They never told us! "
                        d " But, but but! I'm grateful that we got to go there because I wouldn't have met my sweet Abbie! "
                        ma " Wow, you really love that guy... "
                        d " Yeeep! Infact, me and Abbie still text eachother! "
                        hide matteneutral at bottom
                        show mattehappy at left
                        ma " Geez, Disk! You even have his number now?! Wow, you're growing up fast... "
                        hide diskneutral at bottom
                        show diskjoyous at right
                        d " Eeeeh? What do you mean??! I'm only 17! "
                        ma " 17 ALREADY?!?!?!? You're so old now!! "
                        d " Says the one that's 16! "
                        ma " Oh please, I'm not as old as you! "
                        scene black with dissolve
                        " You spent the entire break talking and drawing with Matte and Disk. "
                        " People were right, Disk really is a ball of sunshine. "
                        " He's just so energetic... In a good way, obviously. He can light up an entire room with that attitude. "
                        play sound "audio/bellring.mp3"
                        " The bell eventually rang, and you all get up from the bleachers and start walking to the next class. "
                        pause 2.0
                        jump ocgardeningclass1
                    elif matteknow == True and diskknow == False:
                        ma " Now, remember! Don't chicken scratch. You're gonna piss me and multiple artists off if you do that. "
                        x " Okay!...what's chicken scratching? "
                        ma " It's when you do this! "
                        " Matte draws an example on her sketchbook before she shows it to the guy. "
                        x " Ooooh, okay! "
                        " You then greeted them with a nice 'hi' and asked them what they were doing. "
                        ma " Hi, [name]! "
                        x " Hellooo!! "
                        x " Waitwait, Matte! I don't think I got to introduce myself to [name]! "
                        ma " Well, you should do that right now then. It would be rude not to introduce yourself, Disk. "
                        x " Okay!!! "
                        $ diskknow = True
                        d " I'm Disk!! I'm Matte's super cool cousin!! "
                        ma " Yeah, that's right. You're cooler than me. "
                        d " No, you are!! "
                        d " Back onto what we were doing... "
                        d " Matte is teaching me how to draw better! "
                        d " I really want to improve my art skills, hehe... "
                        ma " It's for that one guy from that paper school, isn't it? "
                        hide diskneutral at bottom
                        show diskjoyous at right
                        d " EEEKK!! How did you know?!?!? "
                        ma " Heh, Quinn told me about it. You're real madly inlove with that guy, you know? "
                        d " Mhm, mhm! He's just so cuteeeee!! "
                        ma " Now hold on, did you even interact with that guy and do you even know his name? "
                        hide diskjoyous at bottom
                        show diskneutral at right
                        d " Yes! His name is Abbie, and I helped him out with a lot of things back when we were in Paper School! "
                        " You asked Disk what he meant by 'when we were in paper school'. "
                        d " Oh! right, you don't know? "
                        d " Everyone in this school had to temporarily be in Paper School because of an 'incident' that happened... "
                        d " We don't know what happened, though! They never told us! "
                        d " But, but but! I'm grateful that we got to go there because I wouldn't have met my sweet Abbie! "
                        ma " Wow, you really love that guy... "
                        d " Yeeep! Infact, me and Abbie still text eachother! "
                        hide matteneutral at bottom
                        show mattehappy at left
                        ma " Geez, Disk! You even have his number now?! Wow, you're growing up fast... "
                        hide diskneutral at bottom
                        show diskjoyous at right
                        d " Eeeeh? What do you mean??! I'm only 17! "
                        ma " 17 ALREADY?!?!?!? You're so old now!! "
                        d " Says the one that's 16! "
                        ma " Oh please, I'm not as old as you! "
                        scene black with dissolve
                        " You spent the entire break talking and drawing with Matte and Disk. "
                        " People were right, Disk really is a ball of sunshine. "
                        " He's just so energetic... In a good way, obviously. He can light up an entire room with that attitude. "
                        play sound "audio/bellring.mp3"
                        " The bell eventually rang, and you all get up from the bleachers and start walking to the next class. "
                        pause 2.0
                        jump ocgardeningclass1
                    elif matteknow == False and diskknow == True:
                        x " Now, remember! Don't chicken scratch. You're gonna piss me and multiple artists off if you do that. "
                        d " Okay!...what's chicken scratching? "
                        x " It's when you do this! "
                        " The girl draws an example on her sketchbook before she shows it to Disk. "
                        d " Ooooh, okay! "
                        " You then greeted them with a nice 'hi' and asked them what they were doing. "
                        x " Hi, [name]! "
                        d " Hellooo!! "
                        d " Waitwait! I didn't get to introduce you to my cool cousin! "
                        $ matteknow = True
                        d " This is Matte! She's my very cool and talented cousin! "
                        ma " Wow. Very cool? "
                        d " Yes, very cool! "
                        d " Anyway, back to what we were doing... "
                        d " Matte is teaching me how to draw better! "
                        d " I really want to improve my art skills, hehe... "
                        ma " It's for that one guy from that paper school, isn't it? "
                        hide diskneutral at bottom
                        show diskjoyous at right
                        d " EEEKK!! How did you know?!?!? "
                        ma " Heh, Quinn told me about it. You're real madly inlove with that guy, you know? "
                        d " Mhm, mhm! He's just so cuteeeee!! "
                        ma " Now hold on, did you even interact with that guy and do you even know his name? "
                        hide diskjoyous at bottom
                        show diskneutral at right
                        d " Yes! His name is Abbie, and I helped him out with a lot of things back when we were in Paper School! "
                        " You asked Disk what he meant by 'when we were in paper school'. "
                        d " Oh! right, you don't know? "
                        d " Everyone in this school had to temporarily be in Paper School because of an 'incident' that happened... "
                        d " We don't know what happened, though! They never told us! "
                        d " But, but but! I'm grateful that we got to go there because I wouldn't have met my sweet Abbie! "
                        ma " Wow, you really love that guy... "
                        d " Yeeep! Infact, me and Abbie still text eachother! "
                        hide matteneutral at bottom
                        show mattehappy at left
                        ma " Geez, Disk! You even have his number now?! Wow, you're growing up fast... "
                        hide diskneutral at bottom
                        show diskjoyous at right
                        d " Eeeeh? What do you mean??! I'm only 17! "
                        ma " 17 ALREADY?!?!?!? You're so old now!! "
                        d " Says the one that's 16! "
                        ma " Oh please, I'm not as old as you! "
                        scene black with dissolve
                        " You spent the entire break talking and drawing with Matte and Disk. "
                        " People were right, Disk really is a ball of sunshine. "
                        " He's just so energetic... In a good way, obviously. He can light up an entire room with that attitude. "
                        play sound "audio/bellring.mp3"
                        " The bell eventually rang, and you all get up from the bleachers and start walking to the next class. "
                        pause 2.0
                        jump ocgardeningclass1
                    else:
                        x " Now, remember! Don't chicken scratch. You're gonna piss me and multiple artists off if you do that. "
                        x " Okay!...what's chicken scratching? "
                        x " It's when you do this! "
                        " The girl draws an example on her sketchbook before she shows it to the other guy. "
                        x " Ooooh, okay! "
                        " You then greeted them with a nice 'hi' and asked them what they were doing. "
                        x " Hi, [name]! "
                        x " Hellooo!! "
                        x " Waitwait! I didn't get to introduce you to my cool cousin! "
                        $ matteknow = True
                        x " This is Matte! She's my very cool and talented cousin! "
                        ma " Wow. Very cool? "
                        x " Yes, very cool! "
                        x " Hold on, wait! I almost forgot to introduce myself! "
                        ma " Well, you should do that right now then. It would be rude not to introduce yourself, Disk. "
                        x " Okay!!! "
                        $ diskknow = True
                        d " I'm Disk!! I'm Matte's super cool cousin!! "
                        ma " Yeah, that's right. You're cooler than me. "
                        d " No I'm not, silly... "
                        d " Anyway, back to what we were doing... "
                        d " Matte is teaching me how to draw better! "
                        d " I really want to improve my art skills, hehe... "
                        ma " It's for that one guy from that paper school, isn't it? "
                        hide diskneutral at bottom
                        show diskjoyous at right
                        d " EEEKK!! How did you know?!?!? "
                        ma " Heh, Quinn told me about it. You're real madly inlove with that guy, you know? "
                        d " Mhm, mhm! He's just so cuteeeee!! "
                        ma " Now hold on, did you even interact with that guy and do you even know his name? "
                        hide diskjoyous at bottom
                        show diskneutral at right
                        d " Yes! His name is Abbie, and I helped him out with a lot of things back when we were in Paper School! "
                        " You asked Disk what he meant by 'when we were in paper school'. "
                        d " Oh! right, you don't know? "
                        d " Everyone in this school had to temporarily be in Paper School because of an 'incident' that happened... "
                        d " We don't know what happened, though! They never told us! "
                        d " But, but but! I'm grateful that we got to go there because I wouldn't have met my sweet Abbie! "
                        ma " Wow, you really love that guy... "
                        d " Yeeep! Infact, me and Abbie still text eachother! "
                        hide matteneutral at bottom
                        show mattehappy at left
                        ma " Geez, Disk! You even have his number now?! Wow, you're growing up fast... "
                        hide diskneutral at bottom
                        show diskjoyous at right
                        d " Eeeeh? What do you mean??! I'm only 17! "
                        ma " 17 ALREADY?!?!?!? You're so old now!! "
                        d " Says the one that's 16! "
                        ma " Oh please, I'm not as old as you! "
                        scene black with dissolve
                        " You spent the entire break talking and drawing with Matte and Disk. "
                        " People were right, Disk really is a ball of sunshine. "
                        " He's just so energetic... In a good way, obviously. He can light up an entire room with that attitude. "
                        play sound "audio/bellring.mp3"
                        " The bell eventually rang, and you all get up from the bleachers and start walking to the next class. "
                        pause 2.0
                        jump ocgardeningclass1
                " Nah, I'd rather just chill alone. ":
                    " You decided to sit far from them because you didn't want to disturb them. "
                    " You then pulled out your phone so that you had something to do to keep you entertained. "
                    scene black with dissolve
                    " You spent the entire break looking at your phone while you were in the gym. "
                    " Nothing interesting was going on social media right now - oh wait. "
                    " Apparently there was going to be a play sometime this week. The play is going to take place in this school. "
                    " Not too interesting, but it's something, at least. "
                    play sound "audio/bellring.mp3"
                    " The bell then rang after about 30 minutes of scrolling on social media. "
                    " You got up from where you were sitting, and you went to the next class. "
                    pause 2.0
                    jump ocgardeningclass1
        label occafe3:
            # Notive, Quinn
            scene black with dissolve
            pause 2.0
            scene cafeteria with dissolve
            " You enter the cafeteria and see two of your classmates just chilling. "
            " You're thinking about talking to one of them...but who do you talk to? "
            if notiveknow == True and quinnknow == True:
                menu:
                    "{image=notiveicon} Notive {image=notiveicon} ":
                        jump sigma
                    " {image=quinnicon} Quinn {image=quinnicon} ":
                        jump skibidi
                    " I'd rather just sit alone. ":
                        jump beta
            elif notiveknow == True and quinnknow == False:
                menu:
                    "{image=notiveicon} Notive {image=notiveicon} ":
                        jump sigma
                    " {image=quinnicon} A guy with a mask {image=quinnicon} ":
                        jump skibidi
                    " I'd rather just sit alone. ":
                        jump beta
            elif notiveknow == False and quinnknow == True:
                menu:
                    "{image=notiveicon} A nonbinary looking fellow {image=notiveicon} ":
                        jump sigma
                    " {image=quinnicon} Quinn {image=quinnicon} ":
                        jump skibidi
                    " I'd rather just sit alone. ":
                        jump beta
            else:
                menu:
                    "{image=notiveicon} A nonbinary looking fellow {image=notiveicon} ":
                        jump sigma
                    " {image=quinnicon} A guy with a mask {image=quinnicon} ":
                        jump skibidi
                    " I'd rather just sit alone. ":
                        jump beta
            label sigma:
                # random facts
                show notiveneutral at center with easeinright
                if notiveknow == True:
                    " ...They're just staring at you. Menacingly. "
                    no " ... "
                    no " Hey [name]! Did you know that if you buy a property in egypt... "
                    no " ...What they will do is give you the property? "
                    " Wow, what a nice fun fact. "
                    no " I can give you more funfacts, actually! "
                    no " Did you know... "
                    no " That the programmer for this game has no idea what dialogue to give me? "
                    " Is that a fourth wall break? "
                    no " Yes, it is. "
                    scene black with dissolve
                    " Time to do a cheap timeskip... "
                    " You spent the entire break talking with Notive about random fun facts. "
                    " Some of them were really interesting while others were just straight up questionable. "
                    " At this point, you were wondering how Notive managed to memorize these. "
                    " Magic, I guess? Or just really good memory? "
                    play sound "audio/bellring.mp3"
                    " The bell then rings, meaning that it was time for the next class to start. "
                    " You get up from your seat and started walking back to your classroom for the next class. "
                    pause 2.0
                    jump ocgardeningclass1
                else:
                    " ...They're just staring at you. Menacingly. "
                    x " ... "
                    $ notiveknow = True
                    no " Hey [name]! Did you know that if you buy a property in egypt... "
                    no " ...What they will do is give you the property? "
                    " Wow, what a nice fun fact. Hey, wait, did this guy just somehow make you know their name??? "
                    " Even if they didn't give an introduction???????? "
                    " ...You know what, I'm too tired for this. "
                    no " I can give you more funfacts, actually! "
                    no " Did you know... "
                    no " That the programmer for this game has no idea what dialogue to give me? "
                    " Is that a fourth wall break? "
                    no " Yes, it is. "
                    scene black with dissolve
                    " Time to do a cheap timeskip... "
                    " You spent the entire break talking with Notive about random fun facts. "
                    " Some of them were really interesting while others were just straight up questionable. "
                    " At this point, you were wondering how Notive managed to memorize these. "
                    " Magic, I guess? Or just really good memory? "
                    play sound "audio/bellring.mp3"
                    " The bell then rings, meaning that it was time for the next class to start. "
                    " You get up from your seat and started walking back to your classroom for the next class. "
                    pause 2.0
                    jump ocgardeningclass1
            label skibidi:
                # quinn's feeling stressed out
                show quinnangry at center with easeinleft
                if quinnknow == True:
                    " Quinn seems a little stressed... "
                    " You ask him if he's doing fine and well. "
                    q " Oh, uh... [name]. "
                    q " Sorry, I'm not in the best mood at the moment, but er... "
                    q " I'm feeling a bit stressed, as you can tell. "
                    q " Why, you may ask? Well. "
                    q " My drama club is doing a play, and half the cast forgot their lines during the last rehearsal. "
                    q " I don't know what I'm going to do... "
                    q " Plus, the final thing is at next Monday and everything has to be PERFECT. "
                    q " I know it's monday right now and that we have a lot of time, but still! "
                    q " I need those lines to be remembered and for the props to be all ready! "
                    q " Aghhhh... What should I do, [name]? Do you have any ideas? "
                    " You thought about how you could help Quinn... "
                    " ...You had a pretty good idea come up a bit after thinking for about 5 minutes. "
                    " You explained to Quinn about making a game where they have to keep saying their lines a lot. "
                    " And whoever memorizes their lines the longest they'll get a prize! "
                    " Pretty solid idea, in your opinion. "
                    q " You know, that's actually... "
                    hide quinnangry at bottom
                    show quinnneutral at center
                    q " ...Pretty good! Though, what reward should I give them, hm... "
                    q " Maybe I could give them 5k? since I'm feeling generous, hehe. "
                    " That's like, really generous. "
                    q " Trust me, [name]. Despite how almost everyone is rich in this school, everyone really wants that 5k. "
                    q " It'll go perfectly! "
                    q " Thank you for the idea, [name]. I appreciate it. "
                    play sound "audio/bellring.mp3"
                    pause 1.0
                    q " Oh, uh...looks like the bell rang. "
                    q " I'll get going now. Thanks again, [name]! "
                    scene black with dissolve
                    " You then went to your classroom for the next class. "
                    pause 2.0
                    jump ocgardeningclass1
                else:
                    " He seems a little stressed... "
                    " You ask him if he's doing fine and well. "
                    x " Oh, uh... [name]. "
                    x " Sorry, I'm not in the best mood at the moment, but er... "
                    x " I'm feeling a bit stressed, as you can tell. "
                    x " Why, you may ask? Well. "
                    x " My drama club is doing a play, and half the cast forgot their lines during the last rehearsal. "
                    x " I don't know what I'm going to do... "
                    x " Plus, the final thing is at next Monday and everything has to be PERFECT. "
                    x " I know it's monday right now and that we have a lot of time, but still! "
                    x " I need those lines to be remembered and for the props to be all ready! "
                    x " Aghhhh... What should I do, [name]? Do you have any ideas? "
                    " You thought about how you could help Quinn... "
                    " ...You had a pretty good idea come up a bit after thinking for about 5 minutes. "
                    " You explained to him about making a game where they have to keep saying their lines a lot. "
                    " And whoever memorizes their lines the longest they'll get a prize! "
                    " Pretty solid idea, in your opinion. "
                    x " You know, that's actually... "
                    hide quinnangry at bottom
                    show quinnneutral at center
                    x " ...Pretty good! Though, what reward should I give them, hm... "
                    x " Maybe I could give them 5k? since I'm feeling generous, hehe. "
                    " That's like, really generous. "
                    x " Trust me, [name]. Despite how almost everyone is rich in this school, everyone really wants that 5k. "
                    x " It'll go perfectly! "
                    x " Thank you for the idea, [name]. I appreciate it. "
                    $ quinnknow = True
                    q " I'm Quinn by the way. Almost forgot to introduce myself to you, hehe... "
                    play sound "audio/bellring.mp3"
                    pause 1.0
                    q " Oh, uh...looks like the bell rang. "
                    q " I'll get going now. Thanks again, [name]! "
                    scene black with dissolve
                    " You then went to your classroom for the next class. "
                    pause 2.0
                    jump ocgardeningclass1
            label beta:
                " You decided not to sit next to anyone. "
                " You just sat down on an empty space and just relaxed there. "
                scene black with dissolve
                " You also took this as an opportunity to take a quick nap. "
                " Ahhhh, some nice air conditioning...makes this even more comfortable than it originally was. "
                pause 1.0
                play sound "audio/bellring.mp3"
                " The bell rang, waking you up from your quick nap. "
                " You get up from where you were sitting and went to your next class. "
                pause 2.0
                jump ocgardeningclass1
        label ocrooftop3:
            # Jacob, Temero
            scene black with dissolve
            pause 2.0
            scene rooftop with dissolve
            " You walk up into the rooftop and spot two of your classmates chilling. "
            " You're thinking about talking to one of them, but who do you talk to? "
            if temeroknow == True and jacobknow == True:
                menu:
                    " {image=temeroicon} Temero {image=temeroicon} ":
                        jump temerorooftopint
                    " {image=jacobicon} Jacob {image=jacobicon} ":
                        jump jacobrooftopint
            elif temeroknow == True and jacobknow == False:
                menu:
                    " {image=temeroicon} Temero {image=temeroicon} ":
                        jump temerorooftopint
                    " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                        jump jacobrooftopint
            elif temeroknow == False and jacobknow == True:
                menu:
                    " {image=temeroicon} A girl with a butterfly bow {image=temeroicon} ":
                        jump temerorooftopint
                    " {image=jacobicon} Jacob {image=jacobicon} ":
                        jump jacobrooftopint
            else:
                menu:
                    " {image=temeroicon} A girl with a butterfly bow {image=temeroicon} ":
                        jump temerorooftopint
                    " {image=jacobicon} A guy with goggles and a bandana {image=jacobicon} ":
                        jump jacobrooftopint
            label temerorooftopint:
                # you touch her antennas without permission
                show temeroneutral at center with easeinright
                if temeroknow == True:
                    " Seems like she's distracted with looking at the clouds. "
                    " You look closer and turns out she has butterfly antennas near her goggles. "
                    " Thinking that it was a decoration, you reach up and touch them. "
                    hide temeroneutral at bottom
                    show temeroangry at center
                    " ...Temero looked like she didn't like that at all. "
                    tm " Woah, WOAH! buddy. " with vpunch
                    tm " The next time you do that, you have to ask me permission. "
                    tm " Don't just go touching people without their permission, especially women. "
                    tm " You're gonna look like a creep if you do that! "
                    " You apologize to her and then ask why she reacted that badly to having her antennas touched. "
                    tm " Well, it's because they're real! They're not like, decorations, you know. "
                    tm " Even if you touch them by a bit, it'll feel like I just got a whole ass jumpscare! "
                    tm " So, don't touch them ever again or I'll bite your fingers off. Got it? "
                    " You nod your head, promising not to touch her antennas again. "
                    tm " That's good. "
                    hide temeroangry at bottom
                    show temeroneutral at center
                    tm " Anyway... you wanna know something about Spark? "
                    tm " He has this private twitter account and he acts mad gay on there. "
                    tm " He literally posts his hear me outs there and guess what? "
                    tm " You know this guy, Edward, yeah? He's the guy Spark keeps on talking about. "
                    tm " Spark thinks he's soooo cute but I don't see what he sees in him. "
                    tm " Probably because I like women better than men. "
                    tm " Spark's mad gay over Edward, and I would show you one of Spark's tweets, buuuut... "
                    tm " He'd kill me. And I do not want that to happen. "
                    tm " Better to stay safe rather than staying on danger! "
                    scene black with dissolve
                    " You spent the entire break talking to Temero. "
                    " You never actually knew that she liked girls. But you think that she's cool for that. "
                    " Go my lesbians, go!! "
                    play sound "audio/bellring.mp3"
                    " The bell rings, meaning that it was time for the next class. "
                    " You walked back down from the rooftop so that you could go to your next class. "
                    pause 2.0
                    jump ocgardeningclass1
                else:
                    " Seems like she's distracted with looking at the clouds. "
                    " You look closer and turns out she has butterfly antennas near her goggles. "
                    " Thinking that it was a decoration, you reach up and touch them. "
                    hide temeroneutral at bottom
                    show temeroangry at center
                    " ...She looked like she didn't like that at all. "
                    x " Woah, WOAH! buddy. " with vpunch
                    x " The next time you do that, you have to ask me permission. "
                    x " Don't just go touching people without their permission, especially women. "
                    x " You're gonna look like a creep if you do that! "
                    " You apologize to her and then ask why she reacted that badly to having her antennas touched. "
                    x " Well, it's because they're real! They're not like, decorations, you know. "
                    x " Even if you touch them by a bit, it'll feel like I just got a whole ass jumpscare! "
                    x " So, don't touch them ever again or I'll bite your fingers off. Got it? "
                    " You nod your head, promising not to touch her antennas again. "
                    x " That's good. "
                    hide temeroangry at bottom
                    show temeroneutral at center
                    $ temeroknow = True
                    tm " I'm Temero NEO by the way! Call me Temero, or Neo, or whatever. You're the new kid, yeah? That's cool. "
                    tm " Anyway... you wanna know something about Spark? "
                    tm " He has this private twitter account and he acts mad gay on there. "
                    tm " He literally posts his hear me outs there and guess what? "
                    tm " You know this guy, Edward, yeah? He's the guy Spark keeps on talking about. "
                    tm " Spark thinks he's soooo cute but I don't see what he sees in him. "
                    tm " Probably because I like women better than men. "
                    tm " Spark's mad gay over Edward, and I would show you one of Spark's tweets, buuuut... "
                    tm " He'd kill me. And I do not want that to happen. "
                    tm " Better to stay safe rather than staying on danger! "
                    scene black with dissolve
                    " You spent the entire break talking to Temero. "
                    " You never actually knew that she liked girls. But you think that she's cool for that. "
                    " Go my lesbians, go!! "
                    play sound "audio/bellring.mp3"
                    " The bell rings, meaning that it was time for the next class. "
                    " You walked back down from the rooftop so that you could go to your next class. "
                    pause 2.0
                    jump ocgardeningclass1
            label jacobrooftopint:
                # you touch his bandana and goggles without permission
                show jacobneutral at center with easeinleft
                if jacobknow == True:
                    " He seems to be distracted looking at the ground. "
                    " You've heard that he doesn't like his bandana or goggles being touched, so you decided to test that out. "
                    " You walked behind him and put your hands on his goggles... "
                    " ...Only to get your hand slapped. Thankfully you didn't get hit with his other hand that's quite literally just a saw. "
                    jac " Please don't touch my goggles. "
                    jac " I'm not comfortable with you doing that... "
                    " You apologized to him, and then asked him why he doesn't like his goggles being touched. "
                    jac " ...I don't like to talk about it. "
                    jac " It's more of a personal subject for me. "
                    " ...Well, alright. "
                    scene black with dissolve
                    " You spent the entire break talking to Jacob about random things. "
                    " Nothing really interesting, just about random things. "
                    " Pretty boring, but alright. This is totally not because the programmar hasn't slept the entire day and is really tired at 10:23 AM. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, meaning that it was time for the next class. "
                    " You walked back down from the rooftop so that you could go to your next class. "
                    pause 2.0
                    jump ocgardeningclass1
                else:
                    " He seems to be distracted looking at the ground. "
                    " You've heard that he doesn't like his bandana or goggles being touched, so you decided to test that out. "
                    " You walked behind him and put your hands on his goggles... "
                    " ...Only to get your hand slapped. Thankfully you didn't get hit with his other hand that's quite literally just a saw. "
                    x " Please don't touch my goggles. "
                    x " I'm not comfortable with you doing that... "
                    " You apologized to him, and then asked him why he doesn't like his goggles being touched. "
                    x " ...I don't like to talk about it. "
                    x " It's more of a personal subject for me. "
                    " ...Well, alright. "
                    scene black with dissolve
                    " You spent the entire break talking to the other guy about random things. "
                    " Nothing really interesting, just about random things. "
                    " Pretty boring, but alright. This is totally not because the programmar hasn't slept the entire day and is really tired at 10:23 AM. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, meaning that it was time for the next class. "
                    " You walked back down from the rooftop so that you could go to your next class. "
                    pause 2.0
                    jump ocgardeningclass1
        label oclibrary3:
            # Orchid, Koa, Yinhui + Yangyi
            scene black with dissolve
            pause 2.0
            scene library with dissolve
            " You walk into the library and spot four of your classmates just chilling. "
            " You're thinking about talking to them... but who do you talk to? "
            " You know what, how about I make you guess who to talk to? Try to figure out who is who. "
            " It's easy, don't worry. It's totally not because I'm writing this at exactly 1:30 AM and I'm very tired. "
            menu:
                " An emo kid ":
                    # you read with him
                    show koaneutral at center with easeinright
                    if koaknow == True:
                        " You sit next to him and look at what he was reading. "
                        " You also waited for him to see if he would say anything. "
                        k " ... "
                        " Nothing. He just seems to be really busy reading his book. "
                        " He seems to notice you and he puts the book down in a way so that you both could read it. "
                        " How nice... "
                        " You then started reading with him. "
                        scene black with dissolve
                        " You spent the entire break reading a book with Koa. "
                        " Everytime he was done with reading a page, he would ask you if you were done reading too. "
                        " He would also wait for you patiently if you weren't done reading. "
                        " What a real nice guy...even though he looks pretty emo. "
                        " He enjoyed your company, and you enjoyed his. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, meaning that it was time for the next class. "
                        " You walked back down from the rooftop so that you could go to your next class. "
                        pause 2.0
                        jump ocgardeningclass1
                    else:
                        " You sit next to him and look at what he was reading. "
                        " You also waited for him to see if he would say anything. "
                        x " ... "
                        " Nothing. He just seems to be really busy reading his book. "
                        " He seems to notice you and he puts the book down in a way so that you both could read it. "
                        " How nice... "
                        " You then started reading with him. "
                        scene black with dissolve
                        " You spent the entire break reading a book with the emo guy "
                        " Everytime he was done with reading a page, he would ask you if you were done reading too. "
                        " He would also wait for you patiently if you weren't done reading. "
                        " What a real nice guy...even though he looks pretty emo. "
                        " He enjoyed your company, and you enjoyed his. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, meaning that it was time for the next class. "
                        " You walked back down from the rooftop so that you could go to your next class. "
                        pause 2.0
                        jump ocgardeningclass1
                " A scene kid ":
                    # you yap with them
                    show orchidangry at center with easeinleft
                    if orchidknow == True:
                        oc " Ouuughh.. It's so boring here... "
                        oc " I don't wanna do those assignments either... too boring... "
                        oc " I just wanna yap to someone... "
                        hide orchidangry at bottom
                        show orchidneutral at center
                        oc " ...{w=0.5} Oh! [name]! [name][name][name]! Hi! "
                        oc " Is it okay if I yap about a few things to you? "
                        oc " It's okay if you're not fine with it though, I don't wanna annoy you, hehe... "
                        " You didn't really have anything else to do... so ... "
                        " Sure, you could listen to a yapping session. "
                        oc " Alright!! So... "
                        scene black with dissolve
                        " You spent the entire break listening to Orchid yap about the most random things. "
                        " honestly man im just so tired rn but uh yeah lmao "
                        play sound "audio/bellring.mp3"
                        " The bell rings, meaning that it was time for the next class. "
                        " You walked back down from the rooftop so that you could go to your next class. "
                        pause 2.0
                        jump ocgardeningclass1
                    else:
                        x " Ouuughh.. It's so boring here... "
                        x " I don't wanna do those assignments either... too boring... "
                        x " I just wanna yap to someone... "
                        hide orchidangry at bottom
                        show orchidneutral at center
                        x " ...{w=0.5} Oh! [name]! [name][name][name]! Hi! "
                        $ orchidknow = True
                        oc " I'm Orchid, by the way! I forgot to introduce myself to you, hehe... "
                        oc " Is it okay if I yap about a few things to you? "
                        oc " It's okay if you're not fine with it though, I don't wanna annoy you, hehe... "
                        " You didn't really have anything else to do... so ... "
                        " Sure, you could listen to a yapping session. "
                        oc " Alright!! So... "
                        scene black with dissolve
                        " You spent the entire break listening to Orchid yap about the most random things. "
                        " honestly man im just so tired rn but uh yeah lmao "
                        play sound "audio/bellring.mp3"
                        " The bell rings, meaning that it was time for the next class. "
                        " You walked back down from the rooftop so that you could go to your next class. "
                        pause 2.0
                        jump ocgardeningclass1
                " Twins ":
                    # Yangyi tries to trust you
                    show yinhuineutral at right with easeinleft
                    show yangyineutral at left with easeinleft
                    if yinhuiknow == True and yangyiknow == True:
                        " You spot the twins reading a random book that looked like a children's story book for some reason. "
                        " You didn't judge though. You're the type who listens to skibidi toilet stuff. "
                        " You sat next to them and you could hear one of them reading the book aloud...just a bit quietly since this is a library. "
                        yi " A long time ago, there was a boy in china named Ping who loved flowers... "
                        yi " Anything he planted burst into bloom... "
                        yi " Up came flowers, bushes, and even big fruit trees... "
                        " Yinhui continued to speak until he and his brother spotted you. "
                        ya " [name]!! hi!! we were just reading a book, hehe. "
                        ya " Would you like to join us? "
                        yi " Yang, I don't think- {nw} "
                        ya " Come on, Yin...please...? "
                        yi " ... "
                        yi " Fine. "
                        ya " Yahooo! "
                        ya " Actually, [name]... could you read the story for us? "
                        yi " What's wrong with my story telling? "
                        ya " Nothing's wrong with it, I just want you to have a break form reading! "
                        yi " ...Yeah, right. "
                        ya " Yin, switch seats with [name] so that [they] can read! "
                        yi " Fine... "
                        " Yinhui switched seats with you, and you got ahold of the book. "
                        " You then started to read them the story... "
                        scene black with dissolve
                        " You read the twins a book for the entire break. "
                        " It wasn't long until the twins had their heads rested on your shoulders, and them sleeping. "
                        " You feel as if Yinhui wasn't acting as his usual mean and protective self because of the story. "
                        if kind == True:
                            " I mean, who wouldn't fall asleep with your kind tone? "
                        elif calm == True:
                            " I mean, who wouldn't fall asleep with your calm tone? "
                        elif mean == True:
                            " I mean, your voice did sound a bit scary, but you somehow managed to put them to sleep. Huh. "
                        play sound "audio/bellring.mp3"
                        " The bell then rang not too long after they had fallen asleep. "
                        " Yinhui seemed to be embarrassed that he fell asleep, but Yangyi seemed to not mind falling asleep on you. "
                        " You returned the book to where it originally was according to the twins before you headed out to go to your next class. "
                        pause 2.0
                        jump ocgardeningclass1
                    elif yinhuiknow == True and yangyiknow == False:
                        " You spot the twins reading a random book that looked like a children's story book for some reason. "
                        " You didn't judge though. You're the type who listens to skibidi toilet stuff. "
                        " You sat next to them and you could hear one of them reading the book aloud...just a bit quietly since this is a library. "
                        x " A long time ago, there was a boy in china named Ping who loved flowers... "
                        x " Anything he planted burst into bloom... "
                        x " Up came flowers, bushes, and even big fruit trees... "
                        " He continued to speak until he and his brother spotted you. "
                        ya " [name]!! hi!! we were just reading a book, hehe. "
                        ya " Would you like to join us? "
                        x " Yang, I don't think- {nw} "
                        ya " Come on, Yin...please...? "
                        $ yangyiknow = True
                        yi " ... "
                        yi " Fine. "
                        ya " Yahooo! "
                        ya " Actually, [name]... could you read the story for us? "
                        yi " What's wrong with my story telling? "
                        ya " Nothing's wrong with it, I just want you to have a break form reading! "
                        yi " ...Yeah, right. "
                        ya " Yin, switch seats with [name] so that [they] can read! "
                        yi " Fine... "
                        " Yinhui switched seats with you, and you got ahold of the book. "
                        " You then started to read them the story... "
                        scene black with dissolve
                        " You read the twins a book for the entire break. "
                        " It wasn't long until the twins had their heads rested on your shoulders, and them sleeping. "
                        " You feel as if Yinhui wasn't acting as his usual mean and protective self because of the story. "
                        if kind == True:
                            " I mean, who wouldn't fall asleep with your kind tone? "
                        elif calm == True:
                            " I mean, who wouldn't fall asleep with your calm tone? "
                        elif mean == True:
                            " I mean, your voice did sound a bit scary, but you somehow managed to put them to sleep. Huh. "
                        play sound "audio/bellring.mp3"
                        " The bell then rang not too long after they had fallen asleep. "
                        " Yinhui seemed to be embarrassed that he fell asleep, but Yangyi seemed to not mind falling asleep on you. "
                        " You returned the book to where it originally was according to the twins before you headed out to go to your next class. "
                        pause 2.0
                        jump ocgardeningclass1
                    elif yinhuiknow == False and yangyiknow == True:
                        " You spot the twins reading a random book that looked like a children's story book for some reason. "
                        " You didn't judge though. You're the type who listens to skibidi toilet stuff. "
                        " You sat next to them and you could hear one of them reading the book aloud...just a bit quietly since this is a library. "
                        yi " A long time ago, there was a boy in china named Ping who loved flowers... "
                        yi " Anything he planted burst into bloom... "
                        yi " Up came flowers, bushes, and even big fruit trees... "
                        " He continued to speak until he and his brother spotted you. "
                        x " [name]!! hi!! we were just reading a book, hehe. "
                        x " Would you like to join us? "
                        $ yinhuiknow = True
                        yi " Yang, I don't think- {nw} "
                        ya " Come on, Yin...please...? "
                        yi " ... "
                        yi " Fine. "
                        ya " Yahooo! "
                        ya " Actually, [name]... could you read the story for us? "
                        yi " What's wrong with my story telling? "
                        ya " Nothing's wrong with it, I just want you to have a break form reading! "
                        yi " ...Yeah, right. "
                        ya " Yin, switch seats with [name] so that [they] can read! "
                        yi " Fine... "
                        " Yinhui switched seats with you, and you got ahold of the book. "
                        " You then started to read them the story... "
                        scene black with dissolve
                        " You read the twins a book for the entire break. "
                        " It wasn't long until the twins had their heads rested on your shoulders, and them sleeping. "
                        " You feel as if Yinhui wasn't acting as his usual mean and protective self because of the story. "
                        if kind == True:
                            " I mean, who wouldn't fall asleep with your kind tone? "
                        elif calm == True:
                            " I mean, who wouldn't fall asleep with your calm tone? "
                        elif mean == True:
                            " I mean, your voice did sound a bit scary, but you somehow managed to put them to sleep. Huh. "
                        play sound "audio/bellring.mp3"
                        " The bell then rang not too long after they had fallen asleep. "
                        " Yinhui seemed to be embarrassed that he fell asleep, but Yangyi seemed to not mind falling asleep on you. "
                        " You returned the book to where it originally was according to the twins before you headed out to go to your next class. "
                        pause 2.0
                        jump ocgardeningclass1
                    else:
                        " You spot the twins reading a random book that looked like a children's story book for some reason. "
                        " You didn't judge though. You're the type who listens to skibidi toilet stuff. "
                        " You sat next to them and you could hear one of them reading the book aloud...just a bit quietly since this is a library. "
                        x " A long time ago, there was a boy in china named Ping who loved flowers... "
                        x " Anything he planted burst into bloom... "
                        x " Up came flowers, bushes, and even big fruit trees... "
                        " He continued to speak until he and his brother spotted you. "
                        x " [name]!! hi!! we were just reading a book, hehe. "
                        x " Would you like to join us? "
                        $ yinhuiknow = True
                        x " Yang, I don't think- {nw} "
                        $ yanyiknow = True
                        ya " Come on, Yin...please...? "
                        yi " ... "
                        yi " Fine. "
                        ya " Yahooo! "
                        ya " Actually, [name]... could you read the story for us? "
                        yi " What's wrong with my story telling? "
                        ya " Nothing's wrong with it, I just want you to have a break form reading! "
                        yi " ...Yeah, right. "
                        ya " Yin, switch seats with [name] so that [they] can read! "
                        yi " Fine... "
                        " Yinhui switched seats with you, and you got ahold of the book. "
                        " You then started to read them the story... "
                        scene black with dissolve
                        " You read the twins a book for the entire break. "
                        " It wasn't long until the twins had their heads rested on your shoulders, and them sleeping. "
                        " You feel as if Yinhui wasn't acting as his usual mean and protective self because of the story. "
                        if kind == True:
                            " I mean, who wouldn't fall asleep with your kind tone? "
                        elif calm == True:
                            " I mean, who wouldn't fall asleep with your calm tone? "
                        elif mean == True:
                            " I mean, your voice did sound a bit scary, but you somehow managed to put them to sleep. Huh. "
                        play sound "audio/bellring.mp3"
                        " The bell then rang not too long after they had fallen asleep. "
                        " Yinhui seemed to be embarrassed that he fell asleep, but Yangyi seemed to not mind falling asleep on you. "
                        " You returned the book to where it originally was according to the twins before you headed out to go to your next class. "
                        pause 2.0
                        jump ocgardeningclass1
    label ocgardeningclass1:
        scene gardenroom with dissolve
        " You walked into the pretty gardening room and you could see your other classmates sitting down on the ground near the plants. "
        " This was a very nice gardening room...this would go great for photos. "
        " Well, you couldn't really bring out your phone to take one since the teacher had just arrived. "
        show wisterianeutral at center with easeinright
        x " Hello, my students... "
        " The classroom greeted her with a very energetic 'HELLO!!'...god damn she's pretty. "
        x " Hhmhm... All of you must be quite energetic from Sol's class. "
        x " Anywho... "
        x " I have heard that we have a new student here... "
        x " Tell me, where are they...? "
        " She looked around the room before she spotted you. "
        x " Ah, I haven't seen you here before...Tell me, little one, what's your name...? "
        " You told her that your name was [name]. "
        x " [name]...That's a lovely name, dear child. "
        x " I hope you'll have fun being here at Everleaf high... "
        msw " I am Miss Wisteria... The gardening teacher... "
        msw " Since you're new here, you can ask me any questions you want! "
        $ hyacinthus = renpy.random.randint(1, 2)
        if hyacinthus == 1:
            msw " Now with that out of the way...let's get started with our lesson..."
            scene black with dissolve
            " The class was actually fun because you got to plant stuff. "
            " Plus, the teacher was really nice and gentle with you. "
            " So far, the teachers from here are great. "
            play sound "audio/bellring.mp3"
            " The bell rang a few minutes later, meaning that class was over. "
            " You waited for everyone else to get out of the classroom before you yourself went out to go in the hallway. "
            pause 2.0
            jump ocbreak4
        elif hyacinthus == 2:
            " You think about your question for a bit... "
            " What could you possibly ask this teacher? "
            " You then remembered seeing someone who looked identical to Miss Wisteria not too long ago online. "
            " You remembered their name...Miss Hyacinthus. "
            " You asked her if she knew about her. "
            stop music
            hide wisterianeutral at bottom
            show wisteriaangry at center
            "    {w=10.0} "
            play music "audio/paperhigh.mp3"
            hide wisteriaangry at bottom
            show wisterianeutral at center
            msw " Hello there...? [name]?? "
            msw " You've been staring at me for quite a long time now... "
            msw " I don't know who you're talking about. "
            msw " But...it's quite funny that someone looks like me, hehe. "
            msw " Now with that out of the way...let's get started with our lesson..."
            scene black with dissolve
            " The class was actually fun because you got to plant stuff. "
            " Plus, the teacher was really nice and gentle with you. "
            " So far, the teachers from here are great. "
            play sound "audio/bellring.mp3"
            " The bell rang a few minutes later, meaning that class was over. "
            " You waited for everyone else to get out of the classroom before you yourself went out to go in the hallway. "
            pause 2.0
            jump ocbreak4
        else:
            pass
    label ocbreak4:
        scene hallway with dissolve
        " It's time for another break, and you're thinking about hanging out with your fellow classmates. "
        " Where do you go? "
        menu:
            " {image=carmenicon} The front of the school {image=carmenicon} ":
                jump ocfrontschool4
            " {image=jamicon} The back of the school {image=matteicon} ":
                jump ocbackschool4
            " {image=sparkicon} The gym {image=orchidicon} ":
                jump ocgym4
            " The cafeteria ":
                jump occafe4
            " {image=koaicon} The rooftop {image=koaicon} ":
                jump ocrooftop4
            " The library ":
                jump oclibrary4
    label ocfrontschool4:
        # carmen
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked outside of the school and looked at all of the pretty stuff around you. "
        " Flowers, cars passing by... a mysterious figure standing behind a tree... "
        " wait what "
        " Now hold on, you better go check that out. Just to make sure if you're just tweaking out or if that's a creep or not. "
        " You walked over to the figure and saw that it was just one of your classmates playing the guitar. "
        show carmenneutral at center with easeinleft
        if carmenknow == True:
            ca " ... "
            " It didn't take too long for him to notice that you were standing there. "
            ca " ...!! "
            " You waved at him a bit, just to tell him a little 'hello' "
            " You then pointed at his guitar, then pointed at him as if you were asking if he could play a bit more. "
            " You did a thumbs up to say that his guitar skills were good! "
            ca " ...? "
            " He pointed at himself, as if not believing that you thought his guitar skills were good. "
            " He thought for a moment, probably trying to think of a song to play. "
            " He then gave you a thumbs up and he motioned for you to sit next to him on the ground. "
            " You sat next to him and he started playing a nice tune... "
            scene black with dissolve
            " You spent the entire break spending time with Carmen and listening to his cool tunes. "
            " Honestly, you could've fallen asleep right then and there but you weren't feeling your usual eepiness. "
            " For now, you just chillaxxed with him. "
            play sound "audio/bellring.mp3"
            " The bell rang eventually, stopping Carmen from playing anymore tunes. For now. "
            " You got up from where you were sitting and you went back into the school to go to your next class. "
            pause 2.0
            jump ocphysicsclass1
        else:
            x " ... "
            " It didn't take too long for him to notice that you were standing there. "
            x " ...!! "
            " You waved at him a bit, just to tell him a little 'hello' "
            " You then pointed at his guitar, then pointed at him as if you were asking if he could play a bit more. "
            " You did a thumbs up to say that his guitar skills were good! "
            x " ...? "
            " He pointed at himself, as if not believing that you thought his guitar skills were good. "
            " He thought for a moment, probably trying to think of a song to play. "
            " He then gave you a thumbs up and he motioned for you to sit next to him on the ground. "
            " But, before he started to play a tune, he pulled out a piece of paper that had a note on it... "
            $ carmenknow = True
            " 'Carmen'. He then pointed at himself. This must be his name... "
            " You sat next to him and he started playing a nice tune... "
            scene black with dissolve
            " You spent the entire break spending time with Carmen and listening to his cool tunes. "
            " Honestly, you could've fallen asleep right then and there but you weren't feeling your usual eepiness. "
            " For now, you just chillaxxed with him. "
            play sound "audio/bellring.mp3"
            " The bell rang eventually, stopping Carmen from playing anymore tunes. For now. "
            " You got up from where you were sitting and you went back into the school to go to your next class. "
            pause 2.0
            jump ocphysicsclass1
    label ocbackschool4:
        # jam, matte
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You went to the back of the school to probably eep for a bit, but then you heard the sounds of someone playing a video game. "
        " And talking. Like, two people talking. "
        " Curious, you decided to see what those two people were talking about. "
        show jamneutral at right with easeoutleft
        show matteneutral at left with easeoutleft
        if jamknow == True and matteknow == True:
            ja " So... Why're you here again? "
            ma " I just wanted to spend time with you. "
            ja " Alright...? Why would you wanna spend time with someone like me though? "
            hide matteneutral at bottom
            show mattehappy at left
            ma " Because I want to, silly. "
            ma " And also because I think you're really cool. "
            ja " ...Cool? What makes you think that I'm cool? "
            hide mattehappy at bottom
            show mattesad at left
            ma " You really don't think you're cool, Jam? wow, you really gotta think more positively... "
            hide mattesad at bottom
            show matteneutral at left
            ma " But I think everything about you is cool! "
            ja " ...Even if I can get a little violent to others...? Even if I can be a little rude to you...? "
            ma " Well, yes. Not everyone is perfect, silly. "
            ma " We're all different people, and there's no such thing as a perfect person. "
            ma " We've all got our flaws and stuff no matter how perfect we think we are. "
            ma " But to me, I think you're perfect, Jam. There's nothing that could make me change my mind. "
            ma " I'm not taking any negative comments about yourself! "
            ja " ... "
            hide jamneutral at bottom
            show jamhappy at right
            ja " ...You know... "
            ja " I'm grateful that I got to be your friend. "
            ja " I thought you'd just ignore me back in the very first time we met, but you talked to me. Every single day. "
            ja " And I never found it annoying. "
            ja " I always told you that I wanted to go to this school, but... "
            ja " My family wanted me to go to a different one. "
            ja " You did everything to convince them to let me go here. "
            ja " Even tried suing them at one point. "
            ja " You did so much for me, and yet I never did anything for you. "
            ja " What can I do to repay your kindness? "
            hide matteneutral at bottom
            show mattesurprised at left
            ma " ... "
            hide mattesurprised at bottom
            show mattehappy at left
            ma " ...You've already repaid me, just by me seeing you happy. "
            ma " Making you smile is what matters the most to me. "
            ja " ... "
            ja " ...You're too nice. In a good way. "
            scene black with dissolve
            " Awww. What cuties... "
            " You decided to not eavesdrop on their conversation much longer and you walked back into the school. "
            " Damn, you wonder when you're gonna get friends like that. "
            " That's true friendship right there. Probably something that you'll never get. "
            " I'm sorry, I'm being mean. I really gotta stop otherwise I'm getting fired. "
            " Anyway... "
            play sound "audio/bellring.mp3"
            " As you walked the halls of your school, the bell rings not too long after you went back into the school and started roaming around. "
            " You were about to turn a corner before you immediately turned yourself back so that you could get to your classroom. "
            pause 2.0
            jump ocphysicsclass1
        elif jamknow == True and matteknow == False:
            ja " So... Why're you here again? "
            x " I just wanted to spend time with you. "
            ja " Alright...? Why would you wanna spend time with someone like me though? "
            hide matteneutral at bottom
            show mattehappy at left
            x " Because I want to, silly. "
            x " And also because I think you're really cool. "
            ja " ...Cool? What makes you think that I'm cool? "
            hide mattehappy at bottom
            show mattesad at left
            x " You really don't think you're cool, Jam? wow, you really gotta think more positively... "
            hide mattesad at bottom
            show matteneutral at left
            x " But I think everything about you is cool! "
            ja " ...Even if I can get a little violent to others...? Even if I can be a little rude to you...? "
            x " Well, yes. Not everyone is perfect, silly. "
            x " We're all different people, and there's no such thing as a perfect person. "
            x " We've all got our flaws and stuff no matter how perfect we think we are. "
            x " But to me, I think you're perfect, Jam. There's nothing that could make me change my mind. "
            x " I'm not taking any negative comments about yourself! "
            ja " ... "
            hide jamneutral at bottom
            show jamhappy at right
            ja " ...You know... "
            ja " I'm grateful that I got to be your friend. "
            ja " I thought you'd just ignore me back in the very first time we met, but you talked to me. Every single day. "
            ja " And I never found it annoying. "
            ja " I always told you that I wanted to go to this school, but... "
            ja " My family wanted me to go to a different one. "
            ja " You did everything to convince them to let me go here. "
            ja " Even tried suing them at one point. "
            ja " You did so much for me, and yet I never did anything for you. "
            ja " What can I do to repay your kindness? "
            hide matteneutral at bottom
            show mattesurprised at left
            x " ... "
            hide mattesurprised at bottom
            show mattehappy at left
            x " ...You've already repaid me, just by me seeing you happy. "
            x " Making you smile is what matters the most to me. "
            ja " ... "
            ja " ...You're too nice. In a good way. "
            scene black with dissolve
            " Awww. What cuties... "
            " You decided to not eavesdrop on their conversation much longer and you walked back into the school. "
            " Damn, you wonder when you're gonna get friends like that. "
            " That's true friendship right there. Probably something that you'll never get. "
            " I'm sorry, I'm being mean. I really gotta stop otherwise I'm getting fired. "
            " Anyway... "
            play sound "audio/bellring.mp3"
            " As you walked the halls of your school, the bell rings not too long after you went back into the school and started roaming around. "
            " You were about to turn a corner before you immediately turned yourself back so that you could get to your classroom. "
            pause 2.0
            jump ocphysicsclass1
        elif jamknow == False and matteknow == True:
            x " So... Why're you here again? "
            ma " I just wanted to spend time with you. "
            x " Alright...? Why would you wanna spend time with someone like me though? "
            hide matteneutral at bottom
            show mattehappy at left
            ma " Because I want to, silly. "
            ma " And also because I think you're really cool. "
            x " ...Cool? What makes you think that I'm cool? "
            hide mattehappy at bottom
            show mattesad at left
            ma " You really don't think you're cool, Jam? wow, you really gotta think more positively... "
            hide mattesad at bottom
            show matteneutral at left
            ma " But I think everything about you is cool! "
            x " ...Even if I can get a little violent to others...? Even if I can be a little rude to you...? "
            ma " Well, yes. Not everyone is perfect, silly. "
            ma " We're all different people, and there's no such thing as a perfect person. "
            ma " We've all got our flaws and stuff no matter how perfect we think we are. "
            ma " But to me, I think you're perfect, Jam. There's nothing that could make me change my mind. "
            ma " I'm not taking any negative comments about yourself! "
            x " ... "
            hide jamneutral at bottom
            show jamhappy at right
            x " ...You know... "
            x " I'm grateful that I got to be your friend. "
            x " I thought you'd just ignore me back in the very first time we met, but you talked to me. Every single day. "
            x " And I never found it annoying. "
            x " I always told you that I wanted to go to this school, but... "
            x " My family wanted me to go to a different one. "
            x " You did everything to convince them to let me go here. "
            x " Even tried suing them at one point. "
            x " You did so much for me, and yet I never did anything for you. "
            x " What can I do to repay your kindness? "
            hide matteneutral at bottom
            show mattesurprised at left
            ma " ... "
            hide mattesurprised at bottom
            show mattehappy at left
            ma " ...You've already repaid me, just by me seeing you happy. "
            ma " Making you smile is what matters the most to me. "
            x " ... "
            x " ...You're too nice. In a good way. "
            scene black with dissolve
            " Awww. What cuties... "
            " You decided to not eavesdrop on their conversation much longer and you walked back into the school. "
            " Damn, you wonder when you're gonna get friends like that. "
            " That's true friendship right there. Probably something that you'll never get. "
            " I'm sorry, I'm being mean. I really gotta stop otherwise I'm getting fired. "
            " Anyway... "
            play sound "audio/bellring.mp3"
            " As you walked the halls of your school, the bell rings not too long after you went back into the school and started roaming around. "
            " You were about to turn a corner before you immediately turned yourself back so that you could get to your classroom. "
            pause 2.0
            jump ocphysicsclass1
        else:
            x " So... Why're you here again? "
            x " I just wanted to spend time with you. "
            x " Alright...? Why would you wanna spend time with someone like me though? "
            hide matteneutral at bottom
            show mattehappy at left
            x " Because I want to, silly. "
            x " And also because I think you're really cool. "
            x " ...Cool? What makes you think that I'm cool? "
            hide mattehappy at bottom
            show mattesad at left
            x " You really don't think you're cool, Jam? wow, you really gotta think more positively... "
            hide mattesad at bottom
            show matteneutral at left
            x " But I think everything about you is cool! "
            x " ...Even if I can get a little violent to others...? Even if I can be a little rude to you...? "
            x " Well, yes. Not everyone is perfect, silly. "
            x " We're all different people, and there's no such thing as a perfect person. "
            x " We've all got our flaws and stuff no matter how perfect we think we are. "
            x " But to me, I think you're perfect, Jam. There's nothing that could make me change my mind. "
            x " I'm not taking any negative comments about yourself! "
            x " ... "
            hide jamneutral at bottom
            show jamhappy at right
            x " ...You know... "
            x " I'm grateful that I got to be your friend. "
            x " I thought you'd just ignore me back in the very first time we met, but you talked to me. Every single day. "
            x " And I never found it annoying. "
            x " I always told you that I wanted to go to this school, but... "
            x " My family wanted me to go to a different one. "
            x " You did everything to convince them to let me go here. "
            x " Even tried suing them at one point. "
            x " You did so much for me, and yet I never did anything for you. "
            x " What can I do to repay your kindness? "
            hide matteneutral at bottom
            show mattesurprised at left
            x " ... "
            hide mattesurprised at bottom
            show mattehappy at left
            x " ...You've already repaid me, just by me seeing you happy. "
            x " Making you smile is what matters the most to me. "
            x " ... "
            x " ...You're too nice. In a good way. "
            scene black with dissolve
            " Awww. What cuties... "
            " You decided to not eavesdrop on their conversation much longer and you walked back into the school. "
            " Damn, you wonder when you're gonna get friends like that. "
            " That's true friendship right there. Probably something that you'll never get. "
            " I'm sorry, I'm being mean. I really gotta stop otherwise I'm getting fired. "
            " Anyway... "
            play sound "audio/bellring.mp3"
            " As you walked the halls of your school, the bell rings not too long after you went back into the school and started roaming around. "
            " You were about to turn a corner before you immediately turned yourself back so that you could get to your classroom. "
            pause 2.0
            jump ocphysicsclass1
    label ocgym4:
        # spark. orchid
        # orchid needs advice from Spark
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " As you were walking into the school's gym and walking around to find somewhere to sit... "
        " You saw two of your classmates talking to eachother. "
        " Curious, you decided to sit near them to listen to what they were talking about. "
        show sparkneutral at left with easeinright
        show orchidsad at right with easeinright
        if sparkknow == True and orchidknow == True:
            oc " I don't know, Spark. "
            oc " I've just been feeling this way and I don't like it at all. "
            " Oooh, something serious. Probably best to not say anything for now. "
            sp " Well... I don't really know how to help you since I'm not going through what you're feeling. "
            oc " I don't really need your help or anything, I just want you to listen for a bit. "
            stop music fadeout 0.5
            sp " Alright, then... I'm a good listener, don't worry. "
            play music "audio/emotionalmoment.mp3" fadein 0.5
            hide orchidsad at bottom
            show orchidneutral at right
            oc " This is gonna be a bit embarrasing, but uh... "
            oc " You ever heard of that thing called hypersexuality? "
            sp " I've heard about it before, yeah. "
            oc " Well, I've had that thing. Ever since I was 11 years old, actually. "
            sp " Geez, that must suck... "
            oc " It does suck a whole lot. "
            oc " Having thoughts you don't want to have every now and then... "
            oc " And back then I thought that this was normal. "
            oc " Only then, years later I figured out that it wasn't normal at all. "
            oc " I honestly wish I hadn't clicked on that video... "
            oc " Then I wouldn't have to be this way. "
            oc " I would've been normal. And not like...this. "
            oc " The only thing I've been wanting ever since I figured out that I was weird, was to be normal. "
            oc " It's so hard living like this... "
            sp " ... "
            sp " You know, even after hearing all that, I don't think you're weird. "
            sp " We've all got our problems that we have to go through, and that includes you. "
            sp " In the end, you're going to be just fine. "
            sp " Even though you're suffering now, your suffering would end later. "
            sp " No matter how weird you think you are, you're still my friend. "
            sp " I wouldn't just drop you for being honest with me about how you're feeling. "
            sp " And honestly, I'm proud of you for having the courage to even talk about this to me. "
            sp " Just know that I'll always be there for you. That's what friends are for, aren't they? "
            oc " ... "
            hide orchidneutral at bottom
            show orchidhappy at right
            oc " I honestly thought that you'd find me weird, but you didn't. "
            oc " You're a good friend, Spark. I think the world needs more people like you. "
            hide sparkneutral at bottom
            show sparkhappy at left
            sp " Eh, I'm just saying what I was thinking about your situation. "
            oc " And you've got a good mind and good thoughts. "
            sp " Was I really good at comforting you? "
            oc " Yes. You made me feel better the moment I heard your words! "
            sp " I'm glad I made you feel better then. "
            scene black with dissolve
            stop music fadeout 0.5
            " You decided not to say anything and you were just chilling on your phone whilst you were listening into their conversation. "
            " Damn, never knew that someone could suffer from those things THAT young... "
            " You feel bad for Orchid and wishes that they would feel better soon. "
            " Why were you just listening into their conversation and not saying anything? "
            " Well, you didn't really want to ruin their moment. "
            " You just let them talk about their feelings. "
            play music "audio/paperhigh.mp3" fadein 0.5
            play sound "audio/bellring.mp3"
            " The bell rings a few minutes later, and you get up from your seat to go to the next class. "
            pause 2.0
            jump ocphysicsclass1
        elif sparkknow == True and orchidknow == False:
            x " I don't know, Spark. "
            x " I've just been feeling this way and I don't like it at all. "
            " Oooh, something serious. Probably best to not say anything for now. "
            sp " Well... I don't really know how to help you since I'm not going through what you're feeling. "
            x " I don't really need your help or anything, I just want you to listen for a bit. "
            stop music fadeout 0.5
            sp " Alright, then... I'm a good listener, don't worry. "
            play music "audio/emotionalmoment.mp3" fadein 0.5
            hide orchidsad at bottom
            show orchidneutral at right
            x " This is gonna be a bit embarrasing, but uh... "
            x " You ever heard of that thing called hypersexuality? "
            sp " I've heard about it before, yeah. "
            x " Well, I've had that thing. Ever since I was 11 years old, actually. "
            sp " Geez, that must suck... "
            x " It does suck a whole lot. "
            x " Having thoughts you don't want to have every now and then... "
            x " And back then I thought that this was normal. "
            x " Only then, years later I figured out that it wasn't normal at all. "
            x " I honestly wish I hadn't clicked on that video... "
            x " Then I wouldn't have to be this way. "
            x " I would've been normal. And not like...this. "
            x " The only thing I've been wanting ever since I figured out that I was weird, was to be normal. "
            x " It's so hard living like this... "
            sp " ... "
            sp " You know, even after hearing all that, I don't think you're weird. "
            sp " We've all got our problems that we have to go through, and that includes you. "
            sp " In the end, you're going to be just fine. "
            sp " Even though you're suffering now, your suffering would end later. "
            sp " No matter how weird you think you are, you're still my friend. "
            sp " I wouldn't just drop you for being honest with me about how you're feeling. "
            sp " And honestly, I'm proud of you for having the courage to even talk about this to me. "
            sp " Just know that I'll always be there for you. That's what friends are for, aren't they? "
            x " ... "
            hide orchidneutral at bottom
            show orchidhappy at right
            x " I honestly thought that you'd find me weird, but you didn't. "
            x " You're a good friend, Spark. I think the world needs more people like you. "
            hide sparkneutral at bottom
            show sparkhappy at left
            sp " Eh, I'm just saying what I was thinking about your situation. "
            x " And you've got a good mind and good thoughts. "
            sp " Was I really good at comforting you? "
            x " Yes. You made me feel better the moment I heard your words! "
            sp " I'm glad I made you feel better then. "
            scene black with dissolve
            stop music fadeout 0.5
            " You decided not to say anything and you were just chilling on your phone whilst you were listening into their conversation. "
            " Damn, never knew that someone could suffer from those things THAT young... "
            " You feel bad for the guy venting and wishes that they would feel better soon. "
            " Why were you just listening into their conversation and not saying anything? "
            " Well, you didn't really want to ruin their moment. "
            " You just let them talk about their feelings. "
            play music "audio/paperhigh.mp3" fadein 0.5
            play sound "audio/bellring.mp3"
            " The bell rings a few minutes later, and you get up from your seat to go to the next class. "
            pause 2.0
            jump ocphysicsclass1
        elif sparkknow == False and orchidknow == True:
            oc " I don't know, Spark. "
            oc " I've just been feeling this way and I don't like it at all. "
            " Oooh, something serious. Probably best to not say anything for now. "
            x " Well... I don't really know how to help you since I'm not going through what you're feeling. "
            oc " I don't really need your help or anything, I just want you to listen for a bit. "
            stop music fadeout 0.5
            x " Alright, then... I'm a good listener, don't worry. "
            play music "audio/emotionalmoment.mp3" fadein 0.5
            hide orchidsad at bottom
            show orchidneutral at right
            oc " This is gonna be a bit embarrasing, but uh... "
            oc " You ever heard of that thing called hypersexuality? "
            x " I've heard about it before, yeah. "
            oc " Well, I've had that thing. Ever since I was 11 years old, actually. "
            x " Geez, that must suck... "
            oc " It does suck a whole lot. "
            oc " Having thoughts you don't want to have every now and then... "
            oc " And back then I thought that this was normal. "
            oc " Only then, years later I figured out that it wasn't normal at all. "
            oc " I honestly wish I hadn't clicked on that video... "
            oc " Then I wouldn't have to be this way. "
            oc " I would've been normal. And not like...this. "
            oc " The only thing I've been wanting ever since I figured out that I was weird, was to be normal. "
            oc " It's so hard living like this... "
            x " ... "
            x " You know, even after hearing all that, I don't think you're weird. "
            x " We've all got our problems that we have to go through, and that includes you. "
            x " In the end, you're going to be just fine. "
            x " Even though you're suffering now, your suffering would end later. "
            x " No matter how weird you think you are, you're still my friend. "
            x " I wouldn't just drop you for being honest with me about how you're feeling. "
            x " And honestly, I'm proud of you for having the courage to even talk about this to me. "
            x " Just know that I'll always be there for you. That's what friends are for, aren't they? "
            oc " ... "
            hide orchidneutral at bottom
            show orchidhappy at right
            oc " I honestly thought that you'd find me weird, but you didn't. "
            oc " You're a good friend, Spark. I think the world needs more people like you. "
            hide sparkneutral at bottom
            show sparkhappy at left
            x " Eh, I'm just saying what I was thinking about your situation. "
            oc " And you've got a good mind and good thoughts. "
            x " Was I really good at comforting you? "
            oc " Yes. You made me feel better the moment I heard your words! "
            x " I'm glad I made you feel better then. "
            scene black with dissolve
            stop music fadeout 0.5
            " You decided not to say anything and you were just chilling on your phone whilst you were listening into their conversation. "
            " Damn, never knew that someone could suffer from those things THAT young... "
            " You feel bad for Orchid and wishes that they would feel better soon. "
            " Why were you just listening into their conversation and not saying anything? "
            " Well, you didn't really want to ruin their moment. "
            " You just let them talk about their feelings. "
            play music "audio/paperhigh.mp3" fadein 0.5
            play sound "audio/bellring.mp3"
            " The bell rings a few minutes later, and you get up from your seat to go to the next class. "
            pause 2.0
            jump ocphysicsclass1
        else:
            x " I don't know, Spark. "
            x " I've just been feeling this way and I don't like it at all. "
            " Oooh, something serious. Probably best to not say anything for now. "
            x " Well... I don't really know how to help you since I'm not going through what you're feeling. "
            x " I don't really need your help or anything, I just want you to listen for a bit. "
            stop music fadeout 0.5
            x " Alright, then... I'm a good listener, don't worry. "
            play music "audio/emotionalmoment.mp3" fadein 0.5
            hide orchidsad at bottom
            show orchidneutral at right
            x " This is gonna be a bit embarrasing, but uh... "
            x " You ever heard of that thing called hypersexuality? "
            x " I've heard about it before, yeah. "
            x " Well, I've had that thing. Ever since I was 11 years old, actually. "
            x " Geez, that must suck... "
            x " It does suck a whole lot. "
            x " Having thoughts you don't want to have every now and then... "
            x " And back then I thought that this was normal. "
            x " Only then, years later I figured out that it wasn't normal at all. "
            x " I honestly wish I hadn't clicked on that video... "
            x " Then I wouldn't have to be this way. "
            x " I would've been normal. And not like...this. "
            x " The only thing I've been wanting ever since I figured out that I was weird, was to be normal. "
            x " It's so hard living like this... "
            x " ... "
            x " You know, even after hearing all that, I don't think you're weird. "
            x " We've all got our problems that we have to go through, and that includes you. "
            x " In the end, you're going to be just fine. "
            x " Even though you're suffering now, your suffering would end later. "
            x " No matter how weird you think you are, you're still my friend. "
            x " I wouldn't just drop you for being honest with me about how you're feeling. "
            x " And honestly, I'm proud of you for having the courage to even talk about this to me. "
            x " Just know that I'll always be there for you. That's what friends are for, aren't they? "
            x " ... "
            hide orchidneutral at bottom
            show orchidhappy at right
            x " I honestly thought that you'd find me weird, but you didn't. "
            x " You're a good friend, Spark. I think the world needs more people like you. "
            hide sparkneutral at bottom
            show sparkhappy at left
            x " Eh, I'm just saying what I was thinking about your situation. "
            x " And you've got a good mind and good thoughts. "
            x " Was I really good at comforting you? "
            x " Yes. You made me feel better the moment I heard your words! "
            x " I'm glad I made you feel better then. "
            scene black with dissolve
            stop music fadeout 0.5
            " You decided not to say anything and you were just chilling on your phone whilst you were listening into their conversation. "
            " Damn, never knew that someone could suffer from those things THAT young... "
            " You feel bad for the guy venting and wishes that they would feel better soon. "
            " Why were you just listening into their conversation and not saying anything? "
            " Well, you didn't really want to ruin their moment. "
            " You just let them talk about their feelings. "
            play music "audio/paperhigh.mp3" fadein 0.5
            play sound "audio/bellring.mp3"
            " The bell rings a few minutes later, and you get up from your seat to go to the next class. "
            pause 2.0
            jump ocphysicsclass1
    label occafe4:
        # Nox, Mia, Disk
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walk into the cafeteria and spot your three classmates sitting on different tables. "
        " You're thinking about talking to one of them... but who do you talk to? "
        if noxknow,miaknow,diskknow == True:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump neru
                " {image=miaicon} Mia {image=miaicon} ":
                    jump teto
                " {image=diskicon} Disk {image=diskicon} ":
                    jump miku
        elif noxknow,miaknow == True and diskknow == False:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump neru
                " {image=miaicon} Mia {image=miaicon} ":
                    jump teto
                " {image=diskicon} A energetic looking guy {image=diskicon} ":
                    jump miku
        elif noxknow,diskknow == True and miaknow == False:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump neru
                " {image=miaicon} A girl with a flower on her head {image=miaicon} ":
                    jump teto
                " {image=diskicon} Disk {image=diskicon} ":
                    jump miku
        elif miaknow,diskknow == True and noxknow == False:
            menu:
                " {image=noxicon} A sleepy looking guy {image=noxicon} ":
                    jump neru
                " {image=miaicon} Mia {image=miaicon} ":
                    jump teto
                " {image=diskicon} Disk {image=diskicon} ":
                    jump miku
        elif noxknow == True and miaknow,diskknow == False:
            menu:
                " {image=noxicon} Nox {image=noxicon} ":
                    jump neru
                " {image=miaicon} A girl with a flower on her head {image=miaicon} ":
                    jump teto
                " {image=diskicon} An energetic looking guy {image=diskicon} ":
                    jump miku
        elif miaknow == True and noxknow,diskknow == False:
            menu:
                " {image=noxicon} A sleepy looking guy {image=noxicon} ":
                    jump neru
                " {image=miaicon} Mia {image=miaicon} ":
                    jump teto
                " {image=diskicon} An energetic looking guy {image=diskicon} ":
                    jump miku
        elif diskknow == True and noxknow, miaknow == False:
            menu:
                " {image=noxicon} A sleepy looking guy {image=noxicon} ":
                    jump neru
                " {image=miaicon} A girl with a flower on her head {image=miaicon} ":
                    jump teto
                " {image=diskicon} Disk {image=diskicon} ":
                    jump miku
        else:
            menu:
                " {image=noxicon} A sleepy looking guy {image=noxicon} ":
                    jump neru
                " {image=miaicon} A girl with a flower on her head {image=miaicon} ":
                    jump teto
                " {image=diskicon} An energetic looking guy {image=diskicon} ":
                    jump miku
        label neru:
            show noxneutral at center with easeinright
            if noxknow == True:
                " He seems to look better than he usually does. "
                " Still a little bit tired, but he looks better. "
                " You ask him if he's doing alright now. "
                n " ...Oh, uh...me? "
                n " I'm doing better, yes... "
                n " Though, Mister Altrix told me to rest in the school's clinic for now... "
                n " I'm not complaining, since I get to rest... And since I get to skip the school day... "
                " Lucky ass bitch... Then again he has that sleeping condition so...not so lucky. "
                n " But... I do miss being with my friends... "
                n " Though I don't want to bother them into visiting me at the clinic... "
                n " I think I'd be a bit annoying to them if I do that... "
                n " That's why I just decided to be here instead...To get some food to take my mind off of being annoying... "
                n " Just thinking about a few things while I'm eating... "
                " He sounds pretty lonely. "
                " Maybe you could give him some company...? "
                n " ...? "
                n " You want to...stay with me? "
                " It was as if he thought that you'd leave him after talking to him for a bit. "
                n " ... "
                n " ...Are you sure that I won't bore you...? "
                " You nodded. "
                n " ...Okay... "
                n " I don't really know what to say now, but... "
                n " How about let's talk about our...dreams...? "
                n " It's the only thing I can think about... "
                scene black with dissolve
                " You spent the rest of the break talking with Nox about the dreams you've had. "
                " Compared to the other times you've been with him... "
                " ...He seems more happier talking with you. He must've been getting real lonely. "
                " Poor guy. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes of chatting. "
                " You then get up from your seat, and started walking back to your classroom for the next class. "
                pause 2.0
                jump ocphysicsclass1
            else:
                " Hey, this is the guy that keeps sleeping in your class. "
                " You've heard that this guy got into a little accident...I think, according to Mister Sol? "
                " You can't really remember. You have bad memory. "
                " Anyway, You ask him if he's doing alright now. "
                x " ...Oh, uh...me? "
                x " I'm doing better, yes... "
                x " Though, Mister Altrix told me to rest in the school's clinic for now... "
                x " I'm not complaining, since I get to rest... And since I get to skip the school day... "
                " Lucky ass bitch... Then again he has that sleeping condition so...not so lucky. "
                x " But... I do miss being with my friends... "
                x " Though I don't want to bother them into visiting me at the clinic... "
                x " I think I'd be a bit annoying to them if I do that... "
                x " That's why I just decided to be here instead...To get some food to take my mind off of being annoying... "
                x " Just thinking about a few things while I'm eating... "
                " He sounds pretty lonely. "
                " Maybe you could give him some company...? "
                x " ...? "
                x " You want to...stay with me? "
                " It was as if he thought that you'd leave him after talking to him for a bit. "
                x " ... "
                x " ...Are you sure that I won't bore you...? "
                " You nodded. "
                x " ...Okay... "
                x " I forgot to introduce myself to you earlier, by the way... "
                x " Um... "
                $ noxknow = True
                n " I'm Nox...Nox Cesso...Nice to meet you... "
                n " ... "
                n " I don't really know what to say now, but... "
                n " How about let's talk about our...dreams...? "
                n " It's the only thing I can think about... "
                scene black with dissolve
                " You spent the rest of the break talking with Nox about the dreams you've had. "
                " Compared to the other times you've seen him... "
                " ...He seems more happier talking with you. He must've been getting real lonely. "
                " Poor guy. "
                play sound "audio/bellring.mp3"
                " The bell rings after a few minutes of chatting. "
                " You then get up from your seat, and started walking back to your classroom for the next class. "
                pause 2.0
                jump ocphysicsclass1
        label teto:
            show mianeutral at center with easeinleft
            if miaknow == True:
                " You sat next to Mia to see what she was doing. "
                " Seems like she's just messing with one of her potted plants... "
                " You ask Mia what type of plant that was. "
                m " Oh! [name], hi! "
                m " This plant? This is a cactus, silly! "
                m " Isn't it obvious as to what it is? "
                " ... "
                " Sure you did1 You just needed to make sure that you were seing what you were actually seeing! "
                hide mianeutral at bottom
                show miahappy at center
                m " Uh huh, sure! "
                hide miahappy at bottom
                show mianeutral at center
                m " Anywho, this one's called Maya! "
                m " I like to name my plants, eheh... "
                m " I have a lot of name ideas for my plants! "
                m " Though, if I ever grow way too many plants, then I start to run out of ideas... "
                m " No, I don't want two to have the same name! Then I'll get confused at some point on which one is which, even if they're different plants! "
                " ...You can tell she really likes and care for her plants. "
                " Interesting. You're sure the gardening teacher must like her a lot. "
                " It would be surprising if the gardening teacher doesn't like her. "
                " Then again, you did overhear that Mia was the top student in gardening class... "
                " Makes sense since she likes flowers a lot. "
                " And another thing you've heard is that Miss Wisteria treats Mia like a little sister. "
                " That's pretty wholesome, actually... "
                m " Helloooo? [name]? you there? "
                m " What I said was - If you wanted to know some facts about plants! "
                " Seems like you zoned off into your thoughts for a split second there. "
                " You're pretty sure you can tune off Mia's yapping about plants, so... "
                " You told her that you wanted to hear some of her facts. "
                hide mianeutral at bottom
                show miahappy at center
                m " Yipee! Alright, so...! "
                scene black with dissolve
                " You did not listen to Mia yapping for the entire break. "
                " You kind of just sat there and nodded while you were playing a game of solitaire in your mind. "
                " You even said some 'oh' and 'uh huh's while you were pretending to listen. "
                " Totally made you look like you were actually listening. You're such a professional! "
                play sound "audio/bellring.mp3"
                " The bell rings, cutting you off of your solitaire mind gaming and stopping Mia from yapping to you anymore. "
                " You get up from your seat so that you could go to your next class. "
                pause 2.0
                jump ocphysicsclass1
            else:
                " You sat next to the girl to see what she was doing. "
                " Seems like she's just messing with one of her potted plants... "
                " You ask the girl what type of plant that was. "
                x " Oh! [name], hi! "
                x " This plant? This is a cactus, silly! "
                x " Isn't it obvious as to what it is? "
                " ... "
                " Sure you did1 You just needed to make sure that you were seing what you were actually seeing! "
                hide mianeutral at bottom
                show miahappy at center
                x " Uh huh, sure! "
                hide miahappy at bottom
                show mianeutral at center
                x " Ohhh, right! I didn't get to introduce myself to you yetttt!! I'm so sorry! "
                $ miaknow = True
                m " My name is Mia! I like to plant stuff and flowers around the school! "
                m " This little plant over here is called Maya! "
                m " I like to name my plants, eheh... "
                m " I have a lot of name ideas for my plants! "
                m " Though, if I ever grow way too many plants, then I start to run out of ideas... "
                m " No, I don't want two to have the same name! Then I'll get confused at some point on which one is which, even if they're different plants! "
                " ...You can tell she really likes and care for her plants. "
                " Interesting. You're sure the gardening teacher must like her a lot. "
                " It would be surprising if the gardening teacher doesn't like her. "
                " Then again, you did overhear that Mia was the top student in gardening class... "
                " Makes sense since she likes flowers a lot. "
                " And another thing you've heard is that Miss Wisteria treats Mia like a little sister. "
                " That's pretty wholesome, actually... "
                m " Helloooo? [name]? you there? "
                m " What I said was - If you wanted to know some facts about plants! "
                " Seems like you zoned off into your thoughts for a split second there. "
                " You're pretty sure you can tune off Mia's yapping about plants, so... "
                " You told her that you wanted to hear some of her facts. "
                hide mianeutral at bottom
                show miahappy at center
                m " Yipee! Alright, so...! "
                scene black with dissolve
                " You did not listen to Mia yapping for the entire break. "
                " You kind of just sat there and nodded while you were playing a game of solitaire in your mind. "
                " You even said some 'oh' and 'uh huh's while you were pretending to listen. "
                " Totally made you look like you were actually listening. You're such a professional! "
                play sound "audio/bellring.mp3"
                " The bell rings, cutting you off of your solitaire mind gaming and stopping Mia from yapping to you anymore. "
                " You get up from your seat so that you could go to your next class. "
                pause 2.0
                jump ocphysicsclass1
        label miku:
            show diskneutral at center with easeinright
            if diskknow == True:
                " You sat next to him. "
                " He had his headphones on... "
                " You tapped on his shoulder so that you could get his attention. "
                d " Hm? "
                " Disk took off his headset and he looked around before looking at you. "
                d " Oh, [name]! Sup!! "
                d " You here to chill, too? "
                d " Well! I was just listening to one of my favorite vocaloid artists! "
                " Vocaloid...? "
                " That rings a bell in your mind, but you can't remember what it was. "
                " You asked Disk what vocaloid was, and he seemed to be surprised. "
                d " ...You don't know what vocaloid is?! "
                d " It's really popular, [name]! I'm surprised that you don't know about it! "
                d " Maybe you know what it is, but you just forgot about it? "
                d " You know... vocaloid is the thing where Hatsune Miku came from! "
                " Oh. OH. "
                " Yeah, now you remember. "
                d " There we go! I knew you knew about vocaloid! "
                d " Anyway, you don't mind me talking about my favorite vocaloids, right? "
                d " Whilst I think Miku is good, there's a lot of underrated vocaloids! "
                d " Like for example, Kazehiki and Aoki lapis! "
                d " Whaaat? Kaito, Gumi, Meiko and other somewhat popular vocaloids aren't that underrated... "
                d " They've all got a lot of popular songs! "
                d " Kazehiki is honestly my number 1 favorite. I love how his voice sounds! "
                d " Lemme reccomend a song for you with Kazehiki in it, let me see... "
                " Disk pulls out his phone and pulls out a playlist filled with Kazehiki themed songs. "
                " He then finds two songs that he really likes and shoves his phone into your face. "
                d " Here we go! "
                d " I'd reccomend listening to the Kazehiki cover of Bitter Chocolate Decoration... "
                d " ... And I also reccomend listening to dance of the corpses Kazehiki cover! "
                d " Really, most of his songs are just covers, eheh... I haven't seen someone make an actual song with him just yet! "
                d " If I knew anything about how Vocaloid works, I'd make a song with him singing! "
                d " ...If only I was good at writing lyrics and tuning, eheh... "
                d " Now about Aoki Lapis! She's also really really underrated! "
                d " I'll go get a playlist with some songs that feature her in just a bit, alright? "
                " Disk, once agan, gets his phone and looks into his playlist. "
                " He scrolls for a bit until he finds a song that he likes and shows it to you. "
                d " Here's one of the songs that I like! "
                d " It's called Faster Than A Shooting Star by OccasionalSubs! "
                d " I like it a whole lot, since it's very catchy! "
                " Disk continues to ramble on and on about vocaloids... "
                scene black with dissolve
                " You spent the entire break talking to Disk about underrated vocaloids. "
                " Did you just spend your entire probably 45 minute break talking about vocaloids? yes. "
                " Was it worth it? also yes. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit of yapping. "
                " You getup from your seat so that you could go to your next class. "
                pause 2.0
                jump ocphysicsclass1
            else:
                " You sat next to him. "
                " He had his headphones on... "
                " You tapped on his shoulder so that you could get his attention. "
                x " Hm? "
                " He took off his headset and he looked around before looking at you. "
                x " Oh, [name]! Sup!! "
                x " You here to chill, too? "
                x " Well! I was just listening to one of my favorite vocaloid artists! "
                " Vocaloid...? "
                " That rings a bell in your mind, but you can't remember what it was. "
                " You asked him what vocaloid was, and he seemed to be surprised. "
                x " ...You don't know what vocaloid is?! "
                x " It's really popular, [name]! I'm surprised that you don't know about it! "
                x " Maybe you know what it is, but you just forgot about it? "
                x " You know... vocaloid is the thing where Hatsune Miku came from! "
                " Oh. OH. "
                " Yeah, now you remember. "
                x " There we go! I knew you knew about vocaloid! "
                x " Wait, I almost forgot to introduce myself to you! I'm so sorry! "
                $ diskknow = True
                d " I'm Disk! Nice to meet you! "
                d " Anyway, you don't mind me talking about my favorite vocaloids, right? "
                d " Whilst I think Miku is good, there's a lot of underrated vocaloids! "
                d " Like for example, Kazehiki and Aoki lapis! "
                d " Whaaat? Kaito, Gumi, Meiko and other somewhat popular vocaloids aren't that underrated... "
                d " They've all got a lot of popular songs! "
                d " Kazehiki is honestly my number 1 favorite. I love how his voice sounds! "
                d " Lemme reccomend a song for you with Kazehiki in it, let me see... "
                " Disk pulls out his phone and pulls out a playlist filled with Kazehiki themed songs. "
                " He then finds two songs that he really likes and shoves his phone into your face. "
                d " Here we go! "
                d " I'd reccomend listening to the Kazehiki cover of Bitter Chocolate Decoration... "
                d " ... And I also reccomend listening to dance of the corpses Kazehiki cover! "
                d " Really, most of his songs are just covers, eheh... I haven't seen someone make an actual song with him just yet! "
                d " If I knew anything about how Vocaloid works, I'd make a song with him singing! "
                d " ...If only I was good at writing lyrics and tuning, eheh... "
                d " Now about Aoki Lapis! She's also really really underrated! "
                d " I'll go get a playlist with some songs that feature her in just a bit, alright? "
                " Disk, once agan, gets his phone and looks into his playlist. "
                " He scrolls for a bit until he finds a song that he likes and shows it to you. "
                d " Here's one of the songs that I like! "
                d " It's called Faster Than A Shooting Star by OccasionalSubs! "
                d " I like it a whole lot, since it's very catchy! "
                " Disk continues to ramble on and on about vocaloids... "
                scene black with dissolve
                " You spent the entire break talking to Disk about underrated vocaloids. "
                " Did you just spend your entire probably 45 minute break talking about vocaloids? yes. "
                " Was it worth it? also yes. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit of yapping. "
                " You getup from your seat so that you could go to your next class. "
                pause 2.0
                jump ocphysicsclass1
    label ocrooftop4:
        # Koa - wondering stuff about life
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walked up into the rooftop, taking in the fresh air. "
        " As you walked around, you spotted one of your classmates just staring off into the distance. "
        " Curious as to what they were doing, you walked up to them. "
        show koaneutral at center with easeinleft
        if koaknow == True:
            k " ... "
            k " Oh, uh... hey there. "
            k " Just came here to take a breather. "
            k " I don't really want to deal with my classmates shenanigans right now. "
            k " They're fighting in the library... "
            k " Where even is the librarian? I don't know myself. "
            k " The librarian is almost never there, actually. It's a miracle if they show up. "
            k " ...Actually, I'm not even sure if the librarian is always gone. "
            k " Sometimes, whenever I pass by their desk I would hear some sort of noises from a game. "
            k " Though, when I look behind the desk I don't see anyone. Odd, isn't it? "
            k " I don't mind wanting to game a lot, but sometimes you just have to do your job, you know? "
            k " But, ehhh... I can't just drag them out of their gaming session. That would be rude. "
            k " All we can do is just wait until they decide to come out there and do their job themselves. "
            k " ...Enough of the library talk, um... "
            k " (Jeez, what else can I talk about to keep them entertained?) "
            k " Do you read books? You probably don't, but uh... "
            k " I could show some of my favorite books if you'd like. "
            " You had nothing to do, so you decided that you wanted to see his favorite books. "
            k " Alright... "
            scene black with dissolve
            " You spent the entire break talking with Koa about his favorite books. "
            " You actually found some of them pretty interesting. Even though books might not be your thing. "
            " You thought of reading them at one point, but you'll probably forget to check them out. "
            " Oh well. "
            play sound "audio/bellring.mp3"
            " The bell rings, meaning that it's time for the next class. "
            " You then walk down from the rooftop so that you could go to your next class. "
            pause 2.0
            jump ocphysicsclass1
        else:
            x " ... "
            x " Oh, uh... hey there. "
            x " Just came here to take a breather. "
            $ koaknow = True
            k " I'm Koa, by the way. You must be the new student here. "
            k " I don't really want to deal with my classmates shenanigans right now. "
            k " They're fighting in the library... "
            k " Where even is the librarian? I don't know myself. "
            k " The librarian is almost never there, actually. It's a miracle if they show up. "
            k " ...Actually, I'm not even sure if the librarian is always gone. "
            k " Sometimes, whenever I pass by their desk I would hear some sort of noises from a game. "
            k " Though, when I look behind the desk I don't see anyone. Odd, isn't it? "
            k " I don't mind wanting to game a lot, but sometimes you just have to do your job, you know? "
            k " But, ehhh... I can't just drag them out of their gaming session. That would be rude. "
            k " All we can do is just wait until they decide to come out there and do their job themselves. "
            k " ...Enough of the library talk, um... "
            k " (Jeez, what else can I talk about to keep them entertained?) "
            k " Do you read books? You probably don't, but uh... "
            k " I could show some of my favorite books if you'd like. "
            " You had nothing to do, so you decided that you wanted to see his favorite books. "
            k " Alright... "
            scene black with dissolve
            " You spent the entire break talking with Koa about his favorite books. "
            " You actually found some of them pretty interesting. Even though books might not be your thing. "
            " You thought of reading them at one point, but you'll probably forget to check them out. "
            " Oh well. "
            play sound "audio/bellring.mp3"
            " The bell rings, meaning that it's time for the next class. "
            " You then walk down from the rooftop so that you could go to your next class. "
            pause 2.0
            jump ocphysicsclass1
    label oclibrary4:
        # jacob, notive, yangyi - library fight
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You walked into the library and you could hear the sounds of people arguing. "
        " Just what is going on? Where's the librarian to help out? "
        " You looked around and didn't see where the librarian was, they weren't even at their desk! "
        " You just decided to deal with this situation yourself, and you walked up to the people who were fighting. "
        show jacobangry at left with easeinright
        show notiveangry at center with easeinright
        show yinhuiangry at right with easeinright
        if jacobknow,notiveknow,yangyiknow == True:
            yi " Listen here, you annoying little shits...! "
            no " Hey, I didn't even do anything...why am I involved in this? "
            jac " Because you decided to step in and stop us from fighting, and now Yinhui over here is throwing a tantrum. "
            yi " TANTRUM?! You decided to waltz right in here and steal the book I was reading! " with vpunch
            jac " Not my fault that I thought that someone forgot to put it back in it's spot. "
            yi " YOU LITTLE PRICK!! " with vpunch
            no " Honestly, this is a stupid argument... "
            yi " DOES IT LOOK LIKE I CARE, BITCH?! " with vpunch
            yi " You know what... "
            show yinhuiangry at center with move
            show notiveangry at right with move
            " He then skedaddled on over to where the other guy was and he tried pulling his goggles off. "
            jac " HEY!! NO TOUCHING MY GOGGLES!! " with vpunch
            yi " Oooh, now you're mad! You touch my book, I touch your goggles! "
            yi " If you're wearing goggles like these and a bandana to cover up msot of your features, then you must be MAD ugly underneath all of that! "
            no " Woah, hey! Yin, that's way too far! "
            jac " LET GO OF ME!! " with vpunch
            " Jeez, this is getting way too far, especially if this is caused just by a simple misunderstanding. "
            " You should try to stop them. "
            " You tried to tell them to stop... "
            " ...But they completely ignored you. Let's try again. "
            yi " I'M NOT LETTING YOU GO THAT EASILY! " with vpunch
            " Guys. "
            jac " GET OFF ME, SERIOUSLY. "
            " ...Guys... "
            no " This is way too scary for me to handle-{nw} "
            hide yinhuiangry at bottom
            show yinhuiconfused at center
            hide notiveangry at bottom
            show notivesurprised at right
            hide jacobangry at bottom
            show jacobsurprised at left
            if kind == True:
                " {sc}GUYS!!!!!!!{/sc} " with vpunch
            elif calm == True:
                " {sc}GUYS.{/sc} " with vpunch
            elif mean == True:
                " {sc}WOULD YOU SHUT UP, YOU STUPID IDIOTS?!{/sc} " with vpunch
            yi " ... "
            jac " ... "
            no " ... "
            scene black with dissolve
            " You spent the entire break giving those three guys a scolding. "
            " Geez, people sometimes... "
            " ...Really makes your blood boil. "
            play sound "audio/bellring.mp3"
            " The bell rang, but you stayed back a bit to make sure you made your words clear. "
            " No fighting. Especially in the library. "
            " Once you got your point across, you went into your classroom. "
            pause 2.0
            jump ocphysicsclass1
        elif jacobknow,notiveknow == True and yangyiknow == False:
            x " Listen here, you annoying little shits...! "
            no " Hey, I didn't even do anything...why am I involved in this? "
            jac " Because you decided to step in and stop us from fighting, and now Yinhui over here is throwing a tantrum. "
            x " TANTRUM?! You decided to waltz right in here and steal the book I was reading! " with vpunch
            jac " Not my fault that I thought that someone forgot to put it back in it's spot. "
            x " YOU LITTLE PRICK!! " with vpunch
            no " Honestly, this is a stupid argument... "
            x " DOES IT LOOK LIKE I CARE, BITCH?! " with vpunch
            x " You know what... "
            show yinhuiangry at center with move
            show notiveangry at right with move
            " He then skedaddled on over to where the other guy was and he tried pulling his goggles off. "
            jac " HEY!! NO TOUCHING MY GOGGLES!! " with vpunch
            x " Oooh, now you're mad! You touch my book, I touch your goggles! "
            x " If you're wearing goggles like these and a bandana to cover up msot of your features, then you must be MAD ugly underneath all of that! "
            no " Woah, hey! Yinhui, that's way too far! "
            jac " LET GO OF ME!! " with vpunch
            " Jeez, this is getting way too far, especially if this is caused just by a simple misunderstanding. "
            " You should try to stop them. "
            " You tried to tell them to stop... "
            " ...But they completely ignored you. Let's try again. "
            x " I'M NOT LETTING YOU GO THAT EASILY! " with vpunch
            " Guys. "
            jac " GET OFF ME, SERIOUSLY. "
            " ...Guys... "
            no " This is way too scary for me to handle-{nw} "
            hide yinhuiangry at bottom
            show yinhuiconfused at center
            hide notiveangry at bottom
            show notivesurprised at right
            hide jacobangry at bottom
            show jacobsurprised at left
            if kind == True:
                " {sc}GUYS!!!!!!!{/sc} " with vpunch
            elif calm == True:
                " {sc}GUYS.{/sc} " with vpunch
            elif mean == True:
                " {sc}WOULD YOU SHUT UP, YOU STUPID IDIOTS?!{/sc} " with vpunch
            x " ... "
            jac " ... "
            no " ... "
            scene black with dissolve
            " You spent the entire break giving those three guys a scolding. "
            " Geez, people sometimes... "
            " ...Really makes your blood boil. "
            play sound "audio/bellring.mp3"
            " The bell rang, but you stayed back a bit to make sure you made your words clear. "
            " No fighting. Especially in the library. "
            " Once you got your point across, you went into your classroom. "
            pause 2.0
            jump ocphysicsclass1
        elif jacobknow,yangyiknow == True and notiveknow == False:
            yi " Listen here, you annoying little shits...! "
            x " Hey, I didn't even do anything...why am I involved in this? "
            jac " Because you decided to step in and stop us from fighting, and now Yinhui over here is throwing a tantrum. "
            yi " TANTRUM?! You decided to waltz right in here and steal the book I was reading! " with vpunch
            jac " Not my fault that I thought that someone forgot to put it back in it's spot. "
            yi " YOU LITTLE PRICK!! " with vpunch
            x " Honestly, this is a stupid argument... "
            yi " DOES IT LOOK LIKE I CARE, BITCH?! " with vpunch
            yi " You know what... "
            show yinhuiangry at center with move
            show notiveangry at right with move
            " He then skedaddled on over to where the other guy was and he tried pulling his goggles off. "
            jac " HEY!! NO TOUCHING MY GOGGLES!! " with vpunch
            yi " Oooh, now you're mad! You touch my book, I touch your goggles! "
            yi " If you're wearing goggles like these and a bandana to cover up msot of your features, then you must be MAD ugly underneath all of that! "
            x " Woah, hey! Yin, that's way too far! "
            jac " LET GO OF ME!! " with vpunch
            " Jeez, this is getting way too far, especially if this is caused just by a simple misunderstanding. "
            " You should try to stop them. "
            " You tried to tell them to stop... "
            " ...But they completely ignored you. Let's try again. "
            yi " I'M NOT LETTING YOU GO THAT EASILY! " with vpunch
            " Guys. "
            jac " GET OFF ME, SERIOUSLY. "
            " ...Guys... "
            x " This is way too scary for me to handle-{nw} "
            hide yinhuiangry at bottom
            show yinhuiconfused at center
            hide notiveangry at bottom
            show notivesurprised at right
            hide jacobangry at bottom
            show jacobsurprised at left
            if kind == True:
                " {sc}GUYS!!!!!!!{/sc} " with vpunch
            elif calm == True:
                " {sc}GUYS.{/sc} " with vpunch
            elif mean == True:
                " {sc}WOULD YOU SHUT UP, YOU STUPID IDIOTS?!{/sc} " with vpunch
            yi " ... "
            jac " ... "
            x " ... "
            scene black with dissolve
            " You spent the entire break giving those three guys a scolding. "
            " Geez, people sometimes... "
            " ...Really makes your blood boil. "
            play sound "audio/bellring.mp3"
            " The bell rang, but you stayed back a bit to make sure you made your words clear. "
            " No fighting. Especially in the library. "
            " Once you got your point across, you went into your classroom. "
            pause 2.0
            jump ocphysicsclass1
        elif notiveknow,yangyiknow == True and jacobknow == False:
            yi " Listen here, you annoying little shits...! "
            no " Hey, I didn't even do anything...why am I involved in this? "
            x " Because you decided to step in and stop us from fighting, and now Yinhui over here is throwing a tantrum. "
            yi " TANTRUM?! You decided to waltz right in here and steal the book I was reading! " with vpunch
            x " Not my fault that I thought that someone forgot to put it back in it's spot. "
            yi " YOU LITTLE PRICK!! " with vpunch
            no " Honestly, this is a stupid argument... "
            yi " DOES IT LOOK LIKE I CARE, BITCH?! " with vpunch
            yi " You know what... "
            show yinhuiangry at center with move
            show notiveangry at right with move
            " He then skedaddled on over to where the other guy was and he tried pulling his goggles off. "
            x " HEY!! NO TOUCHING MY GOGGLES!! " with vpunch
            yi " Oooh, now you're mad! You touch my book, I touch your goggles! "
            yi " If you're wearing goggles like these and a bandana to cover up msot of your features, then you must be MAD ugly underneath all of that! "
            no " Woah, hey! Yin, that's way too far! "
            x " LET GO OF ME!! " with vpunch
            " Jeez, this is getting way too far, especially if this is caused just by a simple misunderstanding. "
            " You should try to stop them. "
            " You tried to tell them to stop... "
            " ...But they completely ignored you. Let's try again. "
            yi " I'M NOT LETTING YOU GO THAT EASILY! " with vpunch
            " Guys. "
            x " GET OFF ME, SERIOUSLY. "
            " ...Guys... "
            no " This is way too scary for me to handle-{nw} "
            hide yinhuiangry at bottom
            show yinhuiconfused at center
            hide notiveangry at bottom
            show notivesurprised at right
            hide jacobangry at bottom
            show jacobsurprised at left
            if kind == True:
                " {sc}GUYS!!!!!!!{/sc} " with vpunch
            elif calm == True:
                " {sc}GUYS.{/sc} " with vpunch
            elif mean == True:
                " {sc}WOULD YOU SHUT UP, YOU STUPID IDIOTS?!{/sc} " with vpunch
            yi " ... "
            x " ... "
            no " ... "
            scene black with dissolve
            " You spent the entire break giving those three guys a scolding. "
            " Geez, people sometimes... "
            " ...Really makes your blood boil. "
            play sound "audio/bellring.mp3"
            " The bell rang, but you stayed back a bit to make sure you made your words clear. "
            " No fighting. Especially in the library. "
            " Once you got your point across, you went into your classroom. "
            pause 2.0
            jump ocphysicsclass1
        elif jacobknow == True and notiveknow,yangyiknow == False:
            x " Listen here, you annoying little shits...! "
            x " Hey, I didn't even do anything...why am I involved in this? "
            jac " Because you decided to step in and stop us from fighting, and now Yinhui over here is throwing a tantrum. "
            x " TANTRUM?! You decided to waltz right in here and steal the book I was reading! " with vpunch
            jac " Not my fault that I thought that someone forgot to put it back in it's spot. "
            x " YOU LITTLE PRICK!! " with vpunch
            x " Honestly, this is a stupid argument... "
            x " DOES IT LOOK LIKE I CARE, BITCH?! " with vpunch
            x " You know what... "
            show yinhuiangry at center with move
            show notiveangry at right with move
            " He then skedaddled on over to where the other guy was and he tried pulling his goggles off. "
            jac " HEY!! NO TOUCHING MY GOGGLES!! " with vpunch
            x " Oooh, now you're mad! You touch my book, I touch your goggles! "
            x " If you're wearing goggles like these and a bandana to cover up msot of your features, then you must be MAD ugly underneath all of that! "
            x " Woah, hey! Yin, that's way too far! "
            jac " LET GO OF ME!! " with vpunch
            " Jeez, this is getting way too far, especially if this is caused just by a simple misunderstanding. "
            " You should try to stop them. "
            " You tried to tell them to stop... "
            " ...But they completely ignored you. Let's try again. "
            x " I'M NOT LETTING YOU GO THAT EASILY! " with vpunch
            " Guys. "
            jac " GET OFF ME, SERIOUSLY. "
            " ...Guys... "
            x " This is way too scary for me to handle-{nw} "
            hide yinhuiangry at bottom
            show yinhuiconfused at center
            hide notiveangry at bottom
            show notivesurprised at right
            hide jacobangry at bottom
            show jacobsurprised at left
            if kind == True:
                " {sc}GUYS!!!!!!!{/sc} " with vpunch
            elif calm == True:
                " {sc}GUYS.{/sc} " with vpunch
            elif mean == True:
                " {sc}WOULD YOU SHUT UP, YOU STUPID IDIOTS?!{/sc} " with vpunch
            x " ... "
            jac " ... "
            x " ... "
            scene black with dissolve
            " You spent the entire break giving those three guys a scolding. "
            " Geez, people sometimes... "
            " ...Really makes your blood boil. "
            play sound "audio/bellring.mp3"
            " The bell rang, but you stayed back a bit to make sure you made your words clear. "
            " No fighting. Especially in the library. "
            " Once you got your point across, you went into your classroom. "
            pause 2.0
            jump ocphysicsclass1
        elif notiveknow == True and jacobknow,yangyiknow == False:
            x " Listen here, you annoying little shits...! "
            no " Hey, I didn't even do anything...why am I involved in this? "
            x " Because you decided to step in and stop us from fighting, and now Yinhui over here is throwing a tantrum. "
            x " TANTRUM?! You decided to waltz right in here and steal the book I was reading! " with vpunch
            x " Not my fault that I thought that someone forgot to put it back in it's spot. "
            x " YOU LITTLE PRICK!! " with vpunch
            no " Honestly, this is a stupid argument... "
            x " DOES IT LOOK LIKE I CARE, BITCH?! " with vpunch
            x " You know what... "
            show yinhuiangry at center with move
            show notiveangry at right with move
            " He then skedaddled on over to where the other guy was and he tried pulling his goggles off. "
            x " HEY!! NO TOUCHING MY GOGGLES!! " with vpunch
            x " Oooh, now you're mad! You touch my book, I touch your goggles! "
            x " If you're wearing goggles like these and a bandana to cover up msot of your features, then you must be MAD ugly underneath all of that! "
            no " Woah, hey! Yin, that's way too far! "
            x " LET GO OF ME!! " with vpunch
            " Jeez, this is getting way too far, especially if this is caused just by a simple misunderstanding. "
            " You should try to stop them. "
            " You tried to tell them to stop... "
            " ...But they completely ignored you. Let's try again. "
            x " I'M NOT LETTING YOU GO THAT EASILY! " with vpunch
            " Guys. "
            x " GET OFF ME, SERIOUSLY. "
            " ...Guys... "
            no " This is way too scary for me to handle-{nw} "
            hide yinhuiangry at bottom
            show yinhuiconfused at center
            hide notiveangry at bottom
            show notivesurprised at right
            hide jacobangry at bottom
            show jacobsurprised at left
            if kind == True:
                " {sc}GUYS!!!!!!!{/sc} " with vpunch
            elif calm == True:
                " {sc}GUYS.{/sc} " with vpunch
            elif mean == True:
                " {sc}WOULD YOU SHUT UP, YOU STUPID IDIOTS?!{/sc} " with vpunch
            x " ... "
            x " ... "
            no " ... "
            scene black with dissolve
            " You spent the entire break giving those three guys a scolding. "
            " Geez, people sometimes... "
            " ...Really makes your blood boil. "
            play sound "audio/bellring.mp3"
            " The bell rang, but you stayed back a bit to make sure you made your words clear. "
            " No fighting. Especially in the library. "
            " Once you got your point across, you went into your classroom. "
            pause 2.0
            jump ocphysicsclass1
        elif yangyiknow == True and jacobknow,notiveknow == False:
            yi " Listen here, you annoying little shits...! "
            x " Hey, I didn't even do anything...why am I involved in this? "
            x " Because you decided to step in and stop us from fighting, and now Yinhui over here is throwing a tantrum. "
            yi " TANTRUM?! You decided to waltz right in here and steal the book I was reading! " with vpunch
            x " Not my fault that I thought that someone forgot to put it back in it's spot. "
            yi " YOU LITTLE PRICK!! " with vpunch
            x " Honestly, this is a stupid argument... "
            yi " DOES IT LOOK LIKE I CARE, BITCH?! " with vpunch
            yi " You know what... "
            show yinhuiangry at center with move
            show notiveangry at right with move
            " He then skedaddled on over to where the other guy was and he tried pulling his goggles off. "
            x " HEY!! NO TOUCHING MY GOGGLES!! " with vpunch
            yi " Oooh, now you're mad! You touch my book, I touch your goggles! "
            yi " If you're wearing goggles like these and a bandana to cover up msot of your features, then you must be MAD ugly underneath all of that! "
            x " Woah, hey! Yin, that's way too far! "
            x " LET GO OF ME!! " with vpunch
            " Jeez, this is getting way too far, especially if this is caused just by a simple misunderstanding. "
            " You should try to stop them. "
            " You tried to tell them to stop... "
            " ...But they completely ignored you. Let's try again. "
            yi " I'M NOT LETTING YOU GO THAT EASILY! " with vpunch
            " Guys. "
            x " GET OFF ME, SERIOUSLY. "
            " ...Guys... "
            x " This is way too scary for me to handle-{nw} "
            hide yinhuiangry at bottom
            show yinhuiconfused at center
            hide notiveangry at bottom
            show notivesurprised at right
            hide jacobangry at bottom
            show jacobsurprised at left
            if kind == True:
                " {sc}GUYS!!!!!!!{/sc} " with vpunch
            elif calm == True:
                " {sc}GUYS.{/sc} " with vpunch
            elif mean == True:
                " {sc}WOULD YOU SHUT UP, YOU STUPID IDIOTS?!{/sc} " with vpunch
            yi " ... "
            x " ... "
            x " ... "
            scene black with dissolve
            " You spent the entire break giving those three guys a scolding. "
            " Geez, people sometimes... "
            " ...Really makes your blood boil. "
            play sound "audio/bellring.mp3"
            " The bell rang, but you stayed back a bit to make sure you made your words clear. "
            " No fighting. Especially in the library. "
            " Once you got your point across, you went into your classroom. "
            pause 2.0
            jump ocphysicsclass1
        else:
            x " Listen here, you annoying little shits...! "
            x " Hey, I didn't even do anything...why am I involved in this? "
            x " Because you decided to step in and stop us from fighting, and now Yinhui over here is throwing a tantrum. "
            x " TANTRUM?! You decided to waltz right in here and steal the book I was reading! " with vpunch
            x " Not my fault that I thought that someone forgot to put it back in it's spot. "
            x " YOU LITTLE PRICK!! " with vpunch
            x " Honestly, this is a stupid argument... "
            x " DOES IT LOOK LIKE I CARE, BITCH?! " with vpunch
            x " You know what... "
            show yinhuiangry at center with move
            show notiveangry at right with move
            " He then skedaddled on over to where the other guy was and he tried pulling his goggles off. "
            x " HEY!! NO TOUCHING MY GOGGLES!! " with vpunch
            x " Oooh, now you're mad! You touch my book, I touch your goggles! "
            x " If you're wearing goggles like these and a bandana to cover up msot of your features, then you must be MAD ugly underneath all of that! "
            x " Woah, hey! Yang, that's way too far! "
            x " LET GO OF ME!! " with vpunch
            " Jeez, this is getting way too far, especially if this is caused just by a simple misunderstanding. "
            " You should try to stop them. "
            " You tried to tell them to stop... "
            " ...But they completely ignored you. Let's try again. "
            x " I'M NOT LETTING YOU GO THAT EASILY! " with vpunch
            " Guys. "
            x " GET OFF ME, SERIOUSLY. "
            " ...Guys... "
            x " This is way too scary for me to handle-{nw} "
            hide yinhuiangry at bottom
            show yinhuiconfused at center
            hide notiveangry at bottom
            show notivesurprised at right
            hide jacobangry at bottom
            show jacobsurprised at left
            if kind == True:
                " {sc}GUYS!!!!!!!{/sc} " with vpunch
            elif calm == True:
                " {sc}GUYS.{/sc} " with vpunch
            elif mean == True:
                " {sc}WOULD YOU SHUT UP, YOU STUPID IDIOTS?!{/sc} " with vpunch
            x " ... "
            x " ... "
            x " ... "
            scene black with dissolve
            " You spent the entire break giving those three guys a scolding. "
            " Geez, people sometimes... "
            " ...Really makes your blood boil. "
            play sound "audio/bellring.mp3"
            " The bell rang, but you stayed back a bit to make sure you made your words clear. "
            " No fighting. Especially in the library. "
            " Once you got your point across, you went into your classroom. "
            pause 2.0
            jump ocphysicsclass1
    label ocphysicsclass1:
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walked into the classroom and saw that the teacher was already there. "
        " You got into your seat and got prepared for the class. "
        show luaneutral at center with easeinleft
        x " Okaaay, class... "
        x " Goodmorning. "
        " The class greeted her with a good morning. "
        x " Did we have any assignments? "
        " A teacher forgetting if there's any assignments? "
        " Well, that's most certainly rare to see. "
        " The class answers with a no, and the teacher takes a moment to think. "
        x " ...Okay. "
        x " The other teachers have told me about something, but I can't remember what... "
        x " Something student related... "
        show temeroneutral at right with easeinright
        if temeroknow == True:
            tm " We have a new classmate, Miss Lua. "
        else:
            x " We have a new classmate, Miss Lua. "
        x " Oh. Right, new student, that's right... "
        x " Thank you, 'Mero. You may take your seat now."
        hide temeroneutral at right with easeoutright
        x " So, new student... let's see... "
        " The teacher pulled out her list of students to see who's new. "
        " And that new guy is you! "
        x " ..[name]. Where is [name]? "
        if diqutte == True:
            show diskneutral at left with easeinleft
            if diskknow == True:
                d " [they] [are] right here, miss! "
            else:
                x " [they] [are] right here, miss! "
            hide diskneutral at left with easeoutleft
        elif spatemnox == True:
            show sparkneutral at right with easeinright
            if sparkknow == True:
                sp " [they] [are] right here, miss. "
            else:
                x " [they] [are] right here, miss. "
            hide sparkneutral at right with easeoutright
        elif jamorcar == True:
            show carmenneutral at left with easeinleft
            if carmenknow == True:
                ca " (*Guitar noise!*) ... "
            else:
                x " (*Guitar noise!*) ... "
            " Seems like that guitar noise was for Miss Lua to notice you. "
            hide carmenneutral at left with easeoutleft
        elif koamiajex == True:
            show jexneutral at right with easeinright
            if jexknow == True:
                j " [they] [are] here, miss. "
            else:
                x " [they] [are] here, miss. "
            hide jexneutral at right with easeoutright
        elif jacnotyinyang == True:
            show yangyineutral at left with easeinleft
            if yinhuiknow == True:
                ya " [they] [are] here, miss! "
            else:
                ya " [they] [are] here, miss! "
            hide yangyineutral at left with easeoutleft
        elif alone == True:
            " Some of your classmates just pointed to where you were. "
        " After looking around for a bit, the teacher eventually spotted you. "
        x " Ah. You're the new kid. "
        x " What's your name again? [name]? Alright. "
        msl " I am Miss Lua. I will be your physics teacher. "
        msl " And before you ask anything, yes, Mister Sol is my brother. "
        msl " I get that question a lot everytime I introduce myself... "
        msl " But enough with the talking, let's get started with our lesson for the day. "
        " Miss Lua then goes back to her desk to find some papers and picks them up. "
        " Seems like she wrote those so that she doesn't have to forget what she has to teach for each class. "
        " Pretty good move, but the problem is if you forget to write in it one day. "
        scene black with dissolve
        " Physics class wasn't that entertaining. "
        " All you had to do was just copy a few things. "
        " Atleast you had something in your notebook now. "
        play sound "audio/bellring.mp3"
        " The bell rings, meaning that class was over and it was time for another break. "
        " You wait for everyone else to get out of the classroom first before you could go out yourself. "
        pause 2.0
        jump ocbreak5
    label ocbreak5:
        scene hallway with dissolve
        " It's the fifth break of the day, and you're still thinking of wandering around the school. "
        " Where do you go? "
        menu:
            " {image=yinyangicon} The front of the school {image=yinyangicon} ":
                jump ocfrontschool5
            " {image=jamicon} The back of the school {image=quinnicon} ":
                jump ocbackschool5
            " {image=carmenicon} The gym {image=sparkicon} ":
                jump ocgym5
            " {image=yinyangicon} The cafeteria {image=notiveicon} ":
                jump occafe5
            " {image=jexicon} The rooftop {image=jexicon} ":
                jump ocrooftop5
            " {image=diskicon} The library {image=diskicon} ":
                jump oclibrary5
    label ocfrontschool5:
        # yinhui - talking about how to get his brothers trust
        scene black with dissolve
        pause 2.0
        scene paperschoolfront with dissolve
        " You walked outside the school just to take a breather. "
        " You walked around for a bit and you spotted one of your classmates sitting underneath a nearby tree. "
        " Curious, you decided to walk up to them and see how they're doing. "
        show yangyineutral at center with easeinbottom
        if yinhuiknow == True:
            ya " Hmmm... "
            " He's humming a little tune. Seems to be distracted... "
            " You sat down next to him so that you could see if he would notice you. "
            " He continues humming for a bit until he finally noticed that you were there. "
            ya " O-oh! [name]! Hi there, heheh... "
            ya " I'm sorry that I didn't notice you, I was just...trying to distract myself. "
            " From what? "
            ya " ...Well, you seee... My brother's been acting real grumpy today. "
            ya " He'll get mad by even the smallest things now... "
            ya " I wanted to give him space, so I decided that me and him should take a quick break until he calms down... "
            ya " Besides, what if he accidentally hurt me while he's this mad? "
            ya " Sigh,,,it's only for the best. "
            ya " He'll get so mad if he saw me talking to you like this, hehe... "
            ya " You see, he's very overprotective over me. And since you're new, he doesn't trust you at all... "
            ya " But! I'm sure I'll figure out something to make you guys friends! "
            ya " And if he ever says something mean to you... "
            ya " Tell me what he said, and I'll talk to him about it. "
            ya " I'm sure he also doesn't mean the words that he says. But if he does... "
            ya " ... I don't know ... "
            ya " How about let's change topic? "
            ya " I wanna learn more about you, actually! "
            scene black with dissolve
            " You spent the entire break talking about yourself to Yangyi. "
            " Honestly, he's a nice guy to have a conversation with. "
            " Also pretty understanding. It makes it easy to talk to him about anything. "
            " Which is pretty neat. "
            play sound "audio/bellring.mp3"
            " The bell rings after a couple of minutes of talking. "
            " You get up from where you were sitting and went to your classroom for the final class of the day. "
            pause 2.0
            jump occookingclass1
        else:
            x " Hmmm... "
            " He's humming a little tune. Seems to be distracted... "
            " You sat down next to him so that you could see if he would notice you. "
            " He continues humming for a bit until he finally noticed that you were there. "
            x " O-oh! [name]! Hi there, heheh... "
            x " I've never gotten to introduce myself to you, now that I think about it... "
            $ yinhuiknow = True
            ya " I'm Yangyi! I'm not sure if you've heard of my brother, but um... his name is Yinhui! "
            ya " Anywho, I'm sorry that I didn't notice you, I was just...trying to distract myself. "
            " From what? "
            ya " ...Well, you seee... My brother's been acting real grumpy today. "
            ya " He'll get mad by even the smallest things now... "
            ya " I wanted to give him space, so I decided that me and him should take a quick break until he calms down... "
            ya " Besides, what if he accidentally hurt me while he's this mad? "
            ya " Sigh,,,it's only for the best. "
            ya " He'll get so mad if he saw me talking to you like this, hehe... "
            ya " You see, he's very overprotective over me. And since you're new, he doesn't trust you at all... "
            ya " But! I'm sure I'll figure out something to make you guys friends! "
            ya " And if he ever says something mean to you... "
            ya " Tell me what he said, and I'll talk to him about it. "
            ya " I'm sure he also doesn't mean the words that he says. But if he does... "
            ya " ... I don't know ... "
            ya " How about let's change topic? "
            ya " I wanna learn more about you, actually! "
            scene black with dissolve
            " You spent the entire break talking about yourself to Yangyi. "
            " Honestly, he's a nice guy to have a conversation with. "
            " Also pretty understanding. It makes it easy to talk to him about anything. "
            " Which is pretty neat. "
            play sound "audio/bellring.mp3"
            " The bell rings after a couple of minutes of talking. "
            " You get up from where you were sitting and went to your classroom for the final class of the day. "
            pause 2.0
            jump occookingclass1
    label ocbackschool5:
        # Jam, Quinn - a fight happens!
        scene black with dissolve
        pause 2.0
        scene paperschoolback with dissolve
        " You walk to the back of the school and you could hear some yelling. "
        " Curious, you walked over to the two people who were arguing. "
        show quinnangry at right with easeinleft
        show jamangry at left with easeinleft
        if quinnknow == True and jamknow == True:
            q " I just can't believe you, you know?! "
            ja " What, it was just a simple prank. It's not like it's a big deal. "
            q " YOU ALMOST GOT MY FRIEND CRUSHED???? " with vpunch
            q " How exactly is that just a simple prank, hm?! "
            q " Almost killing someone while we weren't even looking! "
            ja " Look, I didn't expect anyone to be under there, okay? "
            q " Well maybe you should look first before you do anything stupid like that ever again! "
            ja " I {i}did{/i} look, I just dropped it at the time that someone walked under there. "
            ja " Sooo, when I lifted it up, I didn't see that there was someone there. "
            q " Still! It isn't a good idea at all to do something like that! " with vpunch
            ja " Quit being a baby, Quinn. "
            ja " Learn to have some fun in your life. "
            q " Well I don't like your idea of fun, if you think almost killing someone is funny! "
            ja " Ergh. "
            ja " Listen, if you tell this to the teacher, your ass is gonna get screwed. "
            ja " I'm gonna kill you. Cook you. Then feed you to your friends and family. "
            ja " Got that? "
            q " ...Fine. "
            hide quinnangry at right with easeoutright
            hide jamangry at right with easeoutright
            " ...And they left. "
            " You're thinking about being mischevious. You should probably tell a teacher. "
            " Should you though? "
            menu:
                " Yes, be a snitch ":
                    $ jamsnitch = True
                    " We snitching on this ho fr!! "
                    scene black with dissolve
                    pause 2.0
                    scene hallway with dissolve
                    " You walked around the hallways to find a teacher. "
                    " You eventually spotted Mister Altrix, going to his classroom. "
                    show altrixneutral at center with easeinleft
                    " You walk up to him and greet him. "
                    msa " Oh! Um, hello there, [name]... "
                    msa " Can I help you? "
                    " You informed him of what you heard. "
                    hide altrixneutral at bottom
                    show altrixsad at center
                    msa " Oh my... "
                    msa " That's not a harmless prank at all...! "
                    msa " I'll have a talk with Jam later... "
                    msa " Thank you, [name]. For informing me about this... "
                    play sound "audio/bellring.mp3"
                    pause 1.0
                    hide altrixsad at bottom
                    show altrixneutral at center
                    msa " The bell rang... "
                    msa " You should go to your class now, [name]. "
                    msa " You shouldn't be late! "
                    " You nodded and said bye before going to your classroom. "
                    scene black with dissolve
                    " Wonder what's gonna happen to Jam... "
                    pause 2.0
                    jump occookingclass1
                " Nah we dont snitch ":
                    " Yeah, let's not snitch. "
                    " Snitching is for nerds, anyway. "
                    " Let's just go take a walk around the school instead. "
                    scene black with dissolve
                    " You spent the rest of the break walking around the school. "
                    " You overheard a few conversations, and now you have free drama. "
                    " Great! Now you have something to talk about to your friends. "
                    " Though, some conversations were actually pretty concerning, so... "
                    " Best not to talk about those things and keep it to yourself. "
                    " These students should really learn to be more quiet if they're planning to tell secrets. "
                    play sound "audio/bellring.mp3"
                    pause 1.0
                    " The bell rings after a few minutes of walking around and eavesdropping. "
                    " Time to go to the next class, then... "
                    pause 2.0
                    jump occookingclass1
        elif quinnknow == True and jamknow == False:
            q " I just can't believe you, you know?! "
            x " What, it was just a simple prank. It's not like it's a big deal. "
            q " YOU ALMOST GOT MY FRIEND CRUSHED???? " with vpunch
            q " How exactly is that just a simple prank, hm?! "
            q " Almost killing someone while we weren't even looking! "
            x " Look, I didn't expect anyone to be under there, okay? "
            q " Well maybe you should look first before you do anything stupid like that ever again! "
            x " I {i}did{/i} look, I just dropped it at the time that someone walked under there. "
            x " Sooo, when I lifted it up, I didn't see that there was someone there. "
            q " Still! It isn't a good idea at all to do something like that! " with vpunch
            x " Quit being a baby, Quinn. "
            x " Learn to have some fun in your life. "
            q " Well I don't like your idea of fun, if you think almost killing someone is funny! "
            x " Ergh. "
            x " Listen, if you tell this to the teacher, your ass is gonna get screwed. "
            x " I'm gonna kill you. Cook you. Then feed you to your friends and family. "
            x " Got that? "
            q " ...Fine. "
            hide quinnangry at right with easeoutright
            hide jamangry at right with easeoutright
            " ...And they left. "
            " You're thinking about being mischevious. You should probably tell a teacher. "
            " Should you though? "
            menu:
                " Yes, be a snitch ":
                    $ jamsnitch = True
                    " We snitching on this ho fr!! "
                    scene black with dissolve
                    pause 2.0
                    scene hallway with dissolve
                    " You walked around the hallways to find a teacher. "
                    " You eventually spotted Mister Altrix, going to his classroom. "
                    show altrixneutral at center with easeinleft
                    " You walk up to him and greet him. "
                    msa " Oh! Um, hello there, [name]... "
                    msa " Can I help you? "
                    " You informed him of what you heard. "
                    hide altrixneutral at bottom
                    show altrixsad at center
                    msa " Oh my... "
                    msa " That's not a harmless prank at all...! "
                    msa " I'll have a talk with Jam later... "
                    msa " Thank you, [name]. For informing me about this... "
                    play sound "audio/bellring.mp3"
                    pause 1.0
                    hide altrixsad at bottom
                    show altrixneutral at center
                    msa " The bell rang... "
                    msa " You should go to your class now, [name]. "
                    msa " You shouldn't be late! "
                    " You nodded and said bye before going to your classroom. "
                    scene black with dissolve
                    " Wonder what's gonna happen to that girl... "
                    pause 2.0
                    jump occookingclass1
                " Nah we dont snitch ":
                    " Yeah, let's not snitch. "
                    " Snitching is for nerds, anyway. "
                    " Let's just go take a walk around the school instead. "
                    scene black with dissolve
                    " You spent the rest of the break walking around the school. "
                    " You overheard a few conversations, and now you have free drama. "
                    " Great! Now you have something to talk about to your friends. "
                    " Though, some conversations were actually pretty concerning, so... "
                    " Best not to talk about those things and keep it to yourself. "
                    " These students should really learn to be more quiet if they're planning to tell secrets. "
                    play sound "audio/bellring.mp3"
                    pause 1.0
                    " The bell rings after a few minutes of walking around and eavesdropping. "
                    " Time to go to the next class, then... "
                    pause 2.0
                    jump occookingclass1
        elif quinnknow == False and jamknow == True:
            x " I just can't believe you, you know?! "
            ja " What, it was just a simple prank. It's not like it's a big deal. "
            x " YOU ALMOST GOT MY FRIEND CRUSHED???? " with vpunch
            x " How exactly is that just a simple prank, hm?! "
            x " Almost killing someone while we weren't even looking! "
            ja " Look, I didn't expect anyone to be under there, okay? "
            x " Well maybe you should look first before you do anything stupid like that ever again! "
            ja " I {i}did{/i} look, I just dropped it at the time that someone walked under there. "
            ja " Sooo, when I lifted it up, I didn't see that there was someone there. "
            x " Still! It isn't a good idea at all to do something like that! " with vpunch
            ja " Quit being a baby, Quinn. "
            ja " Learn to have some fun in your life. "
            x " Well I don't like your idea of fun, if you think almost killing someone is funny! "
            ja " Ergh. "
            ja " Listen, if you tell this to the teacher, your ass is gonna get screwed. "
            ja " I'm gonna kill you. Cook you. Then feed you to your friends and family. "
            ja " Got that? "
            x " ...Fine. "
            hide quinnangry at right with easeoutright
            hide jamangry at right with easeoutright
            " ...And they left. "
            " You're thinking about being mischevious. You should probably tell a teacher. "
            " Should you though? "
            menu:
                " Yes, be a snitch ":
                    $ jamsnitch = True
                    " We snitching on this ho fr!! "
                    scene black with dissolve
                    pause 2.0
                    scene hallway with dissolve
                    " You walked around the hallways to find a teacher. "
                    " You eventually spotted Mister Altrix, going to his classroom. "
                    show altrixneutral at center with easeinleft
                    " You walk up to him and greet him. "
                    msa " Oh! Um, hello there, [name]... "
                    msa " Can I help you? "
                    " You informed him of what you heard. "
                    hide altrixneutral at bottom
                    show altrixsad at center
                    msa " Oh my... "
                    msa " That's not a harmless prank at all...! "
                    msa " I'll have a talk with Jam later... "
                    msa " Thank you, [name]. For informing me about this... "
                    play sound "audio/bellring.mp3"
                    pause 1.0
                    hide altrixsad at bottom
                    show altrixneutral at center
                    msa " The bell rang... "
                    msa " You should go to your class now, [name]. "
                    msa " You shouldn't be late! "
                    " You nodded and said bye before going to your classroom. "
                    scene black with dissolve
                    " Wonder what's gonna happen to Jam... "
                    pause 2.0
                    jump occookingclass1
                " Nah we dont snitch ":
                    " Yeah, let's not snitch. "
                    " Snitching is for nerds, anyway. "
                    " Let's just go take a walk around the school instead. "
                    scene black with dissolve
                    " You spent the rest of the break walking around the school. "
                    " You overheard a few conversations, and now you have free drama. "
                    " Great! Now you have something to talk about to your friends. "
                    " Though, some conversations were actually pretty concerning, so... "
                    " Best not to talk about those things and keep it to yourself. "
                    " These students should really learn to be more quiet if they're planning to tell secrets. "
                    play sound "audio/bellring.mp3"
                    pause 1.0
                    " The bell rings after a few minutes of walking around and eavesdropping. "
                    " Time to go to the next class, then... "
                    pause 2.0
                    jump occookingclass1
        else:
            x " I just can't believe you, you know?! "
            x " What, it was just a simple prank. It's not like it's a big deal. "
            x " YOU ALMOST GOT MY FRIEND CRUSHED???? " with vpunch
            x " How exactly is that just a simple prank, hm?! "
            x " Almost killing someone while we weren't even looking! "
            x " Look, I didn't expect anyone to be under there, okay? "
            x " Well maybe you should look first before you do anything stupid like that ever again! "
            x " I {i}did{/i} look, I just dropped it at the time that someone walked under there. "
            x " Sooo, when I lifted it up, I didn't see that there was someone there. "
            x " Still! It isn't a good idea at all to do something like that! " with vpunch
            x " Quit being a baby, Quinn. "
            x " Learn to have some fun in your life. "
            x " Well I don't like your idea of fun, if you think almost killing someone is funny! "
            x " Ergh. "
            x " Listen, if you tell this to the teacher, your ass is gonna get screwed. "
            x " I'm gonna kill you. Cook you. Then feed you to your friends and family. "
            x " Got that? "
            x " ...Fine. "
            hide quinnangry at right with easeoutright
            hide jamangry at right with easeoutright
            " ...And they left. "
            " You're thinking about being mischevious. You should probably tell a teacher. "
            " Should you though? "
            menu:
                " Yes, be a snitch ":
                    $ jamsnitch = True
                    " We snitching on this ho fr!! "
                    scene black with dissolve
                    pause 2.0
                    scene hallway with dissolve
                    " You walked around the hallways to find a teacher. "
                    " You eventually spotted Mister Altrix, going to his classroom. "
                    show altrixneutral at center with easeinleft
                    " You walk up to him and greet him. "
                    msa " Oh! Um, hello there, [name]... "
                    msa " Can I help you? "
                    " You informed him of what you heard. "
                    hide altrixneutral at bottom
                    show altrixsad at center
                    msa " Oh my... "
                    msa " That's not a harmless prank at all...! "
                    msa " I'll have a talk with Jam later... "
                    msa " Thank you, [name]. For informing me about this... "
                    play sound "audio/bellring.mp3"
                    pause 1.0
                    hide altrixsad at bottom
                    show altrixneutral at center
                    msa " The bell rang... "
                    msa " You should go to your class now, [name]. "
                    msa " You shouldn't be late! "
                    " You nodded and said bye before going to your classroom. "
                    scene black with dissolve
                    " Wonder what's gonna happen to that girl... "
                    pause 2.0
                    jump occookingclass1
                " Nah we dont snitch ":
                    " Yeah, let's not snitch. "
                    " Snitching is for nerds, anyway. "
                    " Let's just go take a walk around the school instead. "
                    scene black with dissolve
                    " You spent the rest of the break walking around the school. "
                    " You overheard a few conversations, and now you have free drama. "
                    " Great! Now you have something to talk about to your friends. "
                    " Though, some conversations were actually pretty concerning, so... "
                    " Best not to talk about those things and keep it to yourself. "
                    " These students should really learn to be more quiet if they're planning to tell secrets. "
                    play sound "audio/bellring.mp3"
                    pause 1.0
                    " The bell rings after a few minutes of walking around and eavesdropping. "
                    " Time to go to the next class, then... "
                    pause 2.0
                    jump occookingclass1
    label ocgym5:
        # Carmen, Spark - Carmen is curious about spark
        scene black with dissolve
        pause 2.0
        scene gym with dissolve
        " You were walking around the gym, trying to find a seat so that you could just sit down and chillax. "
        " But, of course, you spotted two of your classmates hanging out. "
        " Curious about what they were talking about, you decided to sit next to them. "
        show sparkneutral at left with easeinright
        show carmenneutral at right with easeinright
        if sparkknow == True and carmenknow == True:
            ca " ...? "
            sp " Eh...? Carmen? What is it? "
            ca " ... "
            sp " You're curious about my antennas? "
            sp " Well, um... "
            sp " I just grew them one day, you know? "
            ca " ??? "
            sp " That includes my tail, yes. "
            sp " It just happened randomly when I was 14. "
            sp " Don't know what day it was, but I know it happened when I was 14. "
            ca " ...! "
            sp " You think it's cool...? Thanks. You're cool too, Carmen. "
            " ...Spark's tone sounds weird. "
            " He might be hiding something. Or maybe you're just overthinking things. "
            " But still, he sounded a little nervous when Carmen asked him about his antennas and tail. "
            " Maybe you should talk to him about it... "
            sp " Oh, hi [name]. "
            sp " Did you need something? "
            sp " If you did, I could help you out - {nw} "
            " His phone starts ringing. " with vpunch
            sp " ...Hold on, I have to check this out real quick. "
            hide sparkneutral at bottom
            show sparksad at left
            " He grabs his phone and he seems to be a little surprised at what he's seeing. "
            hide carmeneutral at bottom
            show carmensurprised at right
            sp " ...I have to go, I'm sorry. "
            hide sparksad at right with easeoutright
            show carmensurprised at center with move
            ca " ?! "
            " Without even explaining what was going on, Spark left. "
            " That was weird. Real weird. "
            hide carmensurprised at bottom
            show carmenneutral at center
            ca " ... "
            " Looks like even Carmen agrees with you. "
            " You're gonna have to try and figure out what's going on... "
            play sound "audio/bellring.mp3"
            " ...Maybe tomorrow, then. Since this is your last class. "
            " Let's go back to your classroom. Don't want to be late. "
            scene black with dissolve
            pause 2.0
            jump occookingclass1
        elif sparkknow == True and carmenknow == False:
            x " ...? "
            sp " Eh...? Carmen? What is it? "
            x " ... "
            sp " You're curious about my antennas? "
            sp " Well, um... "
            sp " I just grew them one day, you know? "
            x " ??? "
            sp " That includes my tail, yes. "
            sp " It just happened randomly when I was 14. "
            sp " Don't know what day it was, but I know it happened when I was 14. "
            x " ...! "
            sp " You think it's cool...? Thanks. You're cool too, Carmen. "
            " ...Spark's tone sounds weird. "
            " He might be hiding something. Or maybe you're just overthinking things. "
            " But still, he sounded a little nervous when the other guy asked him about his antennas and tail. "
            " Maybe you should talk to him about it... "
            sp " Oh, hi [name]. "
            sp " Did you need something? "
            sp " If you did, I could help you out - {nw} "
            " His phone starts ringing. " with vpunch
            sp " ...Hold on, I have to check this out real quick. "
            hide sparkneutral at bottom
            show sparksad at left
            " He grabs his phone and he seems to be a little surprised at what he's seeing. "
            hide carmeneutral at bottom
            show carmensurprised at right
            sp " ...I have to go, I'm sorry. "
            hide sparksad at right with easeoutright
            show carmensurprised at center with move
            x " ?! "
            " Without even explaining what was going on, Spark left. "
            " That was weird. Real weird. "
            hide carmensurprised at bottom
            show carmenneutral at center
            x " ... "
            " Looks like even this guy agrees with you. "
            " You're gonna have to try and figure out what's going on... "
            play sound "audio/bellring.mp3"
            " ...Maybe tomorrow, then. Since this is your last class. "
            " Let's go back to your classroom. Don't want to be late. "
            scene black with dissolve
            pause 2.0
            jump occookingclass1
        elif sparkknow == False and carmenknow == True:
            ca " ...? "
            x " Eh...? Carmen? What is it? "
            ca " ... "
            x " You're curious about my antennas? "
            x " Well, um... "
            x " I just grew them one day, you know? "
            ca " ??? "
            x " That includes my tail, yes. "
            x " It just happened randomly when I was 14. "
            x " Don't know what day it was, but I know it happened when I was 14. "
            ca " ...! "
            x " You think it's cool...? Thanks. You're cool too, Carmen. "
            " ...His tone sounds weird. "
            " He might be hiding something. Or maybe you're just overthinking things. "
            " But still, he sounded a little nervous when Carmen asked him about his antennas and tail. "
            " Maybe you should talk to him about it... "
            x " Oh, hi [name]. "
            x " Did you need something? "
            x " If you did, I could help you out - {nw} "
            " His phone starts ringing. " with vpunch
            x " ...Hold on, I have to check this out real quick. "
            hide sparkneutral at bottom
            show sparksad at left
            " He grabs his phone and he seems to be a little surprised at what he's seeing. "
            hide carmeneutral at bottom
            show carmensurprised at right
            x " ...I have to go, I'm sorry. "
            hide sparksad at right with easeoutright
            show carmensurprised at center with move
            ca " ?! "
            " Without even explaining what was going on, he left. "
            " That was weird. Real weird. "
            hide carmensurprised at bottom
            show carmenneutral at center
            ca " ... "
            " Looks like even Carmen agrees with you. "
            " You're gonna have to try and figure out what's going on... "
            play sound "audio/bellring.mp3"
            " ...Maybe tomorrow, then. Since this is your last class. "
            " Let's go back to your classroom. Don't want to be late. "
            scene black with dissolve
            pause 2.0
            jump occookingclass1
        else:
            x " ...? "
            x " Eh...? Carmen? What is it? "
            x " ... "
            x " You're curious about my antennas? "
            x " Well, um... "
            x " I just grew them one day, you know? "
            x " ??? "
            x " That includes my tail, yes. "
            x " It just happened randomly when I was 14. "
            x " Don't know what day it was, but I know it happened when I was 14. "
            x " ...! "
            x " You think it's cool...? Thanks. You're cool too, Carmen. "
            " ...His tone sounds weird. "
            " He might be hiding something. Or maybe you're just overthinking things. "
            " But still, he sounded a little nervous when Carmen asked him about his antennas and tail. "
            " Maybe you should talk to him about it... "
            x " Oh, hi [name]. "
            x " Did you need something? "
            x " If you did, I could help you out - {nw} "
            " His phone starts ringing. " with vpunch
            x " ...Hold on, I have to check this out real quick. "
            hide sparkneutral at bottom
            show sparksad at left
            " He grabs his phone and he seems to be a little surprised at what he's seeing. "
            hide carmeneutral at bottom
            show carmensurprised at right
            x " ...I have to go, I'm sorry. "
            hide sparksad at right with easeoutright
            show carmensurprised at center with move
            x " ?! "
            " Without even explaining what was going on, he left. "
            " That was weird. Real weird. "
            hide carmensurprised at bottom
            show carmenneutral at center
            x " ... "
            " Looks like even this guy agrees with you. "
            " You're gonna have to try and figure out what's going on... "
            play sound "audio/bellring.mp3"
            " ...Maybe tomorrow, then. Since this is your last class. "
            " Let's go back to your classroom. Don't want to be late. "
            scene black with dissolve
            pause 2.0
            jump occookingclass1
    label occafe5:
        # yangyi, notive - yangyi asks for advice
        scene black with dissolve
        pause 2.0
        scene cafeteria with dissolve
        " You walk into the cafeteria, and hear a whole lot of talking, of course. "
        " You look around to find an empty table, and you spot two of your classmates hanging out. "
        " You decided to sit next to them to see what's up. "
        show yinhuitough at left with easeinright
        show notiveneutral at right with easeinright
        if yangyiknow == True and notiveknow == True:
            yi " I don't know, Notive. "
            yi " I feel like I'm being a bit too protective with my brother. "
            no " ...Then how about not being too protective over your brother? "
            yi " That's. Not really helpful, you do know that, right? "
            no " Sorry man, it's the best advice I could give you. "
            yi " I suppose that's fine... "
            no " ...But, uh...hey. There's [name] over here. "
            hide yinhuitough at bottom
            show yinhuineutral at left
            if they == "she","he":
                yi " ...[they]'s here? Seriously? "
            elif they == "they":
                yi " ...[they]'re here? Seriously? "
            no " Yep. Sitting right infront of us. "
            no " If you don't see [them], I might need to buy you some glasses. "
            yi " I can see [them] very clearly, thank you very much... "
            yi " But. Notive, I can't just... "
            " Yinhui makes a few hand gestures to you. "
            " At one point he flipped you off. "
            no " Woah, hey. That's rude. "
            yi " Does it look like I care? Now go tell them. "
            no " Geez, you big baby... "
            no " Sorry [name], mr grumpy pants over here isn't really comfortable enough with you yet. "
            no " Either you gotta leave or you can just... I don't know, not listen to our conversation? "
            " You gave a thumbs up and you put on your earphones and started playing really loud music. "
            yi " Great. Anyway, "
            scene black with dissolve
            " You just sat there listening to music. Well, not really. "
            " You secretly had your volume on low and listened to their entire conversation. "
            " Seems like it's gonna be a bit hard for you to be friends with Yinhui... "
            " You gotta figure out some way to befriend him. Somehow. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, meaning that it was time for class. "
            " You get up from your seat and go to your classroom. "
            pause 2.0
            jump occookingclass1
        elif yangyiknow == True and notiveknow == False:
            yi " I don't know, Notive. "
            yi " I feel like I'm being a bit too protective with my brother. "
            x " ...Then how about not being too protective over your brother? "
            yi " That's. Not really helpful, you do know that, right? "
            x " Sorry man, it's the best advice I could give you. "
            yi " I suppose that's fine... "
            x " ...But, uh...hey. There's [name] over here. "
            hide yinhuitough at bottom
            show yinhuineutral at left
            if they == "she","he":
                yi " ...[they]'s here? Seriously? "
            elif they == "they":
                yi " ...[they]'re here? Seriously? "
            x " Yep. Sitting right infront of us. "
            x " If you don't see [them], I might need to buy you some glasses. "
            yi " I can see [them] very clearly, thank you very much... "
            yi " But. Notive, I can't just... "
            " Yinhui makes a few hand gestures to you. "
            " At one point he flipped you off. "
            x " Woah, hey. That's rude. "
            yi " Does it look like I care? Now go tell [them]. "
            x " Geez, you big baby... "
            x " Sorry [name], mr grumpy pants over here isn't really comfortable enough with you yet. "
            x " Either you gotta leave or you can just... I don't know, not listen to our conversation? "
            " You gave a thumbs up and you put on your earphones and started playing really loud music. "
            yi " Great. Anyway, "
            scene black with dissolve
            " You just sat there listening to music. Well, not really. "
            " You secretly had your volume on low and listened to their entire conversation. "
            " Seems like it's gonna be a bit hard for you to be friends with Yinhui... "
            " You gotta figure out some way to befriend him. Somehow. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, meaning that it was time for class. "
            " You get up from your seat and go to your classroom. "
            pause 2.0
            jump occookingclass1
        elif yangyiknow == False and notiveknow == True:
            x " I don't know, Notive. "
            x " I feel like I'm being a bit too protective with my brother. "
            no " ...Then how about not being too protective over your brother? "
            x " That's. Not really helpful, you do know that, right? "
            no " Sorry man, it's the best advice I could give you. "
            x " I suppose that's fine... "
            no " ...But, uh...hey. There's [name] over here. "
            hide yinhuitough at bottom
            show yinhuineutral at left
            if they == "she","he":
                x " ...[they]'s here? Seriously? "
            elif they == "they":
                x " ...[they]'re here? Seriously? "
            no " Yep. Sitting right infront of us. "
            no " If you don't see [them], I might need to buy you some glasses. "
            x " I can see [them] very clearly, thank you very much... "
            x " But. Notive, I can't just... "
            " The other guy makes a few hand gestures to you. "
            " At one point he flipped you off. "
            no " Woah, hey. That's rude. "
            x " Does it look like I care? Now go tell [them]. "
            no " Geez, you big baby... "
            no " Sorry [name], mr grumpy pants over here isn't really comfortable enough with you yet. "
            no " Either you gotta leave or you can just... I don't know, not listen to our conversation? "
            " You gave a thumbs up and you put on your earphones and started playing really loud music. "
            x " Great. Anyway, "
            scene black with dissolve
            " You just sat there listening to music. Well, not really. "
            " You secretly had your volume on low and listened to their entire conversation. "
            " Seems like it's gonna be a bit hard for you to be friends with that grumpy dude... "
            " You gotta figure out some way to befriend him. Somehow. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, meaning that it was time for class. "
            " You get up from your seat and go to your classroom. "
            pause 2.0
            jump occookingclass1
        else:
            x " I don't know, Notive. "
            x " I feel like I'm being a bit too protective with my brother. "
            x " ...Then how about not being too protective over your brother? "
            x " That's. Not really helpful, you do know that, right? "
            x " Sorry man, it's the best advice I could give you. "
            x " I suppose that's fine... "
            x " ...But, uh...hey. There's [name] over here. "
            hide yinhuitough at bottom
            show yinhuineutral at left
            if they == "she","he":
                x " ...[they]'s here? Seriously? "
            elif they == "they":
                x " ...[they]'re here? Seriously? "
            x " Yep. Sitting right infront of us. "
            x " If you don't see [them], I might need to buy you some glasses. "
            x " I can see [them] very clearly, thank you very much... "
            x " But. Notive, I can't just... "
            " The other guy makes a few hand gestures to you. "
            " At one point he flipped you off. "
            x " Woah, hey. That's rude. "
            x " Does it look like I care? Now go tell [them]. "
            x " Geez, you big baby... "
            x " Sorry [name], mr grumpy pants over here isn't really comfortable enough with you yet. "
            x " Either you gotta leave or you can just... I don't know, not listen to our conversation? "
            " You gave a thumbs up and you put on your earphones and started playing really loud music. "
            x " Great. Anyway, "
            scene black with dissolve
            " You just sat there listening to music. Well, not really. "
            " You secretly had your volume on low and listened to their entire conversation. "
            " Seems like it's gonna be a bit hard for you to be friends with that grumpy dude... "
            " You gotta figure out some way to befriend him. Somehow. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, meaning that it was time for class. "
            " You get up from your seat and go to your classroom. "
            pause 2.0
            jump occookingclass1
    label ocrooftop5:
        # jex - talking about cloud facts
        scene black with dissolve
        pause 2.0
        scene rooftop with dissolve
        " You walk up onto the rooftop, taking in the fresh air. "
        " You decide to walk around for a bit, looking at the sky and sometimes looking at the ground. "
        " After awhile of walking, you spotted one of your classmates gazing at the sky. "
        " Thinking of talking to them, you decided to sit next to them and see how they're doing. "
        show jexneutral at center with easeinbottom
        if jexknow == True:
            j " ...Ah, and that one's a... "
            j " ...[name]? I wasn't expecting you to be here. "
            j " I thought you'd be around somewhere else, not up here. "
            j " But, I don't mind having some company. "
            j " ...While you're here, would you like to hear about some cloud facts? "
            j " I know that they sound pretty boring, but trust me. "
            j " They're quite interesting... "
            j " Like: Did you know that The color of clouds is influenced by the size of their water droplets and ice crystals, as well as the angle of sunlight? "
            j " Told you they'd be pretty interesting. "
            j " Would you like to hear some more? "
            " You had nothing else to do, so you nodded and decided to listen to his cloud facts. "
            j " Alrighty. "
            scene black with dissolve
            " You spent the entire break spending time with Jex. "
            " Some of the cloud facts he spat out were actually pretty interesting.. "
            " He really wasn't lying when he said that they were. "
            " You should probably look up more cloud facts later. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, meaning that it was time for class. "
            " You get up from your seat and go to your classroom. "
            pause 2.0
            jump occookingclass1
        else:
            x " ...Ah, and that one's a... "
            x " ...[name]? I wasn't expecting you to be here. "
            x " I thought you'd be around somewhere else, not up here. "
            x " But, I don't mind having some company. "
            x " ...Ah, that's right. My apologies. "
            x " I forgot to introduce myself to you... "
            $ jexknow = True
            j " I'm Jex. It's a pleasure to have you here with me. "
            j " ...While you're here, would you like to hear about some cloud facts? "
            j " I know that they sound pretty boring, but trust me. "
            j " They're quite interesting... "
            j " Like: Did you know that The color of clouds is influenced by the size of their water droplets and ice crystals, as well as the angle of sunlight? "
            j " Told you they'd be pretty interesting. "
            j " Would you like to hear some more? "
            " You had nothing else to do, so you nodded and decided to listen to his cloud facts. "
            j " Alrighty. "
            scene black with dissolve
            " You spent the entire break spending time with Jex. "
            " Some of the cloud facts he spat out were actually pretty interesting.. "
            " He really wasn't lying when he said that they were. "
            " You should probably look up more cloud facts later. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, meaning that it was time for class. "
            " You get up from your seat and go to your classroom. "
            pause 2.0
            jump occookingclass1
    label oclibrary5:
        # disk - worrying over the next class!
        scene black with dissolve
        pause 2.0
        scene library with dissolve
        " You enter the library, taking in the fresh smell of... books. "
        " What do books even smell like? I don't know, I'm running out of words to describe places now. "
        " I'm just a narrator, man... "
        " Anywho, you spot your classmate reading a book and they seem a bit stressed. "
        " You decided to sit next to them to see what's up. "
        show disksad at center with easeinleft
        if diskknow == True:
            d " Oh jeez, what am I going to do... "
            " He continues to panic for a bit before he sees you. "
            hide disksad at bottom
            show diskneutral at center
            d " Oh, [name]! Lovely to see you! "
            " You asked him what he was panicking over. "
            d " That? Well... "
            hide diskneutral at bottom
            show disksad at center
            d " Cooking class is next, and I promised to impress the cooking teacher with a new dish... "
            d " The thing is, I don't even know what I'm going to make! "
            d " It has to both taste and look good, I'm not even sure what the teacher likes... "
            d " I've been going through this book the librarian gave me, and I'm seeing nothing nice... "
            d " Could you help me get some ideas? Pleaasee? "
            d " I really can't fail this class! "
            " Seems like he's the kid who wants all A's in every class... "
            " No problem. You could certainly help him find a good recipe. "
            " You're an expert, after all...totally. "
            hide disksad at bottom
            show diskneutral at center
            d " Really? you'd help me out? "
            hide diskneutral at bottom
            show diskjoyous at center
            d " Thank you so much, [name]! "
            d " I really appreciate your help! "
            scene black with dissolve
            " You spent your entire break spending time with Disk. "
            " You helped him out with finding a new recipe to give to the cooking teacher. "
            " Eventually, Disk settled on a recipe you showed him. "
            " It was a recipe of a dish called Leche Flan. "
            " You just told him to make it look fancy and then he'll get an A+. "
            play sound "audio/bellring.mp3"
            " The bell rings not too long after you showed him recipe. "
            " You both get up from your seats and go to the next class. "
            pause 2.0
            jump occookingclass1
        else:
            x " Oh jeez, what am I going to do... "
            " He continues to panic for a bit before he sees you. "
            hide disksad at bottom
            show diskneutral at center
            x " Oh, [name]! Lovely to see you! "
            $ diskknow = True
            d " I'm Disk, by the way. I forgot to introduce myself to you, hehe! "
            " You told him that it was nice to meet him too, and then asked him what he was panicking over. "
            d " That? Well... "
            hide diskneutral at bottom
            show disksad at center
            d " Cooking class is next, and I promised to impress the cooking teacher with a new dish... "
            d " The thing is, I don't even know what I'm going to make! "
            d " It has to both taste and look good, I'm not even sure what the teacher likes... "
            d " I've been going through this book the librarian gave me, and I'm seeing nothing nice... "
            d " Could you help me get some ideas? Pleaasee? "
            d " I really can't fail this class! "
            " Seems like he's the kid who wants all A's in every class... "
            " No problem. You could certainly help him find a good recipe. "
            " You're an expert, after all...totally. "
            hide disksad at bottom
            show diskneutral at center
            d " Really? you'd help me out? "
            hide diskneutral at bottom
            show diskjoyous at center
            d " Thank you so much, [name]! "
            d " I really appreciate your help! "
            scene black with dissolve
            " You spent your entire break spending time with Disk. "
            " You helped him out with finding a new recipe to give to the cooking teacher. "
            " Eventually, Disk settled on a recipe you showed him. "
            " It was a recipe of a dish called Leche Flan. "
            " You just told him to make it look fancy and then he'll get an A+. "
            play sound "audio/bellring.mp3"
            " The bell rings not too long after you showed him recipe. "
            " You both get up from your seats and go to the next class. "
            pause 2.0
            jump occookingclass1
    label occookingclass1:
        scene classroom with dissolve
        " You enter the classroom and you see everyone having cooking materials. "
        " ...This classroom isn't even built for cooking. But pretend that it is, just for this class. "
        " The teacher eventually walked into the classroom after a few minutes "
        show jiayuneutral at center with easeinright
        x " Good afternoon, class. "
        " Good afternoon - the entire classroom said. "
        x " We have a new student in this class, is that correct? "
        x " Where are [they]... "
        " She looks around the classroom before she spotted you. "
        x " Ah. You're the new student, eh? "
        x " Since I'm feeling nice, you're gonna have to be exempted for our activity today. "
        x " Seeing that you, of course, didn't know that we're going to be having an activity today. "
        x " And since no one else has extra cooking materials. "
        x " You're gonna have to be one of the taste testers instead, since the activity is to cook something. "
        msx " I am Miss Jiayu, by the way. "
        msx " Mother of Yangyi and Yinhui. "
        if yinhuiknow == True and yangyiknow == True:
            ya " Hi mom!! "
            yi " Hi mom. "
        else:
            x " Hi mom!!/Hi mom. "
            " The twins greeted. "
        msx " Hello, kids... "
        msx " Anywho, there will be a 15 minute timer. "
        " Is that enough for cooking? probably. You don't know, you can't cook for gods sake. "
        msx " In the meantime, you can do whatever you want. "
        hide jiayuneutral at left with easeoutleft
        " Sweet. You get some time to yourself. "
        " You decided to scroll on your phone for the time being... "
        " ...Until it was time for taste testing. "
        scene black with dissolve
        " You tasted some of your classmates food for cooking class. "
        " Some were okay, some were horrendous, "
        if diskknow == True:
            " But the real winner was Disk's leche flan. "
            " The teacher gave him an A+ for that. Yipeee!! "
        else:
            " But the real winner was this one kid's leche flan. "
            " The teacher gave him an A+ for that. Yipeee!! "
        play sound "audio/bellring.mp3"
        " The bell rings, meaning that the school day is over and it was time for everyone to go home. "
        " You waited for everyone else to leave before you could. "
        pause 2.0
        jump ocendday
    label ocendday:
        scene paperschoolfront with dissolve
        " You walked out of the school, ready to go home. "
        " Some of your friends wave goodbye to you, and you waved goodbye to them back. "
        " You then start walking back to your home. "
        stop music fadeout 0.5
        scene black with dissolve
        pause 2.0
        play music "audio/home.mp3" fadein 0.5
        scene mcroom with dissolve
        " Once you got yourself changed into your pajamas, you immediately plopped down onto your bed. "
        " You check your phone to see that you were added into two GC's. "
        " Your school GC, to be specific. And a GC for your classmates to goof off. "
        " You put down your phone and start to sleep. "
        scene black with dissolve
        stop music fadeout 0.5
        " Good night, [name]. "
        pause 2.0
        jump octuesday
