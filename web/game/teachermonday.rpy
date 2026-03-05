label teachermonday:
    if persistent.playedteacher == True:
        pass
    else:
        " Quick warning: This route is going to be a tad bit innaccurate. "
        " No, it's not because of the characters, but because of the main character being a tad bit inaccurate to how actual teachers work."
        " I am not a professional, and I don't know how teachers work. So forgive me if theres any mistakes. "
        " Other than that, enjoy the route. "
    play music "audio/home.mp3" fadein 0.5
    scene mcroom with dissolve
    pause 1.0
    scene black with dissolve
    pause 1.0
    scene mcroom with dissolve
    " You wake up and sit in your bed, rubbing your eyes. "
    " You look at the clock on your phone... "
    " ...7 AM. You're not late. "
    " If you don't know, today's gonna be the first day working as a teacher in a school named Paper High. "
    " You're gonna work there as a gardening teacher. "
    " Not sure why you chose gardening out of all things, but you refuse to teach PE class. "
    " You get into your uniform, and go out to start the day. "
    scene black with dissolve
    stop music fadeout 0.5
    pause 2.0
    show text " DAY 1 - MONDAY "
    pause 2.0
    play music "audio/paperhigh.mp3" fadein 0.5
    scene paperschoolfront with dissolve
    " Ah yes, {i}the{/i} Paper High... "
    " ...You can already tell that this is one chaotic school, judging by from what you've heard online. "
    " It's quiet for now, since it's pretty early in the morning. "
    " You step in, bracing yourself for the chaos that you're about to witness later on. "
    scene black with dissolve
    pause 2.0
    scene hallway with dissolve
    " You walk into the hallways of the school, and see a lot of paper on the ground. "
    " Jeez... don't they have a janitor to clean this stuff or did the janitor just forget to work? "
    " You then remember that you have a meeting with Miss Grace, the principal, in her office. "
    " You rush there, making sure that you don't step on anything so that you don't trip accidentally. "
    scene black with dissolve
    pause 2.0
    scene principalsoffice with dissolve
    show msgraceneutral at center with easeinleft
    " You walked into the principals office, seeing Miss Grace sitting and looking right at you. "
    " You take your seat, and look back at her in a serious way. Getting ready for whatever orders she has for you. "
    msg " [name]... You're quite early. That's good. "
    msg " Now, I hope that you're going to be a good teacher. I don't want to fire you on the first day. "
    msg " You know all of the rules and regulations, yes? "
    " You nod your head. "
    msg " Great. Your classroom will be at the left side of the school and your class starts at 4:30, right after Miss Emily's class. "
    msg " I hope you'll have fun teaching here. The students may be difficult, but it'll be great once they graduate. "
    msg " Another thing I'd like to add... "
    msg " Since we have quite the complicated schedule, you're going to have to roam the school for a bit while it's not your class time. "
    msg " You can visit other teachers whilst they're teaching, but don't make too much of a disturbance. "
    msg " This doesn't mean that you can slack off, however. "
    msg " I can and will give you warnings if I catch you. I have cameras all over the school. "
    msg " You better do something helpful whilst you're in other teachers classrooms. "
    msg " You can help a student struggling, or you could just help the teacher teach if they dont have enough energy to. "
    msg " I hope you understand. "
    msg " Now, get along then. You may go to your classroom. "
    " You nod and stand up, thanking Miss Grace for her time and you leave quietly. "
    scene black with dissolve
    " Geez... working as a teacher here feels nice. The only problem is the slacking off rule... "
    " ...Well, of course you don't have to slack. All jobs are taken seriously. "
    " You thought about a lot of things, until you managed to reach your room. "
    " This was it. This was the moment that you've been waiting for, for the past few days. "
    " You open the door... "
    scene gardenroom with dissolve
    " This is your classroom now. Huh... looks pretty nice, actually. "
    " You can't wait to deal with the troublemakers in your class...If there's gonna be any. "
    " It's still gonna be a few hours until school actually starts, so let's just take a nap. For now. "
    scene black with dissolve
    " You get comfy on the chair where your desk was, and fell asleep. "
    " Damn, this chair is comfy. Wonder if the other teacher chairs are like this, as well... "
    " Good classroom and good chair? perfect. This school was a good choice to work in. "
    " Or maybe not, your opinion could change later. After all, it's your first day. "
    " You're probably gonna have to deal with people not listening to you, most likely. "
    " You have an easy fix for that, though. Just hit them with a slipper and they will. "
    " Atleast that's what those strict asian parents do. "
    " Actually, no. That's either gonna accidentally trigger some trauma or you're gonna get fired. "
    play sound "audio/bellring.mp3"
    scene gardenroom with dissolve
    " The bell rings, awakening you from your precious nap. "
    " You've slept for a few hours, and now it's time for class to start. "
    " You thought about what Miss Grace said...You can hang out with other teachers and help them in things. "
    " You get up from your chair and go out of your classroom to go to the hallways. "
    scene black with dissolve
    pause 2.0
    scene hallway with dissolve
    " The hallways were now filled with students skedaddling to reach their classrooms. "
    " Some even bump into you, not knowing that you were a new teacher... how rude. "
    " Once they were into their classrooms, you thought about something for a few moments... "
    " Which classroom do you want to go? (Which teacher do you want to help out with their class?) "
    menu:
        " {image=misscircleicon} Go into the classroom that has 'Math Class' on it {image=misscircleicon} ":
            jump mscircleint
        " {image=missthavelicon} Go into the classroom that has 'Language class' on it {image=missthavelicon} ":
            jump msthavelint
        " {image=missbloomieicon} Go into the classroom that has 'Science class' on it {image=missbloomieicon} ":
            jump msbloomieint
        " Actually, let's just roam around the school. ":
            jump roamschool
    label mscircleint:
        $ circlelv += 10
        " You decided to go see what the math teacher is up to. "
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        show misscircleneutral at center with dissolve
        x " Now, let's get started with today's lesson! - "
        x " Ah, seems like we have a guest here! Everyone, say hello to... "
        " She takes a moment to read your ID before saying it aloud. "
        x " ...[mr] [name]! "
        " You hear everyone in the classroom greeting you a good morning. Well, almost everyone. "
        x " Now, what brings you here? "
        " You tell her that you came to help in case if theres any students misbehaving or if she had any trouble doing something. "
        hide misscircleneutral at bottom
        show misscirclehappy at center
        x " Why, that's fantastic! I need you to help me make sure that everyone in my class is paying attention. "
        x " You can also help out any students that are having struggles on their activities. I'm planning to give them one right now, eheh.. "
        x " You think you could take the task? "
        " Well, you don't have any other option so you just nodded. "
        " You look at her ID and see her name... "
        $ circleknow = True
        " ...Miss Circle. Well, she's pretty circle, that's true. "
        " Her big compass of a hand kind of intimidates you, but you're sure that she's a great teacher. "
        msc " Splendid! You can sit wherever you'd like! "
        hide misscirclehappy at right with easeoutright
        " Miss Circle then goes to the front to start teaching. "
        " Where would you like to sit? "
        menu:
            " The back ":
                " You decided to sit at the back. "
                " Students sitting in the back are usually the ones that don't pay attention as much... "
                " ...That's why you decided to sit here, from my guess. "
                " But then you wouldn't really be able to look at who's not paying attention from the front. "
                " Oh well, you're the one that chose to sit here anyway. "
                " Whilst you sat here, you managed to catch two studnets using their phones in the middle of class. "
                " And also some that are talking whilst Miss Circle was teaching. "
                " You just bonked them on their head and took away their phones as a punishment. "
                " Once class was over, you returned their phones and watched them walk out of the classroom. "
                " Miss Circle then came up to you after a short bit. "
                show misscircleneutral at center with easeinleft
                msc " My, my! You did quite a great job back there, [name]! "
                hide misscircleneutral at bottom
                show misscirclehappy at center
                msc " You're pretty good, especially since it's your first day of being here. "
                msc " You took care of them pretty well! You have my thanks. "
                msc " I'll get going now, thanks again for helping out. "
                hide misscirclehappy at right with easeoutright
                " She waved you a goodbye before she left the classroom. "
                " Well, you better get something to do for the break. "
                " You head out to the hallways a few moments after Miss Circle did. "
                scene black with dissolve
                pause 2.0
                jump teacherbreak1
            " The front, somewhere near Miss Circle's desk. ":
                " You decided to sit at the front. "
                " You could get a much clearer view of who's not paying attention when you're up here, "
                " That's why you decided to sit here, from my guess. "
                " Pretty good choice. "
                " You saw some students not paying attention; like talking to eachother or being on their phones. "
                if kind == True:
                    " You went over and kindly asked them to pay attention, and took their phones away in secret as they were paying attention to you. "
                elif mean == True:
                    " You went over and took away their phones, and gave the others who weren't paying attention a death glare. "
                    " It got so bad to the point that you actually got the whole class to pay attention. "
                    " You must be THAT scary for them to pay attention like that. "
                elif calm == True:
                    " You went over and kindly asked them to pay attention, and took their phones away in secret as they were paying attention to you. "
                else:
                    ""
                " Once class was over, you returned their phones and watched them walk out of the classroom. "
                " Miss Circle then came up to you after a short bit. "
                show misscircleneutral at center with easeinleft
                msc " My, my! You did quite a great job back there, [name]! "
                hide misscircleneutral at bottom
                show misscirclehappy at center
                msc " You're pretty good, especially since it's your first day of being here. "
                msc " You took care of them pretty well! You have my thanks. "
                msc " I'll get going now, thanks again for helping out. "
                hide misscirclehappy at right with easeoutright
                " She waved you a goodbye before she left the classroom. "
                " Well, you better get something to do for the break. "
                " You head out to the hallways a few moments after Miss Circle did. "
                scene black with dissolve
                pause 2.0
                jump teacherbreak1
    label msthavelint:
        $ thavellv += 10
        " You decided to go see what the language teacher is up to. "
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You entered the classroom and saw the language teacher struggling on getting the students to say a specific word. "
        show msthravelangry at center with easeinleft
        x " I'm not gonna stop until everyone gets this right; how do you pronounce this word? "
        " She pointed at a spanish word that she wrote on the board. "
        " It wasn't really hard to pronounce, so you were wondering why some were struggling. "
        hide msthravelangry at bottom
        show msthravelneutral at center
        " As you watched, she seemed to notice you after a couple of seconds and she stopped teaching to come up to you. "
        " You seem to recognize this woman, you've heard of her before while talking with Miss Grace... "
        $ thavelknow = True
        " This is Miss Thavel. You've got to be careful around her, from what you've heard she can get quite...feral. "
        " Look, I didn't know what word to describe her with, alright? "
        mst " Ah, [mr] [name]! thank the heavens you came here. "
        mst " You came to assist me here, yes? "
        " Well, you don't really have a choice to say no. "
        " You nod your head, wanting to help Miss Thavel because you had nothing better to do. "
        mst " That's great! "
        mst " I need you to help some students who are struggling on some words I'm trying to teach them. "
        mst " Like struggling to pronounce of spell them...but mostly pronouncing them. "
        mst " Do you think that you can handle it? "
        " Again, you have no choice. You just nod your head because funky silly "
        " Can you tell that I'm a non-serious narrator? Is it obvious? Very much. "
        hide msthravelneutral at bottom
        show msthravelhappy at center
        mst " Great! Thank you, [name]! "
        hide msthravelhappy at left with easeoutleft
        " You roamed around the class to see who were struggling on a certain word. "
        " You did find a few students who were struggling, and you helped them out. "
        " Pretty easy job, in all honesty... "
        " One student took a couple of tries, but he eventually got it. "
        " You gave a few of them candy that you had in your pocket because you felt nice. "
        play sound "audio/bellring.mp3"
        " You continued to help out the students until the bell rings, signalling that it was breaktime. "
        " Miss thravel comes up to you, seemingly happy with your help. "
        show msthravelhappy at center with easeinleft
        mst " You did well, [name]! "
        mst " These kids were so annoying, they couldn't even get the simplest words right! "
        mst " Thanks again, [name]. You can be on your way to do something else now. "
        hide msthravelhappy at left with easeoutleft
        " You waved her a goodbye before you went out to the hallways to have some time to explore or get along with the other teachers. "
        scene black with dissolve
        pause 2.0
        jump teacherbreak1
    label msbloomieint:
        $ bloomielv += 10
        " You decided to see what the science teacher is doing. "
        scene black with dissolve
        pause 2.0
        scene classroom with dissolve
        " You walk in, and you could see some students getting into groups. "
        " Maybe they're doing an activity of some sorts. "
        " You could see some students struggling a bit with their experiments. This could be a bit dangerous... "
        " You were busy looking at the students to the point you didn't notice that the science teacher was right next to you. "
        show missbloomieneutral at center with easeinleft
        x " ...You there. "
        " You got a little jumpscared from her in all honesty. You pointed at yourself in confusion. "
        x " Yes, you. "
        x " You're the new teacher for gardening, correct? "
        x " Pleased to meet you. "
        $ bloomieknow = True
        msb " I am Miss Bloomie, science teacher. "
        msb " I assume that Miss Grace has allowed you to help the other subject teachers... "
        msb " ...If she has, then I require your assistance. "
        msb " My students are doing a group project where they make some potions of any kind. "
        msb " About three potions, to be exact. "
        msb " Everyone's potions have to be something different, no one can have the same. "
        msb " Though, it seems like they're struggling to even make just one potion. "
        msb " Could you help them out? Only if you want to, of course. "
        " You nod your head. Making potions sounds interesting... "
        msb " Great. I'll hand you a recipe book for potions so that you know what you're doing. "
        hide missbloomieneutral at left with easeoutleft
        " She hands you the potion recipe book and she goes to watch over the other students in her teachers desk. "
        msb " Everyone, please settle down for a moment. We have a guest. "
        msb " Please greet [mr] [name]; [they] [are] a new teacher in this school. "
        " You hear almost everyone greet you. "
        msb " Now, if you're struggling with making a potion you may ask [them] to help your group out. "
        msb " There's nothing wrong with asking for help. "
        if kind == True:
            msb " [mr] [name] is a nice and kind teacher. "
        elif mean == True:
            msb " [mr] [name] may look mean, but [they] [are] really nice. "
        elif calm == True:
            msb " [mr] [name] is a laid back teacher, so there is nothing to worry about. "
        msb " That is all. Once again, you may ask [mr] [name] for help and you may continue on with your project. "
        " And with that, you go over to a group and help them out with making a potion. "
        " You give them the right instructions and the right materials, and they successfully make one! "
        " That was one out of three, but you're okay with that. "
        " Seems like they're having no troubles with making the other potions now... "
        " You go over to find another group that's struggling and help them out. "
        play sound "audio/bellring.mp3"
        " You continued to do this until you heard the bell ring, signalling that it was time for a break. "
        " You watched all of the students pass their work and go out of the classroom. "
        " Once they were all done, Miss Bloomie walks up to you. "
        show missbloomieneutral at center with easeinleft
        msb " Well done. None of their potions have exploded so far because of you. "
        msb " I thank you for your help, [name]. "
        msb " I wish you a good day. You may get along with your own duties now. "
        hide missbloomieneutral at left with easeoutleft
        " You wave her a goodbye before you exited the classroom to go do your own thing. "
        scene black with dissolve
        pause 2.0
        jump teacherbreak1
    label roamschool:
        " You decided to roam the school for a bit. "
        " Of course, you made sure that no one was skipping class and doing something else. "
        " Like smoking. Or doing the dirty. "
        " Hey, who would even do that here? They'd know that it would be a bad idea to do that stuff, especially in this school. "
        " Still, you have to make sure no one does that. Cause you're immediately sending them to detention. "
        " Or reporting them to the principal and their parents. "
        " You managed to catch someone that was running late to their class though... "
        show abbiesad at center with easeinleft
        a " Eek, I'm late... Miss Circle's going to be mad at me... "
        " How're you going to deal with this situation? "
        if kind == True:
            menu:
                " Reassure him and lead him to his classroom ":
                    " You reassure him that he's only just a few minutes late and nothing bad happens. "
                    " Before you sound like a random adult thats probably a creep, you introduce yourself as the new gardening teacher. "
                    " You offer to walk with him to his classroom. "
                    hide abbiesad at bottom
                    show abbieneutral at center
                    a " R...really...? "
                    " The kid seems surprised that you're actually helping him. "
                    " He thinks about it for a moment, before he responded. "
                    hide abbieneutral at bottom
                    show abbiehappy at center
                    a " O...okay... Thank you... "
                    " You took the kids hand and you led him to his classroom. You asked him where it was first though. "
                    " Eventually, the both of you reach the classroom. "
                    scene black with dissolve
                    pause 2.0
                    scene classroom with dissolve
                    show abbieneutral at left with easeinleft
                    " You let go of his hand, and you were about to leave, but then suddenly... "
                    show misscircleangry at right with easeinright
                    x " Abbie! Where have you been?! " with vpunch
                    " Seems like she's the teacher for this class. "
                    hide misscircleangry at bottom
                    show misscircleneutral at right
                    " She notices you and immediately acts like she isn't mad at all. "
                    x " Oh, hello [mr]... "
                    " She seems to pause, trying to remember what your name was. "
                    " She seems to be struggling for a bit before you pointed at your ID. "
                    x " Oh yes, [mr] [name]! Sorry, sorry... "
                    x " Thank you for bringing little Abbie here, but do you mind telling me why he is late? "
                    x " He perhaps wanted to skip classes? Anything? "
                    " While she does look like she's just innocently asking... "
                    " There's a hint of anger in her eyes. "
                    hide abbieneutral at bottom
                    show abbiesad at left
                    " You look back at Abbie and he seems to be on the verge of crying, but is trying to hide it. "
                    " Poor thing... "
                    " You look back at the teacher, looking at her ID. "
                    $ circleknow = True
                    " Miss Circle... Well, you could see why they called her that, alright. "
                    " You then prepared yourself to defend the student. "
                    " You told Miss Circle that Abbie might've just woken up late and you believe that he doesn't want to skip school. "
                    hide abbiesad at bottom
                    show abbiehappy at left
                    " You also told her that you think Abbie is a good student and would never do anything to skip class. "
                    " ...Let's just hope that she won't get mad at you for saying that. "
                    msc " ... "
                    hide abbiehappy at bottom
                    show abbieneutral at left
                    msc " Well, thank you, [mr] [name]. Abbie, go ahead and take your seat. "
                    a " ...Yes ma'am... "
                    hide abbieneutral at right with easeoutright
                    " She seems oddly calm now... "
                    " It's best to keep an eye on her. "
                    " You then walk out of the classroom, not wanting to cause anymore disturbances. "
                    scene black with dissolve
                    " You've got a few students looking at you as you did. "
                    " Some out of curiousity on who you were, some who were just simply looking to see what was going on. "
                    " You continued to roam around the school. "
                    pause 2.0
                    jump teacherbreak1
                " Do nothing about it and just watch him skedaddle ":
                    hide abbiesad at right with easeoutright
                    " You watched the kid skedaddle to his classroom instead of helping him out a bit. "
                    " You honestly could care less, it's his problem that he got late. "
                    " It's simply just not your problem. "
                    " You continued to roam around the school, making sure no one's skipping. "
                    " You did catch a few students, and they just skedaddled to their classroom before you could lecture them. "
                    " You just had that much aura. "
                    " You continued to do this for the rest of the break, occassionally looking into other classrooms to see what they're doing. "
                    scene black with dissolve
                    pause 2.0
                    jump teacherbreak1
        elif calm == True:
            menu:
                " Reassure him and lead him to his classroom ":
                    " You reassure him that he's only just a few minutes late and nothing bad happens. "
                    " Before you sound like a random adult thats probably a creep, you introduce yourself as the new gardening teacher. "
                    " You offer to walk with him to his classroom. "
                    hide abbiesad at bottom
                    show abbieneutral at center
                    a " R...really...? "
                    " The kid seems surprised that you're actually helping him. "
                    " He thinks about it for a moment, before he responded. "
                    hide abbieneutral at bottom
                    show abbiehappy at center
                    a " O...okay... Thank you... "
                    " You took the kids hand and you led him to his classroom. You asked him where it was first though. "
                    " Eventually, the both of you reach the classroom. "
                    scene black with dissolve
                    pause 2.0
                    scene classroom with dissolve
                    show abbieneutral at left with easeinleft
                    " You let go of his hand, and you were about to leave, but then suddenly... "
                    show misscircleangry at right with easeinright
                    x " Abbie! Where have you been?! " with vpunch
                    " Seems like she's the teacher for this class. "
                    hide misscircleangry at bottom
                    show misscircleneutral at right
                    " She notices you and immediately acts like she isn't mad at all. "
                    x " Oh, hello [mr]... "
                    " She seems to pause, trying to remember what your name was. "
                    " She seems to be struggling for a bit before you pointed at your ID. "
                    x " Oh yes, [mr] [name]! Sorry, sorry... "
                    x " Thank you for bringing little Abbie here, but do you mind telling me why he is late? "
                    x " He perhaps wanted to skip classes? Anything? "
                    " While she does look like she's just innocently asking... "
                    " There's a hint of anger in her eyes. "
                    hide abbieneutral at bottom
                    show abbiesad at left
                    " You look back at Abbie and he seems to be on the verge of crying, but is trying to hide it. "
                    " Poor thing... "
                    " You look back at the teacher, looking at her ID. "
                    $ circleknow = True
                    " Miss Circle... Well, you could see why they called her that, alright. "
                    " You then prepared yourself to defend the student. "
                    " You told Miss Circle that Abbie might've just woken up late and you believe that he doesn't want to skip school. "
                    hide abbiesad at bottom
                    show abbiehappy at left
                    " You also told her that you think Abbie is a good student and would never do anything to skip class. "
                    " ...Let's just hope that she won't get mad at you for saying that. "
                    msc " ... "
                    hide abbiehappy at bottom
                    show abbieneutral at left
                    msc " Well, thank you, [mr] [name]. Abbie, go ahead and take your seat. "
                    a " ...Yes ma'am... "
                    hide abbieneutral at right with easeoutright
                    " She seems oddly calm now... "
                    " It's best to keep an eye on her. "
                    " You then walk out of the classroom, not wanting to cause anymore disturbances. "
                    scene black with dissolve
                    " You've got a few students looking at you as you did. "
                    " Some out of curiousity on who you were, some who were just simply looking to see what was going on. "
                    " You continued to roam around the school. "
                    pause 2.0
                    jump teacherbreak1
                " Do nothing about it and just watch him skedaddle ":
                    hide abbiesad at right with easeoutright
                    " You watched the kid skedaddle to his classroom instead of helping him out a bit. "
                    " You honestly could care less, it's his problem that he got late. "
                    " It's simply just not your problem. "
                    " You continued to roam around the school, making sure no one's skipping. "
                    " You did catch a few students, and they just skedaddled to their classroom before you could lecture them. "
                    " You just had that much aura. "
                    " You continued to do this for the rest of the break, occassionally looking into other classrooms to see what they're doing. "
                    scene black with dissolve
                    pause 2.0
                    jump teacherbreak1
        elif mean == True:
            menu:
                " Reassure him and lead him to his classroom ":
                    " You reassure him that he's only just a few minutes late and nothing bad happens. "
                    " Before you sound like a random adult thats probably a creep, you introduce yourself as the new gardening teacher. "
                    " You offer to walk with him to his classroom. "
                    hide abbiesad at bottom
                    show abbieneutral at center
                    a " R...really...? "
                    " The kid seems surprised that you're actually helping him. "
                    " He thinks about it for a moment, before he responded. "
                    hide abbieneutral at bottom
                    show abbiehappy at center
                    a " O...okay... Thank you... "
                    " You took the kids hand and you led him to his classroom. You asked him where it was first though. "
                    " Eventually, the both of you reach the classroom. "
                    scene black with dissolve
                    pause 2.0
                    scene classroom with dissolve
                    show abbieneutral at left with easeinleft
                    " You let go of his hand, and you were about to leave, but then suddenly... "
                    show misscircleangry at right with easeinright
                    x " Abbie! Where have you been?! " with vpunch
                    " Seems like she's the teacher for this class. "
                    hide misscircleangry at bottom
                    show misscircleneutral at right
                    " She notices you and immediately acts like she isn't mad at all. "
                    x " Oh, hello [mr]... "
                    " She seems to pause, trying to remember what your name was. "
                    " She seems to be struggling for a bit before you pointed at your ID. "
                    x " Oh yes, [mr] [name]! Sorry, sorry... "
                    x " Thank you for bringing little Abbie here, but do you mind telling me why he is late? "
                    x " He perhaps wanted to skip classes? Anything? "
                    " While she does look like she's just innocently asking... "
                    " There's a hint of anger in her eyes. "
                    hide abbieneutral at bottom
                    show abbiesad at left
                    " You look back at Abbie and he seems to be on the verge of crying, but is trying to hide it. "
                    " Poor thing... "
                    " You look back at the teacher, looking at her ID. "
                    $ circleknow = True
                    " Miss Circle... Well, you could see why they called her that, alright. "
                    " You then prepared yourself to defend the student. "
                    " You told Miss Circle that Abbie might've just woken up late and you believe that he doesn't want to skip school. "
                    hide abbiesad at bottom
                    show abbiehappy at left
                    " You also told her that you think Abbie is a good student and would never do anything to skip class. "
                    " ...Let's just hope that she won't get mad at you for saying that. "
                    msc " ... "
                    hide abbiehappy at bottom
                    show abbieneutral at left
                    msc " Well, thank you, [mr] [name]. Abbie, go ahead and take your seat. "
                    a " ...Yes ma'am... "
                    hide abbieneutral at right with easeoutright
                    " She seems oddly calm now... "
                    " It's best to keep an eye on her. "
                    " You then walk out of the classroom, not wanting to cause anymore disturbances. "
                    scene black with dissolve
                    " You've got a few students looking at you as you did. "
                    " Some out of curiousity on who you were, some who were just simply looking to see what was going on. "
                    " You continued to roam around the school. "
                    pause 2.0
                    jump teacherbreak1
                " Well, GET RUSHING TO YOUR CLASSROOM NOW, YOU IDIOT! ":
                    a " EEK!! " with vpunch
                    hide abbiesad at right with easeoutright
                    " You watched the kid skedaddle to his classroom instead of helping him out a bit. "
                    " You honestly could care less, it's his problem that he got late. "
                    " It's simply just not your problem. "
                    " You continued to roam around the school, making sure no one's skipping. "
                    " You did catch a few students, and they just skedaddled to their classroom before you could lecture them. "
                    " You just had that much aura. "
                    " You continued to do this for the rest of the break, occassionally looking into other classrooms to see what they're doing. "
                    scene black with dissolve
                    pause 2.0
                    jump teacherbreak1
    label teacherbreak1:
        scene hallway with dissolve
        " It's breaktime. "
        " Whilst walking around, you spot a few of your fellow teachers. "
        " Which one of them do you talk to? "
        if circleknow == True:
            menu:
                " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                    jump circlebreak1int
                " {image=misterdemiicon} A guy that tripped {image=misterdemiicon} ":
                    jump demibreak1int
                " {image=missemilyicon} A woman having trouble carrying her things {image=missemilyicon} ":
                    jump emilybreak1int
        else:
            menu:
                " {image=misscircleicon} A woman chowing down on some oreos {image=misscircleicon} ":
                    jump circlebreak1int
                " {image=misterdemiicon} A guy that tripped {image=misterdemiicon} ":
                    jump demibreak1int
                " {image=missemilyicon} A woman having trouble carrying her things {image=missemilyicon} ":
                    jump emilybreak1int
        label circlebreak1int:
            if circleknow == True:
                " You decided to check out what Miss Circle is doing. "
                show misscircleneutral at center with easeinright
                msc " *crunching asmr* "
                " ...Seems like she's quite busy chowing down on some oreos. "
                hide misscircleneutral at bottom
                show misscircleangry at center
                " You ask her if you could have some, only to have her very intimidating and sharp compass pointed right at you. "
                msc " NO!! These are my oreos and I'm not sharing!! "
                " Eeeyikes. Well, I guess it's best not to disturb her while she's eating then. "
                " She lowers her compass, and you wait for Miss Circle to finish up eating... "
                hide misscircleangry at bottom
                show misscircleneutral at center
                " She then turns back to normal after awhile. "
                msc " Hmmm... They always taste so good! "
                msc " Sorry about how I acted, [name]. It's just that I love oreos so much! "
                msc " I sometimes wish that I could have all the oreos in the world to myself~ "
                msc " No one gets to have them, only me! "
                " ...Seems like she has a weird thing for oreos. "
                " New information unlocked, I guess? "
                hide misscircleneutral at bottom
                show misscirclehappy at center
                msc " I like all kinds of oreos - All of them taste so good! "
                " Is...is she just going to talk about oreos? "
                msc " I can never get tired of their taste!! They're just so, so delicious! "
                " Yep, she's just gonna talk about oreos now. "
                " You're probably gonna have to deal with this for the rest of the break. "
                " Let's just pretend that you're actually listening, I mean... "
                " Who would want to actually listen to someone yapping about oreos? "
                " Then again, there are people who yap about shrek x sonic fanfiction a whole lot. "
                " ...Wonder why those people like that ship anyway. "
                scene black with dissolve
                " You spent the entire break listening to Miss Circle talk about oreos. "
                " Well, half listening. You were listening whilst making sure students dont cause any trouble in the hallways. "
                " What a good teacher you are! "
                play sound "audio/bellring.mp3"
                " The bell rings soon enough, and Miss circle goes to teach her own class. "
                " Time to find someone you can help again... "
                pause 2.0
                jump class2
            else:
                " You decided to check out what that tall woman is doing. "
                show misscircleneutral at center with easeinright
                x " *crunching asmr* "
                " ...Seems like she's quite busy chowing down on some oreos. "
                hide misscircleneutral at bottom
                show misscircleangry at center
                " You ask her if you could have some, only to have her very intimidating and sharp compass pointed right at you. "
                x " NO!! These are my oreos and I'm not sharing!! "
                " Eeeyikes. Well, I guess it's best not to disturb her while she's eating then. "
                " She lowers her compass, and you wait for her to finish up eating... "
                hide misscircleangry at bottom
                show misscircleneutral at center
                " She then turns back to normal after awhile. "
                x " Hmmm... They always taste so good! "
                x " Sorry about how I acted. It's just that I love oreos so much! "
                x " Hey, wait... you must be the new gardening teacher, correct? "
                x " You're quite tiny! Like the rest of these teachers here, heheh... "
                x " Of course, I don't mean that as an insult. I'm the tallest of all teachers here! "
                x " Wait, right, right. I need to introduce myself. "
                $ circleknow = True
                hide misscircleneutral at bottom
                show misscirclehappy at center
                msc " I'm Miss Circle! I teach math. "
                hide misscirclehappy at bottom
                show misscircleneutral at center
                msc " Pleased to meet you! "
                msc " But now, back to my beloved oreos... "
                msc " I sometimes wish that I could have all the oreos in the world to myself~ "
                msc " No one gets to have them, only me! "
                " ...Seems like she has a weird thing for oreos. "
                " New information unlocked, I guess? "
                hide misscircleneutral at bottom
                show misscirclehappy at center
                msc " I like all kinds of oreos - All of them taste so good! "
                " Is...is she just going to talk about oreos? "
                msc " I can never get tired of their taste!! They're just so, so delicious! "
                " Yep, she's just gonna talk about oreos now. "
                " You're probably gonna have to deal with this for the rest of the break. "
                " Let's just pretend that you're actually listening, I mean... "
                " Who would want to actually listen to someone yapping about oreos? "
                " Then again, there are people who yap about shrek x sonic fanfiction a whole lot. "
                " ...Wonder why those people like that ship anyway. "
                scene black with dissolve
                " You spent the entire break listening to Miss Circle talk about oreos. "
                " Well, half listening. You were listening whilst making sure students dont cause any trouble in the hallways. "
                " What a good teacher you are! "
                play sound "audio/bellring.mp3"
                " The bell rings soon enough, and Miss circle goes to teach her own class. "
                " Time to find someone you can help again... "
                pause 2.0
                jump class2
        label demibreak1int:
            $ demilv += 10
            " Seems like someone tripped...let's go help him up. "
            " You walk over to the man who was trying to get all of his sheets that fell on the ground. "
            " On closer inspection, he doesn't look like a student...perhaps the music teacher? "
            " You crouch down so that you could help him get his sheets. "
            show mrdemineutral at center
            x " Oh no, oh no... Now all of these are dirty... "
            " You heard him mumble to himself. "
            " You continued to get all of his sheets back together and once you were done, you handed them over to him. "
            x " Ack, where did the other sheets go??? I swore they were just here...! "
            x " Oh god, Miss Grace is so gonna kill me...! "
            hide mrdemineutral at bottom
            show mrdemisurprised at center
            " It took him a bit for him to actually notice you. But he eventually did. "
            x " ...O-oh...! I'm sorry for not noticing you sooner...thank you. "
            hide mrdemisurprised at bottom
            show mrdemineutral at center
            " He took the sheets from you and you help him get up. "
            hide mrdemineutral at bottom
            show mrdemihappy at center
            x " Thanks again... It would've took me a bit longer if you hadn't come to help me... "
            hide mrdemihappy at bottom
            show mrdemineutral at center
            x " Hey, wait... If I-I'm correct, you're that new gardening teacher? "
            " Yup, that's you alright. You nodded your head. "
            x " Oh, that's nice! We've haven't had any new teachers come in after awhile, actually... "
            hide mrdemineutral at bottom
            show mrdemisurprised at center
            x " Gah! - Wait, I haven't introduced myself yet, I'm so sorry! "
            $ demiknow = True
            msd " I'm Mister Demi! I...I teach the music class... "
            hide mrdemisurprised at bottom
            show mrdemineutral at center
            play sound "audio/bellring.mp3"
            " Right after you heard Mister Demi introduce himself, you hear the bell ring. "
            msd " O-oh... Oh dear, I'm gonna be late to my own class.. "
            msd " I'll talk to you later, [name]! I'm so sorry, but I really gotta go! "
            hide mrdemineutral at right with easeoutright
            " You wave goodbye to Mister Demi as he goes to skedaddle to his own class. "
            " Time to find someone who you could help again... "
            pause 2.0
            scene black with dissolve
            jump class2
        label emilybreak1int:
            $ emilylv += 10
            " She seems like she's struggling to carry her things. Let's help her out. "
            show msemilysad at center with easeinleft
            x " Come on, I can do this... My classroom.. isn't that...far... "
            " ...She's carrying a whole load of stuff. "
            " Wonder what's all that for... But no time to think, you've got to help her. "
            " You walk up to her and ask if you could help her carry her things. "
            hide msemilysad at bottom
            show msemilyshock at center
            x " Oh...? you want to help me? "
            hide msemilyshock at bottom
            show msemilyneutral at center
            x " Well, of course you can! how about you take half of my stuff, and I'll hold the other half? "
            " You nod your head, before getting on your tip toes to get half of the woman's stuff and get them into your arms. "
            x " Let's get along now. My classroom isn't that far. "
            " You then start to walk with your fellow teacher. It was quiet, until she spoke up. "
            x " So... from what I've been hearing, you're that new gardening teacher, right? "
            " That's you... you nod your head to confirm. "
            x " That's wonderful! We haven't had any new teachers in a bit, actually... "
            $ emilyknow = True
            mse " I'm Miss Emily. I teach history class. "
            mse " I've always been told that I was teaching a boring subject, but I don't really mind. "
            mse " If someone isn't paying attention to my class, I'll just whack them on the head with my trusty ruler here. "
            mse " It always works, eheh... "
            mse " I know it's a little bit harsh but really, you just gotta pay attention to my class and I'll be nice. "
            mse " It's not that hard to do... "
            " You continued to talk to Miss Emily until you eventually reach her room. "
            mse " Well, here's my classroom. "
            mse " I'll be taking some of that now, actually. "
            " Miss Emily goes to put half of her stuff on her table, then takes the stuff you're holding and puts it in the same spot where she put the other stuff. "
            mse " Thanks again for helping me. I would've been a bit more late to my class if it wasn't for you. "
            mse " You can go get going now. "
            hide msemilyneutral at right with easeoutright
            " Miss Emily then goes to sit in her seat as you walk away. "
            play sound "audio/bellring.mp3"
            " ...Well, would you look at that. Time for you to help another teacher. "
            " Who will it be this time? "
            pause 2.0
            scene black with dissolve
            jump class2
        label class2:
            scene hallway with dissolve
            " You walk around the hallways for a few moments, wondering who to help. "
            " After you're done, you saw that three classrooms were having a bit of a problem with their students. "
            " You thought about it for a moment, and you decided who to help. "
            " Who do you wish to help? "
            if emilyknow == True:
                menu:
                    " {image=missemilyicon} Miss Emily {image=missemilyicon} ":
                        jump emilyhelp
                    " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                        jump demihelp
                    " {image=sashaicon} The art teacher {image=sashaicon} ":
                        jump sashahelp
                    " Actually, I'll just roam around. ":
                        jump roam2
            elif demiknow == True:
                menu:
                    " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                        jump emilyhelp
                    " {image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                        jump demihelp
                    " {image=sashaicon} The art teacher {image=sashaicon} ":
                        jump sashahelp
                    " Actually, I'll just roam around. ":
                        jump roam2
            else:
                menu:
                    " {image=missemilyicon} The history teacher {image=missemilyicon} ":
                        jump emilyhelp
                    " {image=misterdemiicon} The music teacher {image=misterdemiicon} ":
                        jump demihelp
                    " {image=sashaicon} The art teacher {image=sashaicon} ":
                        jump sashahelp
                    " Actually, I'll just roam around. ":
                        jump roam2
            label emilyhelp:
                $ emilylv += 10
                if emilyknow == True:
                    " You decided to help Miss Emily, you then walked into her classroom. "
                else:
                    " You decided to help the history teacher, you then walked into their classroom. "
                scene black with dissolve
                pause 2.0
                scene classroom with dissolve
                if emilyknow == True:
                    " You walked into Miss Emily's classroom, and you could both see and hear her problem. "
                    " The students weren't paying attention. Oh boy. "
                    " I mean, who would? It's history class... How are we supposed to use this in our lives? "
                    " Though, you probably shouldn't say that to Emily. I bet she wouldn't like it. "
                    show msemilyangry at center with easeinright
                    mse " ... "
                    " She looks like she's about to blow up in flames any minute now... "
                    " You really don't want to damage your ears from her screaming, so you started thinking of ways to get the class' attention. "
                    " What should you do? "
                    menu:
                        " Yell at everyone for Ms. Emily ":
                            " Alright, here goes nothing... "
                            hide msemilyangry at bottom
                            show msemilyshock at center
                            stop music
                            " {sc}EVERYONE PAY ATTENTION OR I'M BEATING ALL OF YOU UP!!{/sc} " with vpunch
                            " ... "
                            " The class went silent. "
                            " Everyone looked flabbergasted including Miss Emily. "
                            hide msemilyshock at bottom
                            show msemilyneutral at center
                            play music "audio/paperhigh.mp3" fadein 0.5
                            " After a few moments, Miss Emily looked relieved that her class was finally paying attention. "
                            mse " Thank you, [name]... "
                            mse " I couldn't get them to pay attention no matter what I tried, haha. "
                            mse " Now, do me a favor and make sure that they're actually paying attention. "
                            " Ma'am yes Ma'am... "
                            scene black with dissolve
                            " You spent the rest of your time making sure that everyone was paying attention. "
                            " To those who would move their eye to somewhere else other than the black board, you'd give them THE look. "
                            " It actually worked somehow and everyone was paying attention. "
                            " Nice one. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, indicating that class is over and there's gonna be another short break. "
                            " You wait for the students to leave so that you could get out and get a break of your own too. "
                            pause 2.0
                            jump break2
                        " Kindly tell everyone to pay attention ":
                            " You're sure that no one's going to pay attention to you, but it's worth a shot. "
                            " Here we go... "
                            " You kindly tell everyone to pay attention. "
                            " ...And of course, It didn't work. "
                            " Time to scam them, then. "
                            " If you guys pay attention, I'll buy you guys mcdonalds. "
                            hide msemilyangry at bottom
                            show msemilyshock at center
                            " ...And surprisingly, that worked. "
                            " Heh, get scammed. Losers. "
                            " Looks like even Emily is surprised that it worked. "
                            hide msemilyshock at bottom
                            show msemilyneutral at center
                            " Though, she looks thankful that you finally got the class to calm down. "
                            mse " Thank you, [name]... "
                            mse " I couldn't get them to pay attention no matter what I tried, haha. "
                            mse " Now, do me a favor and make sure that they're actually paying attention. "
                            " Ma'am yes Ma'am... "
                            scene black with dissolve
                            " You spent the rest of your time making sure that everyone was paying attention. "
                            " To those who would move their eye to somewhere else other than the black board, you'd give them THE look. "
                            " It actually worked somehow and everyone was paying attention. "
                            " Nice one. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, indicating that class is over and there's gonna be another short break. "
                            " You wait for the students to leave so that you could get out and get a break of your own too. "
                            pause 2.0
                            jump break2
                        " Scam them ":
                            " You didn't really wanna do this, but this is one of the only ways you could get them to behave. "
                            " You breathe in to prepare yourself... "
                            " ...Hey, if you guys behave and pay attention I'll get you all mcdonalds! "
                            hide msemilyangry at bottom
                            show msemilyshock at center
                            " ...And surprisingly, that worked. "
                            " Heh, get scammed. Losers. "
                            " Looks like even Emily is surprised that it worked. "
                            hide msemilyshock at bottom
                            show msemilyneutral at center
                            " Though, she looks thankful that you finally got the class to calm down. "
                            mse " Thank you, [name]... "
                            mse " I couldn't get them to pay attention no matter what I tried, haha. "
                            mse " Now, do me a favor and make sure that they're actually paying attention. "
                            " Ma'am yes Ma'am... "
                            scene black with dissolve
                            " You spent the rest of your time making sure that everyone was paying attention. "
                            " To those who would move their eye to somewhere else other than the black board, you'd give them THE look. "
                            " It actually worked somehow and everyone was paying attention. "
                            " Nice one. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, indicating that class is over and there's gonna be another short break. "
                            " You wait for the students to leave so that you could get out and get a break of your own too. "
                            pause 2.0
                            jump break2
                else:
                    " You walked into the history teacher's classroom, and you could both see and hear their problem. "
                    " The students weren't paying attention. Oh boy. "
                    " I mean, who would? It's history class... How are we supposed to use this in our lives? "
                    " Though, you probably shouldn't say that to the teacher. I bet they wouldn't like it. "
                    show msemilyangry at center with easeinright
                    x " ... "
                    " You look over at her, and you notice her ID... "
                    $ emilyknow = True
                    " Miss Emily. That's her name. "
                    " She looks like she's about to blow up in flames any minute now... "
                    " You really don't want to damage your ears from her screaming, so you started thinking of ways to get the class' attention. "
                    " What should you do? "
                    menu:
                        " Yell at everyone for Ms. Emily ":
                            " Alright, here goes nothing... "
                            hide msemilyangry at bottom
                            show msemilyshock at center
                            stop music
                            " {sc}EVERYONE PAY ATTENTION OR I'M BEATING ALL OF YOU UP!!{/sc} " with vpunch
                            " ... "
                            " The class went silent. "
                            " Everyone looked flabbergasted including Miss Emily. "
                            hide msemilyshock at bottom
                            show msemilyneutral at center
                            play music "audio/paperhigh.mp3" fadein 0.5
                            " After a few moments, Miss Emily looked relieved that her class was finally paying attention. "
                            mse " Thank you, [name]... "
                            mse " I couldn't get them to pay attention no matter what I tried, haha. "
                            mse " Now, do me a favor and make sure that they're actually paying attention. "
                            " Ma'am yes Ma'am... "
                            scene black with dissolve
                            " You spent the rest of your time making sure that everyone was paying attention. "
                            " To those who would move their eye to somewhere else other than the black board, you'd give them THE look. "
                            " It actually worked somehow and everyone was paying attention. "
                            " Nice one. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, indicating that class is over and there's gonna be another short break. "
                            " You wait for the students to leave so that you could get out and get a break of your own too. "
                            pause 2.0
                            jump break2
                        " Kindly tell everyone to pay attention ":
                            " You're sure that no one's going to pay attention to you, but it's worth a shot. "
                            " Here we go... "
                            " You kindly tell everyone to pay attention. "
                            " ...And of course, It didn't work. "
                            " Time to scam them, then. "
                            " If you guys pay attention, I'll buy you guys mcdonalds. "
                            hide msemilyangry at bottom
                            show msemilyshock at center
                            " ...And surprisingly, that worked. "
                            " Heh, get scammed. Losers. "
                            " Looks like even Emily is surprised that it worked. "
                            hide msemilyshock at bottom
                            show msemilyneutral at center
                            " Though, she looks thankful that you finally got the class to calm down. "
                            mse " Thank you, [name]... "
                            mse " I couldn't get them to pay attention no matter what I tried, haha. "
                            mse " Now, do me a favor and make sure that they're actually paying attention. "
                            " Ma'am yes Ma'am... "
                            scene black with dissolve
                            " You spent the rest of your time making sure that everyone was paying attention. "
                            " To those who would move their eye to somewhere else other than the black board, you'd give them THE look. "
                            " It actually worked somehow and everyone was paying attention. "
                            " Nice one. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, indicating that class is over and there's gonna be another short break. "
                            " You wait for the students to leave so that you could get out and get a break of your own too. "
                            pause 2.0
                            jump break2
                        " Scam them ":
                            " You didn't really wanna do this, but this is one of the only ways you could get them to behave. "
                            " You breathe in to prepare yourself... "
                            " ...Hey, if you guys behave and pay attention I'll get you all mcdonalds! "
                            hide msemilyangry at bottom
                            show msemilyshock at center
                            " ...And surprisingly, that worked. "
                            " Heh, get scammed. Losers. "
                            " Looks like even Emily is surprised that it worked. "
                            hide msemilyshock at bottom
                            show msemilyneutral at center
                            " Though, she looks thankful that you finally got the class to calm down. "
                            mse " Thank you, [name]... "
                            mse " I couldn't get them to pay attention no matter what I tried, haha. "
                            mse " Now, do me a favor and make sure that they're actually paying attention. "
                            " Ma'am yes Ma'am... "
                            scene black with dissolve
                            " You spent the rest of your time making sure that everyone was paying attention. "
                            " To those who would move their eye to somewhere else other than the black board, you'd give them THE look. "
                            " It actually worked somehow and everyone was paying attention. "
                            " Nice one. "
                            play sound "audio/bellring.mp3"
                            " The bell rings, indicating that class is over and there's gonna be another short break. "
                            " You wait for the students to leave so that you could get out and get a break of your own too. "
                            pause 2.0
                            jump break2
            label demihelp:
                $ demilv += 10
                if demiknow == True:
                    " You decided to go and help whatever Mister Demi is going through. "
                else:
                    " You decided to go and help whatever the music teacher is going through. "
                scene black with dissolve
                pause 2.0
                scene classroom with dissolve
                if demiknow == True:
                    " You walk into Demi's classroom, finding Demi himself looking quite distressed. More distressed than earlier. "
                    show mrdemineutral at center with easeinleft
                    msd " Okay, um... class, please tell me if you've seen Claire's wallet... "
                    msd " If any of you have it, please know that it isn't funny and I'll be reporting you to the principal... "
                    " Mister Demi seems to panic a bit more, but he slightly calms down when he sees you. "
                    msd " [name]... Hi there... We're having a bit of an issue.. "
                    msd " You see, one of my students, Claire, had lost her wallet... "
                    msd " We're trying to find it right now because apparently she still had it before she entered the classroom... "
                    msd " I...if it's not much trouble to you... Could you...maybe...help...? "
                    msd " Only if you want to, by the way... "
                    " You thought about it for a moment before you nodded, you wanted to help him out. "
                    " After all, you'd be freaking out too and trying to get people to help. "
                    hide mrdemineutral at bottom
                    show mrdemihappy at center
                    msd " Thank you, [name]... Your help is much appreciated... "
                    hide mrdemihappy at bottom
                    show mrdemineutral at center
                    msd " Okay, um... what do you think we should do? "
                    " You started thinking again... "
                    " ...And had an idea. You suggested that you yourself and Demi should check everyone's bags and pockets. "
                    " Just to make sure that they're not hiding anything. Plus, you could also find dangerous things in there. "
                    msd " Sounds like a good idea... You'll take that side of the classroom, and I'll take this one...alright? "
                    " You nodded. "
                    msd " Okay... "
                    msd " Everyone, we'll be checking your bags and pockets... Just to make sure that you guys both didn't steal Claire's wallet and don't have anything dangerous stored in there... "
                    hide mrdemineutral at right with easeoutright
                    " You then started looking at all the student's bags and pockets. "
                    " Of course, you mostly saw normal things, some slightly concerning things... "
                    " Then you reach the very back section. You glanced at the trash can from the back and saw a leather wallet. "
                    " You picked it up and asked the student who lost it, Claire, if it was hers. "
                    show clairehappy at center with easeinleft
                    c " Yeah! That's my wallet! "
                    c " Thank you so much, [mr] [name]! "
                    c " I'm not sure how it got into the trash can though... "
                    c " Someone must've put it there! "
                    hide clairehappy at left with easeoutleft
                    show mrdemineutral at center with easeinright
                    msd " Well, seems like you found it... "
                    msd " I'll be trying to figure out who put the wallet there, and um... "
                    msd " You can stay here for a bit, if you want to... And you could try making sure that no one steals anything from someone while you're here... "
                    hide mrdemineutral at bottom
                    show mrdemihappy at center
                    msd " Thank you for your help again... "
                    scene black with dissolve
                    " You stayed in the classroom and watched over the students in Demi's class. "
                    " Both making sure that everyone behaves and making sure that no one tries to steal anything. "
                    play sound "audio/bellring.mp3"
                    " You stayed until you heard the bell ring, signalling for another break. "
                    " You waited until all of the students went outside the classroom, before you could go outside yourself. "
                    pause 2.0
                    jump break2
                else:
                    " You walk into the music teacher's classroom, finding the teacher himself looking quite distressed. More distressed than earlier. "
                    show mrdemineutral at center with easeinleft
                    x " Okay, um... class, please tell me if you've seen Claire's wallet... "
                    x " If any of you have it, please know that it isn't funny and I'll be reporting you to the principal... "
                    " He seems to panic a bit more, but he slightly calms down when he sees you. "
                    x " [mr] [name]... Hi there... We're having a bit of an issue.. "
                    $ demiknow = True
                    msd " I'm Mister Demi, te music teacher, and um... "
                    msd " You see, one of my students, Claire, had lost her wallet... "
                    msd " We're trying to find it right now because apparently she still had it before she entered the classroom... "
                    msd " I...if it's not much trouble to you... Could you...maybe...help...? "
                    msd " Only if you want to, by the way... "
                    " You thought about it for a moment before you nodded, you wanted to help him out. "
                    " After all, you'd be freaking out too and trying to get people to help. "
                    hide mrdemineutral at bottom
                    show mrdemihappy at center
                    msd " Thank you, [name]... Your help is much appreciated... "
                    hide mrdemihappy at bottom
                    show mrdemineutral at center
                    msd " Okay, um... what do you think we should do? "
                    " You started thinking again... "
                    " ...And had an idea. You suggested that you yourself and Demi should check everyone's bags and pockets. "
                    " Just to make sure that they're not hiding anything. Plus, you could also find dangerous things in there. "
                    msd " Sounds like a good idea... You'll take that side of the classroom, and I'll take this one...alright? "
                    " You nodded. "
                    msd " Okay... "
                    msd " Everyone, we'll be checking your bags and pockets... Just to make sure that you guys both didn't steal Claire's wallet and don't have anything dangerous stored in there... "
                    hide mrdemineutral at right with easeoutright
                    " You then started looking at all the student's bags and pockets. "
                    " Of course, you mostly saw normal things, some slightly concerning things... "
                    " Then you reach the very back section. You glanced at the trash can from the back and saw a leather wallet. "
                    " You picked it up and asked the student who lost it, Claire, if it was hers. "
                    show clairehappy at center with easeinleft
                    c " Yeah! That's my wallet! "
                    c " Thank you so much, [mr] [name]! "
                    c " I'm not sure how it got into the trash can though... "
                    c " Someone must've put it there! "
                    hide clairehappy at left with easeoutleft
                    show mrdemineutral at center with easeinright
                    msd " Well, seems like you found it... "
                    msd " I'll be trying to figure out who put the wallet there, and um... "
                    msd " You can stay here for a bit, if you want to... And you could try making sure that no one steals anything from someone while you're here... "
                    hide mrdemineutral at bottom
                    show mrdemihappy at center
                    msd " Thank you for your help again... "
                    scene black with dissolve
                    " You stayed in the classroom and watched over the students in Demi's class. "
                    " Both making sure that everyone behaves and making sure that no one tries to steal anything. "
                    play sound "audio/bellring.mp3"
                    " You stayed until you heard the bell ring, signalling for another break. "
                    " You waited until all of the students went outside the classroom, before you could go outside yourself. "
                    pause 2.0
                    jump break2
            label sashahelp:
                $ sashalv += 10
                " You decided to see what the art teacher is struggling with. "
                scene black with dissolve
                pause 2.0
                scene classroom with dissolve
                " You walked into the classroom, only finding the classroom to be empty and you could only find the art teacher looking for something. "
                show sashaconfused at center with dissolve
                x " I swore I put it here, come on... "
                hide sashaconfused at bottom
                show sashaangry at center
                x " Come on, where is that stupid thing...! "
                " Geez, she looks a bit scary while she's mad. "
                " You decided to tap her shoulder and ask her what she's looking for. "
                hide sashaangry at bottom
                show sashaneutral at center
                x " Oh...? "
                x " Oh! You're the new gardening teacher! [mr] [name], right? "
                $ sashaknow = True
                mss " I'm Miss Sasha - The art teacher! "
                mss " I also teach the kindergarten students, heh... They're quite the handful, but I can handle it! "
                mss " You see... I'm trying to find the assignments I was supposed to give the kindergarten students for today... "
                mss " And guess what, I lost them... ehh...hehe... "
                mss " I can't really afford to print all of that all over again, since there's no time for that... "
                mss " Could you help me a bit here? Well, if you want to. "
                " You didn't really have anything to do, so you decided to help her out. "
                hide sashaneutral at bottom
                show sashahappy at center
                mss " Thank you! I'll look on this side, and you'll look at that side, okay? "
                hide sashahappy at left with easeoutleft
                " She then gets started with looking. "
                " You start looking in your side too. "
                " You couldn't really find anything, until you found a stack of papers being crushed underneath a painting. "
                " You picked them up and you showed them to Miss Sasha. "
                show sashaneutral at center with easeinleft
                mss " Hm? You found them? "
                hide sashaneutral at bottom
                show sashahappy at center
                mss " Oh, yes! These are the assignments I was supposed to give them today! "
                hide sashahappy at bottom
                show sashaneutral at center
                mss " Thank you very much for your help again, [name]. "
                mss " This would've taken me a bit longer if it wasn't for your help. "
                mss " You can go on now and do whatever you wanted to, I'll be going to the kindergarten classroom! "
                mss " I'll see you later! "
                scene black with dissolve
                " You walked out of the classroom as you parted ways for now with Miss Sasha. "
                " In the meantime, you walked around the halls and made sure that no one was skipping class. "
                " Or doing anything bad in secret. "
                play sound "audio/bellring.mp3"
                " You then heard the bell ring, signalling it was time for a break. "
                " You should take a break, too... "
                pause 2.0
                jump break2
            label roam2:
                " You decided to roam the halls for a bit instead of helping the other teachers. "
                " It's not your problem, anyway. They'll figure it out sooner or later. "
                scene black with dissolve
                " You continued to roam around the school and actually caught a few students skipping class. "
                " You dragged them to their classrooms and you continued on looking for students who were skipping. "
                " Seems like you've gotten everyone... You've checked every nook and cranny of the school. "
                play sound "audio/bellring.mp3"
                " You just roamed around the halls until you heard the bell ring. "
                " Time for a break... "
                pause 2.0
                jump break2
            label break2:
                scene hallway with dissolve
                " You see a few of your fellow teachers talking with eachother. "
                " Who do you want to talk with? "
                if circleknow == True and demiknow,sashaknow,emilyknow == False:
                    menu:
                        " Miss Circle and two other teachers ":
                            jump cirthabloom
                        " Three other teachers you don't recognize ":
                            jump emdemsash
                elif thavelknow == True and demiknow,sashaknow,emilyknow == False:
                    menu:
                        " Miss Thavel and two other teachers ":
                            jump cirthabloom
                        " Three other teachers you don't recognize ":
                            jump emdemsash
                elif bloomieknow == True and demiknow,sashaknow,emilyknow == False:
                    menu:
                        " Miss Bloomie and two other teachers ":
                            jump cirthabloom
                        " Three other teachers you don't recognize ":
                            jump emdemsash
                elif circleknow,demiknow == True and sashaknow,emilyknow == False:
                    menu:
                        " Miss Circle and two other teachers ":
                            jump cirthabloom
                        " Mister Demi and two other teachers ":
                            jump emdemsash
                elif circleknow,sashaknow == True and demiknow,emilyknow == False:
                    menu:
                        " Miss Circle and two other teachers ":
                            jump cirthabloom
                        " Miss Sasha and two other teachers ":
                            jump emdemsash
                elif circleknow,emilyknow == True and demiknow,sashaknow == False:
                    menu:
                        " Miss Circle and two other teachers ":
                            jump cirthabloom
                        " Miss Emily and two other teachers ":
                            jump emdemsash
                elif thavelknow,demiknow == True and sashaknow,emilyknow == False:
                    menu:
                        " Miss Thavel and two other teachers ":
                            jump cirthabloom
                        " Mister Demi and two other teachers ":
                            jump emdemsash
                elif thavelknow,sashaknow == True and demiknow,emilyknow == False:
                    menu:
                        " Miss Thavel and two other teachers ":
                            jump cirthabloom
                        " Miss Sasha and two other teachers ":
                            jump emdemsash
                elif thavelknow,emilyknow == True and demiknow,sashaknow == False:
                    menu:
                        " Miss Thavel and two other teachers ":
                            jump cirthabloom
                        " Miss Emily and two other teachers ":
                            jump emdemsash
                elif bloomieknow,demiknow == True and sashaknow,emilyknow == False:
                    menu:
                        " Miss Bloomie and two other teachers ":
                            jump cirthabloom
                        " Mister Demi and two other teachers ":
                            jump emdemsash
                elif bloomieknow,sashaknow == True and demiknow,emilyknow == False:
                    menu:
                        " Miss Bloomie and two other teachers ":
                            jump cirthabloom
                        " Miss Sasha and two other teachers ":
                            jump emdemsash
                elif bloomieknow,emilyknow == True and demiknow,sashaknow == False:
                    menu:
                        " Miss Bloomie and two other teachers ":
                            jump cirthabloom
                        " Miss Emily and two other teachers ":
                            jump emdemsash
                elif demiknow == True and circleknow,thavelknow,bloomieknow,sashaknow,emilyknow == False:
                    menu:
                        " Three teachers you don't recognize ":
                            jump cirthabloom
                        " Mister Demi and two other teachers ":
                            jump emdemsash
                elif sashaknow == True and circleknow,thavelknow,bloomieknow,demiknow,emilyknow == False:
                    menu:
                        " Three teachers you don't recognize ":
                            jump cirthabloom
                        " Miss Sasha and two other teachers ":
                            jump emdemsash
                elif emilyknow == True and circleknow,thavelknow,bloomieknow,demiknow,sashaknow == False:
                    menu:
                        " Three teachers you don't recognize ":
                            jump cirthabloom
                        " Miss Emily and two other teachers ":
                            jump emdemsash
                elif emilyknow,sashaknow == True and circleknow,thavelknow,bloomieknow,demiknow == False:
                    menu:
                        " Three teachers you don't recognize ":
                            jump cirthabloom
                        " Emily, Sasha, and one other teacher you don't recognize ":
                            jump emdemsash
                elif emilyknow,demiknow == True and circleknow,thavelknow,bloomieknow,sashaknow == False:
                    menu:
                        " Three teachers you don't recognize ":
                            jump cirthabloom
                        " Emily, Demi, and one other teacher you don't recognize ":
                            jump emdemsash
                elif sashaknow,demiknow == True and circleknow,thavelknow,bloomieknow,emilyknow == False:
                    menu:
                        " Three teachers you don't recognize ":
                            jump cirthabloom
                        " Sasha, Demi, and one other teacher you don't recognize ":
                            jump emdemsash
                else:
                    menu:
                        " Three teachers you don't recognize ":
                            jump cirthabloom
                        " Three other teachers you don't recognize ":
                            jump emdemsash
                label cirthabloom:
                    if circleknow == True:
                        " You decided to talk with Miss Circle and those two other very tall teachers. "
                        " Well, except for one. One of them seems to be a little bit too short. "
                    elif thavelknow == True:
                        " You decided to talk with Miss Thavel and those two other very tall teachers. "
                        " Well, except for one. One of them seems to be a little bit too short. "
                    elif bloomieknow == True:
                        " You decided to talk with Miss Bloomie and those two other very tall teachers. "
                    else:
                        " You decided to talk with the three very tall teachers. "
                        " Except for one. One of them seems to be very short compared to the other two. "
                    show missbloomieneutral at right with easeinleft
                    show misscircleneutral at center with easeinleft
                    show msthravelneutral at left with easeinleft
                    if circleknow == True:
                        msc " So... "
                        x " Yes, Circle. I have your oreos. "
                        hide misscircleneutral at bottom
                        show misscirclehappy at center
                        msc " May I have them now? "
                        x " Just don't go too feral while eating them {nw} "
                        " Miss Circle snatches the pack of oreos from the other teachers' hands and starts eating all of them. " with vpunch
                        hide msthravelneutral at bottom
                        show msthravelhappy at left
                        x " My, my, Circle! I don't think anything can beat your love for oreos at this point! "
                        x " Eh... I guess this can make use of the amount of oreos my students keep on giving me. "
                        hide msthravelhappy at bottom
                        show msthravelneutral at left
                        x " You get oreos, Boom-boom? "
                        x " Don't call me that. Also, yes. I used to, from my more older classes. "
                        x " Also, the gardening teacher's here. "
                        x " Ooooh, that's right. We have a new gardening teacher! "
                        x " You're...[name]. Read that from the ID you have there! "
                        x " Glad to have you here. "
                        $ bloomieknow = True
                        $ thavelknow = True
                        msb " I'm Miss Bloomie. I teach science. "
                        mst " And I'm Miss Thavel! I'm teaching language class! "
                        mst " It's good to have you here! "
                        msb " Hm, seems like Miss Circle is busy eating her oreos... "
                        msb " Would you both like to discuss about how we should treat students who aren't paying attention to class? "
                        mst " Sure! We don't really have anything to do right now, anyway. "
                        " You agreed with Miss Thavel, you needed something to do to pass your time. "
                        msb " Great. So... "
                        scene black with dissolve
                        " You talked with Miss Bloomie and Miss Thavel about what you guys should do when some students aren't paying attention to class. "
                        " Bloomie had some pretty good ideas, but Thavel's were pretty much a bit concerning to say the least. "
                        " You just suggested that a thwack on the head would work, but then again that wouldn't look pretty good for both yours and the school's reputation. "
                        " Eeyikers. Just a little scolding will do, then. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, which means that the break for today was over. "
                        " Miss Circle, Miss Bloomie, and Miss Thavel all go to their respective classrooms. "
                        " As you stay outside to figure out who you should help. "
                        pause 2.0
                        jump class3
                    elif thavelknow == True:
                        x " So... "
                        x " Yes, Circle. I have your oreos. "
                        hide misscircleneutral at bottom
                        show misscirclehappy at center
                        x " May I have them now? "
                        x " Just don't go too feral while eating them {nw} "
                        " Miss Circle snatches the pack of oreos from the other teachers' hands and starts eating all of them. " with vpunch
                        hide msthravelneutral at bottom
                        show msthravelhappy at left
                        mst " My, my, Circle! I don't think anything can beat your love for oreos at this point! "
                        x " Eh... I guess this can make use of the amount of oreos my students keep on giving me. "
                        hide msthravelhappy at bottom
                        show msthravelneutral at left
                        mst " You get oreos, Boom-boom? "
                        x " Don't call me that. Also, yes. I used to, from my more older classes. "
                        x " Also, the gardening teacher's here. "
                        mst " Ooooh, that's right. Hi there, [name]! "
                        mst " [their] name is [name] by the way, heheh. [they] helped me out earlier! "
                        x " Glad to have you here. "
                        $ bloomieknow = True
                        $ circleknow = True
                        msb " I'm Miss Bloomie. I teach science. "
                        mst " And I'm pretty sure you already know who I am! "
                        mst " That large woman eating oreos over there is Miss Circle, she teaches math! "
                        mst " It's good to have you here! "
                        msb " Hm, seems like Miss Circle is busy eating her oreos... "
                        msb " Would you both like to discuss about how we should treat students who aren't paying attention to class? "
                        mst " Sure! We don't really have anything to do right now, anyway. "
                        " You agreed with Miss Thavel, you needed something to do to pass your time. "
                        msb " Great. So... "
                        scene black with dissolve
                        " You talked with Miss Bloomie and Miss Thavel about what you guys should do when some students aren't paying attention to class. "
                        " Bloomie had some pretty good ideas, but Thavel's were pretty much a bit concerning to say the least. "
                        " You just suggested that a thwack on the head would work, but then again that wouldn't look pretty good for both yours and the school's reputation. "
                        " Eeyikers. Just a little scolding will do, then. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, which means that the break for today was over. "
                        " Miss Circle, Miss Bloomie, and Miss Thavel all go to their respective classrooms. "
                        " As you stay outside to figure out who you should help. "
                        pause 2.0
                        jump class3
                    elif bloomieknow == True:
                        x " So... "
                        msb " Yes, Circle. I have your oreos. "
                        hide misscircleneutral at bottom
                        show misscirclehappy at center
                        x " May I have them now? "
                        msb " Just don't go too feral while eating them {nw} "
                        " Miss Circle snatches the pack of oreos from the other teachers' hands and starts eating all of them. " with vpunch
                        hide msthravelneutral at bottom
                        show msthravelhappy at left
                        x " My, my, Circle! I don't think anything can beat your love for oreos at this point! "
                        msb " Eh... I guess this can make use of the amount of oreos my students keep on giving me. "
                        hide msthravelhappy at bottom
                        show msthravelneutral at left
                        x " You get oreos, Boom-boom? "
                        msb " Don't call me that. Also, yes. I used to, from my more older classes. "
                        msb " Also, the gardening teacher's here. "
                        x " Ooooh, that's right. We have a new gardening teacher! "
                        x " You're...[name]. Read that from the ID you have there! "
                        msb " Glad to have you here. "
                        $ circleknow = True
                        $ thavelknow = True
                        msb " I'm sure you already know who I am. "
                        msb " [name] over here helped me out in class earlier. "
                        x " Is that so...? "
                        mst " Well then, I'm Miss Thavel! I'm teaching language class! "
                        mst " It's good to have you here! "
                        mst " That large woman over there is Miss Circle, she teaches math! "
                        msb " Hm, seems like Miss Circle is busy eating her oreos... "
                        msb " Would you both like to discuss about how we should treat students who aren't paying attention to class? "
                        mst " Sure! We don't really have anything to do right now, anyway. "
                        " You agreed with Miss Thavel, you needed something to do to pass your time. "
                        msb " Great. So... "
                        scene black with dissolve
                        " You talked with Miss Bloomie and Miss Thavel about what you guys should do when some students aren't paying attention to class. "
                        " Bloomie had some pretty good ideas, but Thavel's were pretty much a bit concerning to say the least. "
                        " You just suggested that a thwack on the head would work, but then again that wouldn't look pretty good for both yours and the school's reputation. "
                        " Eeyikers. Just a little scolding will do, then. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, which means that the break for today was over. "
                        " Miss Circle, Miss Bloomie, and Miss Thavel all go to their respective classrooms. "
                        " As you stay outside to figure out who you should help. "
                        pause 2.0
                        jump class3
                    else:
                        x " So... "
                        x " Yes, Circle. I have your oreos. "
                        hide misscircleneutral at bottom
                        show misscirclehappy at center
                        x " May I have them now? "
                        x " Just don't go too feral while eating them {nw} "
                        " Miss Circle snatches the pack of oreos from the other teachers' hands and starts eating all of them. " with vpunch
                        hide msthravelneutral at bottom
                        show msthravelhappy at left
                        x " My, my, Circle! I don't think anything can beat your love for oreos at this point! "
                        x " Eh... I guess this can make use of the amount of oreos my students keep on giving me. "
                        hide msthravelhappy at bottom
                        show msthravelneutral at left
                        x " You get oreos, Boom-boom? "
                        x " Don't call me that. Also, yes. I used to, from my more older classes. "
                        x " Also, the gardening teacher's here. "
                        x " Ooooh, that's right. We have a new gardening teacher! "
                        x " You're...[name]. Read that from the ID you have there! "
                        x " Glad to have you here. "
                        $ bloomieknow = True
                        $ thavelknow = True
                        $ circleknow = True
                        msb " I'm Miss Bloomie. I teach science. "
                        mst " And I'm Miss Thavel! I'm teaching language class! "
                        mst " That large woman over there is Miss Circle, she teaches math! "
                        mst " It's good to have you here! "
                        msb " Hm, seems like Miss Circle is busy eating her oreos... "
                        msb " Would you both like to discuss about how we should treat students who aren't paying attention to class? "
                        mst " Sure! We don't really have anything to do right now, anyway. "
                        " You agreed with Miss Thavel, you needed something to do to pass your time. "
                        msb " Great. So... "
                        scene black with dissolve
                        " You talked with Miss Bloomie and Miss Thavel about what you guys should do when some students aren't paying attention to class. "
                        " Bloomie had some pretty good ideas, but Thavel's were pretty much a bit concerning to say the least. "
                        " You just suggested that a thwack on the head would work, but then again that wouldn't look pretty good for both yours and the school's reputation. "
                        " Eeyikers. Just a little scolding will do, then. "
                        play sound "audio/bellring.mp3"
                        " The bell rings, which means that the break for today was over. "
                        " Miss Circle, Miss Bloomie, and Miss Thavel all go to their respective classrooms. "
                        " As you stay outside to figure out who you should help. "
                        pause 2.0
                        jump class3
                label emdemsash:
                    if demiknow == True:
                        " You decided to talk with Mister Demi and two other teachers you don't recognize. "
                    elif sashaknow == True:
                        " You decided to talk with Miss Sasha and two other teachers you don't recognize. "
                    elif emilyknow == True:
                        " You decided to talk with Miss Emily and two other teachers you don't recognize. "
                    else:
                        " You decided to talk with three other teachers that you don't recognize. "
                    show msemilyneutral at left with easeinright
                    show mrdemineutral at center with easeinright
                    show sashaneutral at right with easeinright
                    if demiknow == True:
                        x " Hmmm... do you guys have any idea on what I should paint next? "
                        msd " Maybe...I don't know... something nature related? "
                        hide sashaneutral at bottom
                        show sashaconfused at right
                        x " But I've already drawn trees and flowers... "
                        x " How about you go out somewhere, like at the beach if we ever had time, and paint there? "
                        hide sashaconfused at bottom
                        show sashahappy at right
                        x " Oh! Thanks, Em! I'll make sure to do that! "
                        hide sashahappy at bottom
                        show sashaneutral at right
                        x " Hold on, isn't that the new gardening teacher over there? "
                        hide mrdemineutral at bottom
                        show mrdemihappy at center
                        msd " Oh, yeah! That's my friend over there! Hi [name]! "
                        " Really? You've just met him earlier, and he already considers you as a friend? "
                        " That's pretty sweet, actually. What a cutie patootie. "
                        x " It's nice that you're making more friends, Dem! "
                        hide mrdemihappy at bottom
                        show mrdemineutral at center
                        msd " Whaaat? I do make friends though... "
                        x " Eheh, just messing with you a bit there. "
                        $ sashaknow = True
                        $ emilyknow = True
                        x " Oh, right. We should introduce ourselves over here! It would be rude not to. "
                        mss " I'm Miss Sasha! I teach both the kindergarten class and art class! "
                        mse " And I'm Miss Emily, I teach history class. Pleased to meet you, fellow teacher! "
                        msd " Now that you two have introduced yourselves...what should we talk about now...? "
                        mss " Hmm, maybe stuff we like to do in our free time? Other than gradin' the student's papers. "
                        mse " That sounds fun! You in, [name]? "
                        " Well, you don't really have anything else to do. You just nodded as a signal that you wanted to be apart of this. "
                        mss " Alrighty! I'll start! I like to... "
                        scene black with dissolve
                        " You spent the rest of the break talking to the three teachers about what you guys like to do in your free time. "
                        " You were honestly just vibing as they talked. Though, you never really did anything while you had free time. "
                        " You were the kind of [person] who would just play games in your free time. "
                        " Like those brainrot games you'd see in those random tiktok stories that people make. "
                        " They're actually pretty fun. "
                        play sound "audio/bellring.mp3"
                        " You hear the bell ring, meaning that the break was over. "
                        " You then watch as the three teachers you were speaking to going to their respective classrooms, "
                        " As you stood there, waiting for someone that you could help out. "
                        pause 2.0
                        jump class3
                    elif sashaknow == True:
                        mss " Hmmm... do you guys have any idea on what I should paint next? "
                        x " Maybe...I don't know... something nature related? "
                        hide sashaneutral at bottom
                        show sashaconfused at right
                        mss " But I've already drawn trees and flowers... "
                        x " How about you go out somewhere, like at the beach if we ever had time, and paint there? "
                        hide sashaconfused at bottom
                        show sashahappy at right
                        mss " Oh! Thanks, Em! I'll make sure to do that! "
                        hide sashahappy at bottom
                        show sashaneutral at right
                        x " Hold on, isn't that the new gardening teacher over there? "
                        hide sashaneutral at bottom
                        show sashahappy at right
                        mss " Oh! Oh! That's my friend over there! Hi [name]! "
                        " Really? You've just met her earlier, and she already considers you as a friend? "
                        " That's really nice, actually. What a sweet girl. "
                        x " It's nice to know that you two are already friends... "
                        $ demiknow = True
                        $ emilyknow = True
                        x " Oh, right. We should introduce ourselves over here! It would be rude not to. "
                        msd " I'm Mister Demi... I teach music class... "
                        mse " And I'm Miss Emily, I teach history class. Pleased to meet you, fellow teacher! "
                        msd " Now that we have introduced ourselves...what should we talk about now...? "
                        mss " Hmm, maybe stuff we like to do in our free time? Other than gradin' the student's papers. "
                        mse " That sounds fun! You in, [name]? "
                        " Well, you don't really have anything else to do. You just nodded as a signal that you wanted to be apart of this. "
                        mss " Alrighty! I'll start! I like to... "
                        scene black with dissolve
                        " You spent the rest of the break talking to the three teachers about what you guys like to do in your free time. "
                        " You were honestly just vibing as they talked. Though, you never really did anything while you had free time. "
                        " You were the kind of [person] who would just play games in your free time. "
                        " Like those brainrot games you'd see in those random tiktok stories that people make. "
                        " They're actually pretty fun. "
                        play sound "audio/bellring.mp3"
                        " You hear the bell ring, meaning that the break was over. "
                        " You then watch as the three teachers you were speaking to going to their respective classrooms, "
                        " As you stood there, waiting for someone that you could help out. "
                        pause 2.0
                        jump class3
                    elif emilyknow == True:
                        x " Hmmm... do you guys have any idea on what I should paint next? "
                        x " Maybe...I don't know... something nature related? "
                        hide sashaneutral at bottom
                        show sashaconfused at right
                        x " But I've already drawn trees and flowers... "
                        mse " How about you go out somewhere, like at the beach if we ever had time, and paint there? "
                        hide sashaconfused at bottom
                        show sashahappy at right
                        x " Oh! Thanks, Em! I'll make sure to do that! "
                        hide sashahappy at bottom
                        show sashaneutral at right
                        x " Hold on, isn't that the new gardening teacher over there? "
                        hide msemilyneutral at bottom
                        show msemilyhappy at left
                        mse " Oh hello there, friend! "
                        " Really? You've just met her earlier, and she already considers you as a friend? "
                        " That's really nice, actually. "
                        x " It's nice to know that you two are already friends... "
                        $ demiknow = True
                        $ sashaknow = True
                        x " Oh, right. We should introduce ourselves over here! It would be rude not to. "
                        msd " I'm Mister Demi... I teach music class... "
                        mss " I'm Miss Sasha, I teach both the kindergarten class and art class! "
                        msd " Now that we have introduced ourselves...what should we talk about now...? "
                        mss " Hmm, maybe stuff we like to do in our free time? Other than gradin' the student's papers. "
                        mse " That sounds fun! You in, [name]? "
                        " Well, you don't really have anything else to do. You just nodded as a signal that you wanted to be apart of this. "
                        mss " Alrighty! I'll start! I like to... "
                        scene black with dissolve
                        " You spent the rest of the break talking to the three teachers about what you guys like to do in your free time. "
                        " You were honestly just vibing as they talked. Though, you never really did anything while you had free time. "
                        " You were the kind of [person] who would just play games in your free time. "
                        " Like those brainrot games you'd see in those random tiktok stories that people make. "
                        " They're actually pretty fun. "
                        play sound "audio/bellring.mp3"
                        " You hear the bell ring, meaning that the break was over. "
                        " You then watch as the three teachers you were speaking to going to their respective classrooms, "
                        " As you stood there, waiting for someone that you could help out. "
                        pause 2.0
                        jump class3
                    else:
                        x " Hmmm... do you guys have any idea on what I should paint next? "
                        x " Maybe...I don't know... something nature related? "
                        hide sashaneutral at bottom
                        show sashaconfused at right
                        mx " But I've already drawn trees and flowers... "
                        x " How about you go out somewhere, like at the beach if we ever had time, and paint there? "
                        hide sashaconfused at bottom
                        show sashahappy at right
                        x " Oh! Thanks, Em! I'll make sure to do that! "
                        hide sashahappy at bottom
                        show sashaneutral at right
                        x " Hold on, isn't that the new gardening teacher over there? "
                        hide sashaneutral at bottom
                        show sashahappy at right
                        $ sashaknow = True
                        $ demiknow = True
                        $ emilyknow = True
                        x " Oh, right. We should introduce ourselves over here! It would be rude not to. "
                        msd " I'm Mister Demi... I teach music class... "
                        mss " I'm Miss Sasha, I teach both the kindergarten class and art class! "
                        mse " And I'm Miss Emily, I teach history class. Pleased to meet you, fellow teacher! "
                        msd " Now that we have introduced ourselves...what should we talk about now...? "
                        mss " Hmm, maybe stuff we like to do in our free time? Other than gradin' the student's papers. "
                        mse " That sounds fun! You in, [name]? "
                        " Well, you don't really have anything else to do. You just nodded as a signal that you wanted to be apart of this. "
                        mss " Alrighty! I'll start! I like to... "
                        scene black with dissolve
                        " You spent the rest of the break talking to the three teachers about what you guys like to do in your free time. "
                        " You were honestly just vibing as they talked. Though, you never really did anything while you had free time. "
                        " You were the kind of [person] who would just play games in your free time. "
                        " Like those brainrot games you'd see in those random tiktok stories that people make. "
                        " They're actually pretty fun. "
                        play sound "audio/bellring.mp3"
                        " You hear the bell ring, meaning that the break was over. "
                        " You then watch as the three teachers you were speaking to going to their respective classrooms, "
                        " As you stood there, waiting for someone that you could help out. "
                        pause 2.0
                        jump class3
                label class3:
                    scene hallway with dissolve
                    " Time for you to help someone again. Who will it be? "
                    if thavelknow,sashaknow,bloomieknow == True:
                        menu:
                            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                                jump thavelhelpagain
                            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                                jump sashahelpagain
                            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                                jump bloomiehelpagain
                            " I'll just roam around. ":
                                jump roam3
                    elif thavelknow,bloomieknow == True and sashaknow == False:
                        menu:
                            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                                jump thavelhelpagain
                            " {image=sashaicon} The art teacher {image=sashaicon} ":
                                jump sashahelpagain
                            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                                jump bloomiehelpagain
                            " I'll just roam around. ":
                                jump roam3
                    elif thavelknow,sashaknow == True and bloomieknow == False:
                        menu:
                            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                                jump thavelhelpagain
                            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                                jump sashahelpagain
                            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                                jump bloomiehelpagain
                            " I'll just roam around. ":
                                jump roam3
                    elif sashaknow,bloomieknow == True and thavelknow == False:
                        menu:
                            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                                jump thavelhelpagain
                            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                                jump sashahelpagain
                            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                                jump bloomiehelpagain
                            " I'll just roam around. ":
                                jump roam3
                    elif thavelknow == True and bloomieknow,sashaknow == False:
                        menu:
                            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                                jump thavelhelpagain
                            " {image=sashaicon} The art teacher {image=sashaicon} ":
                                jump sashahelpagain
                            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                                jump bloomiehelpagain
                            " I'll just roam around. ":
                                jump roam3
                    elif sashaknow == True and bloomieknow, thavelknow == False:
                        menu:
                            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                                jump thavelhelpagain
                            " {image=sashaicon} Miss Sasha {image=sashaicon} ":
                                jump sashahelpagain
                            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                                jump bloomiehelpagain
                            " I'll just roam around. ":
                                jump roam3
                    elif bloomieknow == True and sashaknow, thavelknow == False:
                        menu:
                            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                                jump thavelhelpagain
                            " {image=sashaicon} The art teacher {image=sashaicon} ":
                                jump sashahelpagain
                            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                                jump bloomiehelpagain
                            " I'll just roam around. ":
                                jump roam3
                    else:
                        menu:
                            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                                jump thavelhelpagain
                            " {image=sashaicon} The art teacher {image=sashaicon} ":
                                jump sashahelpagain
                            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                                jump bloomiehelpagain
                            " I'll just roam around. ":
                                jump roam3
                label thavelhelpagain:
                    if thavelknow == True:
                        " You decided to see if Miss Thavel needed help with anything. "
                    else:
                        " You decided to see if the language teacher help with anything. "
                    scene black with dissolve
                    pause 2.0
                    scene classroom with dissolve
                    if thavelknow == True:
                        " You walk in the classroom and you can hear Miss Thavel being bombarded with questions about the lesson. "
                        " Geez, and you thought language class was easy... "
                        " Seriously, how could anyone have a problem with language class? "
                        " You kindly hush the students down before asking Miss Thavel on what was wrong. "
                        show msthravelsurprised at center with easeinleft
                        " She seems flabbergasted at the amount of questions that's being thrown at her. "
                        " Maybe you should help with answering some of the questions. "
                        hide msthravelsurprised at right with easeoutright
                        " You helped answer some of the student's questions because you're smart. "
                        " And also to save Miss Thavel's ears. "
                        " Even you couldn't believe how much questions they were throwing at you, "
                        " You couldn't even tell which one was serious or not. "
                        scene black with dissolve
                        " ...And you dealt with this. For the entire time. "
                        " The amount of questions they were throwing at you, it was flabbergasting! "
                        " This was only language class and they were fumbling this bad? "
                        " As far as you know, Miss Thavel is a good teacher! "
                        " ...yeah I really have nothing to say here "
                        " sorry guys i got lazy while writing here uhhh ignore this message "
                        play sound "audio/bellring.mp3"
                        " blablabla its breaktime now "
                        pause 2.0
                        jump teacherbreak3
                    else:
                        " You walk in the classroom and you can hear the teacher being bombarded with questions about the lesson. "
                        " Geez, and you thought language class was easy... "
                        " Seriously, how could anyone have a problem with language class? "
                        " You kindly hush the students down before asking the teacher on what was wrong. "
                        show msthravelsurprised at center with easeinleft
                        " You look down and saw her ID... "
                        $ thavelknow = True
                        " Miss Thavel. That's her name. "
                        " She seems flabbergasted at the amount of questions that's being thrown at her. "
                        " Maybe you should help with answering some of the questions. "
                        hide msthravelsurprised at right with easeoutright
                        " You helped answer some of the student's questions because you're smart. "
                        " And also to save Miss Thavel's ears. "
                        " Even you couldn't believe how much questions they were throwing at you, "
                        " You couldn't even tell which one was serious or not. "
                        scene black with dissolve
                        " ...And you dealt with this. For the entire time. "
                        " The amount of questions they were throwing at you, it was flabbergasting! "
                        " This was only language class and they were fumbling this bad? "
                        " As far as you know, Miss Thavel is a good teacher! "
                        " ...yeah I really have nothing to say here "
                        " sorry guys i got lazy while writing here uhhh ignore this message "
                        play sound "audio/bellring.mp3"
                        " blablabla its breaktime now "
                        pause 2.0
                        jump teacherbreak3
                label sashahelpagain:
                    # miss sasha wants you to make sure that the students are doing paintings properly
                    if sashaknow == True:
                        " You decided to see if Miss Sasha needed help in anything. "
                    else:
                        " You decided to see if the art teacher needed help in anything. "
                    scene black with dissolve
                    pause 2.0
                    scene classroom with dissolve
                    if sashaknow == True:
                        " You enter her classroom, and you could see students doing all sorts of paintings. "
                        " Some of them looked good, and some...not the best. "
                        " You then saw Miss Sasha struggling on handling a student, and decided to come over to help her. "
                        show sashaangry at center with easeinleft
                        mss " Hey! What did I tell you about painting crude things?! "
                        o " Heh, hey... It's not a big deal. It's not like the whole world's gonna blow up if I draw stuff like this! "
                        mss " Still, you shouldn't be drawing stuff like this! It's unacceptable! "
                        mss " If you draw things like this, then you're going to be sent straight to detention! "
                        o " Pff, no fun... "
                        mss " Good, erase that thing! Cover it in white paint and paint something else! "
                        " Yikes, didn't know that some students had the balls to paint something like...THAT. "
                        " It's honestly insane. "
                        mss " Geez, these kids get on my nerves... "
                        hide sashaangry at bottom
                        show sashaneutral at center
                        mss " ...? Oh! Hi [name]! I didn't notice you there, eheh... sorry. "
                        mss " Now that you're here though, I do have a small request for you... "
                        hide sashaneutral at bottom
                        show sashasad at center
                        mss " Please make sure that no one in my class draws anything weird... "
                        mss " I don't wanna see any of that, plus they're not even allowed to draw that stuff.. "
                        mss " Could you?? Please?? I also have to check in on the kindergarten class to see if they're doing well... "
                        mss " Pretty please? "
                        " Well, who could say no to a look like that? "
                        hide sashasad at bottom
                        show sashahappy at center
                        " You very obviously accepted her offer. Miss Sasha seems pleased. "
                        mss " Thank you very much, [name]! You're a good one! "
                        hide sashahappy at bottom
                        show sashaneutral at center
                        mss " Everyone, [mr] [name] here will be taking care of the class for the time being! "
                        mss " I'll be checking the kindergarten class to see if they're doing fine, and [name] over here will be watching over! "
                        mss " Don't do anything stupid! "
                        hide sashaneutral at right with easeoutright
                        " Miss Sasha then left. Time to check what the students are painting. "
                        " You first check out what a boy with two feathers on his head was painting. "
                        show engelneutral at center with easeinleft
                        " What are you painting? "
                        e " Hello there, [fancy]. I'm painting a picture of my friend... "
                        e " The girl that's sitting beside me, actually. "
                        e " Do you think it looks fine...? "
                        " You look at his painting... AND DAMN ITS DETAILED! "
                        " You think you just got blessed by the heavens to see such a masterpiece like this. "
                        " You didn't even know people at this age could paint like this! "
                        e " ...You really think it looks good? "
                        hide engelneutral at bottom
                        show engelcontent at center
                        e " Hehe...thank you, [fancy]... "
                        hide engelcontent at right with easeoutright
                        " You pat his head gently and then you went to go check other students paintings. "
                        " You then stop by to a boy with black hair, seemingly puzzled on what he should paint. "
                        show abbieneutral at center with easeinleft
                        a " .... "
                        a " Oh, um...Hi, [fancy]... I haven't started yet because... "
                        a " I don't know what to paint... "
                        " You tried to think about something that could help him. "
                        if kind == True:
                            " You then told him to think about soemthing that makes him happy, and for him to try painting that. "
                            a " Umm... I suppose... "
                            hide abbieneutral at bottom
                            show abbiehappy at center
                            a " My parents {i}do{/i} make me happy... "
                            a " I'll try to paint them, then... "
                            a " Thank you, [fancy]... "
                        elif calm == True:
                            " You then told him to paint a place where he feels safe. "
                            a " Hmmm...Um... Maybe... "
                            hide abbieneutral at bottom
                            show abbiehappy at center
                            a " Maybe I could paint something nature related...? "
                            a " ...Plants help me calm down... "
                            a " I'll try to paint that, then... "
                            a " Thank you, [fancy]... "
                        elif mean == True:
                            " You then told him to paint his struggles. After all, it's good to let your emotions out in forms of art or something. "
                            a " ...That doesn't sound...so bad... "
                            hide abbieneutral at bottom
                            show abbiehappy at center
                            a " Atleast I have something to paint now... "
                            a " Thank you, [fancy]... "
                        hide abbiehappy at right with easeoutright
                        " You then pet his head and you walk away to check out another student's painting. "
                        " You then stop by to see a girl painting something very...interesting, to say the least. "
                        show zipneutral at center with easeinleft
                        z " Heh... "
                        " You thwacked her on the head with a paintbrush and told her not to paint that. " with vpunch
                        hide zipneutral at bottom
                        show zipsad at center
                        z " Hey! I was paid to do this! "
                        z " That guy over there, uh... whatshisname... Skell? Yeah, Skell! "
                        z " He paid me 50$ to paint this! "
                        sk " ...(seriously????????????) "
                        " You thwack her on the head again and tell her that even if she was paid to do it or not, she shouldn't have done it. "
                        " You watch her paint over the drawing with white paint and watch her start over. "
                        " Making sure that she doesn't draw anything weird again. "
                        scene black with dissolve
                        " You spent the entire break helping out students and making sure that they aren't painting anything weird. "
                        " Miss Sasha eventually comes back and she thanks you for your help. "
                        play sound "audio/bellring.mp3"
                        " You and Miss Sasha keep on helping the students until the bell rings. "
                        " You watch all of the students get out before you could get out of the classroom as well so that you could get a break of your own. "
                        pause 2.0
                        jump teacherbreak3
                    else:
                        " You enter the classroom, and you could see students doing all sorts of paintings. "
                        " Some of them looked good, and some...not the best. "
                        " You then saw the teacher struggling on handling a student, and decided to come over to help her. "
                        show sashaangry at center with easeinleft
                        x " Hey! What did I tell you about painting crude things?! "
                        o " Heh, hey... It's not a big deal. It's not like the whole world's gonna blow up if I draw stuff like this! "
                        x " Still, you shouldn't be drawing stuff like this! It's unacceptable! "
                        x " If you draw things like this, then you're going to be sent straight to detention! "
                        o " Pff, no fun... "
                        x " Good, erase that thing! Cover it in white paint and paint something else! "
                        " Yikes, didn't know that some students had the balls to paint something like...THAT. "
                        " It's honestly insane. "
                        x " Geez, these kids get on my nerves... "
                        hide sashaangry at bottom
                        show sashaneutral at center
                        x " ...? Oh! Hi [name]! I didn't notice you there, eheh... sorry. "
                        x " Wait, hold on... I just realized I haven't introduced myself yet to you! "
                        $ sashaknow = True
                        mss " I'm Miss Sasha, I teach art class (it's a bit obvious) and I also teach the kindergarten class! "
                        mss " And now that you're here, I have a small request for you... "
                        hide sashaneutral at bottom
                        show sashasad at center
                        mss " Please make sure that no one in my class draws anything weird... "
                        mss " I don't wanna see any of that, plus they're not even allowed to draw that stuff.. "
                        mss " Could you?? Please?? I also have to check in on the kindergarten class to see if they're doing well... "
                        mss " Pretty please? "
                        " Well, who could say no to a look like that? "
                        hide sashasad at bottom
                        show sashahappy at center
                        " You very obviously accepted her offer. Miss Sasha seems pleased. "
                        mss " Thank you very much, [name]! You're a good one! "
                        hide sashahappy at bottom
                        show sashaneutral at center
                        mss " Everyone, [mr] [name] here will be taking care of the class for the time being! "
                        mss " I'll be checking the kindergarten class to see if they're doing fine, and [name] over here will be watching over! "
                        mss " Don't do anything stupid! "
                        hide sashaneutral at right with easeoutright
                        " Miss Sasha then left. Time to check what the students are painting. "
                        " You first check out what a boy with two feathers on his head was painting. "
                        show engelneutral at center with easeinleft
                        " What are you painting? "
                        e " Hello there, [fancy]. I'm painting a picture of my friend... "
                        e " The girl that's sitting beside me, actually. "
                        e " Do you think it looks fine...? "
                        " You look at his painting... AND DAMN ITS DETAILED! "
                        " You think you just got blessed by the heavens to see such a masterpiece like this. "
                        " You didn't even know people at this age could paint like this! "
                        e " ...You really think it looks good? "
                        hide engelneutral at bottom
                        show engelcontent at center
                        e " Hehe...thank you, [fancy]... "
                        hide engelcontent at right with easeoutright
                        " You pat his head gently and then you went to go check other students paintings. "
                        " You then stop by to a boy with black hair, seemingly puzzled on what he should paint. "
                        show abbieneutral at center with easeinleft
                        a " .... "
                        a " Oh, um...Hi, [fancy]... I haven't started yet because... "
                        a " I don't know what to paint... "
                        " You tried to think about something that could help him. "
                        if kind == True:
                            " You then told him to think about soemthing that makes him happy, and for him to try painting that. "
                            a " Umm... I suppose... "
                            hide abbieneutral at bottom
                            show abbiehappy at center
                            a " My parents {i}do{/i} make me happy... "
                            a " I'll try to paint them, then... "
                            a " Thank you, [fancy]... "
                        elif calm == True:
                            " You then told him to paint a place where he feels safe. "
                            a " Hmmm...Um... Maybe... "
                            hide abbieneutral at bottom
                            show abbiehappy at center
                            a " Maybe I could paint something nature related...? "
                            a " ...Plants help me calm down... "
                            a " I'll try to paint that, then... "
                            a " Thank you, [fancy]... "
                        elif mean == True:
                            " You then told him to paint his struggles. After all, it's good to let your emotions out in forms of art or something. "
                            a " ...That doesn't sound...so bad... "
                            hide abbieneutral at bottom
                            show abbiehappy at center
                            a " Atleast I have something to paint now... "
                            a " Thank you, [fancy]... "
                        hide abbiehappy at right with easeoutright
                        " You then pet his head and you walk away to check out another student's painting. "
                        " You then stop by to see a girl painting something very...interesting, to say the least. "
                        show zipneutral at center with easeinleft
                        z " Heh... "
                        " You thwacked her on the head with a paintbrush and told her not to paint that. " with vpunch
                        hide zipneutral at bottom
                        show zipsad at center
                        z " Hey! I was paid to do this! "
                        z " That guy over there, uh... whatshisname... Skell? Yeah, Skell! "
                        z " He paid me 50$ to paint this! "
                        sk " ...(seriously????????????) "
                        " You thwack her on the head again and tell her that even if she was paid to do it or not, she shouldn't have done it. "
                        " You watch her paint over the drawing with white paint and watch her start over. "
                        " Making sure that she doesn't draw anything weird again. "
                        scene black with dissolve
                        " You spent the entire break helping out students and making sure that they aren't painting anything weird. "
                        " Miss Sasha eventually comes back and she thanks you for your help. "
                        play sound "audio/bellring.mp3"
                        " You and Miss Sasha keep on helping the students until the bell rings. "
                        " You watch all of the students get out before you could get out of the classroom as well so that you could get a break of your own. "
                        pause 2.0
                        jump teacherbreak3
                label bloomiehelpagain:
                    # miss bloomie wants you to help demonstrate something
                    if bloomieknow == True:
                        " You decided to see if Miss Bloomie needs help in anything. "
                    else:
                        " You decided to see if the science teacher needs help in anything. "
                    scene black with dissolve
                    pause 2.0
                    scene classroom with dissolve
                    if bloomieknow == True:
                        " You walk into Bloomie's classroom, to see that she was demonstrating something. "
                        show missbloomieneutral at center with easeinleft
                        msb " Now, for this, I need a volunteer. "
                        msb " Would anyone like to volunteer for a moment? "
                        " ... "
                        " Well, no one was raising their hands. Plus, it as really quiet. "
                        " You could see some other students doing their own things, drawing, being on their phones... "
                        " Damn, no one really is paying attention to the lesson. "
                        msb " ...sigh... "
                        " Soon enough, Miss Bloomie spots you standing near the door and turns to you. "
                        msb " Hello there, [fancy] [name]. "
                        msb " Would you like to come up here and volunteer? since none of my students are raising their hands. "
                        " You don't really have a choice, so you stood next to her and waited for her to do something. "
                        msb " Alright, hold this for me. "
                        " She lends you a bottle with some weird purple liquid in it, and it was even glowing. "
                        msb " So, class, when you're making potions, you shouldn't do this. "
                        msb " And by 'this'; I mean make a red potion mix with a purple potion. Otherwise, this would happen. "
                        " Miss Bloomie gets a drop of a red potion in a different bottle and puts it in the purple potion. "
                        " ...And it result, you get exploded on a bit and got dust all over you. " with vpunch
                        " Great. Your outfit is slightly ruined, but you can just wash this off. "
                        " You cleaned yourself up a bit before Miss Bloomie spoke up once more. "
                        msb " So, make sure you're mixing the right potions so that you won't accidentally blow up the entire school. "
                        msb " (Thank you for your help, [name]. You can watch over the students and make sure they're paying attention now.) "
                        " You nodded and sat somewhere near Miss Bloomie to watch over the class. "
                        scene black with dissolve
                        " You watched over the class for the time being. "
                        " It was a tad bit boring but atleast you did your job and made the class pay attention. "
                        play sound "audio/bellring.mp3"
                        " You then hear the bell ring, and watch the students get out of their seats and go into the hallways. "
                        " You wait for all of them to go out before you could go out yourself. "
                        pause 2.0
                        jump teacherbreak3
                    else:
                        " You walk into the science classroom, to see that the teacher was demonstrating something. "
                        show missbloomieneutral at center with easeinleft
                        x " Now, for this, I need a volunteer. "
                        x " Would anyone like to volunteer for a moment? "
                        " ... "
                        " Well, no one was raising their hands. Plus, it as really quiet. "
                        " You could see some other students doing their own things, drawing, being on their phones... "
                        " Damn, no one really is paying attention to the lesson. "
                        x " ...sigh... "
                        " Soon enough, she spots you standing near the door and turns to you. "
                        x " Hello there, [fancy] [name]. "
                        " You look at her ID... "
                        $ bloomieknow = True
                        " Miss Bloomie. The science teacher, huh? Interesting... "
                        msb " Would you like to come up here and volunteer? since none of my students are raising their hands. "
                        " You don't really have a choice, so you stood next to her and waited for her to do something. "
                        msb " Alright, hold this for me. "
                        " She lends you a bottle with some weird purple liquid in it, and it was even glowing. "
                        msb " So, class, when you're making potions, you shouldn't do this. "
                        msb " And by 'this'; I mean make a red potion mix with a purple potion. Otherwise, this would happen. "
                        " Miss Bloomie gets a drop of a red potion in a different bottle and puts it in the purple potion. "
                        " ...And it result, you get exploded on a bit and got dust all over you. " with vpunch
                        " Great. Your outfit is slightly ruined, but you can just wash this off. "
                        " You cleaned yourself up a bit before Miss Bloomie spoke up once more. "
                        msb " So, make sure you're mixing the right potions so that you won't accidentally blow up the entire school. "
                        msb " (Thank you for your help, [name]. You can watch over the students and make sure they're paying attention now.) "
                        " You nodded and sat somewhere near Miss Bloomie to watch over the class. "
                        scene black with dissolve
                        " You watched over the class for the time being. "
                        " It was a tad bit boring but atleast you did your job and made the class pay attention. "
                        play sound "audio/bellring.mp3"
                        " You then hear the bell ring, and watch the students get out of their seats and go into the hallways. "
                        " You wait for all of them to go out before you could go out yourself. "
                        pause 2.0
                        jump teacherbreak3
                label roam3:
                    " You decided to roam the school to make sure that no one does anything bad, or skip class. "
                    scene black with dissolve
                    " You did this for the entire time class was going on. "
                    " Surprisingly, you couldn't catch anyone who was skipping class or anything of the like. "
                    " Either they were hiding really good, or there were really no students skipping. "
                    " How rare... but it's also a good thing if they're not skipping, of course."
                    play sound "audio/bellring.mp3"
                    " You hear the bell ring, and watch all of the students start to get out of their classrooms. "
                    " You just realized that your class is next after this. Uh oh. "
                    pause 2.0
                    jump teacherbreak3
                label teacherbreak3:
                    scene hallway with dissolve
                    " You just realized that your class is next after this break. "
                    " You have honestly no idea what to do, but then you spot your three fellow teachers. "
                    " Maybe you should go up to them and ask for some advice on what to do. "
                    " Who should you talk to, though? "
                    if demiknow,circleknow,thavelknow == True:
                        menu:
                            "{image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                                jump demiadvice
                            "{image=misscircleicon} Miss Circle {image=misscircleicon}":
                                jump circleadvice
                            "{image=missthavelicon} Miss Thavel {image=missthavelicon}":
                                jump thaveladvice
                    elif demiknow,circleknow == True and thavelknow == False:
                        menu:
                            "{image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                                jump demiadvice
                            "{image=misscircleicon} Miss Circle {image=misscircleicon}":
                                jump circleadvice
                            "{image=missthavelicon} A teacher with deer-ish horns {image=missthavelicon}":
                                jump thaveladvice
                    elif demiknow,thavelknow == True and circleknow == False:
                        menu:
                            "{image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                                jump demiadvice
                            "{image=misscircleicon} A very tall teacher {image=misscircleicon}":
                                jump circleadvice
                            "{image=missthavelicon} Miss Thavel {image=missthavelicon}":
                                jump thaveladvice
                    elif circleknow,thavelknow == True and demiknow == False:
                        menu:
                            "{image=misterdemiicon} A very nervous looking teacher {image=misterdemiicon} ":
                                jump demiadvice
                            "{image=misscircleicon} Miss Circle {image=misscircleicon}":
                                jump circleadvice
                            "{image=missthavelicon} Miss Thavel {image=missthavelicon}":
                                jump thaveladvice
                    elif circleknow == True and demiknow,thavelknow == False:
                        menu:
                            "{image=misterdemiicon} A very nervous looking teacher {image=misterdemiicon} ":
                                jump demiadvice
                            "{image=misscircleicon} Miss Circle {image=misscircleicon}":
                                jump circleadvice
                            "{image=missthavelicon} A teacher with deer-ish horns {image=missthavelicon}":
                                jump thaveladvice
                    elif demiknow == True and circleknow,thavelknow == False:
                        menu:
                            "{image=misterdemiicon} Mister Demi {image=misterdemiicon} ":
                                jump demiadvice
                            "{image=misscircleicon} A very tall teacher {image=misscircleicon}":
                                jump circleadvice
                            "{image=missthavelicon} A teacher with deer-ish horns {image=missthavelicon}":
                                jump thaveladvice
                    elif thavelknow == True and circleknow,demiknow == False:
                        menu:
                            "{image=misterdemiicon} A very nervous looking teacher {image=misterdemiicon} ":
                                jump demiadvice
                            "{image=misscircleicon} A very tall teacher {image=misscircleicon}":
                                jump circleadvice
                            "{image=missthavelicon} Miss Thavel {image=missthavelicon}":
                                jump thaveladvice
                    else:
                        menu:
                            "{image=misterdemiicon} A very nervous looking teacher {image=misterdemiicon} ":
                                jump demiadvice
                            "{image=misscircleicon} A very tall teacher {image=misscircleicon}":
                                jump circleadvice
                            "{image=missthavelicon} A teacher with deer-ish horns {image=missthavelicon}":
                                jump thaveladvice
                    label demiadvice:
                        if demiknow == True:
                            " You decided to walk up to Demi to see if he has any advice for you. "
                            show mrdemineutral at center with easeinleft
                            msd " Hm, I wonder what I should do for the next class... Maybe... "
                            " He seems to be wondering about something, until he spotted you. "
                            hide mrdemineutral at bottom
                            show mrdemihappy at center
                            msd " Oh, hey there, [name]! Did you um... need anything? "
                            " You tell him that your class was next, and you're a little nervous about it. "
                            " You told him that you needed some advice on how to calm down and not freak out when your class starts. "
                            hide mrdemihappy at bottom
                            show mrdemineutral at center
                            msd " Oh, advice...? Well, I'm not really good at that stuff, but I'll try... "
                            msd " Hm... "
                            " He thinks for a bit, trying to come up with something before he spoke up again. "
                            msd " ...Well, what I usually do is hum my favorite song, it helps me calm down a lot... "
                            msd " I'm not sure if it's gonna work for you, but you should atleast try it... "
                            " You thought of your favorite song... "
                            " ...And then you start humming it out. "
                            " Surprisingly, this seems to work as your mind feels more cleared and you feel less nervous. "
                            " You stopped once you were done with the song. "
                            msd " ...That was actually a pretty nice tune... "
                            msd " Did my...technique work? "
                            " You nodded your head. You bowed at him to show him your thankfulness towards him before standing straight up again. "
                            hide mrdemineutral at bottom
                            show mrdemihappy at center
                            msd " W...well, I'm glad that it worked out for you then... "
                            play sound "audio/bellring.mp3"
                            hide mrdemihappy at bottom
                            show mrdemineutral at center
                            msd " ...Oh...looks like the bell's ringing... "
                            msd " I'll see you later, [name]! "
                            hide mrdemineutral at right with easeoutright
                            " You wave a goodbye to Mister Demi before you headed off to your own class. "
                            scene black with dissolve
                            $ mewallbreak = renpy.random.randint (1,2)
                            if mewallbreak == 1:
                                pause 2.0
                                jump class4
                            elif mewallbreak == 2:
                                " i know that its inaccurate on how actual teachers shut up john {nw} "
                                jump class4
                        else:
                            " You decided to walk up to that guy over there to see if he has any advice for you. "
                            show mrdemineutral at center with easeinleft
                            x " Hm, I wonder what I should do for the next class... Maybe... "
                            " He seems to be wondering about something, until he spotted you. "
                            hide mrdemineutral at bottom
                            show mrdemihappy at center
                            x " Oh, hey there! Did you um... need anything? "
                            x " Wait...I don't think we've met before, um... "
                            $ demiknow = True
                            msd " Mister Demi. I teach music class...now that we got that out of the way, did you need anything, or...? "
                            " You tell him that your class was next, and you're a little nervous about it. "
                            " You told him that you needed some advice on how to calm down and not freak out when your class starts. "
                            hide mrdemihappy at bottom
                            show mrdemineutral at center
                            msd " Oh, advice...? Well, I'm not really good at that stuff, but I'll try... "
                            msd " Hm... "
                            " He thinks for a bit, trying to come up with something before he spoke up again. "
                            msd " ...Well, what I usually do is hum my favorite song, it helps me calm down a lot... "
                            msd " I'm not sure if it's gonna work for you, but you should atleast try it... "
                            " You thought of your favorite song... "
                            " ...And then you start humming it out. "
                            " Surprisingly, this seems to work as your mind feels more cleared and you feel less nervous. "
                            " You stopped once you were done with the song. "
                            msd " ...That was actually a pretty nice tune... "
                            msd " Did my...technique work? "
                            " You nodded your head. You bowed at him to show him your thankfulness towards him before standing straight up again. "
                            hide mrdemineutral at bottom
                            show mrdemihappy at center
                            msd " W...well, I'm glad that it worked out for you then... "
                            play sound "audio/bellring.mp3"
                            hide mrdemihappy at bottom
                            show mrdemineutral at center
                            msd " ...Oh...looks like the bell's ringing... "
                            msd " I'll see you later, [name]! "
                            hide mrdemineutral at right with easeoutright
                            " You wave a goodbye to Mister Demi before you headed off to your own class. "
                            scene black with dissolve
                            $ mewallbreak = renpy.random.randint (1,2)
                            if mewallbreak == 1:
                                pause 2.0
                                jump class4
                            elif mewallbreak == 2:
                                " i know that its inaccurate on how actual teachers shut up john {nw} "
                                jump class4
                    label circleadvice:
                        if circleknow == True:
                            " You decided to walk up to Miss Circle to see if she has any advice for you. "
                            show misscircleneutral at center with easeinright
                            msc " Hmmm... "
                            hide misscircleneutral at bottom
                            show misscirclehappy at center
                            msc " Oh, hello there [name]! "
                            hide misscirclehappy at bottom
                            show misscircleneutral at center
                            msc " Hm... you seem quite stessed out. Why's that? "
                            " You tell her that your class was next, and you're a little nervous about it. "
                            " You told her that you needed some advice on how to calm down and not freak out when your class starts. "
                            msc " You wish to get advice from me...? "
                            msc " Well, hm. This is gonna make me think for a bit. "
                            msc " Give me a moment... "
                            " Miss Circle starts thinking on how to help you out of your situation. "
                            " She speaks up after a bit of thinking. "
                            msc " Well, what I did to calm myself down on my first day was think about my favorite food. "
                            hide misscircleneutral at bottom
                            show misscirclehappy at center
                            msc " I'm pretty sure you know what that is! "
                            hide misscirclehappy at bottom
                            show misscircleneutral at center
                            msc " Try doing that right now, and tell me if it works. "
                            msc " Just imagine your favorite food...a lot of it...and imagine that you're gonna get it when we're done here... "
                            " You tried doing just that... "
                            " ...You imagined your favorite food and you almost start drooling with the thought of having millions of it once you're done teaching. "
                            " Seems like it worked. It definitely got you distracted and thinking of more positive thoughts. "
                            msc " Well, seemed like it worked, judging by the look on your face! "
                            msc " I'm glad that I could be of help to you, [name]. "
                            msc " I mean, I used to be anxious on my first days starting out as a teacher too! It's something we all experience as teachers! "
                            play sound "audio/bellring.mp3"
                            msc " Well, would you look at that. The bell rang! "
                            msc " I wish you good luck on your class, [name]! "
                            hide misscircleneutral at left with easeoutleft
                            " You waved her a goodbye before you entered your classroom. "
                            scene black with dissolve
                            $ mewallbreak = renpy.random.randint (1,2)
                            if mewallbreak == 1:
                                pause 2.0
                                jump class4
                            elif mewallbreak == 2:
                                " i know that its inaccurate on how actual teachers shut up john {nw} "
                                jump class4
                        else:
                            " You decided to walk up to that big and tall teacher to see if she has any advice for you. "
                            show misscircleneutral at center with easeinright
                            x " Hmmm... "
                            hide misscircleneutral at bottom
                            show misscirclehappy at center
                            x " Oh, hello there! "
                            hide misscirclehappy at bottom
                            show misscircleneutral at center
                            x " You must be the gardening teacher that the others are talking about. "
                            x " I don't believe that we've met before, so let me introduce myself! "
                            $ circleknow = True
                            msc " I am Miss Circle! I teach math in here. Pleased to meet you, fellow teacher! "
                            msc " Hm... you seem quite stessed out. Why's that? "
                            " You tell her that your class was next, and you're a little nervous about it. "
                            " You told her that you needed some advice on how to calm down and not freak out when your class starts. "
                            msc " You wish to get advice from me...? "
                            msc " Well, hm. This is gonna make me think for a bit. "
                            msc " Give me a moment... "
                            " Miss Circle starts thinking on how to help you out of your situation. "
                            " She speaks up after a bit of thinking. "
                            msc " Well, what I did to calm myself down on my first day was think about my favorite food. "
                            hide misscircleneutral at bottom
                            show misscirclehappy at center
                            msc " I'm pretty sure you know what that is! It's oreos! "
                            msc " Other teachers like you should know that. "
                            hide misscircleehappy at bottom
                            show misscircleneutral at center
                            msc " Try doing that right now, and tell me if it works. "
                            msc " Just imagine your favorite food...a lot of it...and imagine that you're gonna get it when we're done here... "
                            " You tried doing just that... "
                            " ...You imagined your favorite food and you almost start drooling with the thought of having millions of it once you're done teaching. "
                            " Seems like it worked. It definitely got you distracted and thinking of more positive thoughts. "
                            msc " Well, seemed like it worked, judging by the look on your face! "
                            msc " I'm glad that I could be of help to you, [name]. "
                            msc " I mean, I used to be anxious on my first days starting out as a teacher too! It's something we all experience as teachers! "
                            play sound "audio/bellring.mp3"
                            msc " Well, would you look at that. The bell rang! "
                            msc " I wish you good luck on your class, [name]! "
                            hide misscircleneutral at left with easeoutleft
                            " You waved her a goodbye before you entered your classroom. "
                            scene black with dissolve
                            $ mewallbreak = renpy.random.randint (1,2)
                            if mewallbreak == 1:
                                pause 2.0
                                jump class4
                            elif mewallbreak == 2:
                                " i know that its inaccurate on how actual teachers shut up john {nw} "
                                jump class4
                    label thaveladvice:
                        if thavelknow == True:
                            # a place
                            " You decided to walk up to Miss Thavel to see if she has any advice for you. "
                            show msthravelneutral at center with easeinright
                            mst " ...Hmmm... "
                            mst " Oh, wait! Sorry, I didn't notice you there, [name]. Heh. "
                            mst " Anyway, what seems to be the problem? You look a little stressed. "
                            mst " Nah, ya look stressed out of your mind. "
                            mst " You need help or something? Maybe advice? "
                            " You nod your head and tell her that you want advice. "
                            " You tell her that your class was next, and you're a little nervous about it. "
                            " You told her that you needed some advice on how to calm down and not freak out when your class starts. "
                            mst " Oh, that? well, you're just like all of us here when we first started a job here! "
                            mst " Let me see...what could help you out, hm... "
                            " Miss Thavel thinks for a moment, before she manages to come up with something for you. "
                            mst " Hm, well... for me, I thought of taking a vacation in a relaxing space! "
                            mst " Just imagine you there with relaxing music. And keep telling yourself that you're gonna get rest after all of this is over. "
                            mst " Now, this worked for me but I don't know if this works for you. "
                            mst " Go ahead and try it! "
                            " You thought of taking a vacation in somewhere relaxing... "
                            " ...Being in a volcano...ah yes thats so relaxing "
                            " You managed to calm yourself down with Miss Thavel's help! "
                            hide msthravelneutral at bottom
                            show msthravelhappy at center
                            mst " Judging by the look on your face, it worked! "
                            " You nodded and you bowed to show your thankfullness to Miss Thavel. "
                            hide msthravelhappy at bottom
                            show msthravelneutral at center
                            mst " You're welcome, buddy. "
                            play sound "audio/bellring.mp3"
                            mst " Oops, looks like the bell's ringing! "
                            mst " I'll be going now, and uh... "
                            mst " Good luck with your class, alright? Make sure you dont freak out! "
                            hide msthravelneutral at left with easeoutleft
                            " You waved her a goodbye before you entered your classroom. "
                            scene black with dissolve
                            $ mewallbreak = renpy.random.randint (1,2)
                            if mewallbreak == 1:
                                pause 2.0
                                jump class4
                            elif mewallbreak == 2:
                                " i know that its inaccurate on how actual teachers shut up john {nw} "
                                jump class4
                        else:
                            " You walk up to the homan with deer horns to see if she has any advice for you. "
                            show msthravelneutral at center with easeinright
                            x " ...Hmmm... "
                            x " Oh, wait! Sorry, I didn't notice you there. "
                            x " Hmm... you must be the new gardening teacher, yeah? "
                            x " Don't believe that we've met before, so I should introduce myself! "
                            $ thavelknow = True
                            mst " Anyway, what seems to be the problem? You look a little stressed. "
                            mst " Nah, ya look stressed out of your mind. "
                            mst " You need help or something? Maybe advice? "
                            " You nod your head and tell her that you want advice. "
                            " You tell her that your class was next, and you're a little nervous about it. "
                            " You told her that you needed some advice on how to calm down and not freak out when your class starts. "
                            mst " Oh, that? well, you're just like all of us here when we first started a job here! "
                            mst " Let me see...what could help you out, hm... "
                            " Miss Thavel thinks for a moment, before she manages to come up with something for you. "
                            mst " Hm, well... for me, I thought of taking a vacation in a relaxing space! "
                            mst " Just imagine you there with relaxing music. And keep telling yourself that you're gonna get rest after all of this is over. "
                            mst " Now, this worked for me but I don't know if this works for you. "
                            mst " Go ahead and try it! "
                            " You thought of taking a vacation in somewhere relaxing... "
                            " ...Being in a volcano...ah yes thats so relaxing "
                            " You managed to calm yourself down with Miss Thavel's help! "
                            hide msthravelneutral at bottom
                            show msthravelhappy at center
                            mst " Judging by the look on your face, it worked! "
                            " You nodded and you bowed to show your thankfullness to Miss Thavel. "
                            hide msthravelhappy at bottom
                            show msthravelneutral at center
                            mst " You're welcome, buddy. "
                            play sound "audio/bellring.mp3"
                            mst " Oops, looks like the bell's ringing! "
                            mst " I'll be going now, and uh... "
                            mst " Good luck with your class, alright? Make sure you dont freak out! "
                            hide msthravelneutral at left with easeoutleft
                            " You waved her a goodbye before you entered your classroom. "
                            scene black with dissolve
                            $ mewallbreak = renpy.random.randint (1,2)
                            if mewallbreak == 1:
                                pause 2.0
                                jump class4
                            elif mewallbreak == 2:
                                " i know that its inaccurate on how actual teachers shut up john {nw} "
                                jump class4
                label class4:
                    # mc class start
                    scene black with dissolve
                    pause 2.0
                    scene gardenroom with dissolve
                    " It's time for your class. Except no one is really here yet. "
                    " Guess you'll just have to wait for them to come in. "
                    pause 1.5
                    " Eventually, students come into your classroom and take their seats. "
                    " Some of them take some time to look at the pretty scenery your room has before they sat down. "
                    " You know, your room is the best. Nah, you're only kidding. "
                    " You wait for everyone to quiet down before you spoke up. "
                    " You've got to introduce yourself first, of course. Teachers have to do that. "
                    if kind == True:
                        " Hello, I'm [mr] [name]! I will be the new gardening teacher! "
                        " If you have any questions, it's 100 percent okay to ask me!! "
                        " Though, please don't mess up the plants otherwise I'll bite you/j "
                        " ...Seems like the students got comfortable with you real fast because of your introduction. "
                        " They must think that you're a nice teacher now. "
                    elif calm == True:
                        " yooo wsg gangalang im [mr] [name] "
                        " im cool if you have any questions you can js ask me  "
                        " if you do fuck up the plants i will basketball you outta the school "
                        " ...Seems like the students got comfortable with you real fast because of your introduction. "
                        " They probably think that you're a chill teacher. "
                    elif mean == True:
                        " HEY all of you pay attention " with vpunch
                        " my name is [mr] [name] and you all BETTER remember that " with vpunch
                        " If you have any questions then you can ask me but if you fuck with the plants then i will kill you " with vpunch
                        " GOT IT???? " with vpunch
                        " ...you got a [fancy] yes [fancy] from the students so i guess that's good "
                    " Alright, time to do your lesson. "
                    " Your first lesson is to teach the students what gardening tools are and how to use them. "
                    " You start to teach them... "
                    scene black with dissolve
                    " Actually, it wasn't so bad while you were teaching them. "
                    " They actually managed to behave themselves, except for some students. "
                    if kind == True:
                        " Obviously, you just told them to pay attention kindly. "
                        " And if they didn't? They'd be fed to a snake. "
                        " That surely got them to pay attention! "
                    elif mean == True:
                        " Obviously, you yelled at them to get their attention. "
                        " If they didn't pay attention, you'd feed them to a dog. "
                        " That really got them to pay attention, alright. "
                        " What a good teacher you are! "
                    elif calm == True:
                        " Obviously, you just picked up one of the students who werent paying attention... "
                        " ...And almost actually threw them out the room. But you didn't. "
                        " You just messed with them and told them: that would happen if they didn't pay attention to your class. "
                        " You put the kid back down on their seat and continued teaching. "
                        " What a good teacher you are! "
                    play sound "audio/bellring.mp3"
                    " The bell rings, and you dismissed your class. "
                    " You watched everyone leave before you got all your things arranged and left aswell. "
                    pause 2.0
                    jump teacherbreak4
                label teacherbreak4:
                    scene hallway with dissolve
                    " Well, your first class was certainly a bit exhausting. "
                    " You decided to go hang out somewhere for a bit, just to calm you down. "
                    " Where should you go, though? "
                    menu:
                        " {image=misterdemiicon} The rooftop {image=misterdemiicon} ":
                            jump demirooftop
                        " {image=missbloomieicon} The back of the school {image=missbloomieicon} ":
                            jump bloomieback
                        " {image=missemilyicon} The front of the school {image=missemilyicon} ":
                            jump emilyfront
                    label demirooftop:
                        " Let's go to the rooftop, then. "
                        scene black with dissolve
                        pause 2.0
                        scene rooftop with dissolve
                        " You walk up to the rooftop, and it's surprisingly much quieter up here. "
                        " Sure, there's a few student, but they're not really making much noise at all. "
                        " You wander around for a bit, looking at the sky and looking around. "
                        " You then spot one of your fellow teachers standing nearby and just looking at the clouds. "
                        " Seems like he's in deep thought... "
                        " Do you talk to him? "
                        menu:
                            " Yeah sure ":
                                " Alright. Let's walk up to him. "
                                show mrdemihappy at center with easeinright
                                if demiknow == True:
                                    " You stand next to him and wait for him to notice you. "
                                    msd " Hm... The clouds are so pretty... "
                                    hide mrdemihappy at bottom
                                    show mrdemineutral at center
                                    msd " Hm? Is there someone next to me...? "
                                    msd " O-oh! [name]! Sorry that I dind't see you there... "
                                    msd " It's just that... I was kinda busy looking at the clouds. "
                                    msd " Oh, I almost forgot to ask...how was your class? "
                                    " You thought about how your class went... "
                                    if kind == True:
                                        " ...You then told him that it went well. "
                                        hide mrdemineutral at bottom
                                        show mrdemihappy at center
                                        msd " That's good to hear, then... "
                                        hide mrdemihappy at bottom
                                        show mrdemineutral at center
                                    elif mean == True:
                                        " ...You then told him it went fine, but there were kids who weren't paying attention. "
                                        " You told him that you kind of yelled at them for that. "
                                        msd " Well, it's fine... there's kids who don't pay attention in every school... "
                                        msd " I mean, It's not like all of the kids in every school pays attention to class... "
                                    elif calm == True:
                                        " ...You then told him that it went well. "
                                        hide mrdemineutral at bottom
                                        show mrdemihappy at center
                                        msd " That's good to hear, then... "
                                        hide mrdemihappy at bottom
                                        show mrdemineutral at center
                                    " You ask Mister Demi what he was doing. "
                                    msd " You know how in the past, we used to look at clouds and look at what shapes they would make? "
                                    msd " That's what I'm trying to do right now... "
                                    msd " And it's...really...really relaxing... "
                                    msd " Would you like to look at clouds with me...? "
                                    msd " It's okay if you don't want to, I know it's pretty boring... "
                                    " You don't really want Mister Demi to be alone. "
                                    " You decided to hang out with him for a bit. "
                                    scene black with dissolve
                                    " You spent the break looking at clouds with Mister Demi. "
                                    " And, he was right. It was pretty relaxing. "
                                    " It honestly reminded you of the golden days, when you were just a kid and you had nothing to worry about... "
                                    " You miss those days. But then again, you can't turn back time. "
                                    " All you can do now is to try and relive those memories by doing these things. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rings, meaning that your time to relax was over. "
                                    " You and Demi head down the stairs to go back to the hallways. "
                                    pause 2.0
                                    jump class5
                                else:
                                    " You stand next to him and wait for him to notice you. "
                                    x " Hm... The clouds are so pretty... "
                                    hide mrdemihappy at bottom
                                    show mrdemineutral at center
                                    x " Hm? Is there someone next to me...? "
                                    x " O-oh! Sorry that I dind't see you there... "
                                    x " It's just that... I was kinda busy looking at the clouds. "
                                    x " ...Are you...the new gardening teacher? "
                                    x " I don't believe I've gotten to introduce myself to you before, so... "
                                    $ demiknow = True
                                    msd " I'm Mister Demi, I teach music... "
                                    " You tell him that it's nice to meet him, and you ask him what he's doing. "
                                    msd " You know how in the past, we used to look at clouds and look at what shapes they would make? "
                                    msd " That's what I'm trying to do right now... "
                                    msd " And it's...really...really relaxing... "
                                    msd " Would you like to look at clouds with me...? "
                                    msd " It's okay if you don't want to, I know it's pretty boring... "
                                    " You don't really want Mister Demi to be alone. "
                                    " You decided to hang out with him for a bit. "
                                    scene black with dissolve
                                    " You spent the break looking at clouds with Mister Demi. "
                                    " And, he was right. It was pretty relaxing. "
                                    " It honestly reminded you of the golden days, when you were just a kid and you had nothing to worry about... "
                                    " You miss those days. But then again, you can't turn back time. "
                                    " All you can do now is to try and relive those memories by doing these things. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rings, meaning that your time to relax was over. "
                                    " You and Demi head down the stairs to go back to the hallways. "
                                    pause 2.0
                                    jump class5
                            " Nah, don't want to disturb him. ":
                                " Alrighty. "
                                " Instead of walking up to him, you decided to roam around the rooftop for a bit. "
                                " After walking, you decided to look at the clouds. "
                                " You could see them forming into different cute shapes in the sky. "
                                " You used to always look at the clouds in the sky because of the little shapes they would make when you were younger. "
                                " You missed those days. The days where you don't really have anything to worry about. "
                                " But you can't turn back time. All you can do for now is just keep living life as it is. "
                                " Damn, how'd this got you thinking deep? "
                                " No clue, but uh... Atleast you get more narrator dialogue? "
                                scene black with dissolve
                                " You stayed at the rooftop for a bit, admiring the clouds. "
                                " You kinda just zoned out at some point. "
                                play sound "audio/bellring.mp3"
                                " But then you snapped back into reality once you heard the bell ring. "
                                " You went down the stairs to go back into the hallways so that you could help someone else. "
                                pause 2.0
                                jump class5
                    label bloomieback:
                        " Alright, let's go to the back of the school. "
                        scene black with dissolve
                        pause 2.0
                        scene paperschoolback with dissolve
                        " You walk to the back of the school, looking at all the greenery there was. "
                        " You then spot one of your fellow teachers just chilling and looking at her phone. "
                        " Should you walk up to her? "
                        menu:
                            " Yeah sure ":
                                " Alrighty. Let's talk with her. "
                                show missbloomieneutral at center with easeinright
                                if bloomieknow == True:
                                    " She's busy looking at her phone... "
                                    " You just stood next to her and waited for her to notice you. "
                                    msb " ... "
                                    msb " ...Hi, [name]. "
                                    msb " I heard you had your class earlier. "
                                    msb " How was it? "
                                    " You thought about your class from earlier... "
                                    if kind == True:
                                        " ...You told her that your class went well. "
                                        msb " That's good. "
                                    elif calm == True:
                                        " ...You told her that your class went well. "
                                        msb " That's good. "
                                    elif mean == True:
                                        " You told her that your class was a little annoying. "
                                        " You also told her that you had to yell at your class for them to pay attention. "
                                        msb " Good. You're gonna have to do that a lot here. "
                                    " You ask her what she was doing. "
                                    msb " Reminding my students to go do their homework. "
                                    msb " Sometimes they can get forgetful and they won't do their homework. "
                                    msb " Actually, I have a test tomorrow for them. "
                                    msb " I doubt that they would actually study, knowing how they are. "
                                    msb " Though, I know that SOME would atleast study. Like that Engel kid. "
                                    msb " He's a good one. Actually, he's a star student. "
                                    msb " He even sometimes likes to tutor some other students in his free time. "
                                    hide missbloomieneutral at bottom
                                    show missbloomiehappy at center
                                    msb " I like that kid. Always aces my quizzes. "
                                    " ...Look, you know that those are her horns, but you can't help but think that those are her cat ears. "
                                    " Just really, really enlongated cat ears. "
                                    hide missbloomiehappy at bottom
                                    show missbloomieneutral at center
                                    " Out of pure instinct, you started petting her. If she was a real cat, this would've been better. "
                                    msb " ... What are you doing ... "
                                    " Miss Bloomie seems to not enjoy it at first, but then... "
                                    hide missbloomieneutral at bottom
                                    show missbloomiehappy at center
                                    msb " ...:3 "
                                    " She starts liking it. Must've felt good for her. "
                                    " ...Wait, is she purring? "
                                    scene black with dissolve
                                    " You spent the entire break talking with Bloomie and petting her. "
                                    " This was honeslty heaven. For both you and Bloomie. "
                                    " She even felt like a cat, holy moly... "
                                    " You're starting to doubt that those were horns and starting to think that those are cat ears. In disguise. "
                                    " Even though they didn't feel like cat ears. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rings, preventing you from petting Miss Bloomie any further. "
                                    " Hesitant, you move your hand away from her head and you walk back into the school with Miss Bloomie. "
                                    pause 2.0
                                    jump class5
                                else:
                                    " She's busy looking at her phone... "
                                    " You just stood next to her and waited for her to notice you. "
                                    x " ... "
                                    x " ...Hi. "
                                    x " You're the new gardening teacher, yeah? "
                                    x " I don't think I've gotten to meet you before. "
                                    $ bloomieknow = True
                                    msb " I'm Miss Bloomie. I teach science. "
                                    msb " I also heard that you had your class earlier. "
                                    msb " How was it? "
                                    " You thought about your class from earlier... "
                                    if kind == True:
                                        " ...You told her that your class went well. "
                                        msb " That's good. "
                                    elif calm == True:
                                        " ...You told her that your class went well. "
                                        msb " That's good. "
                                    elif mean == True:
                                        " You told her that your class was a little annoying. "
                                        " You also told her that you had to yell at your class for them to pay attention. "
                                        msb " Good. You're gonna have to do that a lot here. "
                                    " You ask her what she was doing. "
                                    msb " Reminding my students to go do their homework. "
                                    msb " Sometimes they can get forgetful and they won't do their homework. "
                                    msb " Actually, I have a test tomorrow for them. "
                                    msb " I doubt that they would actually study, knowing how they are. "
                                    msb " Though, I know that SOME would atleast study. Like that Engel kid. "
                                    msb " He's a good one. Actually, he's a star student. "
                                    msb " He even sometimes likes to tutor some other students in his free time. "
                                    hide missbloomieneutral at bottom
                                    show missbloomiehappy at center
                                    msb " I like that kid. Always aces my quizzes. "
                                    " ...Look, you know that those are her horns, but you can't help but think that those are her cat ears. "
                                    " Just really, really enlongated cat ears. "
                                    hide missbloomiehappy at bottom
                                    show missbloomieneutral at center
                                    " Out of pure instinct, you started petting her. If she was a real cat, this would've been better. "
                                    msb " ... What are you doing ... "
                                    " Miss Bloomie seems to not enjoy it at first, but then... "
                                    hide missbloomieneutral at bottom
                                    show missbloomiehappy at center
                                    msb " ...:3 "
                                    " She starts liking it. Must've felt good for her. "
                                    " ...Wait, is she purring? "
                                    scene black with dissolve
                                    " You spent the entire break talking with Bloomie and petting her. "
                                    " This was honeslty heaven. For both you and Bloomie. "
                                    " She even felt like a cat, holy moly... "
                                    " You're starting to doubt that those were horns and starting to think that those are cat ears. In disguise. "
                                    " Even though they didn't feel like cat ears. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rings, preventing you from petting Miss Bloomie any further. "
                                    " Hesitant, you move your hand away from her head and you walk back into the school with Miss Bloomie. "
                                    pause 2.0
                                    jump class5
                            " Nah, don't want to disturb her. ":
                                " Alright. Let's just chill here then. "
                                scene black with dissolve
                                " You just relaxed at the back of the school. "
                                " You didn't really have anything else to do other than look at your phone or look at the green stuff around you. "
                                " You spent most of your time scrolling on tiktok though. "
                                " ...You didn't see anything interesting other than an AI wolf walk thing. "
                                " The internet is a little weird nowadays. The older times were golden. "
                                " But, that's just my opinion as the narrator. "
                                " If you just got mad at that opinion I just said this aint twitter man "
                                play sound "audio/bellring.mp3"
                                " The bell rings, and you walk back into the school quietly. "
                                pause 2.0
                                jump class5
                    label emilyfront:
                        " Alright, let's go to the front of the school. "
                        scene black with dissolve
                        pause 2.0
                        scene paperschoolfront with dissolve
                        " You walk around the front of the school, taking in the fresh air. "
                        " You walked around for a bit and spotted one of your fellow teachers sitting on one of the benches. "
                        " Do you want to talk to her? "
                        menu:
                            " Yeah sure ":
                                " Alrighty. Let's talk to her. "
                                show msemilyneutral at center with easeinleft
                                if emilyknow == True:
                                    " Emily seemed to be busy doing something on her phone. "
                                    " You waited until she noticed you. "
                                    pause 1.0
                                    " And after some time, she did, infact, notice you. "
                                    mse " Hi [name]! Sorry, I was just a little busy with my phone here, heh... "
                                    mse " Anyway, I heard that you had your first class earlier! "
                                    mse " How was it? Any problems? "
                                    " You thought about how your first class went... "
                                    if kind == True:
                                        " ...And you told her that it went fine, and there were no problems! "
                                        " You had fun, too! "
                                    elif calm == True:
                                        " ...And you told her that it went fine. "
                                        " You told her that the kids loved your humor! "
                                    elif mean == True:
                                        " ...And you told her that there were a few kids who couldn't pay attention. "
                                        " But, you still thought it went fine. "
                                    mse " Well, I'm glad that it went well for you! "
                                    mse " The kids for my class was surprisingly being attentive today... "
                                    mse " I find that odd because they don't usually pay as much attention as they do today. "
                                    mse " Wonder what happened... "
                                    mse " I didn't even have to yell at them once to pay attention! "
                                    mse " It's a nice change, yes, but I doubt that it'll happen again later or tomorrow. "
                                    mse " After all, there's just some students who are trouble makers... "
                                    mse " You just can't escape them! Kids will be kids, I suppose... "
                                    scene black with dissolve
                                    " You spent the rest of the break talking to Miss Emily. "
                                    " In all honesty, she seems like a fun teacher. But it's best not to get her grumpy. "
                                    " ...You think that there were multiple times she got mad all because her students weren't paying attention. "
                                    " And you think that there were multiple times where she wanted to quit. "
                                    " But, she remained standing. Still here, taking this one hell of a job she signed up for. "
                                    " It's impressive, but it's what you have to deal with when you're a teacher. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rings, and you stop talking with Miss Emily. "
                                    " You both then go back into the school, ready for the last class of the day. "
                                    pause 2.0
                                    jump class5
                                else:
                                    " Emily seemed to be busy doing something on her phone. "
                                    " You waited until she noticed you. "
                                    pause 1.0
                                    " And after some time, she did, infact, notice you. "
                                    x " Hi! Sorry, I was just a little busy with my phone here, heh... "
                                    x " You're the new gardening teacher, right? It's so good to meet you! "
                                    $ emilyknow = True
                                    mse " I'm Miss Emily! I teach history! "
                                    mse " Anyway, I heard that you had your first class earlier! "
                                    mse " How was it? Any problems? "
                                    " You thought about how your first class went... "
                                    if kind == True:
                                        " ...And you told her that it went fine, and there were no problems! "
                                        " You had fun, too! "
                                    elif calm == True:
                                        " ...And you told her that it went fine. "
                                        " You told her that the kids loved your humor! "
                                    elif mean == True:
                                        " ...And you told her that there were a few kids who couldn't pay attention. "
                                        " But, you still thought it went fine. "
                                    mse " Well, I'm glad that it went well for you! "
                                    mse " The kids for my class was surprisingly being attentive today... "
                                    mse " I find that odd because they don't usually pay as much attention as they do today. "
                                    mse " Wonder what happened... "
                                    mse " I didn't even have to yell at them once to pay attention! "
                                    mse " It's a nice change, yes, but I doubt that it'll happen again later or tomorrow. "
                                    mse " After all, there's just some students who are trouble makers... "
                                    mse " You just can't escape them! Kids will be kids, I suppose... "
                                    scene black with dissolve
                                    " You spent the rest of the break talking to Miss Emily. "
                                    " In all honesty, she seems like a fun teacher. But it's best not to get her grumpy. "
                                    " ...You think that there were multiple times she got mad all because her students weren't paying attention. "
                                    " And you think that there were multiple times where she wanted to quit. "
                                    " But, she remained standing. Still here, taking this one hell of a job she signed up for. "
                                    " It's impressive, but it's what you have to deal with when you're a teacher. "
                                    play sound "audio/bellring.mp3"
                                    " The bell rings, and you stop talking with Miss Emily. "
                                    " You both then go back into the school, ready for the last class of the day. "
                                    pause 2.0
                                    jump class5
                            " Nah, don't want to disturb her. ":
                                " Alright. I suppose we'll just relax here for a bit. "
                                " You seat down on a nearby bench and you pulled out your phone... "
                                " To have you atleast somewhat entertained, of course. "
                                scene black with dissolve
                                " You spent the rest of the break just chillaxing outside of the school. "
                                " Nothing really interesting happens while you're out there. "
                                " You check your phone, and seems like there's nothing interesting going on in any of the social media apps that you have. "
                                " Boring... "
                                play sound "audio/bellring.mp3"
                                " The bell rings, and you get up from your seat. "
                                " You put your phone back into your pocket and you go back into the school. "
                                pause 2.0
                                jump class5
                label class5:
                    scene hallway with dissolve
                    " Seems like it's gonna be the last classes for the day. "
                    " You're thinking of helping some teachers. "
                    " Who do you want to help? "
                    if circleknow,thavelknow,bloomieknow == True:
                        menu:
                            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                                jump circlehelpyeah
                            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                                jump thavelhelpyeah
                            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                                jump bloomiehelpyeah
                            " I'll just roam around instead. ":
                                jump roam5
                    elif circleknow,thavelknow == True and bloomieknow == False:
                        menu:
                            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                                jump circlehelpyeah
                            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                                jump thavelhelpyeah
                            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                                jump bloomiehelpyeah
                            " I'll just roam around instead. ":
                                jump roam5
                    elif thavelknow,bloomieknow == True and circleknow == False:
                        menu:
                            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                                jump circlehelpyeah
                            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                                jump thavelhelpyeah
                            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                                jump bloomiehelpyeah
                            " I'll just roam around instead. ":
                                jump roam5
                    elif circleknow,bloomieknow == True and thavelknow == False:
                        menu:
                            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                                jump circlehelpyeah
                            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                                jump thavelhelpyeah
                            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                                jump bloomiehelpyeah
                            " I'll just roam around instead. ":
                                jump roam5
                    elif circleknow == True and thavelknow,bloomieknow == False:
                        menu:
                            " {image=misscircleicon} Miss Circle {image=misscircleicon} ":
                                jump circlehelpyeah
                            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                                jump thavelhelpyeah
                            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                                jump bloomiehelpyeah
                            " I'll just roam around instead. ":
                                jump roam5
                    elif thavelknow == True and circleknow,bloomieknow == False:
                        menu:
                            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                                jump circlehelpyeah
                            " {image=missthavelicon} Miss Thavel {image=missthavelicon} ":
                                jump thavelhelpyeah
                            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                                jump bloomiehelpyeah
                            " I'll just roam around instead. ":
                                jump roam5
                    elif bloomieknow == True and circleknow,thavelknow == False:
                        menu:
                            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                                jump circlehelpyeah
                            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                                jump thavelhelpyeah
                            " {image=missbloomieicon} Miss Bloomie {image=missbloomieicon} ":
                                jump bloomiehelpyeah
                            " I'll just roam around instead. ":
                                jump roam5
                    else:
                        menu:
                            " {image=misscircleicon} The math teacher {image=misscircleicon} ":
                                jump circlehelpyeah
                            " {image=missthavelicon} The language teacher {image=missthavelicon} ":
                                jump thavelhelpyeah
                            " {image=missbloomieicon} The science teacher {image=missbloomieicon} ":
                                jump bloomiehelpyeah
                            " I'll just roam around instead. ":
                                jump roam5
                label circlehelpyeah:
                    if circleknow == True:
                        " Alright, let's go help Miss Circle then. "
                    else:
                        " Alright, let's go help the math teacher, then. "
                    scene black with dissolve
                    pause 2.0
                    scene classroom with dissolve
                    if circleknow == True:
                        " You enter Miss Circle's classroom, and it seems that she's busy teaching right now. "
                        " You aren't sure if she actually needs help or not. "
                        " But, then she comes up to you after a few minutes of you looking around. "
                        show misscircleneutral at center with easeinright
                        msc " Why, if it isn't [name]! "
                        msc " You came in at the right time, actually. I just need a bit of help. "
                        msc " I need you to make sure that my students actually understood the lesson I just taught them! "
                        " And what are we supposed to do...? "
                        msc " Ask them questions about what they learned in the lesson. "
                        msc " If they get it wrong, just correct them. "
                        msc " Not too hard, right? "
                        " You nodded, this was a pretty easy job, in all honesty... "
                        hide misscircleneutral at bottom
                        show misscirclehappy at center
                        msc " Thank you, [name]! "
                        msc " Hopefully asking for this much help doesn't bother you, eheh.. "
                        hide miscirclehappy at left with easeoutleft
                        " Alright, let's get started on helping other students. "
                        scene black with dissolve
                        " You spent the entire last period helping other students who were struggling. "
                        " You made sure that they fully understood the lesson and corrected them once they got something wrong. "
                        if kind == True:
                            " You were being kind and patient with them, because you knew that they would get the answer right in the end. "
                            " And if they don't? Well, stuff like that happens, and it's alright. "
                        elif calm == True:
                            " You were being nice and chill with them, because you're lowkey just a chill guy. "
                            " Everytime they got something wrong you'd say that they lost aura points until they got it right. "
                        elif mean == True:
                            " You were being a bit rude to them, but only to the ones that were being a bit annoying. Like that Oliver kid. "
                            " And the other kids? You were being calm with them. "
                            " What a good teacher you are! You totally aren't on the verge of throwing a slipper at one of the students! "
                        " To your surprise, some of the students actually got the answers correct to your questions in about 1-3 tries only. "
                        " But there was one kid who was struggling quite a bit. Two kids, actually. "
                        " You remember one having a leaf on his head, while the other had sock puppets on her hands. "
                        " They struggled for quite a bit to the point they had to stay back for a bit when class ended, but they eventually got it. "
                        " You were just that much of a chill guy. "
                        play sound "audio/bellring.mp3"
                        " Well, time to go home. "
                        pause 2.0
                        jump endday
                    else:
                        " You enter the math teacher's classroom, and it seems that she's busy teaching right now. "
                        " You aren't sure if she actually needs help or not. "
                        " But, then she comes up to you after a few minutes of you looking around. "
                        show misscircleneutral at center with easeinright
                        x " Why, if it isn't the new gardening teacher! "
                        $ circleknow = True
                        msc " I'm Miss Circle. I teach math class. "
                        msc " You came in at the right time, actually. I just need a bit of help. "
                        msc " I need you to make sure that my students actually understood the lesson I just taught them! "
                        " And what are we supposed to do...? "
                        msc " Ask them questions about what they learned in the lesson. "
                        msc " If they get it wrong, just correct them. "
                        msc " Not too hard, right? "
                        " You nodded, this was a pretty easy job, in all honesty... "
                        hide misscircleneutral at bottom
                        show misscirclehappy at center
                        msc " Thank you, [name]! "
                        msc " Hopefully asking for this much help doesn't bother you, eheh.. "
                        hide miscirclehappy at left with easeoutleft
                        " Alright, let's get started on helping other students. "
                        scene black with dissolve
                        " You spent the entire last period helping other students who were struggling. "
                        " You made sure that they fully understood the lesson and corrected them once they got something wrong. "
                        if kind == True:
                            " You were being kind and patient with them, because you knew that they would get the answer right in the end. "
                            " And if they don't? Well, stuff like that happens, and it's alright. "
                        elif calm == True:
                            " You were being nice and chill with them, because you're lowkey just a chill guy. "
                            " Everytime they got something wrong you'd say that they lost aura points until they got it right. "
                        elif mean == True:
                            " You were being a bit rude to them, but only to the ones that were being a bit annoying. Like that Oliver kid. "
                            " And the other kids? You were being calm with them. "
                            " What a good teacher you are! You totally aren't on the verge of throwing a slipper at one of the students! "
                        " To your surprise, some of the students actually got the answers correct to your questions in about 1-3 tries only. "
                        " But there was one kid who was struggling quite a bit. Two kids, actually. "
                        " You remember one having a leaf on his head, while the other had sock puppets on her hands. "
                        " They struggled for quite a bit to the point they had to stay back for a bit when class ended, but they eventually got it. "
                        " You were just that much of a chill guy. "
                        play sound "audio/bellring.mp3"
                        " Well, time to go home. "
                        pause 2.0
                        jump endday
                label thavelhelpyeah:
                    # help thavel in demonstrating a spanish sentence
                    if thavelknow == True:
                        " Alright, let's go help Miss Thavel, then. "
                    else:
                        " Alright, let's go help the language teacher, then. "
                    scene black with dissolve
                    pause 2.0
                    scene classroom with dissolve
                    if thavelknow == True:
                        " You enter the language classroom, and you immediately start hearing Miss Thavel speak in spanish. "
                        show msthravelneutral at center with easeinleft
                        mst " Ustedes, perras, no entienden lo que estoy diciendo ahora mismo, son perdedoras. "
                        " ...Yeah, you have absolutely no idea what she's saying. "
                        " Seems like the class doesn't understand what she's saying either. "
                        " She sighs, looking as if she just lost hope in humanity before she looked at you. "
                        mst " ...Oh, [name]! Hello. "
                        mst " Could you help me real quick? "
                        mst " We just need to have a conversation in spanish. "
                        " You thought about it for a moment... "
                        " ...Well, you do remember a few words from your spanish lessons on Duolingo. "
                        " It shouldn't be that hard. "
                        mst " Marvelous! Alright, children. Me and [mr] [name] here will have a nice conversation in spanish. "
                        mst " Listen closely! "
                        mst " Buenos días, idiota! "
                        " Buenos días, puta!! "
                        mst " ¿Qué tal tu día? Espero que no haya ido nada bien. "
                        " Mi día iba bien hasta que vi tu cara! "
                        mst " See, kids? "
                        " You were pretty sure that what you were saying wasn't nice at all. "
                        " But, oh well. Atleast the kids don't know. "
                        " ...Atleast. "
                        scene black with dissolve
                        " You then decided to stick around in the language classroom for the last period. "
                        " Just to make sure that everything was going well. "
                        " And just to make sure that no one starts doing stupid shit in the middle of class. "
                        " What a good teacher you are! "
                        play sound "audio/bellring.mp3"
                        " Well, seems like the last class is over. "
                        " Time to get out, and go back home. "
                        pause 2.0
                        jump endday
                    else:
                        " You enter the language classroom, and you immediately start hearing the teacher speak in spanish. "
                        show msthravelneutral at center with easeinleft
                        x " Ustedes, perras, no entienden lo que estoy diciendo ahora mismo, son perdedoras. "
                        " ...Yeah, you have absolutely no idea what she's saying. "
                        " Seems like the class doesn't understand what she's saying either. "
                        " She sighs, looking as if she just lost hope in humanity before she looked at you. "
                        x " ...Oh! Hello there, [fancy]. "
                        $ thavelknow = True
                        mst " I'm Miss Thavel, the language teacher. "
                        mst " If you don't mind, could you help me real quick? It'll only just take a few minutes. "
                        mst " We just need to have a conversation in spanish. "
                        " You thought about it for a moment... "
                        " ...Well, you do remember a few words from your spanish lessons on Duolingo. "
                        " It shouldn't be that hard. "
                        mst " Marvelous! Alright, children. Me and [mr] [name] here will have a nice conversation in spanish. "
                        mst " Listen closely! "
                        mst " Buenos días, idiota! "
                        " Buenos días, puta!! "
                        mst " ¿Qué tal tu día? Espero que no haya ido nada bien. "
                        " Mi día iba bien hasta que vi tu cara! "
                        mst " See, kids? "
                        " You were pretty sure that what you were saying wasn't nice at all. "
                        " But, oh well. Atleast the kids don't know. "
                        " ...Atleast. "
                        scene black with dissolve
                        " You then decided to stick around in the language classroom for the last period. "
                        " Just to make sure that everything was going well. "
                        " And just to make sure that no one starts doing stupid shit in the middle of class. "
                        " What a good teacher you are! "
                        play sound "audio/bellring.mp3"
                        " Well, seems like the last class is over. "
                        " Time to get out, and go back home. "
                        pause 2.0
                        jump endday
                label bloomiehelpyeah:
                    if bloomieknow == True:
                        " Alright, let's go help Miss Bloomie, then. "
                    else:
                        " Alright, let's go help the science teacher, then. "
                    scene black with dissolve
                    pause 2.0
                    scene classroom with dissolve
                    if bloomieknow == True:
                        " You enter the classroom, only to find that it was empty. "
                        " Seems like Miss Bloomie had ended the class early. "
                        " Though, you saw a lot of science stuff on all of the desks in the classroom. "
                        " Seems like the students were preparing for something, but turns out the teacher just ended the class. "
                        " You then spot Miss Bloomie cleaning things up, so you walk up to her. "
                        show missbloomieneutral at center with easeinright
                        msb " ...Hey. "
                        " Miss Bloomie was putting all of the science vials and other things to the side. "
                        " Obviously, she was putting them in a safe area so that they wouldn't break. These things were pretty expensive, from what you've heard at least. "
                        msb " I'm just cleaning things up. "
                        " You ask her if she wants you to help her. "
                        msb " ...Well, that would make things a little faster. Why not? "
                        " You nodded, then you started to put all of the things in their respective places. "
                        " The silence between you two were loud, but at the same time it was also comfortable. "
                        " Just helping your friend out, doing something to end the day faster... "
                        " It felt nice, in an odd way. "
                        " Look I know my grammar here is dying but bear with me here... "
                        " After a few more minutes of comfortable silence, you then ask her why she ended her class lately. "
                        msb " ... "
                        msb " I have somewhere important to go to. "
                        msb " I need to see someone important there. It's nothing serious, don't worry. "
                        " ...Mysterious. You know she won't tell you where she's going or who she's meeting up with, so you didn't bother to push further. "
                        " You just continued cleaning up to her, in comfortable silence. "
                        scene black with dissolve
                        " With your help, Miss Bloomie cleaned the classroom much faster. "
                        " She thanked you before she left in a hurry. "
                        play sound "audio/bellring.mp3"
                        " The bell then rang. Time to go home. "
                        pause 2.0
                        jump endday
                    else:
                        " You enter the classroom, only to find that it was empty. "
                        " Seems like the teacher had ended the class early. "
                        " Though, you saw a lot of science stuff on all of the desks in the classroom. "
                        " Seems like the students were preparing for something, but turns out the teacher just ended the class. "
                        " You then spot the science teacher cleaning things up, so you walk up to her. "
                        show missbloomieneutral at center with easeinright
                        x " ...Hey. "
                        " She was putting all of the science vials and other things to the side. "
                        " Obviously, she was putting them in a safe area so that they wouldn't break. These things were pretty expensive, from what you've heard at least. "
                        x " ...You must be the new gardening teacher, if I'm correct. "
                        x " It's nice to meet you. "
                        $ bloomieknow = True
                        msb " I'm Miss Bloomie. I teach science. "
                        " You told her that it was nice to meet her too, before you asked what she was doing. "
                        msb " I'm just cleaning things up. "
                        " You ask her if she wants you to help her. "
                        msb " ...Well, that would make things a little faster. Why not? "
                        " You nodded, then you started to put all of the things in their respective places. "
                        " The silence between you two were loud, but at the same time it was also comfortable. "
                        " Just helping your friend out, doing something to end the day faster... "
                        " It felt nice, in an odd way. "
                        " Look I know my grammar here is dying but bear with me here... "
                        " After a few more minutes of comfortable silence, you then ask her why she ended her class lately. "
                        msb " ... "
                        msb " I have somewhere important to go to. "
                        msb " I need to see someone important there. It's nothing serious, don't worry. "
                        " ...Mysterious. You know she won't tell you where she's going or who she's meeting up with, so you didn't bother to push further. "
                        " You just continued cleaning up to her, in comfortable silence. "
                        scene black with dissolve
                        " With your help, Miss Bloomie cleaned the classroom much faster. "
                        " She thanked you before she left in a hurry. "
                        play sound "audio/bellring.mp3"
                        " The bell then rang. Time to go home. "
                        pause 2.0
                        jump endday
                label roam5:
                    " You decided not to help any teachers and decided to roam around the school. "
                    " Not to slack off, but to check if there are any students who are skipping the last period. "
                    scene black with dissolve
                    " And in the end, you did spot students who were slacking off. "
                    " You took them to their respective classes and you went back to roaming the halls. "
                    " You spotted nothing interesting, that was until you saw a door. "
                    " A door that was labelled as 'Alice's room', and a sign not to enter. "
                    " You thought that it was odd, and you wondered who was Alice. "
                    " You even thought of entering the room after a few minutes of thinking... "
                    " ...But you eventually decided not to. "
                    " It does say not to enter it, so you're not going to. "
                    " You're just gonna have to go on with what you were doing earlier. And that is to check if anyone's slacking off. "
                    play sound "audio/bellring.mp3"
                    " The bell eventually rings, after an hour of you roaming the halls. "
                    " Seems like it's time to go home. "
                    pause 2.0
                    jump endday
                label endday:
                    scene gardenroom with dissolve
                    " You go back to your classroom so that you could pack up your things. "
                    " Before you pack up though, you've got to make sure that everything's nice and tidy for tomorrow. "
                    " You fix some of the plants positions, and you made sure that everything was clean. "
                    " You then started to pack up all of your things, like paperwork you had to do. "
                    " While you were doing this, you couldn't help but think that this day has been going a little bit too fast for your liking. "
                    " You don't even know how you yourself pointed it out that this day has been going fast, you just somehow did. "
                    " Time goes by fast, hm. "
                    " You were eventually done with packing things up, and you left your classroom. "
                    scene black with dissolve
                    pause 2.0
                    scene paperschoolfront with dissolve
                    " You step outside of the school, seeing students walking around and saying their goodbyes to eachother. "
                    " Some were still hanging around, just chilling. "
                    " Some students actually stopped by to greet you, they even gave you welcome gifts. "
                    " You thanked them. So far, these students were being nice to you. "
                    " You knew damn well that there were going to be a whole lot of trouble makers though. So you shouldn't get used to the kindness they gave you. "
                    " You then hopped into your car, driving back to your home. "
                    scene black with dissolve
                    stop music fadeout 0.5
                    pause 2.0
                    play music "audio/home.mp3" fadein 0.5
                    scene mcroom with dissolve
                    " Once you arrived home and changed out of your uniform, you immediately plopped down onto your bed. "
                    " This has been a long day, and you were completely exhausted. "
                    " Though, in your opinion... your experience here at Paper High has been good so far. "
                    " Your phone buzzes, you just got a new notification. "
                    " You checked your messaging app and turns out you got invited to a group chat filled with the teachers in paper high, including the principal. "
                    " The principal and the other teachers all welcomed you. "
                    " But, you were honestly too tired to respond, so all that you could do is just heart their messages before immediately going to sleep. "
                    scene black with dissolve
                    stop music fadeout 0.5
                    " ...Goodnight. "
                    pause 2.0
                    jump teachertuesday
