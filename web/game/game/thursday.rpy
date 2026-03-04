label thursday:
    show text " DAY 4 - THURSDAY "
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
    " Huh, looks like it's not time to go to class yet. "
    " Infact, you've got a whole 40 minutes just to hang out. "
    " You didn't know that you decided to come in early.. "
    " What should you do to pass the time? "
    if clairebeatup == True:
        menu:
            " Apologize to Claire ":
                $ clairesorry = True
                $ clairebeatup = False
                " It's time, that's why I gave you this option. "
                " Let's go ahead and do that. "
                " You look around to find the girl you were looking for... "
                " And eventually found her walking to her locker. "
                " With enough courage, you walked up to her. "
                show claireneutral at center with easeinright
                c " ...? "
                c " Oh, um. It's you. "
                c " ...You had something to tell me? "
                " You told her that you were sorry for all of the things you've done to her. "
                " You told her that you didn't mean it and you were just in a bad mood. "
                " The reason why you told her this only now was because you were afraid of how she would react. "
                " Afraid that you were seen as a bad person when you didn't mean to do the things you did. "
                " You told her that you were sorry, again. And you asked for forgiveness... "
                c " ... "
                c " Well, as long as you don't do it again... "
                c " ...Then I forgive you! "
                " You hoped that you didn't scare her too much. "
                c " You? scare me? "
                c " Silly, what're you talking about? "
                " You told her that you saw her being scared when you did what you did on monday. "
                " Was your vision tricking you at that time?? "
                c " Oh, no...I wasn't scared at all, actually! "
                c " I was just a little bit pissed that you were stomping on my books. "
                c " But not scared! "
                c " Must've been your eyes playing tricks on you, hm? "
                c " But anyway... "
                c " I'm glad that you said sorry for the things that you've done. "
                c " I don't really want our relationship to be foiled on the first day... "
                c " Let's be friends from now on, yeah? "
                " You nodded in agreement. "
                hide claireneutral at bottom
                show clairehappy at center
                c " Great! "
                hide clairehappy at bottom
                show claireneutral at center
                c " Let's get going to class now though. "
                c " Better to be early than be late! "
                c " I'll see you there, [name]! "
                hide claireneutral at left with easeinleft
                scene black with dissolve
                " You then went to your classroom for the first class. "
                pause 2.0
                jump mathclassthurs
            " Go to class early ":
                " Wow, boring. "
                " Let's go though. "
                " You have nothing interesting to do anyway. "
                scene black with dissolve
                pause 2.0
                jump mathclassthurs
    else:
        menu:
            " Go to class early ":
                " Wow, boring. "
                " Let's go though. "
                " You have nothing interesting to do anyway. "
                scene black with dissolve
                pause 2.0
                jump mathclassthurs
label mathclassthurs:
    scene classroom with dissolve
    " You sat down on your seat and waited for the teacher to arrive. "
    " It was taking her quite a bit to arrive... "
    " While you were waiting, you decided to draw in your notebook for a bit. "
    " You just drew a little stickman guy. Nothing too special. "
    " His name is going to be bob. "
    " Hi bob! "
    " The teacher eventually arrives, and you close your notebook as if you weren't doing anything. "
    show misscircleneutral at center with easeinright
    msc " Good morning, class! "
    msc " I hope all of you are doing well this morning. "
    msc " I know all of you are excited due to the fact that it's almost going to be the weekend... "
    msc " Though, you've still got to go through today and friday. "
    msc " Don't get too excited now! "
    msc " We've still got to talk about our lesson for today. "
    msc " Alright, so we're going to have to find X... "
    msc " And then we just... "
    scene black with dissolve
    " Your eyes feel droopy at the sound of math. "
    " Though, you try keeping yourself awake since you can't exactly slack off. "
    " Otherwise you're going to be absolutely cooked by the teachers. "
    " And you don't want that at the first week of being in the school at all. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for a break. "
    " You get up from your seat and you walked to the hallways. "
    " Time for your first break of the day... "
    pause 2.0
    jump thursbreak1

label thursbreak1:
    scene hallway with dissolve
    if oligangjoin == True:
        jump thursoligang1
    " Where do you want to go for this break? "
    menu:
        " {image=engelicon} The front of the school {image=robbyicon} ":
            jump thursfrontschool1
        " {image=rubyicon} The back of the school {image=rileyicon} ":
            jump thursbackschool1
        " {image=skellicon} The gym {image=lanaicon} ":
            jump thursgym1
        "  {image=popularicon} The cafeteria {image=cubbieicon} ":
            jump thurscafeteria1
        " {image=kevinicon} The rooftop {image=claireicon} ":
            jump thursrooftop1
        " {image=abbieicon} The library {image=bubbleicon} ":
            jump thurslibrary1

label thursfrontschool1:
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of the school and spotted two of your classmates talking with eachother. "
    " Wondering what they're talking about, you decided to join into their conversation. "
    " Let's see just what they're talking about today... "
    show engelneutral at left with easeinright
    show robbyneutral at right with easeinright
    if engelknow == True and robbyknow == True:
        rb " Look, Engel - I just think that if she'd calmed down for a moment... "
        rb " Then I could FINALLY have a breather. "
        e " Well, Robby... have you tried telling her to...politely, shut up? "
        hide robbyneutral at bottom
        show robbyangry at right
        rb " You have no idea just how many times I've tried doing that. "
        rb " But no matter what, it's always Oliver this, Oliver that... "
        rb " Can't I have some time to myself without having Oliver's name being thrown around?! "
        rb " I already know how 'great' he is, you don't need to keep blasting it in my ear! "
        e " Eeeyikes... "
        e " And you're saying that you want to find some way of telling her... "
        e " Telling her that she's being annoying - without hurting her? "
        hide robbyangry at bottom
        show robbyneutral at right
        rb " That's the thing. "
        rb " You see, whenever I say something bad about her, even if it's only a little bit bad... "
        rb " She's going to make a fuss over it for weeks. "
        rb " Always going to throw my words on my face just for being 'mean' to her. "
        rb " When really, I'm just out here trying to tell her the truth. "
        rb " And the truth is, I just want a normal conversation with her - "
        rb " - Without all the Oliver bullshit. "
        rb " It's getting really tiring having to deal with it, in all honesty. "
        rb " Every day? Oliver. Every afternoon? Oliver. Every night? Oliver. "
        rb " All of it is Oliver and I'm sick of it and tired. "
        e " Well... maybe you could, I dunno... "
        menu:
            " Tell her the truth ":
                $ robbrileylv += 10
                rb " Huh, what was that? "
                " You told him that he should just tell Riley the truth about how he really feels. "
                " Even if Riley is going to be upset about it, sometimes... "
                " ...You just need to tell them the truth to just make them understand. "
                hide engelneutral at bottom
                show engelcontent at left
                e " [name]'s got a point here, you know. "
                rb " And what if she doesn't understand? "
                " If she doesn't understand, you tell him that it's just gonna take her a bit to process. "
                " Just tell her that you didn't mean her any harm when you tell her the truth, "
                " And tell her how you really feel about talking with her. "
                rb " ...That actually doesn't sound like a bad idea. "
                rb " I'll have to talk to her about this later... "
                hide engelcontent at bottom
                show engelneutral at left
                e " And when do you plan on telling her? "
                rb " I dunno, maybe on the third break? "
                rb " Still gotta think of something to say, you know... "
                rb " So that I don't fumble up my words and everything... "
                rb " Things are gonna be real awkward if that happens. "
                e " Mhm. Best to think things out first before doing them. "
                rb " Yeah, well...Thanks for the help, you two. "
                scene black with dissolve
                " You spent the rest of the break talking with Robby and Engel. "
                " You didn't know Riley talked about Oliver so much to the point that even Robby's crashing out about it... "
                " Well, Riley's a fangirl. Of course she would talk about him a lot. "
                " But you weren't expecting Robby to even crash out about it. "
                " Very interesting information... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " Listen to Engel's idea ":
                $ engellv += 10
                e " ...Just talk to her about it? "
                rb " Uh. What. "
                e " Just tell her how you feel, Robby. "
                e " Even if Riley's going to be upset about it, "
                e " She has to know how you really feel. "
                e " You don't have to hold in your thoughts about how you feel everytime Riley talks about him. "
                e " In fact, that's just going to lead to worser things if you do that. "
                e " And if she doesn't understand the things you're saying - "
                e " - It's just going to take her a bit to process what you just said. "
                e " At first she'll think that you're spouting out nonsense, but after a bit... "
                e " She'll slowly start to understand, bit by bit. "
                e " And if she doesn't ever understand, then let's just say that she's a lost cause. "
                e " I don't mean to be mean but that's just really how I think of her... "
                rb " ...That actually doesn't sound like a bad idea. "
                rb " I'll have to talk to her about this later... "
                e " And when do you plan on telling her? "
                rb " I dunno, maybe on the third break? "
                rb " Still gotta think of something to say, you know... "
                rb " So that I don't fumble up my words and everything... "
                rb " Things are gonna be real awkward if that happens. "
                e " Mhm. Best to think things out first before doing them. "
                rb " Yeah, well...Thanks for the help, you two. "
                scene black with dissolve
                " You spent the rest of the break talking with Robby and Engel. "
                " You didn't know Riley talked about Oliver so much to the point that even Robby's crashing out about it... "
                " Well, Riley's a fangirl. Of course she would talk about him a lot. "
                " But you weren't expecting Robby to even crash out about it. "
                " Very interesting information... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
    elif engelknow == True and robbyknow == False:
        x " Look, Engel - I just think that if she'd calmed down for a moment... "
        x " Then I could FINALLY have a breather. "
        $ robbyknow = True
        e " Well, Robby... have you tried telling her to...politely, shut up? "
        hide robbyneutral at bottom
        show robbyangry at right
        rb " You have no idea just how many times I've tried doing that. "
        rb " But no matter what, it's always Oliver this, Oliver that... "
        rb " Can't I have some time to myself without having Oliver's name being thrown around?! "
        rb " I already know how 'great' he is, you don't need to keep blasting it in my ear! "
        e " Eeeyikes... "
        e " And you're saying that you want to find some way of telling her... "
        e " Telling her that she's being annoying - without hurting her? "
        hide robbyangry at bottom
        show robbyneutral at right
        rb " That's the thing. "
        rb " You see, whenever I say something bad about her, even if it's only a little bit bad... "
        rb " She's going to make a fuss over it for weeks. "
        rb " Always going to throw my words on my face just for being 'mean' to her. "
        rb " When really, I'm just out here trying to tell her the truth. "
        rb " And the truth is, I just want a normal conversation with her - "
        rb " - Without all the Oliver bullshit. "
        rb " It's getting really tiring having to deal with it, in all honesty. "
        rb " Every day? Oliver. Every afternoon? Oliver. Every night? Oliver. "
        rb " All of it is Oliver and I'm sick of it and tired. "
        e " Well... maybe you could, I dunno... "
        menu:
            " Tell her the truth ":
                $ robbrileylv += 10
                rb " Huh, what was that? "
                " You told him that he should just tell Riley the truth about how he really feels. "
                " Even if Riley is going to be upset about it, sometimes... "
                " ...You just need to tell them the truth to just make them understand. "
                hide engelneutral at bottom
                show engelcontent at left
                e " [name]'s got a point here, you know. "
                rb " And what if she doesn't understand? "
                " If she doesn't understand, you tell him that it's just gonna take her a bit to process. "
                " Just tell her that you didn't mean her any harm when you tell her the truth, "
                " And tell her how you really feel about talking with her. "
                rb " ...That actually doesn't sound like a bad idea. "
                rb " I'll have to talk to her about this later... "
                hide engelcontent at bottom
                show engelneutral at left
                e " And when do you plan on telling her? "
                rb " I dunno, maybe on the third break? "
                rb " Still gotta think of something to say, you know... "
                rb " So that I don't fumble up my words and everything... "
                rb " Things are gonna be real awkward if that happens. "
                e " Mhm. Best to think things out first before doing them. "
                rb " Yeah, well...Thanks for the help, you two. "
                scene black with dissolve
                " You spent the rest of the break talking with Robby and Engel. "
                " You didn't know Riley talked about Oliver so much to the point that even Robby's crashing out about it... "
                " Well, Riley's a fangirl. Of course she would talk about him a lot. "
                " But you weren't expecting Robby to even crash out about it. "
                " Very interesting information... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " Listen to Engel's idea ":
                $ engellv += 10
                e " ...Just talk to her about it? "
                rb " Uh. What. "
                e " Just tell her how you feel, Robby. "
                e " Even if Riley's going to be upset about it, "
                e " She has to know how you really feel. "
                e " You don't have to hold in your thoughts about how you feel everytime Riley talks about him. "
                e " In fact, that's just going to lead to worser things if you do that. "
                e " And if she doesn't understand the things you're saying - "
                e " - It's just going to take her a bit to process what you just said. "
                e " At first she'll think that you're spouting out nonsense, but after a bit... "
                e " She'll slowly start to understand, bit by bit. "
                e " And if she doesn't ever understand, then let's just say that she's a lost cause. "
                e " I don't mean to be mean but that's just really how I think of her... "
                rb " ...That actually doesn't sound like a bad idea. "
                rb " I'll have to talk to her about this later... "
                e " And when do you plan on telling her? "
                rb " I dunno, maybe on the third break? "
                rb " Still gotta think of something to say, you know... "
                rb " So that I don't fumble up my words and everything... "
                rb " Things are gonna be real awkward if that happens. "
                e " Mhm. Best to think things out first before doing them. "
                rb " Yeah, well...Thanks for the help, you two. "
                scene black with dissolve
                " You spent the rest of the break talking with Robby and Engel. "
                " You didn't know Riley talked about Oliver so much to the point that even Robby's crashing out about it... "
                " Well, Riley's a fangirl. Of course she would talk about him a lot. "
                " But you weren't expecting Robby to even crash out about it. "
                " Very interesting information... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
    elif engelknow == False and robbyknow == True:
        rb " Look, Engel - I just think that if she'd calmed down for a moment... "
        $ engelknow = True
        rb " Then I could FINALLY have a breather. "
        e " Well, Robby... have you tried telling her to...politely, shut up? "
        hide robbyneutral at bottom
        show robbyangry at right
        rb " You have no idea just how many times I've tried doing that. "
        rb " But no matter what, it's always Oliver this, Oliver that... "
        rb " Can't I have some time to myself without having Oliver's name being thrown around?! "
        rb " I already know how 'great' he is, you don't need to keep blasting it in my ear! "
        e " Eeeyikes... "
        e " And you're saying that you want to find some way of telling her... "
        e " Telling her that she's being annoying - without hurting her? "
        hide robbyangry at bottom
        show robbyneutral at right
        rb " That's the thing. "
        rb " You see, whenever I say something bad about her, even if it's only a little bit bad... "
        rb " She's going to make a fuss over it for weeks. "
        rb " Always going to throw my words on my face just for being 'mean' to her. "
        rb " When really, I'm just out here trying to tell her the truth. "
        rb " And the truth is, I just want a normal conversation with her - "
        rb " - Without all the Oliver bullshit. "
        rb " It's getting really tiring having to deal with it, in all honesty. "
        rb " Every day? Oliver. Every afternoon? Oliver. Every night? Oliver. "
        rb " All of it is Oliver and I'm sick of it and tired. "
        e " Well... maybe you could, I dunno... "
        menu:
            " Tell her the truth ":
                $ robbrileylv += 10
                rb " Huh, what was that? "
                " You told him that he should just tell Riley the truth about how he really feels. "
                " Even if Riley is going to be upset about it, sometimes... "
                " ...You just need to tell them the truth to just make them understand. "
                hide engelneutral at bottom
                show engelcontent at left
                e " [name]'s got a point here, you know. "
                rb " And what if she doesn't understand? "
                " If she doesn't understand, you tell him that it's just gonna take her a bit to process. "
                " Just tell her that you didn't mean her any harm when you tell her the truth, "
                " And tell her how you really feel about talking with her. "
                rb " ...That actually doesn't sound like a bad idea. "
                rb " I'll have to talk to her about this later... "
                hide engelcontent at bottom
                show engelneutral at left
                e " And when do you plan on telling her? "
                rb " I dunno, maybe on the third break? "
                rb " Still gotta think of something to say, you know... "
                rb " So that I don't fumble up my words and everything... "
                rb " Things are gonna be real awkward if that happens. "
                e " Mhm. Best to think things out first before doing them. "
                rb " Yeah, well...Thanks for the help, you two. "
                scene black with dissolve
                " You spent the rest of the break talking with Robby and Engel. "
                " You didn't know Riley talked about Oliver so much to the point that even Robby's crashing out about it... "
                " Well, Riley's a fangirl. Of course she would talk about him a lot. "
                " But you weren't expecting Robby to even crash out about it. "
                " Very interesting information... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " Listen to Engel's idea ":
                $ engellv += 10
                e " ...Just talk to her about it? "
                rb " Uh. What. "
                e " Just tell her how you feel, Robby. "
                e " Even if Riley's going to be upset about it, "
                e " She has to know how you really feel. "
                e " You don't have to hold in your thoughts about how you feel everytime Riley talks about him. "
                e " In fact, that's just going to lead to worser things if you do that. "
                e " And if she doesn't understand the things you're saying - "
                e " - It's just going to take her a bit to process what you just said. "
                e " At first she'll think that you're spouting out nonsense, but after a bit... "
                e " She'll slowly start to understand, bit by bit. "
                e " And if she doesn't ever understand, then let's just say that she's a lost cause. "
                e " I don't mean to be mean but that's just really how I think of her... "
                rb " ...That actually doesn't sound like a bad idea. "
                rb " I'll have to talk to her about this later... "
                e " And when do you plan on telling her? "
                rb " I dunno, maybe on the third break? "
                rb " Still gotta think of something to say, you know... "
                rb " So that I don't fumble up my words and everything... "
                rb " Things are gonna be real awkward if that happens. "
                e " Mhm. Best to think things out first before doing them. "
                rb " Yeah, well...Thanks for the help, you two. "
                scene black with dissolve
                " You spent the rest of the break talking with Robby and Engel. "
                " You didn't know Riley talked about Oliver so much to the point that even Robby's crashing out about it... "
                " Well, Riley's a fangirl. Of course she would talk about him a lot. "
                " But you weren't expecting Robby to even crash out about it. "
                " Very interesting information... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
    else:
        x " Look, Engel - I just think that if she'd calmed down for a moment... "
        x " Then I could FINALLY have a breather. "
        $ engelknow = True
        $ robbyknow = True
        e " Well, Robby... have you tried telling her to...politely, shut up? "
        hide robbyneutral at bottom
        show robbyangry at right
        rb " You have no idea just how many times I've tried doing that. "
        rb " But no matter what, it's always Oliver this, Oliver that... "
        rb " Can't I have some time to myself without having Oliver's name being thrown around?! "
        rb " I already know how 'great' he is, you don't need to keep blasting it in my ear! "
        e " Eeeyikes... "
        e " And you're saying that you want to find some way of telling her... "
        e " Telling her that she's being annoying - without hurting her? "
        hide robbyangry at bottom
        show robbyneutral at right
        rb " That's the thing. "
        rb " You see, whenever I say something bad about her, even if it's only a little bit bad... "
        rb " She's going to make a fuss over it for weeks. "
        rb " Always going to throw my words on my face just for being 'mean' to her. "
        rb " When really, I'm just out here trying to tell her the truth. "
        rb " And the truth is, I just want a normal conversation with her - "
        rb " - Without all the Oliver bullshit. "
        rb " It's getting really tiring having to deal with it, in all honesty. "
        rb " Every day? Oliver. Every afternoon? Oliver. Every night? Oliver. "
        rb " All of it is Oliver and I'm sick of it and tired. "
        e " Well... maybe you could, I dunno... "
        menu:
            " Tell her the truth ":
                $ robbrileylv += 10
                rb " Huh, what was that? "
                " You told him that he should just tell Riley the truth about how he really feels. "
                " Even if Riley is going to be upset about it, sometimes... "
                " ...You just need to tell them the truth to just make them understand. "
                hide engelneutral at bottom
                show engelcontent at left
                e " [name]'s got a point here, you know. "
                rb " And what if she doesn't understand? "
                " If she doesn't understand, you tell him that it's just gonna take her a bit to process. "
                " Just tell her that you didn't mean her any harm when you tell her the truth, "
                " And tell her how you really feel about talking with her. "
                rb " ...That actually doesn't sound like a bad idea. "
                rb " I'll have to talk to her about this later... "
                hide engelcontent at bottom
                show engelneutral at left
                e " And when do you plan on telling her? "
                rb " I dunno, maybe on the third break? "
                rb " Still gotta think of something to say, you know... "
                rb " So that I don't fumble up my words and everything... "
                rb " Things are gonna be real awkward if that happens. "
                e " Mhm. Best to think things out first before doing them. "
                rb " Yeah, well...Thanks for the help, you two. "
                scene black with dissolve
                " You spent the rest of the break talking with Robby and Engel. "
                " You didn't know Riley talked about Oliver so much to the point that even Robby's crashing out about it... "
                " Well, Riley's a fangirl. Of course she would talk about him a lot. "
                " But you weren't expecting Robby to even crash out about it. "
                " Very interesting information... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " Listen to Engel's idea ":
                $ engellv += 10
                e " ...Just talk to her about it? "
                rb " Uh. What. "
                e " Just tell her how you feel, Robby. "
                e " Even if Riley's going to be upset about it, "
                e " She has to know how you really feel. "
                e " You don't have to hold in your thoughts about how you feel everytime Riley talks about him. "
                e " In fact, that's just going to lead to worser things if you do that. "
                e " And if she doesn't understand the things you're saying - "
                e " - It's just going to take her a bit to process what you just said. "
                e " At first she'll think that you're spouting out nonsense, but after a bit... "
                e " She'll slowly start to understand, bit by bit. "
                e " And if she doesn't ever understand, then let's just say that she's a lost cause. "
                e " I don't mean to be mean but that's just really how I think of her... "
                rb " ...That actually doesn't sound like a bad idea. "
                rb " I'll have to talk to her about this later... "
                e " And when do you plan on telling her? "
                rb " I dunno, maybe on the third break? "
                rb " Still gotta think of something to say, you know... "
                rb " So that I don't fumble up my words and everything... "
                rb " Things are gonna be real awkward if that happens. "
                e " Mhm. Best to think things out first before doing them. "
                rb " Yeah, well...Thanks for the help, you two. "
                scene black with dissolve
                " You spent the rest of the break talking with Robby and Engel. "
                " You didn't know Riley talked about Oliver so much to the point that even Robby's crashing out about it... "
                " Well, Riley's a fangirl. Of course she would talk about him a lot. "
                " But you weren't expecting Robby to even crash out about it. "
                " Very interesting information... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
label thursbackschool1:
    # ruby and riley
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school and found two of your classmates talking with eachother. "
    " Wondering what they're talking about, you decided to join their conversation. "
    show rubyneutral at right with easeinleft
    show rileyneutral at left with easeinleft
    if rubyknow == True and rileyknow == True:
        ru " Heya [name]! "
        ru " Have you seen Robby anywhere? "
        ru " My friend Riley over here has been looking for him... "
        " You shrug, not knowing where the person mentioned was. "
        " You then asked Ruby why she was looking for Robby. "
        hide rileyneutral at bottom
        show rileyhappy at left
        ri " It's cause I have something new to make for Oliver! "
        ri " Now, I know nothing about machinery... "
        ri " Soooo, why not make Robby do it for me? "
        ri " He likes to make stuff for fun! "
        ri " So it SHOULD be a good idea to make him make something for Oliver! "
        ri " I call it...the Olibot! "
        ru " Wow...interesting! "
        ru " So what's it gonna do? "
        hide rileyhappy at bottom
        show rileyneutral at left
        ri " Well, for an example... "
        ri " It's going to generate out random prank ideas for Oliver! "
        ri " Just so that they don't have to struggle with coming up on their own pranks! "
        ri " It's great, right? And not only that... "
        ri " It can also be a bar of soap dispenser! "
        ri " I dunno how Robby's going to make that work, but I know Oliver loves soap! "
        ri " It would only be right to add that in, right? "
        ru " Mhm! Uh, wait.. "
        ru " I just got a notification from Robby. "
        ru " Give me a moment... "
        " Ruby looks at her phone for a moment... "
        hide rubyneutral at bottom
        show rubysad at right
        " ...She doesn't look pleased at what she's seeing. "
        hide rubysad at bottom
        show rubyneutral at right
        " She then immediately changes her expression once she puts her phone back. "
        ru " You know what, I don't think Robby's in the mood to make things right now! "
        ru " He said he isn't feeling well today, Riley. "
        hide rileyneutral at bottom
        show rileysad at left
        ri " Huh...? Why...? "
        ri " I was even planning to give that gift to Oliver today... "
        ru " Well, let's just say that Robby just needs a break from making things. "
        ru " You know artists getting artblock, right? "
        ru " Basically that with Robby. You're just going to have to wait. "
        ri " Okay... "
        ru " (Psst...[name]!) "
        ru " (I'm gonna whisper this to you to not hurt Riley, but...) "
        ru " (Could you promise not to tell this to her right now?) "
        ru " (Apparently, Robby doesn't want to deal with Riley right now because...) "
        ru " (He's honestly tired of her talking about Oliver and just needs time to think.) "
        ru " (Do you think you can promise to keep this a secret?) "
        menu:
            " my lips are sealed ":
                $ rubylv += 10
                hide rubyneutral at bottom
                show rubyhappy at right
                ru " (Thank you, [name]!) "
                ru " (I really appreciate it...) "
                ru " (And I'm sure that Robby's going to appreciate it too.) "
                ru " (Thanks again for your cooperation!) "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Riley. "
                " Olibot sounds like a pretty nice name... "
                " Maybe they should've gone for Botliver? "
                " No, that sounds really weird. A robots liver... "
                " Robots don't even have livers, but it still sounds weird. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " i can try i guess ":
                $ rubylv += 5
                hide rubyneutral at bottom
                show rubyhappy at right
                ru " (Thank you, [name]!) "
                ru " (I really appreciate it...) "
                ru " (And I'm sure that Robby's going to appreciate it too.) "
                ru " (Thanks again for your cooperation!) "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Riley. "
                " Olibot sounds like a pretty nice name... "
                " Maybe they should've gone for Botliver? "
                " No, that sounds really weird. A robots liver... "
                " Robots don't even have livers, but it still sounds weird. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
    elif rubyknow == True and rileyknow == False:
        ru " Heya [name]! "
        ru " Have you seen Robby anywhere? "
        $ rileyknow = True
        ru " My friend Riley over here has been looking for him... "
        " You shrug, not knowing where the person mentioned was. "
        " You then asked Ruby why she was looking for Robby. "
        hide rileyneutral at bottom
        show rileyhappy at left
        ri " It's cause I have something new to make for Oliver! "
        ri " Now, I know nothing about machinery... "
        ri " Soooo, why not make Robby do it for me? "
        ri " He likes to make stuff for fun! "
        ri " So it SHOULD be a good idea to make him make something for Oliver! "
        ri " I call it...the Olibot! "
        ru " Wow...interesting! "
        ru " So what's it gonna do? "
        hide rileyhappy at bottom
        show rileyneutral at left
        ri " Well, for an example... "
        ri " It's going to generate out random prank ideas for Oliver! "
        ri " Just so that they don't have to struggle with coming up on their own pranks! "
        ri " It's great, right? And not only that... "
        ri " It can also be a bar of soap dispenser! "
        ri " I dunno how Robby's going to make that work, but I know Oliver loves soap! "
        ri " It would only be right to add that in, right? "
        ru " Mhm! Uh, wait.. "
        ru " I just got a notification from Robby. "
        ru " Give me a moment... "
        " Ruby looks at her phone for a moment... "
        hide rubyneutral at bottom
        show rubysad at right
        " ...She doesn't look pleased at what she's seeing. "
        hide rubysad at bottom
        show rubyneutral at right
        " She then immediately changes her expression once she puts her phone back. "
        ru " You know what, I don't think Robby's in the mood to make things right now! "
        ru " He said he isn't feeling well today, Riley. "
        hide rileyneutral at bottom
        show rileysad at left
        ri " Huh...? Why...? "
        ri " I was even planning to give that gift to Oliver today... "
        ru " Well, let's just say that Robby just needs a break from making things. "
        ru " You know artists getting artblock, right? "
        ru " Basically that with Robby. You're just going to have to wait. "
        ri " Okay... "
        ru " (Psst...[name]!) "
        ru " (I'm gonna whisper this to you to not hurt Riley, but...) "
        ru " (Could you promise not to tell this to her right now?) "
        ru " (Apparently, Robby doesn't want to deal with Riley right now because...) "
        ru " (He's honestly tired of her talking about Oliver and just needs time to think.) "
        ru " (Do you think you can promise to keep this a secret?) "
        menu:
            " my lips are sealed ":
                $ rubylv += 10
                hide rubyneutral at bottom
                show rubyhappy at right
                ru " (Thank you, [name]!) "
                ru " (I really appreciate it...) "
                ru " (And I'm sure that Robby's going to appreciate it too.) "
                ru " (Thanks again for your cooperation!) "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Riley. "
                " Olibot sounds like a pretty nice name... "
                " Maybe they should've gone for Botliver? "
                " No, that sounds really weird. A robots liver... "
                " Robots don't even have livers, but it still sounds weird. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " i can try i guess ":
                $ rubylv += 5
                hide rubyneutral at bottom
                show rubyhappy at right
                ru " (Thank you, [name]!) "
                ru " (I really appreciate it...) "
                ru " (And I'm sure that Robby's going to appreciate it too.) "
                ru " (Thanks again for your cooperation!) "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Riley. "
                " Olibot sounds like a pretty nice name... "
                " Maybe they should've gone for Botliver? "
                " No, that sounds really weird. A robots liver... "
                " Robots don't even have livers, but it still sounds weird. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
    elif rubyknow == False and rileyknow == True:
        x " Heya [name]! "
        $ rubyknow = True
        ru " Before I say anything - I'm Ruby, nice to meet you! "
        ru " Anyways, have you seen Robby anywhere? "
        ru " My friend Riley over here has been looking for him... "
        " You shrug, not knowing where the person mentioned was. "
        " You then asked Ruby why she was looking for Robby. "
        hide rileyneutral at bottom
        show rileyhappy at left
        ri " It's cause I have something new to make for Oliver! "
        ri " Now, I know nothing about machinery... "
        ri " Soooo, why not make Robby do it for me? "
        ri " He likes to make stuff for fun! "
        ri " So it SHOULD be a good idea to make him make something for Oliver! "
        ri " I call it...the Olibot! "
        ru " Wow...interesting! "
        ru " So what's it gonna do? "
        hide rileyhappy at bottom
        show rileyneutral at left
        ri " Well, for an example... "
        ri " It's going to generate out random prank ideas for Oliver! "
        ri " Just so that they don't have to struggle with coming up on their own pranks! "
        ri " It's great, right? And not only that... "
        ri " It can also be a bar of soap dispenser! "
        ri " I dunno how Robby's going to make that work, but I know Oliver loves soap! "
        ri " It would only be right to add that in, right? "
        ru " Mhm! Uh, wait.. "
        ru " I just got a notification from Robby. "
        ru " Give me a moment... "
        " Ruby looks at her phone for a moment... "
        hide rubyneutral at bottom
        show rubysad at right
        " ...She doesn't look pleased at what she's seeing. "
        hide rubysad at bottom
        show rubyneutral at right
        " She then immediately changes her expression once she puts her phone back. "
        ru " You know what, I don't think Robby's in the mood to make things right now! "
        ru " He said he isn't feeling well today, Riley. "
        hide rileyneutral at bottom
        show rileysad at left
        ri " Huh...? Why...? "
        ri " I was even planning to give that gift to Oliver today... "
        ru " Well, let's just say that Robby just needs a break from making things. "
        ru " You know artists getting artblock, right? "
        ru " Basically that with Robby. You're just going to have to wait. "
        ri " Okay... "
        ru " (Psst...[name]!) "
        ru " (I'm gonna whisper this to you to not hurt Riley, but...) "
        ru " (Could you promise not to tell this to her right now?) "
        ru " (Apparently, Robby doesn't want to deal with Riley right now because...) "
        ru " (He's honestly tired of her talking about Oliver and just needs time to think.) "
        ru " (Do you think you can promise to keep this a secret?) "
        menu:
            " my lips are sealed ":
                $ rubylv += 10
                hide rubyneutral at bottom
                show rubyhappy at right
                ru " (Thank you, [name]!) "
                ru " (I really appreciate it...) "
                ru " (And I'm sure that Robby's going to appreciate it too.) "
                ru " (Thanks again for your cooperation!) "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Riley. "
                " Olibot sounds like a pretty nice name... "
                " Maybe they should've gone for Botliver? "
                " No, that sounds really weird. A robots liver... "
                " Robots don't even have livers, but it still sounds weird. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " i can try i guess ":
                $ rubylv += 5
                hide rubyneutral at bottom
                show rubyhappy at right
                ru " (Thank you, [name]!) "
                ru " (I really appreciate it...) "
                ru " (And I'm sure that Robby's going to appreciate it too.) "
                ru " (Thanks again for your cooperation!) "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Riley. "
                " Olibot sounds like a pretty nice name... "
                " Maybe they should've gone for Botliver? "
                " No, that sounds really weird. A robots liver... "
                " Robots don't even have livers, but it still sounds weird. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
    else:
        x " Heya [name]! "
        $ rubyknow = True
        $ rileyknow = True
        ru " Before I say anything - I'm Ruby, nice to meet you! "
        ru " Anyways, have you seen Robby anywhere? "
        ru " My friend Riley over here has been looking for him... "
        " You shrug, not knowing where the person mentioned was. "
        " You then asked Ruby why she was looking for Robby. "
        hide rileyneutral at bottom
        show rileyhappy at left
        ri " It's cause I have something new to make for Oliver! "
        ri " Now, I know nothing about machinery... "
        ri " Soooo, why not make Robby do it for me? "
        ri " He likes to make stuff for fun! "
        ri " So it SHOULD be a good idea to make him make something for Oliver! "
        ri " I call it...the Olibot! "
        ru " Wow...interesting! "
        ru " So what's it gonna do? "
        hide rileyhappy at bottom
        show rileyneutral at left
        ri " Well, for an example... "
        ri " It's going to generate out random prank ideas for Oliver! "
        ri " Just so that they don't have to struggle with coming up on their own pranks! "
        ri " It's great, right? And not only that... "
        ri " It can also be a bar of soap dispenser! "
        ri " I dunno how Robby's going to make that work, but I know Oliver loves soap! "
        ri " It would only be right to add that in, right? "
        ru " Mhm! Uh, wait.. "
        ru " I just got a notification from Robby. "
        ru " Give me a moment... "
        " Ruby looks at her phone for a moment... "
        hide rubyneutral at bottom
        show rubysad at right
        " ...She doesn't look pleased at what she's seeing. "
        hide rubysad at bottom
        show rubyneutral at right
        " She then immediately changes her expression once she puts her phone back. "
        ru " You know what, I don't think Robby's in the mood to make things right now! "
        ru " He said he isn't feeling well today, Riley. "
        hide rileyneutral at bottom
        show rileysad at left
        ri " Huh...? Why...? "
        ri " I was even planning to give that gift to Oliver today... "
        ru " Well, let's just say that Robby just needs a break from making things. "
        ru " You know artists getting artblock, right? "
        ru " Basically that with Robby. You're just going to have to wait. "
        ri " Okay... "
        ru " (Psst...[name]!) "
        ru " (I'm gonna whisper this to you to not hurt Riley, but...) "
        ru " (Could you promise not to tell this to her right now?) "
        ru " (Apparently, Robby doesn't want to deal with Riley right now because...) "
        ru " (He's honestly tired of her talking about Oliver and just needs time to think.) "
        ru " (Do you think you can promise to keep this a secret?) "
        menu:
            " my lips are sealed ":
                $ rubylv += 10
                hide rubyneutral at bottom
                show rubyhappy at right
                ru " (Thank you, [name]!) "
                ru " (I really appreciate it...) "
                ru " (And I'm sure that Robby's going to appreciate it too.) "
                ru " (Thanks again for your cooperation!) "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Riley. "
                " Olibot sounds like a pretty nice name... "
                " Maybe they should've gone for Botliver? "
                " No, that sounds really weird. A robots liver... "
                " Robots don't even have livers, but it still sounds weird. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " i can try i guess ":
                $ rubylv += 5
                hide rubyneutral at bottom
                show rubyhappy at right
                ru " (Thank you, [name]!) "
                ru " (I really appreciate it...) "
                ru " (And I'm sure that Robby's going to appreciate it too.) "
                ru " (Thanks again for your cooperation!) "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Riley. "
                " Olibot sounds like a pretty nice name... "
                " Maybe they should've gone for Botliver? "
                " No, that sounds really weird. A robots liver... "
                " Robots don't even have livers, but it still sounds weird. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump languageclassthurs
label thursgym1:
    # skell and lana
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked to the gym and spotted two of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if skellknow == True and lanaknow == True:
        menu:
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump sigmagirl
            " {image=skellicon} Skell {image=skellicon} ":
                jump skibidiboyles
    elif skellknow == True and lanaknow == False:
        menu:
            " {image=lanaicon} A girl with sock puppets for hands {image=lanaicon} ":
                jump sigmagirl
            " {image=skellicon} Skell {image=skellicon} ":
                jump skibidiboyles
    elif skellknow == False and lanaknow == True:
        menu:
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump sigmagirl
            " {image=skellicon} An emo boy {image=skellicon} ":
                jump skibidiboyles
    else:
        menu:
            " {image=lanaicon} A girl with sock puppets for hands {image=lanaicon} ":
                jump sigmagirl
            " {image=skellicon} An emo boy {image=skellicon} ":
                jump skibidiboyles
    label sigmagirl:
        show lananeutral at center with easeinleft
        if lanaknow == True:
            l " Hmm...what else can I do today? "
            l " I could go ahead and walk around the school... "
            l " ...But then again, nothing interesting is probably going on... "
            l " And Abbie's been really busy lately... "
            l " Hmhmmm... "
            " Lana looks around before noticing you being there. "
            hide lananeutral at bottom
            show lanahappy at center
            l " [name]!! It's real nice to see you!! "
            l " I was just thinking of what I should do! "
            hide lanahappy at bottom
            show lananeutral at center
            l " What I should do for the break, of course. "
            l " I have absolutely no idea what I could do this time! "
            l " I mean, I could go ahead and make some new ocs... "
            l " But I already have a lot of them! "
            l " I mean, there's nothing wrong with having too many ocs, buuuut... "
            l " I don't really have any ideas for making a new one. "
            l " I could make a new sock puppet, but honestly... "
            l " My socks are starting to run out a bit and  I can't really buy another pair of socks. "
            l " I only have a bit as my daily allowance, after all! "
            l " Or, maybe I could.. "
            menu:
                " Continue your story of Juliana and Pedro " if lanalv >= 15 or lanalv == 15:
                    $ lanalv += 10
                    l " Wait, Juliana and Pedro? "
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " I can't believe I forgot about them, ohhh my heavens! "
                    l " Thank you for reminding me of them, [name]! "
                    l " I'll come up with something real quick, hold on... "
                    hide lanahappy at bottom
                    show lananeutral at center
                    " Lana thinks for a good bit with the plot... "
                    " And then she finally has an idea! "
                    l " Alright, the last time we talked about them - "
                    l " Pedro was hanging out with Rainier, right? "
                    l " And Juliana just found out about them, hmm... "
                    l " Let's get on with the continuation, then! "
                    " Lana coughs for a bit before she gets into character. "
                    hide lananeutral at bottom
                    show lanaangry at center
                    ju " How could you, Pedro! "
                    ju " Getting with another man... "
                    ju " Another man that was my BEST FRIEND! "
                    ju " You've broken my heart once, and now you've completely shattered my heart to millions and trillions of pieces! "
                    hide lanaangry at bottom
                    show lanasad at center
                    pe " It's not my fault that you happened to be friends with my new lover, Juliana! "
                    pe " I'm sorry for breaking your heart once more, I didn't mean to do all of this to you! "
                    pe " I hope you can forgive me, and we can put this in the past... "
                    pe " ...And we can move on and become nothing more than friends. "
                    ju " That's enough! I've heard enough from you! "
                    hide lanasad at bottom
                    show lananeutral at center
                    l " A little short today, but atleast it's content, right? "
                    l " What will happen next? Find out on the next episode of Juliana and Pedro! "
                    l " Whew...that was fun! "
                    l " I should start thinking about what should happen next, hmhm... "
                    l " Thank you for reminding me of them once again, [name]! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Lana about the new Juliana and Pedro episode. "
                    " In your honest opinion, it was absolute and utter peak. "
                    " You're already dying to get more content. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your language class. "
                    " You walked out of the gym and went to your classroom. "
                    pause 2.0
                    jump languageclassthurs
                " How about we just talk to eachother ":
                    l " You wanna talk to me? "
                    l " Alright, we can do that! "
                    l " What do we talk about though? hm... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Lana. "
                    " You guys just talked about random things... "
                    " Like what a glue factory is. "
                    " You guys searched it up, and -...oh. "
                    " Well that's certainly a way to find out what a glue factory is. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your language class. "
                    " You walked out of the gym and went to your classroom. "
                    pause 2.0
                    jump languageclassthurs
        else:
            x " Hmm...what else can I do today? "
            x " I could go ahead and walk around the school... "
            x " ...But then again, nothing interesting is probably going on... "
            x " And Abbie's been really busy lately... "
            x " Hmhmmm... "
            " She looks around before noticing you being there. "
            hide lananeutral at bottom
            show lanahappy at center
            x " [name]!! It's real nice to see you!! "
            $ lanaknow = True
            l " I'm Lana, by the way! Nice to meet you! "
            l " I was just thinking of what I should do! "
            hide lanahappy at bottom
            show lananeutral at center
            l " What I should do for the break, of course. "
            l " I have absolutely no idea what I could do this time! "
            l " I mean, I could go ahead and make some new ocs... "
            l " But I already have a lot of them! "
            l " I mean, there's nothing wrong with having too many ocs, buuuut... "
            l " I don't really have any ideas for making a new one. "
            l " I could make a new sock puppet, but honestly... "
            l " My socks are starting to run out a bit and  I can't really buy another pair of socks. "
            l " I only have a bit as my daily allowance, after all! "
            l " Or, maybe I could.. "
            menu:
                " Continue your story of Juliana and Pedro " if lanalv >= 15 or lanalv == 15:
                    $ lanalv += 10
                    l " Wait, Juliana and Pedro? "
                    hide lananeutral at bottom
                    show lanahappy at center
                    l " I can't believe I forgot about them, ohhh my heavens! "
                    l " Thank you for reminding me of them, [name]! "
                    l " I'll come up with something real quick, hold on... "
                    hide lanahappy at bottom
                    show lananeutral at center
                    " Lana thinks for a good bit with the plot... "
                    " And then she finally has an idea! "
                    l " Alright, the last time we talked about them - "
                    l " Pedro was hanging out with Rainier, right? "
                    l " And Juliana just found out about them, hmm... "
                    l " Let's get on with the continuation, then! "
                    " Lana coughs for a bit before she gets into character. "
                    hide lananeutral at bottom
                    show lanaangry at center
                    ju " How could you, Pedro! "
                    ju " Getting with another man... "
                    ju " Another man that was my BEST FRIEND! "
                    ju " You've broken my heart once, and now you've completely shattered my heart to millions and trillions of pieces! "
                    hide lanaangry at bottom
                    show lanasad at center
                    pe " It's not my fault that you happened to be friends with my new lover, Juliana! "
                    pe " I'm sorry for breaking your heart once more, I didn't mean to do all of this to you! "
                    pe " I hope you can forgive me, and we can put this in the past... "
                    pe " ...And we can move on and become nothing more than friends. "
                    ju " That's enough! I've heard enough from you! "
                    hide lanasad at bottom
                    show lananeutral at center
                    l " A little short today, but atleast it's content, right? "
                    l " What will happen next? Find out on the next episode of Juliana and Pedro! "
                    l " Whew...that was fun! "
                    l " I should start thinking about what should happen next, hmhm... "
                    l " Thank you for reminding me of them once again, [name]! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Lana about the new Juliana and Pedro episode. "
                    " In your honest opinion, it was absolute and utter peak. "
                    " You're already dying to get more content. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your language class. "
                    " You walked out of the gym and went to your classroom. "
                    pause 2.0
                    jump languageclassthurs
                " How about we just talk to eachother ":
                    l " You wanna talk to me? "
                    l " Alright, we can do that! "
                    l " What do we talk about though? hm... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Lana. "
                    " You guys just talked about random things... "
                    " Like what a glue factory is. "
                    " You guys searched it up, and -...oh. "
                    " Well that's certainly a way to find out what a glue factory is. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your language class. "
                    " You walked out of the gym and went to your classroom. "
                    pause 2.0
                    jump languageclassthurs
    label skibidiboyles:
        show skellneutral at center with easeinright
        if skellknow == True:
            sk " ...Hm. "
            " Looks like he's playing a game on his phone. "
            " Don't know what the game is, but it looks pretty cool. "
            " You didn't wanna distract him, so you just watched. "
            sk " ...? "
            " Seems like he noticed you watching. "
            " How do I know? well... "
            " He moved himself closer to you so that you can have a better view. "
            " Huh, yeah this game looks better now that he's closer. "
            " From what you're seeing, it was a team based game. "
            " And his team was winning. "
            " I mean, from what you could see - Skell was pretty goated at the game. "
            " Killing people left and right... "
            " Well, he's making it look real easy. "
            " If you tried to play this game, you're sure he'd beat your ass. "
            " You kinda wanted to distract him for a bit, but you don't know how... "
            " Wait, didn't you say that you DIDN'T want to distract him? "
            " Looks like you changed your mind, huh. "
            " Hm, let's think a bit here. "
            " What could potentially make a emo guy distracted? "
            " After a bit of thinking, you had a few ideas. "
            " What should you do to distract him from his game. "
            menu:
                " Compliment him out of nowhere " if skelllv >= 15 or skelllv == 15:
                    $ skelllv += 10
                    " You decided to complimet him out of nowhere. "
                    " You've seen people compliment him before, and you've seen him get real flustered over it. "
                    " It might cause him to get confused mid game. Which is perfect, for you. "
                    " You think up of a compliment you could give him while he's playing... "
                    " ...After a few good seconds of thinking, you managed to come up with one. "
                    " You inhaled, gathered your thoughts before saying your compliment... "
                    mc " ...You're kind of cute whenever you're concentrated. "
                    hide skellneutral at bottom
                    show skellsurprised at center
                    sk " ...HUH??? "
                    " That got him distracted by a LOT. "
                    " He even stopped playing for a bit just to look at you with the most flabbergasted look he can ever give you. "
                    " When he realizes that he's still in game, he immediately locks back in. "
                    " He still manages to win the round though, and once he does, he hops off the game. "
                    hide skellsurprised at bottom
                    show skellneutral at center
                    sk " Jesus, you can't just say things like that... "
                    sk " I'm not exactly used to compliments, so it...kinda gets me distracted. "
                    sk " Did you...did you do that on purpose? Just to mess with me? "
                    hide skellneutral at bottom
                    show skellhappy at center
                    sk " ...I'm gonna tickle you for that. "
                    sk " COME HERE, YOU LITTLE SHIT!! " with vpunch
                    scene black with dissolve
                    " You spent the rest of the break being chased by Skell. "
                    " At one point while you were being chased, you somehow tripped on air... "
                    " Leading to you being tickled by Skell for a good bit. "
                    " He stopped after a minute or so and you guys just hung out for a bit. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a little bit of you two talking. "
                    " You got out of the gym so that you could go to your language class. "
                    pause 2.0
                    jump languageclassthurs
                " be a little shit and block the screen ":
                    $ skelllv += 5
                    " You decided to be a little shit and block his screen. "
                    " You placed your hand over his phone so that he couldn't see... "
                    hide skellneutral at bottom
                    show skellangry at center
                    sk " Hey..! "
                    sk " Stop that! "
                    " Skell removed your hand from the phone, and he continued gaming. "
                    " After a few minutes of hardcore gaming, his team eventually won. "
                    " The moment the winning screen popped up, he closed his phone and put it back into his pocket. "
                    hide skellangry at bottom
                    show skellneutral at center
                    sk " ...You were trying to distract me, weren't you? "
                    hide skellneutral at bottom
                    show skellhappy at center
                    sk " ...I'm gonna tickle you for that. "
                    sk " COME HERE, YOU LITTLE SHIT!! " with vpunch
                    scene black with dissolve
                    " You spent the rest of the break being chased by Skell. "
                    " At one point while you were being chased, you somehow tripped on air... "
                    " Leading to you being tickled by Skell for a good bit. "
                    " He stopped after a minute or so and you guys just hung out for a bit. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a little bit of you two talking. "
                    " You got out of the gym so that you could go to your language class. "
                    pause 2.0
                    jump languageclassthurs
        else:
            x " ...Hm. "
            " Looks like he's playing a game on his phone. "
            " Don't know what the game is, but it looks pretty cool. "
            " You didn't wanna distract him, so you just watched. "
            x " ...? "
            " Seems like he noticed you watching. "
            " How do I know? well... "
            " He moved himself closer to you so that you can have a better view. "
            " Huh, yeah this game looks better now that he's closer. "
            " From what you're seeing, it was a team based game. "
            $ skellknow = True
            " By the way, this guy's name was Skell, from what you've heard. "
            " Anyway, his team was winning. "
            " I mean, from what you could see - Skell was pretty goated at the game. "
            " Killing people left and right... "
            " Well, he's making it look real easy. "
            " If you tried to play this game, you're sure he'd beat your ass. "
            " You kinda wanted to distract him for a bit, but you don't know how... "
            " Wait, didn't you say that you DIDN'T want to distract him? "
            " Looks like you changed your mind, huh. "
            " Hm, let's think a bit here. "
            " What could potentially make a emo guy distracted? "
            " After a bit of thinking, you had a few ideas. "
            " What should you do to distract him from his game. "
            menu:
                " Compliment him out of nowhere " if skelllv >= 15 or skelllv == 15:
                    $ skelllv += 10
                    " You decided to complimet him out of nowhere. "
                    " You've seen people compliment him before, and you've seen him get real flustered over it. "
                    " It might cause him to get confused mid game. Which is perfect, for you. "
                    " You think up of a compliment you could give him while he's playing... "
                    " ...After a few good seconds of thinking, you managed to come up with one. "
                    " You inhaled, gathered your thoughts before saying your compliment... "
                    mc " ...You're kind of cute whenever you're concentrated. "
                    hide skellneutral at bottom
                    show skellsurprised at center
                    sk " ...HUH??? "
                    " That got him distracted by a LOT. "
                    " He even stopped playing for a bit just to look at you with the most flabbergasted look he can ever give you. "
                    " When he realizes that he's still in game, he immediately locks back in. "
                    " He still manages to win the round though, and once he does, he hops off the game. "
                    hide skellsurprised at bottom
                    show skellneutral at center
                    sk " Jesus, you can't just say things like that... "
                    sk " I'm not exactly used to compliments, so it...kinda gets me distracted. "
                    sk " Did you...did you do that on purpose? Just to mess with me? "
                    hide skellneutral at bottom
                    show skellhappy at center
                    sk " ...I'm gonna tickle you for that. "
                    sk " COME HERE, YOU LITTLE SHIT!! " with vpunch
                    scene black with dissolve
                    " You spent the rest of the break being chased by Skell. "
                    " At one point while you were being chased, you somehow tripped on air... "
                    " Leading to you being tickled by Skell for a good bit. "
                    " He stopped after a minute or so and you guys just hung out for a bit. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a little bit of you two talking. "
                    " You got out of the gym so that you could go to your language class. "
                    pause 2.0
                    jump languageclassthurs
                " be a little shit and block the screen ":
                    $ skelllv += 5
                    " You decided to be a little shit and block his screen. "
                    " You placed your hand over his phone so that he couldn't see... "
                    hide skellneutral at bottom
                    show skellangry at center
                    sk " Hey..! "
                    sk " Stop that! "
                    " Skell removed your hand from the phone, and he continued gaming. "
                    " After a few minutes of hardcore gaming, his team eventually won. "
                    " The moment the winning screen popped up, he closed his phone and put it back into his pocket. "
                    hide skellangry at bottom
                    show skellneutral at center
                    sk " ...You were trying to distract me, weren't you? "
                    hide skellneutral at bottom
                    show skellhappy at center
                    sk " ...I'm gonna tickle you for that. "
                    sk " COME HERE, YOU LITTLE SHIT!! " with vpunch
                    scene black with dissolve
                    " You spent the rest of the break being chased by Skell. "
                    " At one point while you were being chased, you somehow tripped on air... "
                    " Leading to you being tickled by Skell for a good bit. "
                    " He stopped after a minute or so and you guys just hung out for a bit. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a little bit of you two talking. "
                    " You got out of the gym so that you could go to your language class. "
                    pause 2.0
                    jump languageclassthurs
label thurscafeteria1:
    # lizzy and petunia, cubbie
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and spotted the three of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if popularknow == True and cubbieknow == True:
        menu:
            " {image=popularicon} Lizzy and Petunia {image=popularicon} ":
                jump stinkycoolrock
            " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                jump sillypoppipo
    elif popularknow == True and cubbieknow == False:
        menu:
            " {image=popularicon} Lizzy and Petunia {image=popularicon} ":
                jump stinkycoolrock
            " {image=cubbieicon} A innocent cat guy {image=cubbieicon} ":
                jump sillypoppipo
    elif popularknow == False and cubbieknow == True:
        menu:
            " {image=popularicon} The popular girls {image=popularicon} ":
                jump stinkycoolrock
            " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                jump sillypoppipo
    else:
        menu:
            " {image=popularicon} The popular girls {image=popularicon} ":
                jump stinkycoolrock
            " {image=cubbieicon} A innocent cat guy {image=cubbieicon} ":
                jump sillypoppipo
    label stinkycoolrock:
        show petuniaangry at left with easeinright
        show lizzyangry at right with easeinright
        if popularknow == True:
            p " You just don't seem to get it, do you?! "
            lz " I don't even know what you're talking about in the first place! "
            " Uh oh, looks like they're arguing. "
            " This might've been a bad time to come over... "
            " All you can kinda do is just listen to whatever they're arguing about. "
            p " I've been TRYING my best to apologize to you - "
            p " But you always ignore me! I'm trying to help us out here, you know?! "
            p " I don't even know why you're mad in the first place! "
            p " How can I know what to apologize for if you won't tell me?! "
            lz " You wouldn't understand if I told you! "
            lz " And I think you'd know why if you took a second to look in our COMMENT SECTION! "
            p " What do our fans have to do with this?! "
            p " What, someone gave you a little hate comment? Couldn't handle it? "
            p " Come ON Liz! You're better than that! "
            p " God, you always make big deals out of something so small! "
            lz " It's not that at all! "
            lz " Jesus christ, you NEVER understand! "
            lz " You know what, I'm out! "
            lz " You'll find it out later. "
            lz " Or not, considering how you focus on getting BITCHES so much! "
            hide lizzyangry at right with easeoutright
            show petuniaangry at center with move
            p " HEY!! "
            p " God that little...! "
            " You asked her if she was going to be alright. "
            hide petuniaangry at bottom
            show petuniasad at center
            p " ...I dunno. "
            p " Look, I've tried asking her what's wrong with her - "
            p " But whenever I do, she just gives me the stink eye! "
            p " Like, hellooo? did I do something wrong? "
            p " God, she never makes sense... "
            hide petuniasad at bottom
            show petunianeutral at center
            p " But who cares about her? "
            p " You're going to be my very new best friend! "
            p " My time with you is going to be great! "
            scene black with dissolve
            " Lord almighty, you've got to bring them back. "
            " There's no way you're going to be this girl's new bestfriend. "
            " You are NOT becoming a replacement for someone. "
            " You've got to figure out how to bring them back though. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, time for your language class. "
            " You immediately skedaddled out of the cafeteria the moment you heard the bell ring. "
            pause 2.0
            jump languageclassthurs
        else:
            x " You just don't seem to get it, do you?! "
            x " I don't even know what you're talking about in the first place! "
            " Uh oh, looks like they're arguing. "
            " This might've been a bad time to come over... "
            " All you can kinda do is just listen to whatever they're arguing about. "
            x " I've been TRYING my best to apologize to you - "
            x " But you always ignore me! I'm trying to help us out here, you know?! "
            x " I don't even know why you're mad in the first place! "
            x " How can I know what to apologize for if you won't tell me?! "
            x " You wouldn't understand if I told you! "
            x " And I think you'd know why if you took a second to look in our COMMENT SECTION! "
            x " What do our fans have to do with this?! "
            x " What, someone gave you a little hate comment? Couldn't handle it? "
            x " Come ON Liz! You're better than that! "
            x " God, you always make big deals out of something so small! "
            x " It's not that at all! "
            x " Jesus christ, you NEVER understand! "
            x " You know what, I'm out! "
            x " You'll find it out later. "
            x " Or not, considering how you focus on getting BITCHES so much! "
            hide lizzyangry at right with easeoutright
            show petuniaangry at center with move
            x " HEY!! "
            x " God that little...! "
            " You asked her if she was going to be alright. "
            hide petuniaangry at bottom
            show petuniasad at center
            x " ...I dunno. "
            x " Look, I've tried asking her what's wrong with her - "
            x " But whenever I do, she just gives me the stink eye! "
            x " Like, hellooo? did I do something wrong? "
            x " God, she never makes sense... "
            hide petuniasad at bottom
            show petunianeutral at center
            x " But who cares about her? "
            x " You're going to be my very new best friend! "
            x " My time with you is going to be great! "
            $ popularknow = True
            p " I'm Petunia, by the way. "
            scene black with dissolve
            " Lord almighty, you've got to bring them back. "
            " There's no way you're going to be this girl's new bestfriend. "
            " You are NOT becoming a replacement for someone. "
            " You've got to figure out how to bring them back though. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, time for your language class. "
            " You immediately skedaddled out of the cafeteria the moment you heard the bell ring. "
            pause 2.0
            jump languageclassthurs
    label sillypoppipo:
        show cubbieneutral at center with easeinleft
        if cubbieknow == True:
            cb " ... "
            " Cubbie motioned for you to sit with him. "
            " The moment you sat with him, he pointed at a table... "
            " The table he was pointing at was the one with two girls arguing. "
            hide cubbieneutral at bottom
            show cubbiesad at center
            cb " ... "
            " Cubbie seems a little worried for them. "
            " From what you've heard about those girls, those girls were always together. "
            " Wonder what happened to them... "
            " Maybe a misunderstanding happened? that's most likely. "
            " Still, it's odd that they're fighting considering the fact you've heard that they're best friends.. "
            " But then again, friends do quarrel sometimes. "
            " So maybe they're going to be better tomorrow. "
            " And if not? Well, uh... "
            " Let's just pray that they're going to be better next week, then. "
            " Best friends fighting is always sad, yet also entertaining at the same time. "
            " Due to the amount of gossip you could get from them. "
            " But we're sort of getting out of topic. "
            " Cubbie still seems a little worried while watching the girls fight... "
            " You should probably do something to comfort him. "
            " What should you do to make Cubbie feel better? "
            menu:
                " Pat his head and reassure him ":
                    $ cubbielv += 10
                    hide cubbiesad at bottom
                    show cubbieneutral at center
                    " You reassured him that they were probably going to be fine tomorrrow. "
                    " You know that friendships are sometimes going to have their bad days, "
                    " So they're probably going to forgive eachother tomorrow for whatever they did. "
                    cb " ...:D "
                    " Cubbie seems to feel better hearing your words and feeling the pats on his head. "
                    " ...I'm starting to question the writing in this universe. "
                    " Send help. I didn't want to be here. "
                    scene black with dissolve
                    " You spent the rest of the break hanging out with Cubbie. "
                    " And also watching the argument right infront of you. "
                    " You wonder what the girls were even arguing about... "
                    " It's not your business though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your language class. "
                    " You got out of the cafeteria and went to your classroom. "
                    pause 2.0
                    jump languageclassthurs
                " Say nothing, Do nothing, Watch the drama. ":
                    hide cubbiesad at bottom
                    show cubbieneutral at center
                    cb " ... "
                    " Cubbie saw that you were just watching the argument infront of you... "
                    " He just decided to stay silent and watch the argument too. "
                    " What else could he do, really? "
                    scene black with dissolve
                    " You spent the rest of the break hanging out with Cubbie. "
                    " And also watching the argument right infront of you. "
                    " You wonder what the girls were even arguing about... "
                    " It's not your business though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your language class. "
                    " You got out of the cafeteria and went to your classroom. "
                    pause 2.0
                    jump languageclassthurs
        else:
            x " ... "
            " From what you've heard, this little guy's name is Cubbie. "
            $ cubbieknow = True
            " He can speak, but he mostly prefers not to. "
            " Cubbie motioned for you to sit with him. "
            " The moment you sat with him, he pointed at a table... "
            " The table he was pointing at was the one with two girls arguing. "
            hide cubbieneutral at bottom
            show cubbiesad at center
            cb " ... "
            " Cubbie seems a little worried for them. "
            " From what you've heard about those girls, those girls were always together. "
            " Wonder what happened to them... "
            " Maybe a misunderstanding happened? that's most likely. "
            " Still, it's odd that they're fighting considering the fact you've heard that they're best friends.. "
            " But then again, friends do quarrel sometimes. "
            " So maybe they're going to be better tomorrow. "
            " And if not? Well, uh... "
            " Let's just pray that they're going to be better next week, then. "
            " Best friends fighting is always sad, yet also entertaining at the same time. "
            " Due to the amount of gossip you could get from them. "
            " But we're sort of getting out of topic. "
            " Cubbie still seems a little worried while watching the girls fight... "
            " You should probably do something to comfort him. "
            " What should you do to make Cubbie feel better? "
            menu:
                " Pat his head and reassure him ":
                    $ cubbielv += 10
                    hide cubbiesad at bottom
                    show cubbieneutral at center
                    " You reassured him that they were probably going to be fine tomorrrow. "
                    " You know that friendships are sometimes going to have their bad days, "
                    " So they're probably going to forgive eachother tomorrow for whatever they did. "
                    cb " ...:D "
                    " Cubbie seems to feel better hearing your words and feeling the pats on his head. "
                    " ...I'm starting to question the writing in this universe. "
                    " Send help. I didn't want to be here. "
                    scene black with dissolve
                    " You spent the rest of the break hanging out with Cubbie. "
                    " And also watching the argument right infront of you. "
                    " You wonder what the girls were even arguing about... "
                    " It's not your business though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your language class. "
                    " You got out of the cafeteria and went to your classroom. "
                    pause 2.0
                    jump languageclassthurs
                " Say nothing, Do nothing, Watch the drama. ":
                    hide cubbiesad at bottom
                    show cubbieneutral at center
                    cb " ... "
                    " Cubbie saw that you were just watching the argument infront of you... "
                    " He just decided to stay silent and watch the argument too. "
                    " What else could he do, really? "
                    scene black with dissolve
                    " You spent the rest of the break hanging out with Cubbie. "
                    " And also watching the argument right infront of you. "
                    " You wonder what the girls were even arguing about... "
                    " It's not your business though. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your language class. "
                    " You got out of the cafeteria and went to your classroom. "
                    pause 2.0
                    jump languageclassthurs
label thursrooftop1:
    # kevin and claire
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked to the rooftop and spotted two of your classmates talking to eachother. "
    if clairebeatup == True:
        " You kinda lost your chance to apologize to Claire here, so.. "
        " Yeah, sorry. "
        scene black
        pause 2.0
        jump languageclassthurs
    else:
        pass
    " Wondering what they're talking about, you decided to join their conversation. "
    show kevinneutral at left with easeinright
    show claireneutral at right with easeinright
    if kevinknow == True and claireknow == True:
        kv " Honestly, I think I prefer season 1. "
        c " Really...? is it because the voices are better? "
        kv " Well, yeah. "
        kv " The old voices were way better than the new ones. "
        kv " I mean, I get it - "
        kv " - People change in time, but still... "
        kv " The old voices gave the characters more personality. "
        hide kevinneutral at bottom
        show kevinangry at left
        kv " I mean Towellette sounded so sassy back then! "
        kv " Now she just...sounds so bland. "
        c " Well for me, I honestly like both! "
        " You greeted them and then asked what they were talking about. "
        hide kevinangry at bottom
        show kevinneutral at left
        c " Oh hello there, [name]! "
        c " Me and Kevin were just talking about the new season of Towellette and Soapsy. "
        c " It's a pretty interesting show...don't really know if it's your thing. "
        kv " Mhm. Though I'm not really interested in the things they show on screen, if you...get what I mean. "
        kv " I'm honestly there for the designs and the story since it's plot is interesting. "
        kv " There ARE some questionably design choices, but I guess you can't really change it. "
        kv " Besides, I don't want to be like one of those... "
        c " ...Those 'redesigning characters' people? "
        kv " Specifically the ones who redesign them to the point that they're unrecognizeable, yes. "
        kv " And the ones who change their skin colors. Like, is it that hard to just color them how they are? "
        kv " I don't care if you don't know how to shade that skin color - skin color is skin color, dude. "
        c " I completely agree with that, Kevin! "
        c " Oh right, [name]... "
        c " Question: even though I'm sure you haven't heard of the new voices, buuuut... "
        c " Do you prefer season 1 voices or season 2? "
        menu:
            " Season 1 ":
                $ kevinlv += 10
                hide kevinneutral at bottom
                show kevinhappy at left
                kv " See? [name] knows true peak. "
                kv " Don't get me wrong, the new voices are just fine... "
                kv " But they really just don't top the old ones. "
                kv " It's just my opinion though, of course. "
                kv " Not like I'm trying to force it on you guys. "
                c " Yeah, don't worry. I respect your opinion. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Kevin and Claire. "
                " You feel like the whole Towellette and Soapsy thing is a reference to something else... "
                " Can't place a finger on what it might be a reference too though. "
                " Let's just say its a reference to a funny anime. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " Season 2 ":
                kv " Well uh...you do you then, I guess. "
                c " I think that the voices from season 1 and 2 are alright... "
                c " But we respect your opinion [name], don't worry! "
                scene black with dissolve
                " You spent the rest of the break hanging out with Kevin and Claire. "
                " You feel like the whole Towellette and Soapsy thing is a reference to something else... "
                " Can't place a finger on what it might be a reference too though. "
                " Let's just say its a reference to a funny anime. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " Man I don't care about voices, I'm just there for new content ":
                $ clairelv += 10
                hide claireneutral at bottom
                show clairehappy at right
                c " Yeah, me too! "
                c " As long as it's new content, then I'm happy! "
                kv " ...You guys do you, then. "
                kv " Respect yall's opinions though. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Kevin and Claire. "
                " You feel like the whole Towellette and Soapsy thing is a reference to something else... "
                " Can't place a finger on what it might be a reference too though. "
                " Let's just say its a reference to a funny anime. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassthurs
    elif kevinknow == True and claireknow == False:
        kv " Honestly, I think I prefer season 1. "
        x " Really...? is it because the voices are better? "
        kv " Well, yeah. "
        kv " The old voices were way better than the new ones. "
        kv " I mean, I get it - "
        kv " - People change in time, but still... "
        kv " The old voices gave the characters more personality. "
        hide kevinneutral at bottom
        show kevinangry at left
        kv " I mean Towellette sounded so sassy back then! "
        kv " Now she just...sounds so bland. "
        x " Well for me, I honestly like both! "
        " You greeted them and then asked what they were talking about. "
        hide kevinangry at bottom
        show kevinneutral at left
        x " Oh hello there, [name]! "
        x " Don't think I've introduced myself to you before... "
        $ claireknow = True
        c " I'm Claire! It's really nice to meet you! "
        c " Anyway... "
        c " Me and Kevin were just talking about the new season of Towellette and Soapsy. "
        c " It's a pretty interesting show...don't really know if it's your thing. "
        kv " Mhm. Though I'm not really interested in the things they show on screen, if you...get what I mean. "
        kv " I'm honestly there for the designs and the story since it's plot is interesting. "
        kv " There ARE some questionably design choices, but I guess you can't really change it. "
        kv " Besides, I don't want to be like one of those... "
        c " ...Those 'redesigning characters' people? "
        kv " Specifically the ones who redesign them to the point that they're unrecognizeable, yes. "
        kv " And the ones who change their skin colors. Like, is it that hard to just color them how they are? "
        kv " I don't care if you don't know how to shade that skin color - skin color is skin color, dude. "
        c " I completely agree with that, Kevin! "
        c " Oh right, [name]... "
        c " Question: even though I'm sure you haven't heard of the new voices, buuuut... "
        c " Do you prefer season 1 voices or season 2? "
        menu:
            " Season 1 ":
                $ kevinlv += 10
                hide kevinneutral at bottom
                show kevinhappy at left
                kv " See? [name] knows true peak. "
                kv " Don't get me wrong, the new voices are just fine... "
                kv " But they really just don't top the old ones. "
                kv " It's just my opinion though, of course. "
                kv " Not like I'm trying to force it on you guys. "
                c " Yeah, don't worry. I respect your opinion. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Kevin and Claire. "
                " You feel like the whole Towellette and Soapsy thing is a reference to something else... "
                " Can't place a finger on what it might be a reference too though. "
                " Let's just say its a reference to a funny anime. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " Season 2 ":
                kv " Well uh...you do you then, I guess. "
                c " I think that the voices from season 1 and 2 are alright... "
                c " But we respect your opinion [name], don't worry! "
                scene black with dissolve
                " You spent the rest of the break hanging out with Kevin and Claire. "
                " You feel like the whole Towellette and Soapsy thing is a reference to something else... "
                " Can't place a finger on what it might be a reference too though. "
                " Let's just say its a reference to a funny anime. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " Man I don't care about voices, I'm just there for new content ":
                $ clairelv += 10
                hide claireneutral at bottom
                show clairehappy at right
                c " Yeah, me too! "
                c " As long as it's new content, then I'm happy! "
                kv " ...You guys do you, then. "
                kv " Respect yall's opinions though. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Kevin and Claire. "
                " You feel like the whole Towellette and Soapsy thing is a reference to something else... "
                " Can't place a finger on what it might be a reference too though. "
                " Let's just say its a reference to a funny anime. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassthurs
    elif kevinknow == False and claireknow == True:
        x " Honestly, I think I prefer season 1. "
        c " Really...? is it because the voices are better? "
        x " Well, yeah. "
        x " The old voices were way better than the new ones. "
        x " I mean, I get it - "
        x " - People change in time, but still... "
        x " The old voices gave the characters more personality. "
        hide kevinneutral at bottom
        show kevinangry at left
        x " I mean Towellette sounded so sassy back then! "
        x " Now she just...sounds so bland. "
        c " Well for me, I honestly like both! "
        " You greeted them and then asked what they were talking about. "
        hide kevinangry at bottom
        show kevinneutral at left
        c " Oh hello there, [name]! "
        $ kevinknow = True
        c " Me and Kevin were just talking about the new season of Towellette and Soapsy. "
        c " It's a pretty interesting show...don't really know if it's your thing. "
        kv " Mhm. Though I'm not really interested in the things they show on screen, if you...get what I mean. "
        kv " I'm honestly there for the designs and the story since it's plot is interesting. "
        kv " There ARE some questionably design choices, but I guess you can't really change it. "
        kv " Besides, I don't want to be like one of those... "
        c " ...Those 'redesigning characters' people? "
        kv " Specifically the ones who redesign them to the point that they're unrecognizeable, yes. "
        kv " And the ones who change their skin colors. Like, is it that hard to just color them how they are? "
        kv " I don't care if you don't know how to shade that skin color - skin color is skin color, dude. "
        c " I completely agree with that, Kevin! "
        c " Oh right, [name]... "
        c " Question: even though I'm sure you haven't heard of the new voices, buuuut... "
        c " Do you prefer season 1 voices or season 2? "
        menu:
            " Season 1 ":
                $ kevinlv += 10
                hide kevinneutral at bottom
                show kevinhappy at left
                kv " See? [name] knows true peak. "
                kv " Don't get me wrong, the new voices are just fine... "
                kv " But they really just don't top the old ones. "
                kv " It's just my opinion though, of course. "
                kv " Not like I'm trying to force it on you guys. "
                c " Yeah, don't worry. I respect your opinion. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Kevin and Claire. "
                " You feel like the whole Towellette and Soapsy thing is a reference to something else... "
                " Can't place a finger on what it might be a reference too though. "
                " Let's just say its a reference to a funny anime. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " Season 2 ":
                kv " Well uh...you do you then, I guess. "
                c " I think that the voices from season 1 and 2 are alright... "
                c " But we respect your opinion [name], don't worry! "
                scene black with dissolve
                " You spent the rest of the break hanging out with Kevin and Claire. "
                " You feel like the whole Towellette and Soapsy thing is a reference to something else... "
                " Can't place a finger on what it might be a reference too though. "
                " Let's just say its a reference to a funny anime. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " Man I don't care about voices, I'm just there for new content ":
                $ clairelv += 10
                hide claireneutral at bottom
                show clairehappy at right
                c " Yeah, me too! "
                c " As long as it's new content, then I'm happy! "
                kv " ...You guys do you, then. "
                kv " Respect yall's opinions though. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Kevin and Claire. "
                " You feel like the whole Towellette and Soapsy thing is a reference to something else... "
                " Can't place a finger on what it might be a reference too though. "
                " Let's just say its a reference to a funny anime. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassthurs
    else:
        x " Honestly, I think I prefer season 1. "
        x " Really...? is it because the voices are better? "
        x " Well, yeah. "
        x " The old voices were way better than the new ones. "
        x " I mean, I get it - "
        x " - People change in time, but still... "
        x " The old voices gave the characters more personality. "
        hide kevinneutral at bottom
        show kevinangry at left
        x " I mean Towellette sounded so sassy back then! "
        x " Now she just...sounds so bland. "
        x " Well for me, I honestly like both! "
        " You greeted them and then asked what they were talking about. "
        hide kevinangry at bottom
        show kevinneutral at left
        x " Oh hello there, [name]! "
        x " Don't think I've introduced myself to you before... "
        $ claireknow = True
        c " I'm Claire! It's really nice to meet you! "
        c " Anyway... "
        $ kevinknow = True
        c " Me and Kevin were just talking about the new season of Towellette and Soapsy. "
        c " It's a pretty interesting show...don't really know if it's your thing. "
        kv " Mhm. Though I'm not really interested in the things they show on screen, if you...get what I mean. "
        kv " I'm honestly there for the designs and the story since it's plot is interesting. "
        kv " There ARE some questionably design choices, but I guess you can't really change it. "
        kv " Besides, I don't want to be like one of those... "
        c " ...Those 'redesigning characters' people? "
        kv " Specifically the ones who redesign them to the point that they're unrecognizeable, yes. "
        kv " And the ones who change their skin colors. Like, is it that hard to just color them how they are? "
        kv " I don't care if you don't know how to shade that skin color - skin color is skin color, dude. "
        c " I completely agree with that, Kevin! "
        c " Oh right, [name]... "
        c " Question: even though I'm sure you haven't heard of the new voices, buuuut... "
        c " Do you prefer season 1 voices or season 2? "
        menu:
            " Season 1 ":
                $ kevinlv += 10
                hide kevinneutral at bottom
                show kevinhappy at left
                kv " See? [name] knows true peak. "
                kv " Don't get me wrong, the new voices are just fine... "
                kv " But they really just don't top the old ones. "
                kv " It's just my opinion though, of course. "
                kv " Not like I'm trying to force it on you guys. "
                c " Yeah, don't worry. I respect your opinion. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Kevin and Claire. "
                " You feel like the whole Towellette and Soapsy thing is a reference to something else... "
                " Can't place a finger on what it might be a reference too though. "
                " Let's just say its a reference to a funny anime. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " Season 2 ":
                kv " Well uh...you do you then, I guess. "
                c " I think that the voices from season 1 and 2 are alright... "
                c " But we respect your opinion [name], don't worry! "
                scene black with dissolve
                " You spent the rest of the break hanging out with Kevin and Claire. "
                " You feel like the whole Towellette and Soapsy thing is a reference to something else... "
                " Can't place a finger on what it might be a reference too though. "
                " Let's just say its a reference to a funny anime. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassthurs
            " Man I don't care about voices, I'm just there for new content ":
                $ clairelv += 10
                hide claireneutral at bottom
                show clairehappy at right
                c " Yeah, me too! "
                c " As long as it's new content, then I'm happy! "
                kv " ...You guys do you, then. "
                kv " Respect yall's opinions though. "
                scene black with dissolve
                " You spent the rest of the break hanging out with Kevin and Claire. "
                " You feel like the whole Towellette and Soapsy thing is a reference to something else... "
                " Can't place a finger on what it might be a reference too though. "
                " Let's just say its a reference to a funny anime. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your language class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump languageclassthurs
label thurslibrary1:
    # abbie and bubble
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked to the library and spotted two of your classmates doing their own things. "
    " Wondering what they're doing, you decided to talk to one of them. "
    " Who do you talk to for this break? "
    if abbieknow == True and bubbleknow == True:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump sevenminutes
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump inheaven
    else:
        menu:
            " {image=abbieicon} A shy kid {image=abbieicon} ":
                jump sevenminutes
            " {image=bubbleicon} A girl made up of bubbles {image=bubbleicon} ":
                jump inheaven
    label sevenminutes:
        show abbieneutral at center with easeinleft
        if abbieknow == True:
            a " Hm... "
            " He seems to be reading a book. "
            " Upon closer look, it seems to be a book about... "
            " ...Fighting better? "
            " Well that was unexpected. "
            " You decided to sit next to him, and the moment you do... "
            " ...He immediately closes the book out of embarrassment. "
            a " [name]...!! "
            a " Um...while I am happy to see you... "
            a " You...didn't see what I was reading, right...? "
            " You told him that you saw. "
            hide abbieneutral at bottom
            show abbiesad at center
            a " Aw... "
            a " Sorry...it's a little stupid that I wanna fight... "
            a " Especially since I know how weak I am... "
            a " You don't have to rub it in my face... "
            menu:
                " It's okay, you just wanna learn how to be tougher " if abbieteach == True:
                    $ abbielv += 10
                    " You told him that it was alright and gave him a pat on the back. "
                    " Then you asked him how his self-training is going. "
                    hide abbiesad at bottom
                    show abbiehappy at center
                    a " Oh um...my self training...? "
                    a " It's been doing great, actually... "
                    a " You're probably going to be proud of me when I say this, but... "
                    a " I actually managed to punch a hole in a wall... "
                    hide abbiehappy at bottom
                    show abbieneutral at center
                    a " ...I know it's probably concerning, but... "
                    a " Trust me when I say this - it wasn't the walls of my room or the walls in school... "
                    a " ...But I just punched an abandoned house while walking home... "
                    a " I didn't expect my training to go that well... "
                    a " You've been a great teacher, [name]... "
                    a " And not only that, but you've been a great friend... "
                    a " I, um...I hope we can spend more time with eachother... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Abbie. "
                    " You're honestly really proud that Abbie's been getting stronger. "
                    " This means that Abbie might be able to actually defend himself whenever Oliver messes with him. "
                    " The thought makes you feel happy. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for your language class. "
                    " You walked out of the library and went to your classroom. "
                    pause 2.0
                    jump languageclassthurs
                " Tell him that it's alright ":
                    $ abbielv += 5
                    a " Oh, uh...really? "
                    a " Thanks, then... "
                    " Abbie doesn't talk a lot while you're there. "
                    " It feels awkward, but somehow a nice feeling of awkward. "
                    scene black with dissolve
                    " You spent the rest of the break hanging out in the library. "
                    " Since Abbie looked like he wasn't comfortable with talking, you decided not to say anything. "
                    " Instead, you grabbed a random book and started reading that to pass the time. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for your language class. "
                    " You walked out of the library and went to your classroom. "
                    pause 2.0
                    jump languageclassthurs
        else:
            x " Hm... "
            " He seems to be reading a book. "
            " Upon closer look, it seems to be a book about... "
            " ...Fighting better? "
            " Well that was unexpected. "
            " You decided to sit next to him, and the moment you do... "
            " ...He immediately closes the book out of embarrassment. "
            x " [name]...!! "
            x " Um...while I am happy to see you... "
            x " You...didn't see what I was reading, right...? "
            " You told him that you saw. "
            hide abbieneutral at bottom
            show abbiesad at center
            x " Aw... "
            x " Sorry...it's a little stupid that I wanna fight... "
            x " Especially since I know how weak I am... "
            x " You don't have to rub it in my face... "
            menu:
                " It's okay, you just wanna learn how to be tougher " if abbieteach == True:
                    $ abbielv += 10
                    " You told him that it was alright and gave him a pat on the back. "
                    " Then you asked him how his self-training is going. "
                    hide abbiesad at bottom
                    show abbiehappy at center
                    a " Oh um...my self training...? "
                    a " It's been doing great, actually... "
                    a " You're probably going to be proud of me when I say this, but... "
                    a " I actually managed to punch a hole in a wall... "
                    hide abbiehappy at bottom
                    show abbieneutral at center
                    a " ...I know it's probably concerning, but... "
                    a " Trust me when I say this - it wasn't the walls of my room or the walls in school... "
                    a " ...But I just punched an abandoned house while walking home... "
                    a " I didn't expect my training to go that well... "
                    a " You've been a great teacher, [name]... "
                    a " And not only that, but you've been a great friend... "
                    a " I, um...I hope we can spend more time with eachother... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Abbie. "
                    " You're honestly really proud that Abbie's been getting stronger. "
                    " This means that Abbie might be able to actually defend himself whenever Oliver messes with him. "
                    " The thought makes you feel happy. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for your language class. "
                    " You walked out of the library and went to your classroom. "
                    pause 2.0
                    jump languageclassthurs
                " Tell him that it's alright ":
                    $ abbielv += 5
                    x " Oh, uh...really? "
                    x " Thanks, then... "
                    $ abbieknow = True
                    a " And, uh...I'm Abbie, by the way... nice to meet you... "
                    " Abbie doesn't talk a lot while you're there. "
                    " It feels awkward, but somehow a nice feeling of awkward. "
                    scene black with dissolve
                    " You spent the rest of the break hanging out in the library. "
                    " Since Abbie looked like he wasn't comfortable with talking, you decided not to say anything. "
                    " Instead, you grabbed a random book and started reading that to pass the time. "
                    play sound "audio/bellring.mp3"
                    " The bell rings, looks like it's time for your language class. "
                    " You walked out of the library and went to your classroom. "
                    pause 2.0
                    jump languageclassthurs
    label inheaven:
        show bubbleneutral at center with easeinright
        if bubbleknow == True:
            b " Hmhmhmmm... "
            b " A little dust here, a little dust there... "
            b " Darn, this place hasn't been cleaned in awhile, hasn't it? "
            b " Good thing Miss Circle asked me to clean up... "
            b " Hmhmmmm...wonder what Claire is doing right now... "
            " You coughed so that you could get her attention. "
            hide bubbleneutral at bottom
            show bubblehappy at center
            b " Oh, [name]!! Hiya!! "
            b " It's really nice to see you here, hehe... "
            hide bubblehappy at bottom
            show bubbleneutral at center
            b " I'm cleaning the bookshelves here because Miss Circle asked me to. "
            b " She kinda saw how dirty and dusty everything was, sooo... "
            b " The moment she came in, she asked me to do it! "
            b " Not like I'm complaining or anything, at least this gives me something to do! "
            b " But, uh...I do have to admit... "
            b " Cleaning alone is a little tiring. "
            b " And plus, with how big this library is - I'm sure it's gonna take me forever to clean up! "
            b " I don't want to be here until closing time! "
            b " Hmmmm...if you don't mind... "
            b " Could you help me clean up for a mit? "
            menu:
                " I don't mind ":
                    $ bubblelv += 10
                    hide bubbleneutral at bottom
                    show bubblehappy at center
                    b " Awesome! "
                    b " Since I'm already cleaning this side, how about you clean the other side? "
                    b " Oh, heres an extra duster! "
                    scene black with dissolve
                    " You spent the rest of the break cleaning the library with Bubble. "
                    " It was honestly kinda fun, in a way. "
                    " You joked here and there with Bubble about being castle maids from animes... "
                    " ...Cleaning up the caslte and what not. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, you guys managed to clean a good amount before it rang. "
                    " You then walked to your classroom for your language class. "
                    pause 2.0
                    jump languageclassthurs
                " I do mind ":
                    b " Oh, uh...alright! "
                    b " I'm sure it's not gonna take me that long, haha... "
                    b " Though, if you ever need something, just tell me! "
                    b " I'll be right here! "
                    scene black with dissolve
                    " You spent the rest of the break hanging out in the library. "
                    " Every now and then you would look at Bubble cleaning... "
                    " But then immediately looking back to whatever you were doing in the library. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your language class. "
                    " You walked to your classroom after a bit. "
                    pause 2.0
                    jump languageclassthurs
        else:
            x " Hmhmhmmm... "
            x " A little dust here, a little dust there... "
            x " Darn, this place hasn't been cleaned in awhile, hasn't it? "
            x " Good thing Miss Circle asked me to clean up... "
            x " Hmhmmmm...wonder what Claire is doing right now... "
            " You coughed so that you could get her attention. "
            hide bubbleneutral at bottom
            show bubblehappy at center
            x " Oh, [name]!! Hiya!! "
            x " It's really nice to see you here, hehe... "
            $ bubbleknow = True
            b " I'm Bubble, by the way! Nice to meet you! "
            hide bubblehappy at bottom
            show bubbleneutral at center
            b " I'm cleaning the bookshelves here because Miss Circle asked me to. "
            b " She kinda saw how dirty and dusty everything was, sooo... "
            b " The moment she came in, she asked me to do it! "
            b " Not like I'm complaining or anything, at least this gives me something to do! "
            b " But, uh...I do have to admit... "
            b " Cleaning alone is a little tiring. "
            b " And plus, with how big this library is - I'm sure it's gonna take me forever to clean up! "
            b " I don't want to be here until closing time! "
            b " Hmmmm...if you don't mind... "
            b " Could you help me clean up for a mit? "
            menu:
                " I don't mind ":
                    $ bubblelv += 10
                    hide bubbleneutral at bottom
                    show bubblehappy at center
                    b " Awesome! "
                    b " Since I'm already cleaning this side, how about you clean the other side? "
                    b " Oh, heres an extra duster! "
                    scene black with dissolve
                    " You spent the rest of the break cleaning the library with Bubble. "
                    " It was honestly kinda fun, in a way. "
                    " You joked here and there with Bubble about being castle maids from animes... "
                    " ...Cleaning up the caslte and what not. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, you guys managed to clean a good amount before it rang. "
                    " You then walked to your classroom for your language class. "
                    pause 2.0
                    jump languageclassthurs
                " I do mind ":
                    b " Oh, uh...alright! "
                    b " I'm sure it's not gonna take me that long, haha... "
                    b " Though, if you ever need something, just tell me! "
                    b " I'll be right here! "
                    scene black with dissolve
                    " You spent the rest of the break hanging out in the library. "
                    " Every now and then you would look at Bubble cleaning... "
                    " But then immediately looking back to whatever you were doing in the library. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your language class. "
                    " You walked to your classroom after a bit. "
                    pause 2.0
                    jump languageclassthurs
label thursoligang1:
    scene black with dissolve
    pause 2.0
    scene oligangclub with dissolve
    " You walked into the room and found only Oliver in the room. "
    " Curious on where the others were, you decided to walk up to him. "
    show oliverneutral at center with easeinleft
    o " Oooo, hey there, [name]. "
    o " Wondering where the others are? "
    o " They're just planning stuff back at the library. "
    o " You see... "
    o " We're planning on thrashing the library while everyone else is in class. "
    o " Right now they're just kinda messing with Bubble. "
    o " Bubble's cleaning the library 'cause Circle asked her to, "
    o " And Edward and Zip are secretly adding dust piles here and there. "
    o " Everytime she's not looking - they're adding them to places she's already cleaned before. "
    o " A way to get her annoyed, truly. "
    o " Anyway, what was that question I was gonna ask you... "
    o " Oh yeah. "
    o " You wanna join us in thrashing the library? "
    o " It's gonna be fun, especially since it's with us - trust me. "
    menu:
        " sure lmao ":
            $ oliganglv += 10
            hide oliverneutral at bottom
            show oliverhappy at center
            o " Great. "
            o " We'll go to the library early, then. "
            o " Don't know how we're gonna keep eachother entertained, buuuut... "
            o " I guess I could share my soap lunch with you. "
            scene black with dissolve
            " You walked to the library with Oliver. "
            " You two then waited for the bell to ring... "
            " ...While also eating some real good soap. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, and you and the other three waited for everyone to get to their classrooms. "
            " Once Zip made sure everything was clear, you guys started trashing everything. "
            " You're pretty sure that the librarian wasn't even there to witness, so you were all good. "
            " After a good few minutes of thrashing, you all then went to the classroom for the language class. "
            pause 2.0
            jump languageclassthurs
        " Nah dont feel like it ":
            o " Damn, alright. "
            o " We'll be in the library if you need anything. "
            o " Or just give Edward a text if you need something. "
            hide oliverneutral at right with easeoutright
            o " See ya. "
            scene black with dissolve
            " You spent the rest of the break hanging out in the room. "
            " You didn't really do anything much, just played some games on your phone. "
            " Check the school GC every now and then... "
            " But gaming, mostly. "
            " You wonder how badly Oliver and the other two are gonna thrash the library... "
            play sound "audio/bellring.mp3"
            " The bell rings, looks like it's time for your language class. "
            " You walked out of the room and went to your classroom. "
            pause 2.0
            jump languageclassthurs
label languageclassthurs:
    scene classroom with dissolve
    " The moment you walked into the classroom, the teacher was already there. "
    " You took your seat respectfully and listened to whatever the teacher was saying. "
    show msthravelneutral at center with easeinleft
    mst " ...We're going to be having an assignment that's due next week wednesday. "
    mst " Engel's going to send it in your GC for you all to do on the weekends! "
    mst " Oh, and other days, of course. "
    mst " (Hm...I do wonder where Oliver, Zip, and Edward are...) "
    mst " (Oh well, not like I care!) "
    mst " (They're my favorite students after all.) "
    mst " (I'll just let them do whatever they want, hehe.) "
    mst " Ahem! "
    mst " If you have a question for me about the assignment, please ask me about it once our class is over. "
    mst " I'd rather just get into our lesson now, I don't want to waste time. "
    mst " Aaaanyway, get your notebooks and pens out... "
    mst " ...For some more note taking! "
    mst " Hopefully your hands are still working and ready for notetaking. "
    mst " If not, then too bad! "
    scene black with dissolve
    " You spent the rest of class taking down notes. "
    if oligangjoin == False:
        " Three students seemed to arrive late... "
        " But it seemed ilke the teacher didn't even care. "
    else:
        " Looks like the teacher didn't mind that you and the gang showed up late. "
        " Interesting... "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for another break. "
    " You got up from your seat and walked out of your classroom to go to the hallways. "
    pause 2.0
    jump thursbreak2

label thursbreak2:
    scene hallway with dissolve
    if oligangjoin == True:
        jump thursoligang2
    else:
        pass
    " Where do you wanna go for this break? "
    menu:
        " {image=rubyicon} The front of the school {image=cubbieicon} ":
            jump thursfrontschool2
        " {image=skellicon} The back of the school {image=robbyicon} ":
            jump thursbackschool2
        "  {image=abbieicon} The gym {image=kevinicon} ":
            jump thursgym2
        " {image=engelicon} The cafeteria {image=rileyicon} ":
            jump thurscafeteria2
        " {image=popularicon} The rooftop {image=bubbleicon} ":
            jump thursrooftop2
        " {image=claireicon} The library {image=popularicon} ":
            jump thurslibrary2

label thursfrontschool2:
    # cubbie and ruby
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of the school and spotted two of your classmates talking with eachother. "
    " Wondering what they're talking about, you decided to join their conversation. "
    show cubbieneutral at right with easeinleft
    show rubyneutral at left with easeinleft
    if cubbieknow == True and rubyknow == True:
        ru " I know that your voice sounds good, Cubbie! "
        ru " You trusted me enough so that I could hear it... "
        ru " No matter what everyone else says - I've always got your back! "
        ru " It's what friends are for, after all! "
        cb " ... "
        " The person Ruby was talking to didn't look like they believed her. "
        " But, regardless - they still looked thankful for her words. "
        " After it got a bit quiet, you decided to make them acknowledge your existence by coughing. "
        hide rubyneutral at bottom
        show rubyhappy at left
        ru " Oh heeeyy, [name]! "
        ru " My friend Cubbie over here was just feeling a little insecure over his voice. "
        ru " Aaaaand I reassured him about it! "
        hide rubyhappy at bottom
        show rubysad at left
        ru " Though it looks like he doesn't really believe me... "
        ru " I don't really like it when people who are literally so perfect judge themselves... "
        ru " I just don't get how people can view themselves so horribly! "
        cb " ... "
        " Even without speaking, Cubbie looks like he's reassuring Ruby that he was fine. "
        " It was just his thoughts speaking to him about how disguting his voice sounded. "
        " Though of course, those are just thoughts and not actual facts. "
        " Very strong thoughts, though. "
        menu:
            " Tell Cubbie something nice ":
                hide rubysad at bottom
                show rubyneutral at left
                $ cubbielv += 10
                " You told Cubbie something nice about his voice... "
                " ...Even though you didn't hear it yet, you're sure that he sounds alright. "
                " Not everyone has a perfect voice anyway. "
                " Everyone's different and that's okay, it shouldn't be a reason to beat ourselves up for it. "
                " Even if you don't got a voice like a singer, your voice is still unique in it's own way. "
                " Even if you don't think so - there's always people out there who will love you for who you are. "
                " And will love your voice for how it sounds. "
                hide cubbieneutral at bottom
                show cubbiehappy at right
                cb " ...:D! "
                " Looks like Cubbie felt a little more happier when he heard your words. "
                " Mission successful, you made him happy. "
                hide rubyneutral at bottom
                show rubyhappy at left
                ru " Aw, [name]! "
                ru " You got him to smile, that's nice! "
                ru " [name] has a point, Cubbie... "
                ru " We'll always love you for who you are, because we're your bestest of friends! "
                ru " We'll always have your back, even in the darkest of hours! "
                ru " Everytime your thoughts kick in, make sure to tell us what's going on, okay? "
                hide rubyhappy at bottom
                show rubyneutral at left
                ru " Of course, only when you're comfortable and whatnot. "
                ru " We don't want to force you if you don't want to say! "
                cb " :) "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Cubbie. "
                " If any one of you is struggling with insecurities, just know that there's someone out there who loves you for who you are. "
                " Even if there's no one right now, doesn't mean that there's not gonna be anyone in the future. "
                " Like they say - everything's gonna be okay, you're just going to have to deal with the pains for a bit. "
                " The pains for now, but in the future, you'll get your well deserved rest. <3 "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You got back into the school and went to your classroom for your next class. "
                pause 2.0
                jump scienceclassthurs
            " Comfort Ruby ":
                # ruby still sad
                $ rubylv += 10
                " You told Ruby that having insecurities was a normal thing for other people. "
                " Though some might have none, there are others who think that they have a lot. "
                " It's mostly a normal thing to happen during teenage years, but it doesn't mean that it's good. "
                " People who think about their insecurities too much kinda lose themselves trying to make themselves look better. "
                " When in reality, they look just fine. "
                " Even if they don't look fine in their own eyes, there's always gonna be people who are gonna love them for who they are. "
                " And even if it looks like no one likes them right now, "
                " It doesn't mean that someone who would like them wouldn't appear in the future. "
                " You've just gotta wait for the right time for them to show up. "
                " Always stay hopeful, even in the darkest of times in your life. "
                hide rubysad at bottom
                show rubyneutral at left
                ru " Wow, [name]... "
                ru " Those were some really inspiring words to hear from you...! "
                ru " Not only did I get some new advice... "
                ru " But I also learnt a lot from you! "
                ru " Thank you, truly, [name]. "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Cubbie. "
                " If any one of you is struggling with insecurities, just know that there's someone out there who loves you for who you are. "
                " Even if there's no one right now, doesn't mean that there's not gonna be anyone in the future. "
                " Like they say - everything's gonna be okay, you're just going to have to deal with the pains for a bit. "
                " The pains for now, but in the future, you'll get your well deserved rest. <3 "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You got back into the school and went to your classroom for your next class. "
                pause 2.0
                jump scienceclassthurs
            " man idk what to say tbh lets just stay quiet ":
                hide rubysad at bottom
                show rubyneutral at left
                ru " Anyway, I've gotta change the topic before things get too sad... "
                ru " Processing on what to talk about... "
                ru " ...Hm, have you guys seen the whole AI thing? "
                cb " ...? "
                " Cubbie isn't sure of what Ruby was talking about. "
                " You've heard a lot of things about AI, so you weren't sure on what Ruby was talking about. "
                ru " There's this app where you can talk to your favorite characters! "
                ru " They're just AI though. "
                ru " But still, I've heard that it's pretty great! "
                ru " Lots of people use it daily, and...should I actually be concerned about that? "
                ru " Most likely. "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Cubbie. "
                " You feel like you've heard about that whole AI thing before... "
                " Can't really put a finger on where though. "
                " Oh well, it's probably not that important anyway. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked back into the school and went to your classroom for the next class. "
                pause 2.0
                jump scienceclassthurs
    elif cubbieknow == True and rubyknow == False:
        x " I know that your voice sounds good, Cubbie! "
        x " You trusted me enough so that I could hear it... "
        x " No matter what everyone else says - I've always got your back! "
        x " It's what friends are for, after all! "
        cb " ... "
        " The person that girl was talking to didn't look like they believed her. "
        " But, regardless - they still looked thankful for her words. "
        " After it got a bit quiet, you decided to make them acknowledge your existence by coughing. "
        hide rubyneutral at bottom
        show rubyhappy at left
        x " Oh heeeyy, [name]! "
        x " Hold on there just a moment... "
        x " I don't think I've got to introduce myself to you yet before! "
        x " Silly me...I was supposed to introduce myself on monday! Sorry... "
        $ rubyknow = True
        ru " I'm Ruby, it's nice to meet you! "
        ru " My friend Cubbie over here was just feeling a little insecure over his voice. "
        ru " Aaaaand I reassured him about it! "
        hide rubyhappy at bottom
        show rubysad at left
        ru " Though it looks like he doesn't really believe me... "
        ru " I don't really like it when people who are literally so perfect judge themselves... "
        ru " I just don't get how people can view themselves so horribly! "
        cb " ... "
        " Even without speaking, Cubbie looks like he's reassuring Ruby that he was fine. "
        " It was just his thoughts speaking to him about how disguting his voice sounded. "
        " Though of course, those are just thoughts and not actual facts. "
        " Very strong thoughts, though. "
        menu:
            " Tell Cubbie something nice ":
                hide rubysad at bottom
                show rubyneutral at left
                $ cubbielv += 10
                " You told Cubbie something nice about his voice... "
                " ...Even though you didn't hear it yet, you're sure that he sounds alright. "
                " Not everyone has a perfect voice anyway. "
                " Everyone's different and that's okay, it shouldn't be a reason to beat ourselves up for it. "
                " Even if you don't got a voice like a singer, your voice is still unique in it's own way. "
                " Even if you don't think so - there's always people out there who will love you for who you are. "
                " And will love your voice for how it sounds. "
                hide cubbieneutral at bottom
                show cubbiehappy at right
                cb " ...:D! "
                " Looks like Cubbie felt a little more happier when he heard your words. "
                " Mission successful, you made him happy. "
                hide rubyneutral at bottom
                show rubyhappy at left
                ru " Aw, [name]! "
                ru " You got him to smile, that's nice! "
                ru " [name] has a point, Cubbie... "
                ru " We'll always love you for who you are, because we're your bestest of friends! "
                ru " We'll always have your back, even in the darkest of hours! "
                ru " Everytime your thoughts kick in, make sure to tell us what's going on, okay? "
                hide rubyhappy at bottom
                show rubyneutral at left
                ru " Of course, only when you're comfortable and whatnot. "
                ru " We don't want to force you if you don't want to say! "
                cb " :) "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Cubbie. "
                " If any one of you is struggling with insecurities, just know that there's someone out there who loves you for who you are. "
                " Even if there's no one right now, doesn't mean that there's not gonna be anyone in the future. "
                " Like they say - everything's gonna be okay, you're just going to have to deal with the pains for a bit. "
                " The pains for now, but in the future, you'll get your well deserved rest. <3 "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You got back into the school and went to your classroom for your next class. "
                pause 2.0
                jump scienceclassthurs
            " Comfort Ruby ":
                # ruby still sad
                $ rubylv += 10
                " You told Ruby that having insecurities was a normal thing for other people. "
                " Though some might have none, there are others who think that they have a lot. "
                " It's mostly a normal thing to happen during teenage years, but it doesn't mean that it's good. "
                " People who think about their insecurities too much kinda lose themselves trying to make themselves look better. "
                " When in reality, they look just fine. "
                " Even if they don't look fine in their own eyes, there's always gonna be people who are gonna love them for who they are. "
                " And even if it looks like no one likes them right now, "
                " It doesn't mean that someone who would like them wouldn't appear in the future. "
                " You've just gotta wait for the right time for them to show up. "
                " Always stay hopeful, even in the darkest of times in your life. "
                hide rubysad at bottom
                show rubyneutral at left
                ru " Wow, [name]... "
                ru " Those were some really inspiring words to hear from you...! "
                ru " Not only did I get some new advice... "
                ru " But I also learnt a lot from you! "
                ru " Thank you, truly, [name]. "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Cubbie. "
                " If any one of you is struggling with insecurities, just know that there's someone out there who loves you for who you are. "
                " Even if there's no one right now, doesn't mean that there's not gonna be anyone in the future. "
                " Like they say - everything's gonna be okay, you're just going to have to deal with the pains for a bit. "
                " The pains for now, but in the future, you'll get your well deserved rest. <3 "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You got back into the school and went to your classroom for your next class. "
                pause 2.0
                jump scienceclassthurs
            " man idk what to say tbh lets just stay quiet ":
                hide rubysad at bottom
                show rubyneutral at left
                ru " Anyway, I've gotta change the topic before things get too sad... "
                ru " Processing on what to talk about... "
                ru " ...Hm, have you guys seen the whole AI thing? "
                cb " ...? "
                " Cubbie isn't sure of what Ruby was talking about. "
                " You've heard a lot of things about AI, so you weren't sure on what Ruby was talking about. "
                ru " There's this app where you can talk to your favorite characters! "
                ru " They're just AI though. "
                ru " But still, I've heard that it's pretty great! "
                ru " Lots of people use it daily, and...should I actually be concerned about that? "
                ru " Most likely. "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Cubbie. "
                " You feel like you've heard about that whole AI thing before... "
                " Can't really put a finger on where though. "
                " Oh well, it's probably not that important anyway. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked back into the school and went to your classroom for the next class. "
                pause 2.0
                jump scienceclassthurs
    elif cubbieknow == False and rubyknow == True:
        ru " I know that your voice sounds good, Cubbie! "
        ru " You trusted me enough so that I could hear it... "
        ru " No matter what everyone else says - I've always got your back! "
        ru " It's what friends are for, after all! "
        x " ... "
        " The person Ruby was talking to didn't look like they believed her. "
        " But, regardless - they still looked thankful for her words. "
        " After it got a bit quiet, you decided to make them acknowledge your existence by coughing. "
        hide rubyneutral at bottom
        show rubyhappy at left
        ru " Oh heeeyy, [name]! "
        $ cubbieknow = True
        ru " My friend Cubbie over here was just feeling a little insecure over his voice. "
        ru " Aaaaand I reassured him about it! "
        hide rubyhappy at bottom
        show rubysad at left
        ru " Though it looks like he doesn't really believe me... "
        ru " I don't really like it when people who are literally so perfect judge themselves... "
        ru " I just don't get how people can view themselves so horribly! "
        cb " ... "
        " Even without speaking, Cubbie looks like he's reassuring Ruby that he was fine. "
        " It was just his thoughts speaking to him about how disguting his voice sounded. "
        " Though of course, those are just thoughts and not actual facts. "
        " Very strong thoughts, though. "
        menu:
            " Tell Cubbie something nice ":
                hide rubysad at bottom
                show rubyneutral at left
                $ cubbielv += 10
                " You told Cubbie something nice about his voice... "
                " ...Even though you didn't hear it yet, you're sure that he sounds alright. "
                " Not everyone has a perfect voice anyway. "
                " Everyone's different and that's okay, it shouldn't be a reason to beat ourselves up for it. "
                " Even if you don't got a voice like a singer, your voice is still unique in it's own way. "
                " Even if you don't think so - there's always people out there who will love you for who you are. "
                " And will love your voice for how it sounds. "
                hide cubbieneutral at bottom
                show cubbiehappy at right
                cb " ...:D! "
                " Looks like Cubbie felt a little more happier when he heard your words. "
                " Mission successful, you made him happy. "
                hide rubyneutral at bottom
                show rubyhappy at left
                ru " Aw, [name]! "
                ru " You got him to smile, that's nice! "
                ru " [name] has a point, Cubbie... "
                ru " We'll always love you for who you are, because we're your bestest of friends! "
                ru " We'll always have your back, even in the darkest of hours! "
                ru " Everytime your thoughts kick in, make sure to tell us what's going on, okay? "
                hide rubyhappy at bottom
                show rubyneutral at left
                ru " Of course, only when you're comfortable and whatnot. "
                ru " We don't want to force you if you don't want to say! "
                cb " :) "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Cubbie. "
                " If any one of you is struggling with insecurities, just know that there's someone out there who loves you for who you are. "
                " Even if there's no one right now, doesn't mean that there's not gonna be anyone in the future. "
                " Like they say - everything's gonna be okay, you're just going to have to deal with the pains for a bit. "
                " The pains for now, but in the future, you'll get your well deserved rest. <3 "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You got back into the school and went to your classroom for your next class. "
                pause 2.0
                jump scienceclassthurs
            " Comfort Ruby ":
                # ruby still sad
                $ rubylv += 10
                " You told Ruby that having insecurities was a normal thing for other people. "
                " Though some might have none, there are others who think that they have a lot. "
                " It's mostly a normal thing to happen during teenage years, but it doesn't mean that it's good. "
                " People who think about their insecurities too much kinda lose themselves trying to make themselves look better. "
                " When in reality, they look just fine. "
                " Even if they don't look fine in their own eyes, there's always gonna be people who are gonna love them for who they are. "
                " And even if it looks like no one likes them right now, "
                " It doesn't mean that someone who would like them wouldn't appear in the future. "
                " You've just gotta wait for the right time for them to show up. "
                " Always stay hopeful, even in the darkest of times in your life. "
                hide rubysad at bottom
                show rubyneutral at left
                ru " Wow, [name]... "
                ru " Those were some really inspiring words to hear from you...! "
                ru " Not only did I get some new advice... "
                ru " But I also learnt a lot from you! "
                ru " Thank you, truly, [name]. "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Cubbie. "
                " If any one of you is struggling with insecurities, just know that there's someone out there who loves you for who you are. "
                " Even if there's no one right now, doesn't mean that there's not gonna be anyone in the future. "
                " Like they say - everything's gonna be okay, you're just going to have to deal with the pains for a bit. "
                " The pains for now, but in the future, you'll get your well deserved rest. <3 "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You got back into the school and went to your classroom for your next class. "
                pause 2.0
                jump scienceclassthurs
            " man idk what to say tbh lets just stay quiet ":
                hide rubysad at bottom
                show rubyneutral at left
                ru " Anyway, I've gotta change the topic before things get too sad... "
                ru " Processing on what to talk about... "
                ru " ...Hm, have you guys seen the whole AI thing? "
                cb " ...? "
                " Cubbie isn't sure of what Ruby was talking about. "
                " You've heard a lot of things about AI, so you weren't sure on what Ruby was talking about. "
                ru " There's this app where you can talk to your favorite characters! "
                ru " They're just AI though. "
                ru " But still, I've heard that it's pretty great! "
                ru " Lots of people use it daily, and...should I actually be concerned about that? "
                ru " Most likely. "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Cubbie. "
                " You feel like you've heard about that whole AI thing before... "
                " Can't really put a finger on where though. "
                " Oh well, it's probably not that important anyway. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked back into the school and went to your classroom for the next class. "
                pause 2.0
                jump scienceclassthurs
    else:
        x " I know that your voice sounds good, Cubbie! "
        x " You trusted me enough so that I could hear it... "
        x " No matter what everyone else says - I've always got your back! "
        x " It's what friends are for, after all! "
        x " ... "
        " The person that girl was talking to didn't look like they believed her. "
        " But, regardless - they still looked thankful for her words. "
        " After it got a bit quiet, you decided to make them acknowledge your existence by coughing. "
        hide rubyneutral at bottom
        show rubyhappy at left
        x " Oh heeeyy, [name]! "
        x " Hold on there just a moment... "
        x " I don't think I've got to introduce myself to you yet before! "
        x " Silly me...I was supposed to introduce myself on monday! Sorry... "
        $ rubyknow = True
        ru " I'm Ruby, it's nice to meet you! "
        $ cubbieknow = True
        ru " My friend Cubbie over here was just feeling a little insecure over his voice. "
        ru " Aaaaand I reassured him about it! "
        hide rubyhappy at bottom
        show rubysad at left
        ru " Though it looks like he doesn't really believe me... "
        ru " I don't really like it when people who are literally so perfect judge themselves... "
        ru " I just don't get how people can view themselves so horribly! "
        cb " ... "
        " Even without speaking, Cubbie looks like he's reassuring Ruby that he was fine. "
        " It was just his thoughts speaking to him about how disguting his voice sounded. "
        " Though of course, those are just thoughts and not actual facts. "
        " Very strong thoughts, though. "
        menu:
            " Tell Cubbie something nice ":
                hide rubysad at bottom
                show rubyneutral at left
                $ cubbielv += 10
                " You told Cubbie something nice about his voice... "
                " ...Even though you didn't hear it yet, you're sure that he sounds alright. "
                " Not everyone has a perfect voice anyway. "
                " Everyone's different and that's okay, it shouldn't be a reason to beat ourselves up for it. "
                " Even if you don't got a voice like a singer, your voice is still unique in it's own way. "
                " Even if you don't think so - there's always people out there who will love you for who you are. "
                " And will love your voice for how it sounds. "
                hide cubbieneutral at bottom
                show cubbiehappy at right
                cb " ...:D! "
                " Looks like Cubbie felt a little more happier when he heard your words. "
                " Mission successful, you made him happy. "
                hide rubyneutral at bottom
                show rubyhappy at left
                ru " Aw, [name]! "
                ru " You got him to smile, that's nice! "
                ru " [name] has a point, Cubbie... "
                ru " We'll always love you for who you are, because we're your bestest of friends! "
                ru " We'll always have your back, even in the darkest of hours! "
                ru " Everytime your thoughts kick in, make sure to tell us what's going on, okay? "
                hide rubyhappy at bottom
                show rubyneutral at left
                ru " Of course, only when you're comfortable and whatnot. "
                ru " We don't want to force you if you don't want to say! "
                cb " :) "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Cubbie. "
                " If any one of you is struggling with insecurities, just know that there's someone out there who loves you for who you are. "
                " Even if there's no one right now, doesn't mean that there's not gonna be anyone in the future. "
                " Like they say - everything's gonna be okay, you're just going to have to deal with the pains for a bit. "
                " The pains for now, but in the future, you'll get your well deserved rest. <3 "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You got back into the school and went to your classroom for your next class. "
                pause 2.0
                jump scienceclassthurs
            " Comfort Ruby ":
                # ruby still sad
                $ rubylv += 10
                " You told Ruby that having insecurities was a normal thing for other people. "
                " Though some might have none, there are others who think that they have a lot. "
                " It's mostly a normal thing to happen during teenage years, but it doesn't mean that it's good. "
                " People who think about their insecurities too much kinda lose themselves trying to make themselves look better. "
                " When in reality, they look just fine. "
                " Even if they don't look fine in their own eyes, there's always gonna be people who are gonna love them for who they are. "
                " And even if it looks like no one likes them right now, "
                " It doesn't mean that someone who would like them wouldn't appear in the future. "
                " You've just gotta wait for the right time for them to show up. "
                " Always stay hopeful, even in the darkest of times in your life. "
                hide rubysad at bottom
                show rubyneutral at left
                ru " Wow, [name]... "
                ru " Those were some really inspiring words to hear from you...! "
                ru " Not only did I get some new advice... "
                ru " But I also learnt a lot from you! "
                ru " Thank you, truly, [name]. "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Cubbie. "
                " If any one of you is struggling with insecurities, just know that there's someone out there who loves you for who you are. "
                " Even if there's no one right now, doesn't mean that there's not gonna be anyone in the future. "
                " Like they say - everything's gonna be okay, you're just going to have to deal with the pains for a bit. "
                " The pains for now, but in the future, you'll get your well deserved rest. <3 "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You got back into the school and went to your classroom for your next class. "
                pause 2.0
                jump scienceclassthurs
            " man idk what to say tbh lets just stay quiet ":
                hide rubysad at bottom
                show rubyneutral at left
                ru " Anyway, I've gotta change the topic before things get too sad... "
                ru " Processing on what to talk about... "
                ru " ...Hm, have you guys seen the whole AI thing? "
                cb " ...? "
                " Cubbie isn't sure of what Ruby was talking about. "
                " You've heard a lot of things about AI, so you weren't sure on what Ruby was talking about. "
                ru " There's this app where you can talk to your favorite characters! "
                ru " They're just AI though. "
                ru " But still, I've heard that it's pretty great! "
                ru " Lots of people use it daily, and...should I actually be concerned about that? "
                ru " Most likely. "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Cubbie. "
                " You feel like you've heard about that whole AI thing before... "
                " Can't really put a finger on where though. "
                " Oh well, it's probably not that important anyway. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked back into the school and went to your classroom for the next class. "
                pause 2.0
                jump scienceclassthurs
label thursbackschool2:
    # skell and robby
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school and spotted two of your classmates talking with eachother. "
    " Being curious about what they're talking about, you walked over to listen to their conversation. "
    show robbyneutral at left with easeinright
    show skellneutral at right with easeinright
    if robbyknow == True and skellknow == True:
        rb " I don't know, Skell. "
        rb " I don't know if she'll even listen to me at this rate... "
        sk " You tried talking to her about it? "
        rb " Well I {i}tried{/i} talking to her about the conversation I'm going to have with her next break... "
        hide robbyneutral at bottom
        show robbyangry at left
        rb " But she kept going on and on about her new creation! "
        rb " What's it called...Olibot??? "
        rb " Now that name just sounds so, so...SO STUPID!! "
        rb " And that's not the only thing that's stupid - it's the fact that she kept pushing me to make it! "
        rb " Like, hello? Can't you read the damn ROOM?! "
        rb " I clearly don't feel like talking to you right now about that new thing you want me to make - "
        sk " Robby, breathe. "
        rb " - And how about talking to Oliver himself if you want something new?! "
        rb " Surely he'd enjoy hearing all those compliments about himself rather than talking about it to me - "
        hide skellneutral at bottom
        show skellsad at right
        sk " Robby... "
        sk " I get that you're mad, but you've gotta calm down... "
        rb " And she's just a real nuisance to talk to! "
        rb " Sometimes I wonder why I even put up with her! "
        rb " God, all of this just makes me wanna - "
        menu:
            " *violently shake him out of it* ":
                $ robbrileylv += 10
                hide robbyangry at bottom
                show robbyneutral at left
                rb " HUH - ?! "
                " You started violently shaking Robby out of his little rant. "
                " You didn't know how else you were gonna get him out of his ranting session, so you did this. "
                " Eventually, you stopped and surprisingly, it got him to calm down. "
                " The weird things you could get people to calm down... "
                rb " Uh, sorry for suddenly ranting like that. "
                rb " Thanks for snapping me out of it, [name]. "
                " You just gave him a thumbs up as a 'you're welcome'. "
                rb " But, yeah... Riley HAS been wearing me out a lot. "
                rb " She's just gotta understand that sometimes there's times where I don't want to talk to her. "
                rb " And that there's times that I just don't feel like doing anything. "
                rb " While it is fun to talk to her... "
                rb " It's also a little painful to try and get her to tone down her energy sometimes. "
                hide skellsad at bottom
                show skellneutral at right
                sk " But you ARE planning to tell her about all this later, right? "
                sk " If you are, just make sure to play with your words right. "
                sk " Otherwise she's just going to throw a whole fit over it. "
                rb " Yeah, yeah... "
                rb " I know that, but thanks for telling me anyway. "
                scene black with dissolve
                " You spent the rest of the break talking with Robby and Skell. "
                " If you didn't stop Robby from talking there... "
                " I'm pretty sure that he'd go on and on until the bell rang. "
                " Good thing you stopped him though. "
                " I wouldn't want to write an entire paragraph that would make this game's code 20k lines long. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump scienceclassthurs
            " Do absolutely nothing about this ":
                " If you had popcorn, you'd be eating that thing UP. "
                " The imaginary popcorn that somehow pops up whenever there's a dramatic scene...a classic. "
                sk " Oh boy... "
                sk " He's gonna be at this for the entire break, isn't he... "
                sk " Might as well my headsets... "
                sk " There's no way I'm listening to all of this. "
                scene black with dissolve
                " You spent the rest of the break listening to Robby rant. "
                " You weren't listening into it that much since you were playing a game of ping pong in your head... "
                " ...But you did hear a lot of stuff about Riley being annoying. "
                " Hopefully Riley didn't walk by listen to everything Robby just said. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump scienceclassthurs
    elif robbyknow == True and skellknow == False:
        rb " I don't know, Skell. "
        $ skellknow = True
        rb " I don't know if she'll even listen to me at this rate... "
        sk " You tried talking to her about it? "
        rb " Well I {i}tried{/i} talking to her about the conversation I'm going to have with her next break... "
        hide robbyneutral at bottom
        show robbyangry at left
        rb " But she kept going on and on about her new creation! "
        rb " What's it called...Olibot??? "
        rb " Now that name just sounds so, so...SO STUPID!! "
        rb " And that's not the only thing that's stupid - it's the fact that she kept pushing me to make it! "
        rb " Like, hello? Can't you read the damn ROOM?! "
        rb " I clearly don't feel like talking to you right now about that new thing you want me to make - "
        sk " Robby, breathe. "
        rb " - And how about talking to Oliver himself if you want something new?! "
        rb " Surely he'd enjoy hearing all those compliments about himself rather than talking about it to me - "
        hide skellneutral at bottom
        show skellsad at right
        sk " Robby... "
        sk " I get that you're mad, but you've gotta calm down... "
        rb " And she's just a real nuisance to talk to! "
        rb " Sometimes I wonder why I even put up with her! "
        rb " God, all of this just makes me wanna - "
        menu:
            " *violently shake him out of it* ":
                $ robbrileylv += 10
                hide robbyangry at bottom
                show robbyneutral at left
                rb " HUH - ?! "
                " You started violently shaking Robby out of his little rant. "
                " You didn't know how else you were gonna get him out of his ranting session, so you did this. "
                " Eventually, you stopped and surprisingly, it got him to calm down. "
                " The weird things you could get people to calm down... "
                rb " Uh, sorry for suddenly ranting like that. "
                rb " Thanks for snapping me out of it, [name]. "
                " You just gave him a thumbs up as a 'you're welcome'. "
                rb " But, yeah... Riley HAS been wearing me out a lot. "
                rb " She's just gotta understand that sometimes there's times where I don't want to talk to her. "
                rb " And that there's times that I just don't feel like doing anything. "
                rb " While it is fun to talk to her... "
                rb " It's also a little painful to try and get her to tone down her energy sometimes. "
                hide skellsad at bottom
                show skellneutral at right
                sk " But you ARE planning to tell her about all this later, right? "
                sk " If you are, just make sure to play with your words right. "
                sk " Otherwise she's just going to throw a whole fit over it. "
                rb " Yeah, yeah... "
                rb " I know that, but thanks for telling me anyway. "
                scene black with dissolve
                " You spent the rest of the break talking with Robby and Skell. "
                " If you didn't stop Robby from talking there... "
                " I'm pretty sure that he'd go on and on until the bell rang. "
                " Good thing you stopped him though. "
                " I wouldn't want to write an entire paragraph that would make this game's code 20k lines long. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump scienceclassthurs
            " Do absolutely nothing about this ":
                " If you had popcorn, you'd be eating that thing UP. "
                " The imaginary popcorn that somehow pops up whenever there's a dramatic scene...a classic. "
                sk " Oh boy... "
                sk " He's gonna be at this for the entire break, isn't he... "
                sk " Might as well my headsets... "
                sk " There's no way I'm listening to all of this. "
                scene black with dissolve
                " You spent the rest of the break listening to Robby rant. "
                " You weren't listening into it that much since you were playing a game of ping pong in your head... "
                " ...But you did hear a lot of stuff about Riley being annoying. "
                " Hopefully Riley didn't walk by listen to everything Robby just said. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump scienceclassthurs
    elif robbyknow == False and skellknow == True:
        x " I don't know, Skell. "
        x " I don't know if she'll even listen to me at this rate... "
        sk " You tried talking to her about it? "
        x " Well I {i}tried{/i} talking to her about the conversation I'm going to have with her next break... "
        hide robbyneutral at bottom
        show robbyangry at left
        x " But she kept going on and on about her new creation! "
        x " What's it called...Olibot??? "
        x " Now that name just sounds so, so...SO STUPID!! "
        x " And that's not the only thing that's stupid - it's the fact that she kept pushing me to make it! "
        x " Like, hello? Can't you read the damn ROOM?! "
        x " I clearly don't feel like talking to you right now about that new thing you want me to make - "
        $ robbyknow = True
        sk " Robby, breathe. "
        rb " - And how about talking to Oliver himself if you want something new?! "
        rb " Surely he'd enjoy hearing all those compliments about himself rather than talking about it to me - "
        hide skellneutral at bottom
        show skellsad at right
        sk " Robby... "
        sk " I get that you're mad, but you've gotta calm down... "
        rb " And she's just a real nuisance to talk to! "
        rb " Sometimes I wonder why I even put up with her! "
        rb " God, all of this just makes me wanna - "
        menu:
            " *violently shake him out of it* ":
                $ robbrileylv += 10
                hide robbyangry at bottom
                show robbyneutral at left
                rb " HUH - ?! "
                " You started violently shaking Robby out of his little rant. "
                " You didn't know how else you were gonna get him out of his ranting session, so you did this. "
                " Eventually, you stopped and surprisingly, it got him to calm down. "
                " The weird things you could get people to calm down... "
                rb " Uh, sorry for suddenly ranting like that. "
                rb " Thanks for snapping me out of it, [name]. "
                " You just gave him a thumbs up as a 'you're welcome'. "
                rb " But, yeah... Riley HAS been wearing me out a lot. "
                rb " She's just gotta understand that sometimes there's times where I don't want to talk to her. "
                rb " And that there's times that I just don't feel like doing anything. "
                rb " While it is fun to talk to her... "
                rb " It's also a little painful to try and get her to tone down her energy sometimes. "
                hide skellsad at bottom
                show skellneutral at right
                sk " But you ARE planning to tell her about all this later, right? "
                sk " If you are, just make sure to play with your words right. "
                sk " Otherwise she's just going to throw a whole fit over it. "
                rb " Yeah, yeah... "
                rb " I know that, but thanks for telling me anyway. "
                scene black with dissolve
                " You spent the rest of the break talking with Robby and Skell. "
                " If you didn't stop Robby from talking there... "
                " I'm pretty sure that he'd go on and on until the bell rang. "
                " Good thing you stopped him though. "
                " I wouldn't want to write an entire paragraph that would make this game's code 20k lines long. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump scienceclassthurs
            " Do absolutely nothing about this ":
                " If you had popcorn, you'd be eating that thing UP. "
                " The imaginary popcorn that somehow pops up whenever there's a dramatic scene...a classic. "
                sk " Oh boy... "
                sk " He's gonna be at this for the entire break, isn't he... "
                sk " Might as well my headsets... "
                sk " There's no way I'm listening to all of this. "
                scene black with dissolve
                " You spent the rest of the break listening to Robby rant. "
                " You weren't listening into it that much since you were playing a game of ping pong in your head... "
                " ...But you did hear a lot of stuff about Riley being annoying. "
                " Hopefully Riley didn't walk by listen to everything Robby just said. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump scienceclassthurs
    else:
        x " I don't know, Skell. "
        $ skellknow = True
        x " I don't know if she'll even listen to me at this rate... "
        sk " You tried talking to her about it? "
        x " Well I {i}tried{/i} talking to her about the conversation I'm going to have with her next break... "
        hide robbyneutral at bottom
        show robbyangry at left
        x " But she kept going on and on about her new creation! "
        x " What's it called...Olibot??? "
        x " Now that name just sounds so, so...SO STUPID!! "
        x " And that's not the only thing that's stupid - it's the fact that she kept pushing me to make it! "
        x " Like, hello? Can't you read the damn ROOM?! "
        x " I clearly don't feel like talking to you right now about that new thing you want me to make - "
        $ robbyknow = True
        sk " Robby, breathe. "
        rb " - And how about talking to Oliver himself if you want something new?! "
        rb " Surely he'd enjoy hearing all those compliments about himself rather than talking about it to me - "
        hide skellneutral at bottom
        show skellsad at right
        sk " Robby... "
        sk " I get that you're mad, but you've gotta calm down... "
        rb " And she's just a real nuisance to talk to! "
        rb " Sometimes I wonder why I even put up with her! "
        rb " God, all of this just makes me wanna - "
        menu:
            " *violently shake him out of it* ":
                $ robbrileylv += 10
                hide robbyangry at bottom
                show robbyneutral at left
                rb " HUH - ?! "
                " You started violently shaking Robby out of his little rant. "
                " You didn't know how else you were gonna get him out of his ranting session, so you did this. "
                " Eventually, you stopped and surprisingly, it got him to calm down. "
                " The weird things you could get people to calm down... "
                rb " Uh, sorry for suddenly ranting like that. "
                rb " Thanks for snapping me out of it, [name]. "
                " You just gave him a thumbs up as a 'you're welcome'. "
                rb " But, yeah... Riley HAS been wearing me out a lot. "
                rb " She's just gotta understand that sometimes there's times where I don't want to talk to her. "
                rb " And that there's times that I just don't feel like doing anything. "
                rb " While it is fun to talk to her... "
                rb " It's also a little painful to try and get her to tone down her energy sometimes. "
                hide skellsad at bottom
                show skellneutral at right
                sk " But you ARE planning to tell her about all this later, right? "
                sk " If you are, just make sure to play with your words right. "
                sk " Otherwise she's just going to throw a whole fit over it. "
                rb " Yeah, yeah... "
                rb " I know that, but thanks for telling me anyway. "
                scene black with dissolve
                " You spent the rest of the break talking with Robby and Skell. "
                " If you didn't stop Robby from talking there... "
                " I'm pretty sure that he'd go on and on until the bell rang. "
                " Good thing you stopped him though. "
                " I wouldn't want to write an entire paragraph that would make this game's code 20k lines long. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump scienceclassthurs
            " Do absolutely nothing about this ":
                " If you had popcorn, you'd be eating that thing UP. "
                " The imaginary popcorn that somehow pops up whenever there's a dramatic scene...a classic. "
                sk " Oh boy... "
                sk " He's gonna be at this for the entire break, isn't he... "
                sk " Might as well my headsets... "
                sk " There's no way I'm listening to all of this. "
                scene black with dissolve
                " You spent the rest of the break listening to Robby rant. "
                " You weren't listening into it that much since you were playing a game of ping pong in your head... "
                " ...But you did hear a lot of stuff about Riley being annoying. "
                " Hopefully Riley didn't walk by listen to everything Robby just said. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked back into the school and went to your classroom. "
                pause 2.0
                jump scienceclassthurs
label thursgym2:
    # abbie and kevin
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked into the gym and spotted your classmates doing their own things. "
    " Who do you talk to? "
    if abbieknow == True and kevinknow == True:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump sugarappleinstock
            " {image=kevinicon} Kevin {image=kevinicon} ":
                jump elderstrawberryinstock
    elif abbieknow == True and kevinknow == False:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump sugarappleinstock
            " {image=kevinicon} A nerd {image=kevinicon} ":
                jump elderstrawberryinstock
    elif abbieknow == False and kevinknow == True:
        menu:
            " {image=abbieicon} A shy boy {image=abbieicon} ":
                jump sugarappleinstock
            " {image=kevinicon} Kevin {image=kevinicon} ":
                jump elderstrawberryinstock
    else:
        menu:
            " {image=abbieicon} A shy boy {image=abbieicon} ":
                jump sugarappleinstock
            " {image=kevinicon} A nerd {image=kevinicon} ":
                jump elderstrawberryinstock
    label sugarappleinstock:
        show abbieneutral at center with easeinleft
        if abbieknow == True:
            a " H...hello [name]... "
            a " Um... "
            a " (God, I don't know what to talk about...) "
            a " (Maybe I could talk about something random?) "
            a " (But what if [they] don't like the thing I'm gonna talk about??) "
            a " (I really don't want this to just be awkward silence...) "
            a " (I'll just go ahead and do a random topic, then...!) "
            a " (Here goes...) "
            a " A...uhh... "
            a " Have you heard of that one...gardening game...? "
            a " It's been pretty popular recently... "
            a " But...I honestly don't get why It's so popular... "
            a " I mean, the idea is nice and all... "
            a " But...why are all of the textures repeated...?? "
            a " It should've had atleast different textures for diversity... "
            a " ...And also, have you seen how overpriced certain things are...? "
            a " I get that it's supposed to keep newer players from getting them... "
            a " But...it's just too much, you get me...? "
            a " I literally saw one of the plants there costing 1B dollars... "
            a " That's just w-way too much...! "
            a " Especially for something that's base value is 200k... "
            a " How do I know this...? "
            a " I've actually played the game a bit before... "
            a " But I quit 5 days in once I noticed how bad things were... "
            a " ...And wasn't there drama with the creators...? "
            a " Drama with the creators adding to the bad down sides of the game... "
            a " ...It just makes it look worse than it already is... "
            a " I'm sorry if you like this game... "
            a " But I just don't like it myself, sorry... "
            menu:
                " I don't really like it that much either ":
                    $ abbielv += 5
                    a " Oh, uh...really? "
                    a " Glad we share the same opinion then... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Abbie. "
                    " Honestly, if you like that slop... "
                    " I'm very much concerned for you. "
                    " Please hop off your computer and touch grass. "
                    " No, sugar apple is not in stock and your braincells aren't in stock either. "
                    " Just an opinion, don't cancel me on twitter. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your science class. "
                    " You then walked to your classroom for your next class. "
                    pause 2.0
                    jump scienceclassthurs
                " I like this game though... ":
                    $ abbielv -= 5
                    a " Sorry...again... "
                    a " I didn't mean to upset you, it's just my opinion... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Abbie. "
                    " Honestly, if you like that slop... "
                    " I'm very much concerned for you. "
                    " Please hop off your computer and touch grass. "
                    " No, sugar apple is not in stock and your braincells aren't in stock either. "
                    " Just an opinion, don't cancel me on twitter. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your science class. "
                    " You then walked to your classroom for your next class. "
                    pause 2.0
                    jump scienceclassthurs
        else:
            x " H...hello [name]... "
            x " Um... "
            x " I don't think I introduced myself before...did I...? "
            x " Sorry, I forgot to do that... "
            $ abbieknow = True
            a " I'm Abbie...it's nice to meet you... "
            a " Uh... "
            a " (God, I don't know what to talk about...) "
            a " (Maybe I could talk about something random?) "
            a " (But what if [they] don't like the thing I'm gonna talk about??) "
            a " (I really don't want this to just be awkward silence...) "
            a " (I'll just go ahead and do a random topic, then...!) "
            a " (Here goes...) "
            a " A...uhh... "
            a " Have you heard of that one...gardening game...? "
            a " It's been pretty popular recently... "
            a " But...I honestly don't get why It's so popular... "
            a " I mean, the idea is nice and all... "
            a " But...why are all of the textures repeated...?? "
            a " It should've had atleast different textures for diversity... "
            a " ...And also, have you seen how overpriced certain things are...? "
            a " I get that it's supposed to keep newer players from getting them... "
            a " But...it's just too much, you get me...? "
            a " I literally saw one of the plants there costing 1B dollars... "
            a " That's just w-way too much...! "
            a " Especially for something that's base value is 200k... "
            a " How do I know this...? "
            a " I've actually played the game a bit before... "
            a " But I quit 5 days in once I noticed how bad things were... "
            a " ...And wasn't there drama with the creators...? "
            a " Drama with the creators adding to the bad down sides of the game... "
            a " ...It just makes it look worse than it already is... "
            a " I'm sorry if you like this game... "
            a " But I just don't like it myself, sorry... "
            menu:
                " I don't really like it that much either ":
                    $ abbielv += 5
                    a " Oh, uh...really? "
                    a " Glad we share the same opinion then... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Abbie. "
                    " Honestly, if you like that slop... "
                    " I'm very much concerned for you. "
                    " Please hop off your computer and touch grass. "
                    " No, sugar apple is not in stock and your braincells aren't in stock either. "
                    " Just an opinion, don't cancel me on twitter. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your science class. "
                    " You then walked to your classroom for your next class. "
                    pause 2.0
                    jump scienceclassthurs
                " I like this game though... ":
                    $ abbielv -= 5
                    a " Sorry...again... "
                    a " I didn't mean to upset you, it's just my opinion... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Abbie. "
                    " Honestly, if you like that slop... "
                    " I'm very much concerned for you. "
                    " Please hop off your computer and touch grass. "
                    " No, sugar apple is not in stock and your braincells aren't in stock either. "
                    " Just an opinion, don't cancel me on twitter. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your science class. "
                    " You then walked to your classroom for your next class. "
                    pause 2.0
                    jump scienceclassthurs
    label elderstrawberryinstock:
        show kevinneutral at center with easeinright
        if kevinknow == True:
            " You walked up to him and looked at what he was doing. "
            " From what you could see, he was looking at a video on his phone. "
            " Huh, for once, he wasn't studying. "
            " Suprisingly, really...everytime you saw this guy, he'd be seen studying almost everytime. "
            " A change like this is very, very interesting. "
            " Maybe he's been slacking off and you just didn't notice. "
            " You then coughed so that you could get his attention. "
            kv " Ah, [name]. "
            kv " Apologies that I didn't notice you sooner. "
            kv " I was just busy watching this video to educate myself... "
            hide kevinneutral at bottom
            show kevinhappy at center
            kv " ...And I'll tell you - it's great! "
            kv " I'm learning new things that I haven't before! "
            kv " Well, I do that daily whenever I come here, but still - "
            kv " This video is great for students who are struggling a bit in behvaior.. "
            kv " Oh? what video am I talking about? well, I'll give you a hint..."
            kv " This video is truly a great way to learn the {b}Basics in Behaviour{/b}! "
            hide kevinhappy at bottom
            show kevinneutral at center
            kv " Huh, I feel as if I accidentally referenced something else there. "
            kv " But, truly...this is the fundamental paper education. "
            menu:
                " I agree with that ":
                    $ kevinlv += 10
                    hide kevinneutral at bottom
                    show kevinhappy at center
                    kv " I'm happy that you agree! "
                    kv " Come here, sit next to me. "
                    hide kevinhappy at bottom
                    show kevinneutral at center
                    kv " I'm most certain that you have nothing to do. "
                    kv " I usually see you walking around the halls or talking to someone... "
                    kv " Well, you're talking to me right now. "
                    kv " But do you still perhaps want to watch this video with me? "
                    " He was right, you really had nothing else to do. "
                    " You nodded your head and decided to watch something with him. "
                    kv " Wonderful. "
                    scene black with dissolve
                    " You spent the rest of the break watching a video with Kevin. "
                    " He really was right, the video was truly the basics in behaviour... "
                    " You could really learn a thing or two from that video. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your science class. "
                    " You then walked to your classroom for your next class. "
                    pause 2.0
                    jump scienceclassthurs
                " I don't agree with that ":
                    kv " Oh, uh...okay. "
                    kv " How about you watch this video with me though? "
                    kv " I'm most certain that you have nothing to do. "
                    kv " I usually see you walking around the halls or talking to someone... "
                    kv " Well, you're talking to me right now. "
                    kv " But do you still perhaps want to watch this video with me? "
                    " He was right, you really had nothing else to do. "
                    " You nodded your head and decided to watch something with him. "
                    kv " Wonderful. "
                    scene black with dissolve
                    " You spent the rest of the break watching a video with Kevin. "
                    " He really was right, the video was truly the basics in behaviour... "
                    " You could really learn a thing or two from that video. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your science class. "
                    " You then walked to your classroom for your next class. "
                    pause 2.0
                    jump scienceclassthurs
        else:
            " You walked up to him and looked at what he was doing. "
            " From what you could see, he was looking at a video on his phone. "
            " Huh, for once, he wasn't studying. "
            " Suprisingly, really...everytime you saw this guy, he'd be seen studying almost everytime. "
            " A change like this is very, very interesting. "
            " Maybe he's been slacking off and you just didn't notice. "
            " You then coughed so that you could get his attention. "
            x " Ah, [name]. "
            x " Apologies that I didn't notice you sooner. "
            x " I was just busy watching this video to educate myself... "
            $ kevinknow = True
            kv " I'm Kevin, by the way, I don't think I've introduced myself to you before. "
            kv " Anywho... "
            hide kevinneutral at bottom
            show kevinhappy at center
            kv " ...I'll tell you, the video? - it's great! "
            kv " I'm learning new things that I haven't before! "
            kv " Well, I do that daily whenever I come here, but still - "
            kv " This video is great for students who are struggling a bit in behvaior.. "
            kv " Oh? what video am I talking about? well, I'll give you a hint..."
            kv " This video is truly a great way to learn the {b}Basics in Behaviour{/b}! "
            hide kevinhappy at bottom
            show kevinneutral at center
            kv " Huh, I feel as if I accidentally referenced something else there. "
            kv " But, truly...this is the fundamental paper education. "
            menu:
                " I agree with that ":
                    $ kevinlv += 10
                    hide kevinneutral at bottom
                    show kevinhappy at center
                    kv " I'm happy that you agree! "
                    kv " Come here, sit next to me. "
                    hide kevinhappy at bottom
                    show kevinneutral at center
                    kv " I'm most certain that you have nothing to do. "
                    kv " I usually see you walking around the halls or talking to someone... "
                    kv " Well, you're talking to me right now. "
                    kv " But do you still perhaps want to watch this video with me? "
                    " He was right, you really had nothing else to do. "
                    " You nodded your head and decided to watch something with him. "
                    kv " Wonderful. "
                    scene black with dissolve
                    " You spent the rest of the break watching a video with Kevin. "
                    " He really was right, the video was truly the basics in behaviour... "
                    " You could really learn a thing or two from that video. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your science class. "
                    " You then walked to your classroom for your next class. "
                    pause 2.0
                    jump scienceclassthurs
                " I don't agree with that ":
                    kv " Oh, uh...okay. "
                    kv " How about you watch this video with me though? "
                    kv " I'm most certain that you have nothing to do. "
                    kv " I usually see you walking around the halls or talking to someone... "
                    kv " Well, you're talking to me right now. "
                    kv " But do you still perhaps want to watch this video with me? "
                    " He was right, you really had nothing else to do. "
                    " You nodded your head and decided to watch something with him. "
                    kv " Wonderful. "
                    scene black with dissolve
                    " You spent the rest of the break watching a video with Kevin. "
                    " He really was right, the video was truly the basics in behaviour... "
                    " You could really learn a thing or two from that video. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your science class. "
                    " You then walked to your classroom for your next class. "
                    pause 2.0
                    jump scienceclassthurs
label thurscafeteria2:
    # engel and riley
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and spotted two of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if engelknow == True and rileyknow == True:
        menu:
            " {image=engelicon} Engel {image=engelicon} ":
                jump fuckingbirdinstock
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump loveberryinstock
    elif engelknow == True and rileyknow == False:
        menu:
            " {image=engelicon} Engel {image=engelicon} ":
                jump fuckingbirdinstock
            " {image=rileyicon} An insane girl {image=rileyicon} ":
                jump loveberryinstock
    elif engelknow == False and rileyknow == True:
        menu:
            " {image=engelicon} A guy with feathers on his head {image=engelicon} ":
                jump fuckingbirdinstock
            " {image=rileyicon} Riley {image=rileyicon} ":
                jump loveberryinstock
    else:
        menu:
            " {image=engelicon} A guy with feathers on his head {image=engelicon} ":
                jump fuckingbirdinstock
            " {image=rileyicon} An insane girl {image=rileyicon} ":
                jump loveberryinstock
    label loveberryinstock:
        show rileyneutral at center with easeinright
        if rileyknow == True:
            ri " Hahahah...hi there [name]!! "
            ri " I talked to Robby about this new thing I'm making for Oliver... "
            ri " You know about it, right? Olibot? "
            ri " Hehe...my ideas are sooo good! "
            ri " Though, while I was talking to Robby... "
            ri " He seemed kinda mad at me?? "
            ri " I dunno why, but he looked REALLY annoyed. "
            ri " I'm just trying to propose my idea to you, dude! "
            ri " Not like I'm calling you an insult or anything... "
            hide rileyneutral at bottom
            show rileysad at center
            ri " ...Okay, but really... "
            ri " I don't know why he's upset!! "
            ri " Was it something I did? something I said? "
            ri " I mean, I did ask him why he looked mad after I finished with my whole idea, buuut... "
            ri " After that, he kinda just..left! "
            ri " He didn't explain anything at all! "
            ri " How am I gonna know what you're upset about if you don't tell me?! "
            ri " Waaah, this is all so confusing... "
            " ...You might know the reason why Robby is upset with her. "
            " You asked her if she talks about Oliver a lot. "
            " A question with a very obvious answer, but it can also provide as a little clue for Riley on the reason why. "
            hide rileysad at bottom
            show rileyneutral at center
            ri " Duh, of course I do! "
            ri " How could I not? He's perfect - he's my entire universe! "
            ri " And - oh. "
            hide rileyneutral at bottom
            show rileysad at center
            " Riley's face very slowly turns into a frown the moment she realizes what you were getting at. "
            " Wow, didn't expect her to get it that quickly. "
            hide rileysad at bottom
            show rileyangry at center
            ri " Well, I don't CARE if he doesn't like me talking about Oliver! "
            ri " I'll talk about him whenever want! "
            " ...Jesus christ. "
            scene black with dissolve
            " You spent the rest of the break talking with Riley. "
            " I think I can see why Robby is just a little bit pissed off about Riley... "
            " Maybe they should talk this out next break. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You walked out of the cafeteria and then went to your classroom. "
            pause 2.0
            jump scienceclassthurs
        else:
            x " Hahahah...hi there [name]!! "
            $ rileyknow = True
            ri " I'm Riley - Oliver's wife and girlfriend! "
            " How can one be someone's wife and girlfriend at the same time? "
            ri " Anywayyy, enough with that introduction bullshit!! "
            ri " I talked to Robby about this new thing I'm making for Oliver... "
            ri " You know about it, right? Olibot? "
            ri " Hehe...my ideas are sooo good! "
            ri " Though, while I was talking to Robby... "
            ri " He seemed kinda mad at me?? "
            ri " I dunno why, but he looked REALLY annoyed. "
            ri " I'm just trying to propose my idea to you, dude! "
            ri " Not like I'm calling you an insult or anything... "
            hide rileyneutral at bottom
            show rileysad at center
            ri " ...Okay, but really... "
            ri " I don't know why he's upset!! "
            ri " Was it something I did? something I said? "
            ri " I mean, I did ask him why he looked mad after I finished with my whole idea, buuut... "
            ri " After that, he kinda just..left! "
            ri " He didn't explain anything at all! "
            ri " How am I gonna know what you're upset about if you don't tell me?! "
            ri " Waaah, this is all so confusing... "
            " ...You might know the reason why Robby is upset with her. "
            " You asked her if she talks about Oliver a lot. "
            " A question with a very obvious answer, but it can also provide as a little clue for Riley on the reason why. "
            hide rileysad at bottom
            show rileyneutral at center
            ri " Duh, of course I do! "
            ri " How could I not? He's perfect - he's my entire universe! "
            ri " And - oh. "
            hide rileyneutral at bottom
            show rileysad at center
            " Riley's face very slowly turns into a frown the moment she realizes what you were getting at. "
            " Wow, didn't expect her to get it that quickly. "
            hide rileysad at bottom
            show rileyangry at center
            ri " Well, I don't CARE if he doesn't like me talking about Oliver! "
            ri " I'll talk about him whenever want! "
            " ...Jesus christ. "
            scene black with dissolve
            " You spent the rest of the break talking with Riley. "
            " I think I can see why Robby is just a little bit pissed off about Riley... "
            " Maybe they should talk this out next break. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You walked out of the cafeteria and then went to your classroom. "
            pause 2.0
            jump scienceclassthurs
    label fuckingbirdinstock:
        show engelneutral at center with easeinleft
        if engelknow == True:
            e " Hmm, let's see... "
            e " A little fold here, a little fold there... "
            e " I don't think this is right... "
            e " Maybe I should just do this? "
            " Looks like he's busy doing origami or something. "
            " You don't know how he's doing it, but it looks like it takes a lot of skill. "
            " You have a lot of respect for this guy. You could never do something like this. "
            " Unless if you concentrate a lot and follow the instructions, then you probably could. "
            " It's rare to see you concentrate a lot though with how distracted your mind is. "
            e " A little bit there... "
            e " Aaaaannd...done! "
            e " Hmm, a little imperfect on the edges, but it should be fine for Claire. "
            e " A wonderful addition to her scrapbook. "
            " After a bit of looking at his new creation, he eventually notices you. "
            " People always notice you a little late, that's a thing you've noticed... "
            " Either they're too busy doing their own thing or they're busy talking to eachother. "
            " Huh. Interesting fun fact, I guess. "
            hide engelneutral at bottom
            show engelhappy at center
            e " Hello there, [name]. "
            e " I'm just doing a paper origami for Claire. "
            e " She's been looking for things to add in her scrap book... "
            e " And I thought that this would be a fine addition. "
            e " Look here... "
            " He showed off his little origami to you. "
            " It was a nice little paper butterfly. "
            " Nothing too special like a paper swan, but it's a nice creation. "
            e " It looks cute, right? "
            e " I could teach you how to make this... "
            e " It's simple, don't worry. "
            e " Just follow my instructions and you'll understand. "
            e " But uh...do you really wanna learn? "
            e " I don't wanna force you if you don't want to. "
            menu:
                " teach me pls ":
                    $ engellv += 10
                    hide engelhappy at bottom
                    show engelcontent at center
                    e " Alrighty then, if that's what you want... "
                    e " Here, let me grab a piece of paper for you. "
                    e " Now from here on out, follow my lead. "
                    e " So first, you fold this... "
                    scene black with dissolve
                    " You spent the rest of the break making paper butterflies with Engel. "
                    " It was honestly a bit addicting to do... "
                    " You could do this every now and then in your free time. "
                    play sound "audio/bellring.mp3"
                    " The bell ringsafter a bit, looks like it's time for another class. "
                    " You walked out of the cafeteria and went to your classroom. "
                    pause 2.0
                    jump scienceclassthurs
                " nah im good ":
                    hide engelhappy at bottom
                    show engelneutral at center
                    e " Okay, if that's what you want... "
                    e " Though I could let you watch me make some more little butterflies. "
                    e " If you don't mind, of course. "
                    " You had nothing else to do for this break, so you agreed. "
                    e " Wonderful. "
                    scene black with dissolve
                    " You spent the rest of the break making paper butterflies with Engel. "
                    " It was honestly a bit addicting to do... "
                    " You could do this every now and then in your free time. "
                    play sound "audio/bellring.mp3"
                    " The bell ringsafter a bit, looks like it's time for another class. "
                    " You walked out of the cafeteria and went to your classroom. "
                    pause 2.0
                    jump scienceclassthurs
        else:
            x " Hmm, let's see... "
            x " A little fold here, a little fold there... "
            x " I don't think this is right... "
            x " Maybe I should just do this? "
            " Looks like he's busy doing origami or something. "
            " You don't know how he's doing it, but it looks like it takes a lot of skill. "
            " You have a lot of respect for this guy. You could never do something like this. "
            " Unless if you concentrate a lot and follow the instructions, then you probably could. "
            " It's rare to see you concentrate a lot though with how distracted your mind is. "
            x " A little bit there... "
            x " Aaaaannd...done! "
            x " Hmm, a little imperfect on the edges, but it should be fine for Claire. "
            x " A wonderful addition to her scrapbook. "
            " After a bit of looking at his new creation, he eventually notices you. "
            " People always notice you a little late, that's a thing you've noticed... "
            " Either they're too busy doing their own thing or they're busy talking to eachother. "
            " Huh. Interesting fun fact, I guess. "
            hide engelneutral at bottom
            show engelhappy at center
            x " Hello there, [name]. "
            x " I believe we haven't met before... "
            $ engelknow = True
            e " I'm Engel, your classmate. It's nice to meet you. "
            e " And right now, I'm just doing a paper origami for my friend, Claire. "
            e " She's been looking for things to add in her scrap book... "
            e " And I thought that this would be a fine addition. "
            e " Look here... "
            " He showed off his little origami to you. "
            " It was a nice little paper butterfly. "
            " Nothing too special like a paper swan, but it's a nice creation. "
            e " It looks cute, right? "
            e " I could teach you how to make this... "
            e " It's simple, don't worry. "
            e " Just follow my instructions and you'll understand. "
            e " But uh...do you really wanna learn? "
            e " I don't wanna force you if you don't want to. "
            menu:
                " teach me pls ":
                    $ engellv += 10
                    hide engelhappy at bottom
                    show engelcontent at center
                    e " Alrighty then, if that's what you want... "
                    e " Here, let me grab a piece of paper for you. "
                    e " Now from here on out, follow my lead. "
                    e " So first, you fold this... "
                    scene black with dissolve
                    " You spent the rest of the break making paper butterflies with Engel. "
                    " It was honestly a bit addicting to do... "
                    " You could do this every now and then in your free time. "
                    play sound "audio/bellring.mp3"
                    " The bell ringsafter a bit, looks like it's time for another class. "
                    " You walked out of the cafeteria and went to your classroom. "
                    pause 2.0
                    jump scienceclassthurs
                " nah im good ":
                    hide engelhappy at bottom
                    show engelneutral at center
                    e " Okay, if that's what you want... "
                    e " Though I could let you watch me make some more little butterflies. "
                    e " If you don't mind, of course. "
                    " You had nothing else to do for this break, so you agreed. "
                    e " Wonderful. "
                    scene black with dissolve
                    " You spent the rest of the break making paper butterflies with Engel. "
                    " It was honestly a bit addicting to do... "
                    " You could do this every now and then in your free time. "
                    play sound "audio/bellring.mp3"
                    " The bell ringsafter a bit, looks like it's time for another class. "
                    " You walked out of the cafeteria and went to your classroom. "
                    pause 2.0
                    jump scienceclassthurs
label thursrooftop2:
    # petunia and bubble
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked onto the rooftop and spotted two of your classmates talking with eachother. "
    " Wondering what they're talking about, you decided to join into their conversation. "
    show petunianeutral at left with easeinright
    show bubbleneutral at right with easeinright
    if popularknow == True and bubbleknow == True:
        p " Hey there, [name]!! "
        b " Uh, hi...[name]. "
        p " I was just talking with my good friend Bubble over here! "
        p " Turns out she likes a lot of things that we like too! "
        p " Isn't that really interesting? "
        " You could tell that Bubble was just a little bit uncomfortable. "
        " You don't know what's going on, but you needed to figure it out. "
        p " Anywayyy, be right back. "
        p " Gotta pick something up that my dad made me. "
        p " Have fun, you two! "
        hide petunianeutral at right with easeoutright
        show bubbleneutral at center with move
        b " ... "
        b " Now that she's gone... "
        hide bubbleneutral at bottom
        show bubblesad at center
        b " You've gotta help me out here, [name]!! "
        b " You have no idea how much she's been trash talking about Lizzy... "
        b " I know they do this sometimes - argue, butbut...!! "
        b " It still breaks my heart whenever they're acting like this towards eachother! "
        b " Just...maybe tell her something about Lizzy? "
        b " I don't know if that's going to work, but I hope it does! "
        b " Oh shoot, she's coming back! "
        hide bubblesad at bottom
        show bubbleneutral at center
        show bubbleneutral at right with move
        show petunianeutral at left with easeinright
        p " I'm baaaaaack!! "
        p " Honestly, I'm having a lot of fun talking with you guys!! "
        p " We should talk more often!! "
        menu:
            " Oooor we could talk with Lizzy ":
                $ popularlv += 10
                p " ...Huh? "
                hide petunianeutral at bottom
                show petuniasad at left
                p " ...We don't talk about her. "
                p " Didn't I tell you that already? "
                p " Let's just talk about something else. "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Bubble. "
                " You should really just try to get Petunia and Lizzy back together... "
                " You can't really stand seeing Petunia and Lizzy break up like this. "
                " ...And break up as in friendship breakup, not romance breakup. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class "
                " You got down from the rooftop and went to your next class. "
                pause 2.0
                jump scienceclassthurs
            " *Say nothing* ":
                b " ...([name], come onnn...) "
                p " I just love talking to you guys! "
                p " Maybe we could become a new trio? "
                p " Good idea, right? "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Bubble. "
                " You should really just try to get Petunia and Lizzy back together... "
                " You can't really stand seeing Petunia and Lizzy break up like this. "
                " ...And break up as in friendship breakup, not romance breakup. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class "
                " You got down from the rooftop and went to your next class. "
                pause 2.0
                jump scienceclassthurs
    elif popularknow == True and bubbleknow == False:
        p " Hey there, [name]!! "
        x " Uh, hi...[name]. "
        $ bubbleknow = True
        p " I was just talking with my good friend Bubble over here! "
        p " Turns out she likes a lot of things that we like too! "
        p " Isn't that really interesting? "
        " You could tell that Bubble was just a little bit uncomfortable. "
        " You don't know what's going on, but you needed to figure it out. "
        p " Anywayyy, be right back. "
        p " Gotta pick something up that my dad made me. "
        p " Have fun, you two! "
        hide petunianeutral at right with easeoutright
        show bubbleneutral at center with move
        b " ... "
        b " Now that she's gone... "
        hide bubbleneutral at bottom
        show bubblesad at center
        b " You've gotta help me out here, [name]!! "
        b " You have no idea how much she's been trash talking about Lizzy... "
        b " I know they do this sometimes - argue, butbut...!! "
        b " It still breaks my heart whenever they're acting like this towards eachother! "
        b " Just...maybe tell her something about Lizzy? "
        b " I don't know if that's going to work, but I hope it does! "
        b " Oh shoot, she's coming back! "
        hide bubblesad at bottom
        show bubbleneutral at center
        show bubbleneutral at right with move
        show petunianeutral at left with easeinright
        p " I'm baaaaaack!! "
        p " Honestly, I'm having a lot of fun talking with you guys!! "
        p " We should talk more often!! "
        menu:
            " Oooor we could talk with Lizzy ":
                $ popularlv += 10
                p " ...Huh? "
                hide petunianeutral at bottom
                show petuniasad at left
                p " ...We don't talk about her. "
                p " Didn't I tell you that already? "
                p " Let's just talk about something else. "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Bubble. "
                " You should really just try to get Petunia and Lizzy back together... "
                " You can't really stand seeing Petunia and Lizzy break up like this. "
                " ...And break up as in friendship breakup, not romance breakup. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class "
                " You got down from the rooftop and went to your next class. "
                pause 2.0
                jump scienceclassthurs
            " *Say nothing* ":
                b " ...([name], come onnn...) "
                p " I just love talking to you guys! "
                p " Maybe we could become a new trio? "
                p " Good idea, right? "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Bubble. "
                " You should really just try to get Petunia and Lizzy back together... "
                " You can't really stand seeing Petunia and Lizzy break up like this. "
                " ...And break up as in friendship breakup, not romance breakup. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class "
                " You got down from the rooftop and went to your next class. "
                pause 2.0
                jump scienceclassthurs
    elif popularknow == False and bubbleknow == True:
        x " Hey there, [name]!! "
        b " Uh, hi...[name]. "
        x " Don't think I introduced myself to you yet, so... "
        $ popularknow = True
        p " I'm Petunia! Nice to meet you! "
        p " I was just talking with my good friend Bubble over here! "
        p " Turns out she likes a lot of things that we like too! "
        p " Isn't that really interesting? "
        " You could tell that Bubble was just a little bit uncomfortable. "
        " You don't know what's going on, but you needed to figure it out. "
        p " Anywayyy, be right back. "
        p " Gotta pick something up that my dad made me. "
        p " Have fun, you two! "
        hide petunianeutral at right with easeoutright
        show bubbleneutral at center with move
        b " ... "
        b " Now that she's gone... "
        hide bubbleneutral at bottom
        show bubblesad at center
        b " You've gotta help me out here, [name]!! "
        b " You have no idea how much she's been trash talking about Lizzy... "
        b " I know they do this sometimes - argue, butbut...!! "
        b " It still breaks my heart whenever they're acting like this towards eachother! "
        b " Just...maybe tell her something about Lizzy? "
        b " I don't know if that's going to work, but I hope it does! "
        b " Oh shoot, she's coming back! "
        hide bubblesad at bottom
        show bubbleneutral at center
        show bubbleneutral at right with move
        show petunianeutral at left with easeinright
        p " I'm baaaaaack!! "
        p " Honestly, I'm having a lot of fun talking with you guys!! "
        p " We should talk more often!! "
        menu:
            " Oooor we could talk with Lizzy ":
                $ popularlv += 10
                p " ...Huh? "
                hide petunianeutral at bottom
                show petuniasad at left
                p " ...We don't talk about her. "
                p " Didn't I tell you that already? "
                p " Let's just talk about something else. "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Bubble. "
                " You should really just try to get Petunia and Lizzy back together... "
                " You can't really stand seeing Petunia and Lizzy break up like this. "
                " ...And break up as in friendship breakup, not romance breakup. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class "
                " You got down from the rooftop and went to your next class. "
                pause 2.0
                jump scienceclassthurs
            " *Say nothing* ":
                b " ...([name], come onnn...) "
                p " I just love talking to you guys! "
                p " Maybe we could become a new trio? "
                p " Good idea, right? "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Bubble. "
                " You should really just try to get Petunia and Lizzy back together... "
                " You can't really stand seeing Petunia and Lizzy break up like this. "
                " ...And break up as in friendship breakup, not romance breakup. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class "
                " You got down from the rooftop and went to your next class. "
                pause 2.0
                jump scienceclassthurs
    else:
        x " Hey there, [name]!! "
        x " Uh, hi...[name]. "
        x " Don't think I introduced myself to you yet, so... "
        $ popularknow = True
        p " I'm Petunia! Nice to meet you! "
        $ bubbleknow = True
        p " I was just talking with my good friend Bubble over here! "
        p " Turns out she likes a lot of things that we like too! "
        p " Isn't that really interesting? "
        " You could tell that Bubble was just a little bit uncomfortable. "
        " You don't know what's going on, but you needed to figure it out. "
        p " Anywayyy, be right back. "
        p " Gotta pick something up that my dad made me. "
        p " Have fun, you two! "
        hide petunianeutral at right with easeoutright
        show bubbleneutral at center with move
        b " ... "
        b " Now that she's gone... "
        hide bubbleneutral at bottom
        show bubblesad at center
        b " You've gotta help me out here, [name]!! "
        b " You have no idea how much she's been trash talking about Lizzy... "
        b " I know they do this sometimes - argue, butbut...!! "
        b " It still breaks my heart whenever they're acting like this towards eachother! "
        b " Just...maybe tell her something about Lizzy? "
        b " I don't know if that's going to work, but I hope it does! "
        b " Oh shoot, she's coming back! "
        hide bubblesad at bottom
        show bubbleneutral at center
        show bubbleneutral at right with move
        show petunianeutral at left with easeinright
        p " I'm baaaaaack!! "
        p " Honestly, I'm having a lot of fun talking with you guys!! "
        p " We should talk more often!! "
        menu:
            " Oooor we could talk with Lizzy ":
                $ popularlv += 10
                p " ...Huh? "
                hide petunianeutral at bottom
                show petuniasad at left
                p " ...We don't talk about her. "
                p " Didn't I tell you that already? "
                p " Let's just talk about something else. "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Bubble. "
                " You should really just try to get Petunia and Lizzy back together... "
                " You can't really stand seeing Petunia and Lizzy break up like this. "
                " ...And break up as in friendship breakup, not romance breakup. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class "
                " You got down from the rooftop and went to your next class. "
                pause 2.0
                jump scienceclassthurs
            " *Say nothing* ":
                b " ...([name], come onnn...) "
                p " I just love talking to you guys! "
                p " Maybe we could become a new trio? "
                p " Good idea, right? "
                scene black with dissolve
                " You spent the rest of the break talking with Petunia and Bubble. "
                " You should really just try to get Petunia and Lizzy back together... "
                " You can't really stand seeing Petunia and Lizzy break up like this. "
                " ...And break up as in friendship breakup, not romance breakup. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class "
                " You got down from the rooftop and went to your next class. "
                pause 2.0
                jump scienceclassthurs

label thurslibrary2:
    # claire and lizzy
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    if clairebeatup == True and clairesorry == False:
        " You can't interact with someone here because you didn't apologize. "
        " Sorry not sorry. "
        scene black
        pause 2.0
        jump scienceclassthurs
    else:
        pass
    " You walked into the library and spotted your two classmates talking with eachother. "
    " Wondering on what they're talking about, you decided to join their conversation. "
    show claireneutral at right with easeinleft
    show lizzyneutral at left with easeinleft
    if claireknow == True and popularknow == True:
        c " As much as I'd like to be your 'best friend'... "
        c " I don't want to be a replacement for someone. "
        lz " What do you mean? "
        " Looks like they're too busy with their conversation to even notice you. "
        " Atleast you can get free drama with this... "
        lz " I don't think I understand what you're saying... "
        c " I know that you and Petunia can get back together... "
        c " You two are a iconic duo! "
        c " Besides, you and Petunia have had your disagreements every now and then, right? "
        c " I know that you two can come back together again! "
        c " I'm pretty sure the school would be less iconic without you two... "
        lz " ...You don't really know what you're saying, Claire. "
        lz " I can't get Petunia to understand what I'm feeling. "
        lz " She would never understand if I told her. "
        lz " I know that it's good to tell her the truth, but... "
        lz " I'm just a little bit afraid of her judging me for it. "
        lz " I know that we're friends, but she could probably take it as a joke... "
        lz " She never took certain things seriously, anyway. "
        lz " That's just like her. "
        lz " You know what, I'm just going to... "
        c " Roam around school for a bit? "
        lz " Yeah, just to get things off of my mind. "
        lz " Thank you for listening, I guess. "
        c " No problem, Lizzy. "
        c " I hope you and Petunia can reconnect with eachother... "
        lz " ...Yeah, whatever. "
        scene black with dissolve
        " After that, they went their own seperate ways. "
        " You just decided to hang out at the library cause you had absolutely nothing to do. "
        " You also used the free time to play games on your phone. "
        " Epic gaming session at your school! "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You walked out of the library and went to your classroom for science class. "
        pause 2.0
        jump scienceclassthurs
    elif claireknow == True and popularknow == False:
        c " As much as I'd like to be your 'best friend'... "
        c " I don't want to be a replacement for someone. "
        x " What do you mean? "
        " Looks like they're too busy with their conversation to even notice you. "
        " Atleast you can get free drama with this... "
        x " I don't think I understand what you're saying... "
        c " I know that you and Petunia can get back together... "
        c " You two are a iconic duo! "
        c " Besides, you and Petunia have had your disagreements every now and then, right? "
        c " I know that you two can come back together again! "
        c " I'm pretty sure the school would be less iconic without you two... "
        x " ...You don't really know what you're saying, Claire. "
        x " I can't get Petunia to understand what I'm feeling. "
        x " She would never understand if I told her. "
        x " I know that it's good to tell her the truth, but... "
        x " I'm just a little bit afraid of her judging me for it. "
        x " I know that we're friends, but she could probably take it as a joke... "
        x " She never took certain things seriously, anyway. "
        x " That's just like her. "
        x " You know what, I'm just going to... "
        c " Roam around school for a bit? "
        x " Yeah, just to get things off of my mind. "
        x " Thank you for listening, I guess. "
        c " No problem, Lizzy. "
        c " I hope you and Petunia can reconnect with eachother... "
        x " ...Yeah, whatever. "
        scene black with dissolve
        " After that, they went their own seperate ways. "
        " You just decided to hang out at the library cause you had absolutely nothing to do. "
        " You also used the free time to play games on your phone. "
        " Epic gaming session at your school! "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You walked out of the library and went to your classroom for science class. "
        pause 2.0
        jump scienceclassthurs
    elif claireknow == False and popularknow == True:
        x " As much as I'd like to be your 'best friend'... "
        x " I don't want to be a replacement for someone. "
        lz " What do you mean? "
        " Looks like they're too busy with their conversation to even notice you. "
        " Atleast you can get free drama with this... "
        lz " I don't think I understand what you're saying... "
        x " I know that you and Petunia can get back together... "
        x " You two are a iconic duo! "
        x " Besides, you and Petunia have had your disagreements every now and then, right? "
        x " I know that you two can come back together again! "
        x " I'm pretty sure the school would be less iconic without you two... "
        lz " ...You don't really know what you're saying, Claire. "
        lz " I can't get Petunia to understand what I'm feeling. "
        lz " She would never understand if I told her. "
        lz " I know that it's good to tell her the truth, but... "
        lz " I'm just a little bit afraid of her judging me for it. "
        lz " I know that we're friends, but she could probably take it as a joke... "
        lz " She never took certain things seriously, anyway. "
        lz " That's just like her. "
        lz " You know what, I'm just going to... "
        x " Roam around school for a bit? "
        lz " Yeah, just to get things off of my mind. "
        lz " Thank you for listening, I guess. "
        x " No problem, Lizzy. "
        x " I hope you and Petunia can reconnect with eachother... "
        lz " ...Yeah, whatever. "
        scene black with dissolve
        " After that, they went their own seperate ways. "
        " You just decided to hang out at the library cause you had absolutely nothing to do. "
        " You also used the free time to play games on your phone. "
        " Epic gaming session at your school! "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You walked out of the library and went to your classroom for science class. "
        pause 2.0
        jump scienceclassthurs
    else:
        x " As much as I'd like to be your 'best friend'... "
        x " I don't want to be a replacement for someone. "
        x " What do you mean? "
        " Looks like they're too busy with their conversation to even notice you. "
        " Atleast you can get free drama with this... "
        x " I don't think I understand what you're saying... "
        x " I know that you and Petunia can get back together... "
        x " You two are a iconic duo! "
        x " Besides, you and Petunia have had your disagreements every now and then, right? "
        x " I know that you two can come back together again! "
        x " I'm pretty sure the school would be less iconic without you two... "
        x " ...You don't really know what you're saying, Claire. "
        x " I can't get Petunia to understand what I'm feeling. "
        x " She would never understand if I told her. "
        x " I know that it's good to tell her the truth, but... "
        x " I'm just a little bit afraid of her judging me for it. "
        x " I know that we're friends, but she could probably take it as a joke... "
        x " She never took certain things seriously, anyway. "
        x " That's just like her. "
        x " You know what, I'm just going to... "
        x " Roam around school for a bit? "
        x " Yeah, just to get things off of my mind. "
        x " Thank you for listening, I guess. "
        x " No problem, Lizzy. "
        x " I hope you and Petunia can reconnect with eachother... "
        x " ...Yeah, whatever. "
        scene black with dissolve
        " After that, they went their own seperate ways. "
        " You just decided to hang out at the library cause you had absolutely nothing to do. "
        " You also used the free time to play games on your phone. "
        " Epic gaming session at your school! "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You walked out of the library and went to your classroom for science class. "
        pause 2.0
        jump scienceclassthurs
label thursoligang2:
    scene black with dissolve
    pause 2.0
    scene oligangclub with dissolve
    " You walked into the room and saw only Edward there. "
    " Looks like he was working on this robot thingy... "
    " Curious about it, you decided to walk closer to him. "
    show edwardneutral at center with easeinleft
    ed " Yo, [name]. "
    ed " If yer wondering where the others are, they're just looking for information. "
    ed " Information about what everyone thinks about the Lizzy and Petunia thing. "
    ed " AAAAND also planning to bully Petunia and Lizzy for it. "
    ed " Great idea, right? but not really considering that most of the school would probably answer with... "
    hide edwardneutral at bottom
    show edwardangry at center
    ed " Oh, I hope they get better soon! or: I don't really care about them... "
    ed " Jeez, how can people be so lame in this school? "
    ed " When is everyone gonna wake up and realize that we need some DRAMA? "
    ed " God... "
    hide edwardangry at bottom
    show edwardneutral at center
    ed " Anyway, while you're here... "
    ed " How about you hold my tools for me real quick? "
    ed " I don't want you to just stand there awkwardly. "
    ed " Oh, and the thing I'm working on right now is just a little thing I'd call... "
    ed " The spybot. Totally original, trust me. "
    ed " It's got this really cool feature whereit goes invisible and records things... "
    ed " Can be audio or video, too. "
    ed " I'm such a genius...anyway, you gonna help with my tools or what? "
    menu:
        " sure ":
            $ oliganglv += 10
            hide edwardneutral at bottom
            show edwardhappy at center
            ed " Good. "
            ed " Here, just take all of these... "
            scene black with dissolve
            " You spent the rest of the break helping Edward with his tools. "
            " The tools were a little heavy, but you could handle them. "
            " You basically just stood there and held the tools for him. "
            " How productive you were bein right now! "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the room and went to your classroom for science class. "
            pause 2.0
            jump scienceclassthurs
        " nah ":
            ed " Suit yourself then! "
            scene black with dissolve
            " You spent the rest of the break relaxing in the room. "
            " Did absolutely nothing and just played games on your phone... "
            " ...Enjoying the spare time you've got. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You walked out of the room and went to your classroom for science class. "
            pause 2.0
            jump scienceclassthurs

label scienceclassthurs:
    scene classroom with dissolve
    " You walked into the classroom and sat down onto your seat. "
    " As you waited for the teacher to arrive, you noticed that there were a few bottles on the teachers desk. "
    " You're going to assume that the teacher is just going to do a demonstration today. "
    " Which means...no taking down notes! Yay! "
    " After a few minutes, the teacher arrives and stands infront of the class. "
    " You acted as if you weren't secretly celebrating the fact of no copying for this time. "
    show missbloomieneutral at center with easeinright
    msb " Hello, class. "
    msb " Today I'll be demonstrating a few things from our lesson yesterday to you. "
    msb " Please pay attention so that you know how things work. "
    msb " The things here I show will also come up in the quiz im going to give you in two weeks. "
    msb " Even if I'm not letting you all take down notes right now, "
    msb " Make sure to take MENTAL notes for now. "
    msb " I hope that every one of you can remember every single detail I do. "
    " That's...a pretty extreme thing. "
    " But okay, sure. "
    scene black with dissolve
    " You spent the rest of class hours taking down mental notes of everything that the science teacher was doing. "
    " It was a little hard to remember things at first, but you eventually got a hold of things. "
    " ...And managed to remember about four things from the class that you just had! "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for another break. "
    " You get up from your seat and you walked to the hallways. "
    pause 2.0
    jump thursbreak3

label thursbreak3:
    scene hallway with dissolve
    if oligangjoin == True:
        jump thursoligang3
    else:
        pass
    " Where do you wanna go for this break? "
    menu:
        " {image=popularicon} The front of the school {image=popularicon} ":
            jump thursfrontschool3
        " {image=abbieicon} The back of the school {image=cubbieicon} ":
            jump thursbackschool3
        " {image=rubyicon} The gym {image=lanaicon} ":
            jump thursgym3
        " {image=bubbleicon} The cafeteria {image=kevinicon} ":
            jump thurscafeteria3
        " {image=robbyicon} The rooftop {image=rileyicon} ":
            jump thursrooftop3
        " {image=engelicon} The library {image=claireicon} ":
            jump thurslibrary3

label thursfrontschool3:
    # the girls ignoring eachother // petunia and lizzy
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of the school and spotted two of your classmates looking angrily at eachother. "
    " Wondering what's up, you decided to walk to them. "
    show petuniaangry at left with easeinright
    show lizzyangry at right with easeinright
    if popularknow == True:
        p " ... "
        lz " ... "
        " Looks like they're staring pretty intensely at eachother. "
        " It looks like they're having a staring contest without context... "
        " But isn't that what they're doing, technically? "
        " I mean, they're staring at eachother and not blinking... "
        " Well they are in game, but...you know what, nevermind. "
        p " ...Guess I should leave. "
        p " I refuse to be with a bag of hot trash. "
        lz " Me neither. "
        hide petuniaangry at right with easeoutright
        show lizzyangry at center with move
        " And with that, the bunny girl leaves. "
        " Only leaving the other girl to be with you. "
        " You didn't really want this to be awkward, but you also didn't want to say the wrong thing. "
        " You just waited there patiently for her to say something. "
        " And after a bit of waiting, she eventually did say something. "
        hide lizzyangry at bottom
        show lizzysad at center
        lz " I really hate being mad at her like this... "
        lz " But how could I not be mad at her? "
        lz " If I'm gonna be honest, she's sometimes too loud. "
        lz " And she makes jokes whenever I'm being serious. "
        lz " I don't really like it when she does that...but I never told her. "
        lz " Maybe she'll just treat THAT as a joke too. "
        lz " Not a maybe, but a most likely scenario. "
        lz " 'LOL Lizzy, you're so funny!' "
        lz " I'm not even trying to. "
        lz " I want you to understand how I feel without you making fun of me for it. "
        lz " Sure there's times where you DO understand, "
        lz " But what about the rest? "
        lz " What was going through your head whenever you heard me say those words? "
        lz " ...She just can't seem to get it, can't she. "
        menu:
            " Maybe you should tell her how you really feel ":
                $ popularlv += 10
                lz " You think it's a good idea to? "
                " You nod. "
                " Even though she can't really understand what you're saying... "
                " It's still good to tell her. "
                " And if she doesn't understand, just keep insisting that you're being serious. "
                " Being taken as a joke isn't funny, and she should know that. "
                hide lizzysad at bottom
                show lizzyneutral at center
                lz " Well...I guess. "
                lz " Thanks for listening, you, uh.. [person]. "
                lz " I appreciate it. "
                scene black with dissolve
                " You spent the rest of the break talking with Lizzy. "
                " You wonder how long it's gonna take for them to be friends again... "
                " Probably until tomorrow. Or maybe in two days. "
                " Would be surprising if it somehow made it to the next week. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and went into your classroom. "
                pause 2.0
                jump historyclassthurs
            " *Say absolutely nothing* ":
                hide lizzysad at bottom
                show lizzyneutral at center
                lz " Eh, I shouldn't be rambling about this to you. "
                lz " Thanks for listening, you, uh.. [person]. "
                lz " I appreciate it. "
                scene black with dissolve
                " You spent the rest of the break talking with Lizzy. "
                " You wonder how long it's gonna take for them to be friends again... "
                " Probably until tomorrow. Or maybe in two days. "
                " Would be surprising if it somehow made it to the next week. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and went into your classroom. "
                pause 2.0
                jump historyclassthurs
    else:
        x " ... "
        x " ... "
        " Looks like they're staring pretty intensely at eachother. "
        " It looks like they're having a staring contest without context... "
        " But isn't that what they're doing, technically? "
        " I mean, they're staring at eachother and not blinking... "
        " Well they are in game, but...you know what, nevermind. "
        x " ...Guess I should leave. "
        x " I refuse to be with a bag of hot trash. "
        x " Me neither. "
        hide petuniaangry at right with easeoutright
        show lizzyangry at center with move
        " And with that, the bunny girl leaves. "
        " Only leaving the other girl to be with you. "
        " You didn't really want this to be awkward, but you also didn't want to say the wrong thing. "
        " You just waited there patiently for her to say something. "
        " And after a bit of waiting, she eventually did say something. "
        hide lizzyangry at bottom
        show lizzysad at center
        x " I really hate being mad at her like this... "
        x " But how could I not be mad at her? "
        x " If I'm gonna be honest, she's sometimes too loud. "
        x " And she makes jokes whenever I'm being serious. "
        x " I don't really like it when she does that...but I never told her. "
        x " Maybe she'll just treat THAT as a joke too. "
        x " Not a maybe, but a most likely scenario. "
        $ popularknow = True
        lz " 'LOL Lizzy, you're so funny!' "
        lz " I'm not even trying to. "
        lz " I want you to understand how I feel without you making fun of me for it. "
        lz " Sure there's times where you DO understand, "
        lz " But what about the rest? "
        lz " What was going through your head whenever you heard me say those words? "
        lz " ...She just can't seem to get it, can't she. "
        menu:
            " Maybe you should tell her how you really feel ":
                $ popularlv += 10
                lz " You think it's a good idea to? "
                " You nod. "
                " Even though she can't really understand what you're saying... "
                " It's still good to tell her. "
                " And if she doesn't understand, just keep insisting that you're being serious. "
                " Being taken as a joke isn't funny, and she should know that. "
                hide lizzysad at bottom
                show lizzyneutral at center
                lz " Well...I guess. "
                lz " Thanks for listening, you, uh.. [person]. "
                lz " I appreciate it. "
                scene black with dissolve
                " You spent the rest of the break talking with Lizzy. "
                " You wonder how long it's gonna take for them to be friends again... "
                " Probably until tomorrow. Or maybe in two days. "
                " Would be surprising if it somehow made it to the next week. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and went into your classroom. "
                pause 2.0
                jump historyclassthurs
            " *Say absolutely nothing* ":
                hide lizzysad at bottom
                show lizzyneutral at center
                lz " Eh, I shouldn't be rambling about this to you. "
                lz " Thanks for listening, you, uh.. [person]. "
                lz " I appreciate it. "
                scene black with dissolve
                " You spent the rest of the break talking with Lizzy. "
                " You wonder how long it's gonna take for them to be friends again... "
                " Probably until tomorrow. Or maybe in two days. "
                " Would be surprising if it somehow made it to the next week. "
                play sound "audio/bellring.mp3"
                " The bell rings, looks like it's time for another class. "
                " You walked back into the school and went into your classroom. "
                pause 2.0
                jump historyclassthurs
label thursbackschool3:
    # Abbie wants to train with you // cubbie makes you a flower crown
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school and spotted two of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if abbieknow == True and cubbieknow == True:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump yinyinu
            " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                jump sayuyu
    elif abbieknow == True and cubbieknow == False:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump yinyinu
            " {image=cubbieicon} A cat guy {image=cubbieicon} ":
                jump sayuyu
    elif abbieknow == False and cubbieknow == True:
        menu:
            " {image=abbieicon} A shy looking guy {image=abbieicon} ":
                jump yinyinu
            " {image=cubbieicon} Cubbie {image=cubbieicon} ":
                jump sayuyu
    else:
        menu:
            " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                jump yinyinu
            " {image=cubbieicon} A cat guy {image=cubbieicon} ":
                jump sayuyu
    label yinyinu:
        # if lv is lower than 15, abbie says nothing
        show abbieneutral at center with easeinright
        if abbieknow == True:
            a " [name]... It's nice to see you here... "
            a " ...Uh... "
            a " ...I was actually thinking of doing something... "
            if abbielv >= 15 or abbielv == 15:
                a " Uh, you know how I've been taking up on training...? "
                a " I know that I've been doing good, but... "
                a " I wanna be better... "
                a " You know...so that I could have a better chance on actually hitting Oliver...? "
                a " It would mean the world to me if I manage to stand up for myself to him like that... "
                a " So, um... "
                a " If it doesn't bother you... "
                a " Could I...could I train with you just for this break? "
                a " You don't have to say yes... "
                a " I'm not gonna force you to train me, if you don't want to... "
                menu:
                    " LETS TRAIN EVEN THOUGH I DONT KNOW SHIT RAAAHH ":
                        $ abbielv += 10
                        hide abbieneutral at bottom
                        show abbiehappy at center
                        a " Really...? "
                        a " Hehe, thanks, [name]... "
                        a " You're the best...! "
                        a " I brought this training dummy that I made myself that we could use... "
                        a " How it fit in my bag...? Um... "
                        a " I actually don't know...it just did... "
                        " Game logic strikes again. "
                        scene black with dissolve
                        " You spent the rest of the break training with Abbie. "
                        " As you were training with him, you could very much tell that he's improved. "
                        " Seeing him improving makes you proud of him, a lot. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your next class. "
                        " You then went back into the school and you went to your classroom for the next class. "
                        pause 2.0
                        jump historyclassthurs
                    " I'm actually busy right now, sorry ":
                        a " Ah, okay... "
                        a " I'll be here training on my own then.. "
                        a " If you need something from me, just tell me..."
                        a " Have fun on whatever you're doing... "
                        scene black with dissolve
                        " You spent the rest of the break wandering around the school. "
                        " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
                        " Wonder what that's about. "
                        " It's not your business, but honestly you can't help but be curious. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your next class. "
                        " You then walked to your classroom after a bit. "
                        pause 2.0
                        jump historyclassthurs
            else:
                a " But, I kind of forgot, oops... "
                " Looks like Abbie was supposed to say something here, but you don't have enough LV. "
                " Shucks. Let's go for a different route then... "
                a " Um...to not make this awkward... "
                a " How about we talk about something...? "
                a " Like, have you ever heard of that one song...what's it called again...? "
                a " Blow my mind out? "
                a " I really like that song... "
                a " I think it's really catchy, and it has a deep meaning, too... "
                hide abbieneutral at bottom
                show abbiehappy at center
                a " Maybe you should listen to it sometime... "
                a " Or don't, if you don't want to... "
                a " I'm not gonna force you or anything... "
                scene black with dissolve
                " You spent the rest of the break talking with Abbie. "
                " Oh yeah, I recognize that song it mentioned. "
                " I think it's the one that goes: Lucky is he, who lives aware? "
                " Yeah, that's the one. Pretty good song, in all honesty. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your history class. "
                " You went back into the school and went to your classroom. "
                pause 2.0
                jump historyclassthurs
        else:
            x " [name]... It's nice to see you here... "
            x " ...Uh... "
            x " I don't think we've met before, actually... "
            $ abbieknow = True
            a " I'm Abbie...um...it's nice to meet you... "
            a " Uh... "
            a " ...I was actually thinking of doing something... "
            if abbielv >= 15 or abbielv == 15:
                a " Uh, you know how I've been taking up on training...? "
                a " I know that I've been doing good, but... "
                a " I wanna be better... "
                a " You know...so that I could have a better chance on actually hitting Oliver...? "
                a " It would mean the world to me if I manage to stand up for myself to him like that... "
                a " So, um... "
                a " If it doesn't bother you... "
                a " Could I...could I train with you just for this break? "
                a " You don't have to say yes... "
                a " I'm not gonna force you to train me, if you don't want to... "
                menu:
                    " LETS TRAIN EVEN THOUGH I DONT KNOW SHIT RAAAHH ":
                        $ abbielv += 10
                        hide abbieneutral at bottom
                        show abbiehappy at center
                        a " Really...? "
                        a " Hehe, thanks, [name]... "
                        a " You're the best...! "
                        a " I brought this training dummy that I made myself that we could use... "
                        a " How it fit in my bag...? Um... "
                        a " I actually don't know...it just did... "
                        " Game logic strikes again. "
                        scene black with dissolve
                        " You spent the rest of the break training with Abbie. "
                        " As you were training with him, you could very much tell that he's improved. "
                        " Seeing him improving makes you proud of him, a lot. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your next class. "
                        " You then went back into the school and you went to your classroom for the next class. "
                        pause 2.0
                        jump historyclassthurs
                    " I'm actually busy right now, sorry ":
                        a " Ah, okay... "
                        a " I'll be here training on my own then.. "
                        a " If you need something from me, just tell me..."
                        a " Have fun on whatever you're doing... "
                        scene black with dissolve
                        " You spent the rest of the break wandering around the school. "
                        " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
                        " Wonder what that's about. "
                        " It's not your business, but honestly you can't help but be curious. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for your next class. "
                        " You then walked to your classroom after a bit. "
                        pause 2.0
                        jump historyclassthurs
            else:
                a " But, I kind of forgot, oops... "
                " Looks like Abbie was supposed to say something here, but you don't have enough LV. "
                " Shucks. Let's go for a different route then... "
                a " Um...to not make this awkward... "
                a " How about we talk about something...? "
                a " Like, have you ever heard of that one song...what's it called again...? "
                a " Blow my mind out? "
                a " I really like that song... "
                a " I think it's really catchy, and it has a deep meaning, too... "
                hide abbieneutral at bottom
                show abbiehappy at center
                a " Maybe you should listen to it sometime... "
                a " Or don't, if you don't want to... "
                a " I'm not gonna force you or anything... "
                scene black with dissolve
                " You spent the rest of the break talking with Abbie. "
                " Oh yeah, I recognize that song it mentioned. "
                " I think it's the one that goes: Lucky is he, who lives aware? "
                " Yeah, that's the one. Pretty good song, in all honesty. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your history class. "
                " You went back into the school and went to your classroom. "
                pause 2.0
                jump historyclassthurs
    label sayuyu:
        show cubbieneutral at center with easeinleft
        if cubbieknow == True:
            " You walked over to him and looked at what he was doing. "
            " You're not sure if you've seen someone make flower crowns before, but here we are. "
            " ... the previous dialogue is the programmer struggling to remember things. "
            " But anyway, the flower crowns look very nicely done. "
            " You sat down next to him and asked him where he learned to make those. "
            " Buuuut then remembered that he can't really talk. Great. "
            cb " ... "
            " Though, he CAN speak with those little signs he can do. "
            " He said that he learnt how to make them because of his mom, aww. "
            " He also told you that his mom used to love flower crowns a lot. "
            " That's why he tried practicing with her a lot back then to impress her. "
            " And all of that practice eventually ended up with this. "
            " Well, they do say...practice makes perfect. "
            " Cause what you're seeing right now is utter perfection. "
            " You haven't seen an imperfect flower crown, but this is the real good stuff. "
            " You told him that you liked the flower crown he made a lot. "
            hide cubbieneutral at bottom
            show cubbiehappy at center
            cb " ...! "
            " Looks like he's happy to hear that. "
            cb " ...? "
            " Oh hey, looks like he's asking you a question. "
            " Let me just translate that... "
            " Oh, he's asking if you want one. "
            " Wanting one as in wanting a flower crown specifically for you. "
            " Do you want Cubbie to make a flower crown for you? "
            menu:
                " gimme them flowers ":
                    $ cubbielv += 10
                    cb " ...!! "
                    " Hearing your response, Cubbie gets to work. "
                    " He looks around for some flowers near by, and took some of them... "
                    " To make this really cool and awesome flower crown, just for you! "
                    " You waited patiently for him to finish up his work... "
                    " As you were waiting, you spotted a bee coming up to you. "
                    " You were praying that it didn't come near you and Cubbie, aaannd... "
                    " Oh, it literally just buzzed away. Huh. "
                    " Looks like even bees think you're stinky. "
                    " Cubbie eventually gets done with his work and he puts it on your head. "
                    " Using your phone's camera, you look at yourself... "
                    " AND HOT DAMN YOU LOOKED GREAT!! "
                    " You're keeping this for the rest of the day now. "
                    " You thanked Cubbie for his wonderful work. "
                    cb " :D! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Cubbie. "
                    " Talking about stuff that isn't as interesting to others... "
                    " Like flowers and other stuff. "
                    " And how flowers would taste. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your history class. "
                    " You went back into the school and went to your classroom. "
                    pause 2.0
                    jump historyclassthurs
                " nah cause if I did, I'd eat them ":
                    hide cubbiehappy at bottom
                    show cubbieneutral at center
                    cb " ...! "
                    " Cubbie seems to be amused by your joke. "
                    " Actually, it was a mix of amused and concerned. "
                    " Mostly amused though. "
                    " He knew you were joking, but he was also a little bit concerned. "
                    " Concerned if you would actually eat them or not. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Cubbie. "
                    " Talking about stuff that isn't as interesting to others... "
                    " Like flowers and other stuff. "
                    " And how flowers would taste. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your history class. "
                    " You went back into the school and went to your classroom. "
                    pause 2.0
                    jump historyclassthurs
        else:
            " Oh hey, it's this kid. You've heard of him before. "
            $ cubbieknow = True
            " His name is Cubbie - he's one of the more smarter students. "
            " He also doesn't really talk that much since he's not comfortable with his voice. "
            " Don't force him to talk if he really doesn't want to. Anyway... "
            " You walked over to him and looked at what he was doing. "
            " You're not sure if you've seen someone make flower crowns before, but here we are. "
            " ... the previous dialogue is the programmer struggling to remember things. "
            " But anyway, the flower crowns look very nicely done. "
            " You sat down next to him and asked him where he learned to make those. "
            " Buuuut then remembered that he can't really talk. Great. "
            cb " ... "
            " Though, he CAN speak with those little signs he can do. "
            " He said that he learnt how to make them because of his mom, aww. "
            " He also told you that his mom used to love flower crowns a lot. "
            " That's why he tried practicing with her a lot back then to impress her. "
            " And all of that practice eventually ended up with this. "
            " Well, they do say...practice makes perfect. "
            " Cause what you're seeing right now is utter perfection. "
            " You haven't seen an imperfect flower crown, but this is the real good stuff. "
            " You told him that you liked the flower crown he made a lot. "
            hide cubbieneutral at bottom
            show cubbiehappy at center
            cb " ...! "
            " Looks like he's happy to hear that. "
            cb " ...? "
            " Oh hey, looks like he's asking you a question. "
            " Let me just translate that... "
            " Oh, he's asking if you want one. "
            " Wanting one as in wanting a flower crown specifically for you. "
            " Do you want Cubbie to make a flower crown for you? "
            menu:
                " gimme them flowers ":
                    $ cubbielv += 10
                    cb " ...!! "
                    " Hearing your response, Cubbie gets to work. "
                    " He looks around for some flowers near by, and took some of them... "
                    " To make this really cool and awesome flower crown, just for you! "
                    " You waited patiently for him to finish up his work... "
                    " As you were waiting, you spotted a bee coming up to you. "
                    " You were praying that it didn't come near you and Cubbie, aaannd... "
                    " Oh, it literally just buzzed away. Huh. "
                    " Looks like even bees think you're stinky. "
                    " Cubbie eventually gets done with his work and he puts it on your head. "
                    " Using your phone's camera, you look at yourself... "
                    " AND HOT DAMN YOU LOOKED GREAT!! "
                    " You're keeping this for the rest of the day now. "
                    " You thanked Cubbie for his wonderful work. "
                    cb " :D! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Cubbie. "
                    " Talking about stuff that isn't as interesting to others... "
                    " Like flowers and other stuff. "
                    " And how flowers would taste. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your history class. "
                    " You went back into the school and went to your classroom. "
                    pause 2.0
                    jump historyclassthurs
                " nah cause if I did, I'd eat them ":
                    hide cubbiehappy at bottom
                    show cubbieneutral at center
                    cb " ...! "
                    " Cubbie seems to be amused by your joke. "
                    " Actually, it was a mix of amused and concerned. "
                    " Mostly amused though. "
                    " He knew you were joking, but he was also a little bit concerned. "
                    " Concerned if you would actually eat them or not. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Cubbie. "
                    " Talking about stuff that isn't as interesting to others... "
                    " Like flowers and other stuff. "
                    " And how flowers would taste. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your history class. "
                    " You went back into the school and went to your classroom. "
                    pause 2.0
                    jump historyclassthurs

label thursgym3:
    # ruby watches lana's show
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked to the gym and spotted the two of your classmates interacting with eachother. "
    " Wondering what they could be talking about, you walked over to them. "
    show lananeutral at right with easeinleft
    show rubyneutral at left with easeinleft
    if lanaknow == True and rubyknow == True:
        $ lanalv += 10
        $ rubylv += 5
        l " [name]! you're just in time for the show! "
        ru " Lana's about to show me her 'Juliana and Pedro'! "
        ru " Heard that it's the second to the last episode, too. "
        ru " Better take down notes on what's happening to make sure if one of my theories is true... "
        l " Woah, Ruby??? You have theories??? "
        l " Over my little show?? aw, shucks! "
        ru " That's how good it is, truly! "
        ru " You KNOW your show is good whenever someone starts making theories about it. "
        ru " Theories can also make things interesting by guessing what's coming next... "
        ru " But we're getting out of topic - "
        ru " Let's get on with the show, please! "
        l " You got it! "
        l " The audience asks and you shall recieve!! "
        l " Ahem... "
        l " So we all know that Pedro is currently in a relationship with Rainier. "
        l " Every now and then, Juliana would bump into them. "
        l " Well - it's not an every now and then, but she would ALWAYS bump into them. "
        l " Seeing them on romantic dates would always get her blood BOILING! "
        l " Just seeing them together reminds her of her old relationship with Pedro... "
        l " A relationship that she couldn't have anymore. "
        l " The more she thought about her loss, the more she felt upset. "
        l " One night - she went out drinking in one of the clubs that were in the city that she was in. "
        l " She thought that she would just be out there to drink, nothing else - "
        l " But then she laid her eyes on the very beautiful bartender there. "
        l " She was surprised that she was feeling this way to a woman, she didn't know she could feel something like this... "
        l " She talked to the woman a bit longer, and eventually, she gave the woman her phone number. "
        l " Right after Juliana went home, she called the woman and they talked until 2 AM... "
        l " And what was this woman's name? her name was Dasha. "
        l " She never thought she could feel this way towards women... "
        l " For now, she's just thinking that they're just random thoughts and it'll pass. "
        l " Aaaaaand, that's it for today, folks! "
        l " What happens next? find out tomorrow, last episode for Juliana and Pedro! "
        hide rubyneutral at bottom
        show rubyhappy at left
        ru " Woot! that was great! "
        ru " Man, I knew Juliana would meet someone else to change her life... "
        ru " But I wasn't expecting for it to be a woman! "
        ru " What an interesting twist, Lana! "
        l " Hehe, thanks! "
        scene black with dissolve
        " You spent the rest of the break talking with Lana and Ruby. "
        " Man that episode was peak! "
        " Wasn't expecting the yuri, but that makes it better! "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You walked out of the gym and went to your classroom for the next class. "
        pause 2.0
        jump historyclassthurs
    elif lanaknow == True and rubyknow == False:
        $ lanalv += 10
        $ rubylv += 5
        l " [name]! you're just in time for the show! "
        x " Lana's about to show me her 'Juliana and Pedro'! "
        x " Heard that it's the second to the last episode, too. "
        x " Better take down notes on what's happening to make sure if one of my theories is true... "
        $ rubyknow = True
        l " Woah, Ruby??? You have theories??? "
        l " Over my little show?? aw, shucks! "
        ru " That's how good it is, truly! "
        ru " You KNOW your show is good whenever someone starts making theories about it. "
        ru " Theories can also make things interesting by guessing what's coming next... "
        ru " But we're getting out of topic - "
        ru " Let's get on with the show, please! "
        l " You got it! "
        l " The audience asks and you shall recieve!! "
        l " Ahem... "
        l " So we all know that Pedro is currently in a relationship with Rainier. "
        l " Every now and then, Juliana would bump into them. "
        l " Well - it's not an every now and then, but she would ALWAYS bump into them. "
        l " Seeing them on romantic dates would always get her blood BOILING! "
        l " Just seeing them together reminds her of her old relationship with Pedro... "
        l " A relationship that she couldn't have anymore. "
        l " The more she thought about her loss, the more she felt upset. "
        l " One night - she went out drinking in one of the clubs that were in the city that she was in. "
        l " She thought that she would just be out there to drink, nothing else - "
        l " But then she laid her eyes on the very beautiful bartender there. "
        l " She was surprised that she was feeling this way to a woman, she didn't know she could feel something like this... "
        l " She talked to the woman a bit longer, and eventually, she gave the woman her phone number. "
        l " Right after Juliana went home, she called the woman and they talked until 2 AM... "
        l " And what was this woman's name? her name was Dasha. "
        l " She never thought she could feel this way towards women... "
        l " For now, she's just thinking that they're just random thoughts and it'll pass. "
        l " Aaaaaand, that's it for today, folks! "
        l " What happens next? find out tomorrow, last episode for Juliana and Pedro! "
        hide rubyneutral at bottom
        show rubyhappy at left
        ru " Woot! that was great! "
        ru " Man, I knew Juliana would meet someone else to change her life... "
        ru " But I wasn't expecting for it to be a woman! "
        ru " What an interesting twist, Lana! "
        l " Hehe, thanks! "
        scene black with dissolve
        " You spent the rest of the break talking with Lana and Ruby. "
        " Man that episode was peak! "
        " Wasn't expecting the yuri, but that makes it better! "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You walked out of the gym and went to your classroom for the next class. "
        pause 2.0
        jump historyclassthurs
    elif lanaknow == False and rubyknow == True:
        $ lanalv += 10
        $ rubylv += 5
        x " [name]! you're just in time for the show! "
        $ lanaknow = True
        ru " Lana's about to show me her 'Juliana and Pedro'! "
        ru " Heard that it's the second to the last episode, too. "
        ru " Better take down notes on what's happening to make sure if one of my theories is true... "
        l " Woah, Ruby??? You have theories??? "
        l " Over my little show?? aw, shucks! "
        ru " That's how good it is, truly! "
        ru " You KNOW your show is good whenever someone starts making theories about it. "
        ru " Theories can also make things interesting by guessing what's coming next... "
        ru " But we're getting out of topic - "
        ru " Let's get on with the show, please! "
        l " You got it! "
        l " The audience asks and you shall recieve!! "
        l " Ahem... "
        l " So we all know that Pedro is currently in a relationship with Rainier. "
        l " Every now and then, Juliana would bump into them. "
        l " Well - it's not an every now and then, but she would ALWAYS bump into them. "
        l " Seeing them on romantic dates would always get her blood BOILING! "
        l " Just seeing them together reminds her of her old relationship with Pedro... "
        l " A relationship that she couldn't have anymore. "
        l " The more she thought about her loss, the more she felt upset. "
        l " One night - she went out drinking in one of the clubs that were in the city that she was in. "
        l " She thought that she would just be out there to drink, nothing else - "
        l " But then she laid her eyes on the very beautiful bartender there. "
        l " She was surprised that she was feeling this way to a woman, she didn't know she could feel something like this... "
        l " She talked to the woman a bit longer, and eventually, she gave the woman her phone number. "
        l " Right after Juliana went home, she called the woman and they talked until 2 AM... "
        l " And what was this woman's name? her name was Dasha. "
        l " She never thought she could feel this way towards women... "
        l " For now, she's just thinking that they're just random thoughts and it'll pass. "
        l " Aaaaaand, that's it for today, folks! "
        l " What happens next? find out tomorrow, last episode for Juliana and Pedro! "
        hide rubyneutral at bottom
        show rubyhappy at left
        ru " Woot! that was great! "
        ru " Man, I knew Juliana would meet someone else to change her life... "
        ru " But I wasn't expecting for it to be a woman! "
        ru " What an interesting twist, Lana! "
        l " Hehe, thanks! "
        scene black with dissolve
        " You spent the rest of the break talking with Lana and Ruby. "
        " Man that episode was peak! "
        " Wasn't expecting the yuri, but that makes it better! "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You walked out of the gym and went to your classroom for the next class. "
        pause 2.0
        jump historyclassthurs
    else:
        $ lanalv += 10
        $ rubylv += 5
        x " [name]! you're just in time for the show! "
        $ lanaknow = True
        x " Lana's about to show me her 'Juliana and Pedro'! "
        $ rubyknow = True
        x " Heard that it's the second to the last episode, too. "
        x " Better take down notes on what's happening to make sure if one of my theories is true... "
        l " Woah, Ruby??? You have theories??? "
        l " Over my little show?? aw, shucks! "
        ru " That's how good it is, truly! "
        ru " You KNOW your show is good whenever someone starts making theories about it. "
        ru " Theories can also make things interesting by guessing what's coming next... "
        ru " But we're getting out of topic - "
        ru " Let's get on with the show, please! "
        l " You got it! "
        l " The audience asks and you shall recieve!! "
        l " Ahem... "
        l " So we all know that Pedro is currently in a relationship with Rainier. "
        l " Every now and then, Juliana would bump into them. "
        l " Well - it's not an every now and then, but she would ALWAYS bump into them. "
        l " Seeing them on romantic dates would always get her blood BOILING! "
        l " Just seeing them together reminds her of her old relationship with Pedro... "
        l " A relationship that she couldn't have anymore. "
        l " The more she thought about her loss, the more she felt upset. "
        l " One night - she went out drinking in one of the clubs that were in the city that she was in. "
        l " She thought that she would just be out there to drink, nothing else - "
        l " But then she laid her eyes on the very beautiful bartender there. "
        l " She was surprised that she was feeling this way to a woman, she didn't know she could feel something like this... "
        l " She talked to the woman a bit longer, and eventually, she gave the woman her phone number. "
        l " Right after Juliana went home, she called the woman and they talked until 2 AM... "
        l " And what was this woman's name? her name was Dasha. "
        l " She never thought she could feel this way towards women... "
        l " For now, she's just thinking that they're just random thoughts and it'll pass. "
        l " Aaaaaand, that's it for today, folks! "
        l " What happens next? find out tomorrow, last episode for Juliana and Pedro! "
        hide rubyneutral at bottom
        show rubyhappy at left
        ru " Woot! that was great! "
        ru " Man, I knew Juliana would meet someone else to change her life... "
        ru " But I wasn't expecting for it to be a woman! "
        ru " What an interesting twist, Lana! "
        l " Hehe, thanks! "
        scene black with dissolve
        " You spent the rest of the break talking with Lana and Ruby. "
        " Man that episode was peak! "
        " Wasn't expecting the yuri, but that makes it better! "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You walked out of the gym and went to your classroom for the next class. "
        pause 2.0
        jump historyclassthurs
label thurscafeteria3:
    # bubble tries to hide away from oliver // kevin needs help carrying books
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked to the cafeteria and spotted two of your classmates doing their own things. "
    " You wanted to talk to one of them, but who do you talk to? "
    if bubbleknow == True and kevinknow == True:
        menu:
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump dkwestewah
            " {image=kevinicon} Kevin {image=kevinicon} ":
                jump kdeastahew
    elif bubbleknow == True and kevinknow == False:
        menu:
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump dkwestewah
            " {image=kevinicon} A nerd {image=kevinicon} ":
                jump kdeastahew
    elif bubbleknow == False and kevinknow == True:
        menu:
            " {image=bubbleicon} A girl made up of bubbles {image=bubbleicon} ":
                jump dkwestewah
            " {image=kevinicon} Kevin {image=kevinicon} ":
                jump kdeastahew
    else:
        menu:
            " {image=bubbleicon} A girl made up of bubbles {image=bubbleicon} ":
                jump dkwestewah
            " {image=kevinicon} A nerd {image=kevinicon} ":
                jump kdeastahew
    label dkwestewah:
        show bubblesad at center with easeinleft
        if bubbleknow == True:
            b " [name], you've gotta help me! " with vpunch
            " You swore you heard someone talking to you... "
            " Maybe it was just the wind. "
            b " Hey, down here! "
            " Never mind, it wasn't just the wind. "
            " You looked underneath the table and found your classmate hiding there. "
            " Wondering why she's hiding, you asked her about it. "
            b " I'm hiding because I overheard that... "
            b " Oliver's going to come after me this break...! "
            b " You've gotta find me a place to hide, [name]! "
            b " I know this isn't a good hiding spot since he can clearly see me... "
            b " So if you have any ideas - please just tell me!! "
            " You quickly thought of some places where she could hide. "
            " Where do you think she should hide? "
            menu:
                " Suck her into your water bottle ":
                    $ bubblelv += 10
                    hide bubblesad at bottom
                    show bubbleconfuse at center
                    b " Good idea - wait what? "
                    b " How's that gonna work? "
                    b " And also, I'm literally made up of, well.. bubbles! "
                    b " Bubbles is literally soap and water! "
                    b " Don't you worry about your water tasting weird? "
                    " You told her it adds to the water's flavor. "
                    b " ...Huh, okay... "
                    hide bubbleconfuse at bottom
                    show bubblesad at center
                    b " Eeek, he's coming! hide me! "
                    hide bubblesad at bottom with easeoutbottom
                    " Bubble then casually transforms herself into her water form and puts herself into your water bottle. "
                    " Huh, you didn't expect for that to work. Atleast she has somewhere to hide now. "
                    " Oh right, Oliver's coming over to you by the way. "
                    show oliverneutral at center with easeinleft
                    o " Hey, idiot. "
                    o " Have you seen that one girl made up of bubbles? "
                    o " Was just planning to give her a nice gift. "
                    " You shook your head and told him that you were just here to drink some water. "
                    o " Really? just water? "
                    o " Gotta at least make it interesting - "
                    o " Ooo, soapy water! "
                    o " Glad to see someone with class in this school. "
                    o " You're still a loser to me though. Cya. "
                    hide oliverneutral at right with easeoutright
                    " And then he leaves. "
                    show bubbleneutral at center with easeinbottom
                    b " Whew...that was a little close... "
                    b " Thank you for helping me, [name]! I appreciate it! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Bubble. "
                    " You truly have taste if you're drinking soapy water. "
                    " I respect you for that. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked out of the cafeteria and then went to your classroom. "
                    pause 2.0
                    jump historyclassthurs
                " Hide in the janitors closet thats in the corner of this room ":
                    $ bubblelv += 10
                    b " I kinda doubt that's gonna work... "
                    b " He's seen me hide in that place before... "
                    b " But, I'll trust you on this one... "
                    b " Don't make it obvious that I'm hiding there! "
                    b " Eeek, he's coming! better go! "
                    hide bubblesad at right with easeoutright
                    " She then leaves. "
                    " Time for you to put on your horrible acting skills... "
                    " You take out your water bottle and drink some of your water. "
                    " It just magically popped up, don't ask me about it. "
                    show oliverneutral at center with easeinleft
                    o " Heya, idiot. "
                    o " You seen a girl made out of bubbles anywhere? "
                    o " Just planning to give her a gift. "
                    " You shook your head and told him that you were just here to drink some water. "
                    o " Really? just water? "
                    o " Gotta at least make it interesting - like soap water. "
                    o " Way better, I tell you. "
                    o " Anyway, I'm not gonna waste my time talking to a loser like you. "
                    o " Later, loser. "
                    hide oliverneutral at right with easeoutright
                    " And then he leaves. "
                    show bubbleneutral at center with easeinleft
                    b " Whew...that was a little close... "
                    b " Thank you for helping me, [name]! I appreciate it! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Bubble. "
                    " You truly have taste if you're drinking soapy water. "
                    " I respect you for that. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked out of the cafeteria and then went to your classroom. "
                    pause 2.0
                    jump historyclassthurs
                " I don't got any hiding spots sorry ":
                    " Before you could even let her say something, you left. "
                    " Wow, feeling rude this break, huh? "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
                    " Wonder what that's about. "
                    " It's not your business, but honestly you can't help but be curious. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You then walked to your classroom after a bit. "
                    pause 2.0
                    jump historyclassthurs
        else:
            x " [name], you've gotta help me! " with vpunch
            " You swore you heard someone talking to you... "
            " Maybe it was just the wind. "
            x " Hey, down here! "
            " Never mind, it wasn't just the wind. "
            " You looked underneath the table and found your classmate hiding there. "
            " Wondering why she's hiding, you asked her about it. "
            $ bubbleknow = True
            b " Before I answer that - I'm Bubble! "
            b " And I'm hiding because I overheard that... "
            b " Oliver's going to come after me this break...! "
            b " You've gotta find me a place to hide, [name]! "
            b " I know this isn't a good hiding spot since he can clearly see me... "
            b " So if you have any ideas - please just tell me!! "
            " You quickly thought of some places where she could hide. "
            " Where do you think she should hide? "
            menu:
                " Suck her into your water bottle ":
                    $ bubblelv += 10
                    hide bubblesad at bottom
                    show bubbleconfuse at center
                    b " Good idea - wait what? "
                    b " How's that gonna work? "
                    b " And also, I'm literally made up of, well.. bubbles! "
                    b " Bubbles is literally soap and water! "
                    b " Don't you worry about your water tasting weird? "
                    " You told her it adds to the water's flavor. "
                    b " ...Huh, okay... "
                    hide bubbleconfuse at bottom
                    show bubblesad at center
                    b " Eeek, he's coming! hide me! "
                    hide bubblesad at bottom with easeoutbottom
                    " Bubble then casually transforms herself into her water form and puts herself into your water bottle. "
                    " Huh, you didn't expect for that to work. Atleast she has somewhere to hide now. "
                    " Oh right, Oliver's coming over to you by the way. "
                    show oliverneutral at center with easeinleft
                    o " Hey, idiot. "
                    o " Have you seen that one girl made up of bubbles? "
                    o " Was just planning to give her a nice gift. "
                    " You shook your head and told him that you were just here to drink some water. "
                    o " Really? just water? "
                    o " Gotta at least make it interesting - "
                    o " Ooo, soapy water! "
                    o " Glad to see someone with class in this school. "
                    o " You're still a loser to me though. Cya. "
                    hide oliverneutral at right with easeoutright
                    " And then he leaves. "
                    show bubbleneutral at center with easeinbottom
                    b " Whew...that was a little close... "
                    b " Thank you for helping me, [name]! I appreciate it! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Bubble. "
                    " You truly have taste if you're drinking soapy water. "
                    " I respect you for that. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked out of the cafeteria and then went to your classroom. "
                    pause 2.0
                    jump historyclassthurs
                " Hide in the janitors closet thats in the corner of this room ":
                    $ bubblelv += 10
                    b " I kinda doubt that's gonna work... "
                    b " He's seen me hide in that place before... "
                    b " But, I'll trust you on this one... "
                    b " Don't make it obvious that I'm hiding there! "
                    b " Eeek, he's coming! better go! "
                    hide bubblesad at right with easeoutright
                    " She then leaves. "
                    " Time for you to put on your horrible acting skills... "
                    " You take out your water bottle and drink some of your water. "
                    " It just magically popped up, don't ask me about it. "
                    show oliverneutral at center with easeinleft
                    o " Heya, idiot. "
                    o " You seen a girl made out of bubbles anywhere? "
                    o " Just planning to give her a gift. "
                    " You shook your head and told him that you were just here to drink some water. "
                    o " Really? just water? "
                    o " Gotta at least make it interesting - like soap water. "
                    o " Way better, I tell you. "
                    o " Anyway, I'm not gonna waste my time talking to a loser like you. "
                    o " Later, loser. "
                    hide oliverneutral at right with easeoutright
                    " And then he leaves. "
                    show bubbleneutral at center with easeinleft
                    b " Whew...that was a little close... "
                    b " Thank you for helping me, [name]! I appreciate it! "
                    scene black with dissolve
                    " You spent the rest of the break talking with Bubble. "
                    " You truly have taste if you're drinking soapy water. "
                    " I respect you for that. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You walked out of the cafeteria and then went to your classroom. "
                    pause 2.0
                    jump historyclassthurs
                " I don't got any hiding spots sorry ":
                    " Before you could even let her say something, you left. "
                    " Wow, feeling rude this break, huh? "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
                    " Wonder what that's about. "
                    " It's not your business, but honestly you can't help but be curious. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You then walked to your classroom after a bit. "
                    pause 2.0
                    jump historyclassthurs
    label kdeastahew:
        show kevinneutral at center with easeinright
        if kevinknow == True:
            kv " God, and I thought studying at the cafeteria was a good idea.. "
            kv " How am I gonna carry all of these books now...? "
            kv " I'm sure I can do this on my own. "
            kv " I just need to do it slowly and steadily... "
            " He picks up a few books, and after a bit, notices you. "
            " He looked a little relieved to see you. "
            kv " Ah, [name]. "
            kv " Thank goodness you're here... "
            kv " I've got something I need help with. "
            kv " You see, I thought it would be a good idea to study in the cafeteria. "
            kv " I could get some food while studying at the same time. "
            kv " Buuut...then I realized just how heavy all of my books in total were. "
            kv " I don't think I could carry them all on my own, unfortunately. "
            kv " I believe I'd only be able to carry 5. "
            " You asked Kevin what got his books to be so heavy. "
            kv " Most likely all of the extra notes I added in for extra explanation. "
            kv " And trust me, I added a LOT. "
            kv " Anyway...do you want to help me with this? "
            kv " It's okay if you don't want to, though. "
            kv " I'm sure I can just do this slowly. "
            kv " Just...transferring each book to my locker... "
            kv " ...One by one. That should be fine. "
            kv " But, I don't mind if you help me with this. "
            menu:
                " Help Kevin ":
                    $ kevinlv += 10
                    hide kevinneutral at bottom
                    show kevinhappy at center
                    kv " Thank you, [name]! "
                    kv " How about you get half, and I get the other half? "
                    kv " It would be easier for both of us. "
                    " You gave him a thumbs up and started getting some of Kevin's books. "
                    " Three books in and GOD they were starting to get heavy. "
                    " The power of knowledge, you guess... "
                    scene black with dissolve
                    " You spent the rest of the break helping Kevin out with his books. "
                    " It was a little difficult with how heavy they were, but you eventually reached his locker. "
                    " You both put all of the notebooks in his locker and then talked for a bit. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the cafeteria and went to your classroom. "
                    pause 2.0
                    jump historyclassthurs
                " I'm busy, sorry ":
                    kv " Ah, that's alright. "
                    kv " I'll be carrying all of these now... "
                    kv " I'll see you in class, [name]. "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
                    " Wonder what that's about. "
                    " It's not your business, but honestly you can't help but be curious. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You then walked to your classroom after a bit. "
                    pause 2.0
                    jump historyclassthurs
        else:
            x " God, and I thought studying at the cafeteria was a good idea.. "
            x " How am I gonna carry all of these books now...? "
            x " I'm sure I can do this on my own. "
            x " I just need to do it slowly and steadily... "
            " He picks up a few books, and after a bit, notices you. "
            " He looked a little relieved to see you. "
            x " Ah, [name]. "
            x " Thank goodness you're here... "
            x " Before I say anything, I need to introduce myself to you first. "
            $ kevinknow = True
            kv " I'm Kevin, nice to meet you. Anywho... "
            kv " I've got something I need help with. "
            kv " You see, I thought it would be a good idea to study in the cafeteria. "
            kv " I could get some food while studying at the same time. "
            kv " Buuut...then I realized just how heavy all of my books in total were. "
            kv " I don't think I could carry them all on my own, unfortunately. "
            kv " I believe I'd only be able to carry 5. "
            " You asked Kevin what got his books to be so heavy. "
            kv " Most likely all of the extra notes I added in for extra explanation. "
            kv " And trust me, I added a LOT. "
            kv " Anyway...do you want to help me with this? "
            kv " It's okay if you don't want to, though. "
            kv " I'm sure I can just do this slowly. "
            kv " Just...transferring each book to my locker... "
            kv " ...One by one. That should be fine. "
            kv " But, I don't mind if you help me with this. "
            menu:
                " Help Kevin ":
                    $ kevinlv += 10
                    hide kevinneutral at bottom
                    show kevinhappy at center
                    kv " Thank you, [name]! "
                    kv " How about you get half, and I get the other half? "
                    kv " It would be easier for both of us. "
                    " You gave him a thumbs up and started getting some of Kevin's books. "
                    " Three books in and GOD they were starting to get heavy. "
                    " The power of knowledge, you guess... "
                    scene black with dissolve
                    " You spent the rest of the break helping Kevin out with his books. "
                    " It was a little difficult with how heavy they were, but you eventually reached his locker. "
                    " You both put all of the notebooks in his locker and then talked for a bit. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked out of the cafeteria and went to your classroom. "
                    pause 2.0
                    jump historyclassthurs
                " I'm busy, sorry ":
                    kv " Ah, that's alright. "
                    kv " I'll be carrying all of these now... "
                    kv " I'll see you in class, [name]. "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
                    " Wonder what that's about. "
                    " It's not your business, but honestly you can't help but be curious. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You then walked to your classroom after a bit. "
                    pause 2.0
                    jump historyclassthurs

label thursrooftop3:
    # robby and riley disagreement
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked up to the rooftop and saw two of your classmates arguing. "
    " Wondering what they're arguing about, you walked over to them. "
    show robbyangry at right with easeinleft
    show rileyangry at left with easeinleft
    if robbyknow == True and rileyknow == True:
        rb " I JUST TOLD YOU THAT I DON'T THINK OLIVER IS THAT INTERESTING! " with vpunch
        ri " HOW COULD YOU SAY THAT ABOUT HIM?! " with vpunch
        ri " HE'S ALL THE WAY INTERESTING, YOU IDIOT! " with vpunch
        ri " I CAN'T JUST HAVE YOU INSULTING MY OLIVER LIKE THAT! " with vpunch
        " Woah, looks like this is some REAL spicy beef here. "
        " Best to just stay out of this and not talk with them. "
        " You don't want to be a victim dragged into this, do you? "
        rb " IT'S JUST MY OPINION, RILEY! " with vpunch
        rb " DON'T YOU KNOW HOW TIRED I GET WHENEVER YOU ASK ME TO MAKE SOMETHING FOR OLIVER?? " with vpunch
        rb " Whenever you talk to me about something - it's about Oliver! "
        rb " Whenever you want something - it's Oliver! "
        rb " It's all OLIVER! I'm sick and tired of hearing the same thing over and over again! "
        ri " Well if you can't get used to THAT, how come Ruby gets used to me talking about him?! "
        rb " That's because Ruby is a robot, you dumbass! "
        rb " Ruby is programmed to be understanding towards her classmates! "
        rb " Of COURSE she would understand you! "
        " ...This is starting to get really beefy. "
        " Maybe you should just...walk away. "
        " It's best for you to not get potentially hurt if one of them gets violent. "
        scene black with dissolve
        " You spent the rest of the break wandering around the school. "
        " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
        " Wonder what that's about. "
        " It's not your business, but honestly you can't help but be curious. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You then walked to your classroom after a bit. "
        pause 2.0
        jump historyclassthurs
    elif robbyknow == True and rileyknow == False:
        rb " I JUST TOLD YOU THAT I DON'T THINK OLIVER IS THAT INTERESTING! " with vpunch
        x " HOW COULD YOU SAY THAT ABOUT HIM?! " with vpunch
        x " HE'S ALL THE WAY INTERESTING, YOU IDIOT! " with vpunch
        x " I CAN'T JUST HAVE YOU INSULTING MY OLIVER LIKE THAT! " with vpunch
        " Woah, looks like this is some REAL spicy beef here. "
        " Best to just stay out of this and not talk with them. "
        " You don't want to be a victim dragged into this, do you? "
        rb " IT'S JUST MY OPINION, RILEY! " with vpunch
        rb " DON'T YOU KNOW HOW TIRED I GET WHENEVER YOU ASK ME TO MAKE SOMETHING FOR OLIVER?? " with vpunch
        rb " Whenever you talk to me about something - it's about Oliver! "
        rb " Whenever you want something - it's Oliver! "
        rb " It's all OLIVER! I'm sick and tired of hearing the same thing over and over again! "
        x " Well if you can't get used to THAT, how come Ruby gets used to me talking about him?! "
        rb " That's because Ruby is a robot, you dumbass! "
        rb " Ruby is programmed to be understanding towards her classmates! "
        rb " Of COURSE she would understand you! "
        " ...This is starting to get really beefy. "
        " Maybe you should just...walk away. "
        " It's best for you to not get potentially hurt if one of them gets violent. "
        scene black with dissolve
        " You spent the rest of the break wandering around the school. "
        " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
        " Wonder what that's about. "
        " It's not your business, but honestly you can't help but be curious. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You then walked to your classroom after a bit. "
        pause 2.0
        jump historyclassthurs
    elif robbyknow == False and rileyknow == True:
        x " I JUST TOLD YOU THAT I DON'T THINK OLIVER IS THAT INTERESTING! " with vpunch
        ri " HOW COULD YOU SAY THAT ABOUT HIM?! " with vpunch
        ri " HE'S ALL THE WAY INTERESTING, YOU IDIOT! " with vpunch
        ri " I CAN'T JUST HAVE YOU INSULTING MY OLIVER LIKE THAT! " with vpunch
        " Woah, looks like this is some REAL spicy beef here. "
        " Best to just stay out of this and not talk with them. "
        " You don't want to be a victim dragged into this, do you? "
        x " IT'S JUST MY OPINION, RILEY! " with vpunch
        x " DON'T YOU KNOW HOW TIRED I GET WHENEVER YOU ASK ME TO MAKE SOMETHING FOR OLIVER?? " with vpunch
        x " Whenever you talk to me about something - it's about Oliver! "
        x " Whenever you want something - it's Oliver! "
        x " It's all OLIVER! I'm sick and tired of hearing the same thing over and over again! "
        ri " Well if you can't get used to THAT, how come Ruby gets used to me talking about him?! "
        x " That's because Ruby is a robot, you dumbass! "
        x " Ruby is programmed to be understanding towards her classmates! "
        x " Of COURSE she would understand you! "
        " ...This is starting to get really beefy. "
        " Maybe you should just...walk away. "
        " It's best for you to not get potentially hurt if one of them gets violent. "
        scene black with dissolve
        " You spent the rest of the break wandering around the school. "
        " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
        " Wonder what that's about. "
        " It's not your business, but honestly you can't help but be curious. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You then walked to your classroom after a bit. "
        pause 2.0
        jump historyclassthurs
    else:
        x " I JUST TOLD YOU THAT I DON'T THINK OLIVER IS THAT INTERESTING! " with vpunch
        x " HOW COULD YOU SAY THAT ABOUT HIM?! " with vpunch
        x " HE'S ALL THE WAY INTERESTING, YOU IDIOT! " with vpunch
        x " I CAN'T JUST HAVE YOU INSULTING MY OLIVER LIKE THAT! " with vpunch
        " Woah, looks like this is some REAL spicy beef here. "
        " Best to just stay out of this and not talk with them. "
        " You don't want to be a victim dragged into this, do you? "
        x " IT'S JUST MY OPINION, RILEY! " with vpunch
        x " DON'T YOU KNOW HOW TIRED I GET WHENEVER YOU ASK ME TO MAKE SOMETHING FOR OLIVER?? " with vpunch
        x " Whenever you talk to me about something - it's about Oliver! "
        x " Whenever you want something - it's Oliver! "
        x " It's all OLIVER! I'm sick and tired of hearing the same thing over and over again! "
        x " Well if you can't get used to THAT, how come Ruby gets used to me talking about him?! "
        x " That's because Ruby is a robot, you dumbass! "
        x " Ruby is programmed to be understanding towards her classmates! "
        x " Of COURSE she would understand you! "
        " ...This is starting to get really beefy. "
        " Maybe you should just...walk away. "
        " It's best for you to not get potentially hurt if one of them gets violent. "
        scene black with dissolve
        " You spent the rest of the break wandering around the school. "
        " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
        " Wonder what that's about. "
        " It's not your business, but honestly you can't help but be curious. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your next class. "
        " You then walked to your classroom after a bit. "
        pause 2.0
        jump historyclassthurs
label thurslibrary3:
    # engel cleans up the library // claire needs help carrying her project
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and saw two of your classmates doing their own things. "
    " You wanted to talk to one of them, but who do you talk to? "
    if engelknow == True and claireknow == True:
        menu:
            " {image=engelicon} Engel {image=engelicon} ":
                jump tatianana
            " {image=claireicon} Claire {image=claireicon} ":
                jump titanana
    elif engelknow == True and claireknow == False:
        menu:
            " {image=engelicon} Engel {image=engelicon} ":
                jump tatianana
            " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                jump titanana
    elif engelknow == False and claireknow == True:
        menu:
            " {image=engelicon} A guy with feathers on his head {image=engelicon} ":
                jump tatianana
            " {image=claireicon} Claire {image=claireicon} ":
                jump titanana
    else:
        menu:
            " {image=engelicon} A guy with feathers on his head {image=engelicon} ":
                jump tatianana
            " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                jump titanana
    label tatianana:
        show engelneutral at center with easeinleft
        if engelknow == True:
            e " Oh dear...who did this...? "
            e " Must've been Oliver and his little gang again... "
            e " Sigh...no one in this school would be willing to pick all of this up... "
            e " I suppose...I'll return everything to their original places. "
            " The library is completely and utterly wrecked. "
            " Yep, this looks like something that Oliver would do. "
            " You cough and asked Engel if he needed any help. "
            hide engelneutral at bottom
            show engelhappy at center
            e " Ah, hello there [name]. "
            e " It's nice of you to offer to help, but... "
            e " I think I can do all of this on my own. "
            e " I don't want to bother you, of course. "
            e " You can go ahead and do something else that you want. "
            menu:
                " I want to help ":
                    $ engellv += 10
                    e " ...You really do want to help, hm? "
                    e " Well then...if you REALLY want to help... "
                    e " You could take that side of the library and I'll take this side. "
                    e " That side has less mess than mine. "
                    " You told him that you were going to take the side with more mess. "
                    e " ...Fine, but if I finish first, then I'm helping you out. "
                    scene black with dissolve
                    " You spent the rest of the break helping Engel with the books. "
                    " Engel actually managed to clean up first and he helped you. "
                    " You guys then talked for a bit the moment you guys finished. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You then walked to your classroom after a bit. "
                    pause 2.0
                    jump historyclassthurs
                " Okay, if you say so ":
                    e " If you need anything, I'll be here. "
                    e " Take care! "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
                    " Wonder what that's about. "
                    " It's not your business, but honestly you can't help but be curious. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You then walked to your classroom after a bit. "
                    pause 2.0
                    jump historyclassthurs
        else:
            x " Oh dear...who did this...? "
            x " Must've been Oliver and his little gang again... "
            x " Sigh...no one in this school would be willing to pick all of this up... "
            x " I suppose...I'll return everything to their original places. "
            " The library is completely and utterly wrecked. "
            " Yep, this looks like something that Oliver would do. "
            $ engelknow = True
            " Hey wait, isn't this that one kid named Engel? oh wow. "
            " You cough and asked Engel if he needed any help. "
            hide engelneutral at bottom
            show engelhappy at center
            e " Ah, hello there [name]. "
            e " It's nice of you to offer to help, but... "
            e " I think I can do all of this on my own. "
            e " I don't want to bother you, of course. "
            e " You can go ahead and do something else that you want. "
            menu:
                " I want to help ":
                    $ engellv += 10
                    e " ...You really do want to help, hm? "
                    e " Well then...if you REALLY want to help... "
                    e " You could take that side of the library and I'll take this side. "
                    e " That side has less mess than mine. "
                    " You told him that you were going to take the side with more mess. "
                    e " ...Fine, but if I finish first, then I'm helping you out. "
                    scene black with dissolve
                    " You spent the rest of the break helping Engel with the books. "
                    " Engel actually managed to clean up first and he helped you. "
                    " You guys then talked for a bit the moment you guys finished. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You then walked to your classroom after a bit. "
                    pause 2.0
                    jump historyclassthurs
                " Okay, if you say so ":
                    e " If you need anything, I'll be here. "
                    e " Take care! "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
                    " Wonder what that's about. "
                    " It's not your business, but honestly you can't help but be curious. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You then walked to your classroom after a bit. "
                    pause 2.0
                    jump historyclassthurs
    label titanana:
        if clairebeatup == True and clairesorry == False:
            " You can't interact with someone here because you didn't apologize. "
            " Sorry not sorry. "
            scene black
            pause 2.0
            jump historyclassthurs
        else:
            pass
        show claireneutral at center with easeinright
        if claireknow == True:
            c " Man, I think I added too much stuff on here... "
            c " But, whatever it takes to please Miss Sasha! "
            c " I'm sure she'll like this... "
            c " Just gotta...carry this... "
            c " God I made this too heavy. Maybe I did add too much stuff... "
            " You poked her shoulder and asked her is she needed help. "
            " You kinda felt like helping this break. "
            c " Hey there, [name]! "
            c " You wanna help me carry my project? "
            c " It's nice of you to offer, but I think I can handle it on my own. "
            c " I just need to carry this to Miss Sasha's classroom! "
            c " I don't want to bother you by making you help me.. "
            c " You can go ahead and do anything you want for the rest of the break! "
            c " Though...I wouldn't mind the help. "
            menu:
                " Help Claire. ":
                    $ clairelv += 10
                    c " Ooh, you really wanna help? "
                    hide claireneutral at bottom
                    show clairehappy at center
                    c " That's very kind of you, [name]! "
                    c " Here, you can do the other side and I'll hold onto this side... "
                    c " It's a little heavy, so be careful! "
                    c " You might drop it on accident, and I don't want that happening... "
                    c " This DID take me all night to make... "
                    scene black with dissolve
                    " You spent the rest of the break helping Claire with carrying her project. "
                    " It was a little bit heavy, yes, but you managed. "
                    " You guys eventually transported it to Miss Sasha's classroom and you guys got to talk for a bit. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You then walked to your classroom after a bit. "
                    pause 2.0
                    jump historyclassthurs
                " Yeah no i gotta go ":
                    c " Mmm...alright! "
                    c " I'll see you later in class then! "
                    c " Take care! "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
                    " Wonder what that's about. "
                    " It's not your business, but honestly you can't help but be curious. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You then walked to your classroom after a bit. "
                    pause 2.0
                    jump historyclassthurs
        else:
            x " Man, I think I added too much stuff on here... "
            x " But, whatever it takes to please Miss Sasha! "
            x " I'm sure she'll like this... "
            x " Just gotta...carry this... "
            x " God I made this too heavy. Maybe I did add too much stuff... "
            " You poked her shoulder and asked her is she needed help. "
            " You kinda felt like helping this break. "
            x " Hey there, [name]! "
            $ claireknow = True
            x " I don't think we've met before...did I not introduce myself to you? "
            c " Ooops, sorry... I'm Claire, it's nice to meet you! Anywho... "
            c " You wanna help me carry my project? "
            c " It's nice of you to offer, but I think I can handle it on my own. "
            c " I just need to carry this to Miss Sasha's classroom! "
            c " I don't want to bother you by making you help me.. "
            c " You can go ahead and do anything you want for the rest of the break! "
            c " Though...I wouldn't mind the help. "
            menu:
                " Help Claire. ":
                    $ clairelv += 10
                    c " Ooh, you really wanna help? "
                    hide claireneutral at bottom
                    show clairehappy at center
                    c " That's very kind of you, [name]! "
                    c " Here, you can do the other side and I'll hold onto this side... "
                    c " It's a little heavy, so be careful! "
                    c " You might drop it on accident, and I don't want that happening... "
                    c " This DID take me all night to make... "
                    scene black with dissolve
                    " You spent the rest of the break helping Claire with carrying her project. "
                    " It was a little bit heavy, yes, but you managed. "
                    " You guys eventually transported it to Miss Sasha's classroom and you guys got to talk for a bit. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You then walked to your classroom after a bit. "
                    pause 2.0
                    jump historyclassthurs
                " Yeah no i gotta go ":
                    c " Mmm...alright! "
                    c " I'll see you later in class then! "
                    c " Take care! "
                    scene black with dissolve
                    " You spent the rest of the break wandering around the school. "
                    " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
                    " Wonder what that's about. "
                    " It's not your business, but honestly you can't help but be curious. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You then walked to your classroom after a bit. "
                    pause 2.0
                    jump historyclassthurs
label thursoligang3:
    scene black with dissolve
    pause 2.0
    scene oligangclub with dissolve
    " You walked into the room and only saw Zip in there. "
    " Wanting to know what she's up to, you decided to walk up to her. "
    show zipneutral at center with easeinleft
    z " Heya there, [name]! "
    z " If you're wondering what I'm doing, it's a uhhh... "
    z " It's a little hard for me to explain, actually. "
    z " But let's say... "
    z " Me and the gang will be going on a little ghost hunting tonight. "
    z " I'm just planning out a few things. "
    z " Like, a uhhh... "
    z " A list of things for us to check out. "
    z " For example: if we see weed, we'll check that out in the list. "
    z " You get what I'm getting at? "
    z " Actually, maybe you could help me out on this. "
    z " Starting to run out of ideas here... "
    menu:
        " sure lol ":
            $ oliganglv += 10
            z " Sweet. "
            scene black with dissolve
            " You spent the rest of the break helping Zip with the list. "
            " You mostly put some stupid stuff there... "
            " I mean, Oliver literally put in WEED. And SOAP. "
            " Edward just put in yaoi. "
            " You decided to put in yuri for fun. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You then walked to your classroom after a bit. "
            pause 2.0
            jump historyclassthurs
        " nah im out ":
            hide zipneutral at bottom
            show zipangry at center
            z " Damn, alright. "
            scene black with dissolve
            " You spent the rest of the break wandering around the school. "
            " While you were walking around, you saw an angry bunny girl storming off to somewhere... "
            " Wonder what that's about. "
            " It's not your business, but honestly you can't help but be curious. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You then walked to your classroom after a bit. "
            pause 2.0
            jump historyclassthurs

label historyclassthurs:
    scene classroom with dissolve
    " You walked into the classroom and patiently waited for the history teacher to arrive. "
    " Whilst you were waiting, you were trying to remember what you had done yesterday... "
    " But alas, your memory is that of a goldfish... "
    " ...Technically, it's the programmer's fault for not remembering. "
    " And technically this is the programmer insulting himself right now. "
    " Funny haha. Play the laugh sound effect now. "
    " Anyway, after a few minutes, the teacher arrives and you lock in. "
    show msemilyneutral at center with easeinright
    mse " Hello, class! "
    mse " Hopefully all of you are having a good day right now... "
    mse " What we're going to do today iiiiiss... "
    mse " ...Talking more about what we had learnt yesterday! "
    mse " Since there's some people who didn't understand what we learnt yesterday, "
    mse " I thought that a review and a little more explanation would do. "
    mse " If you guys have any questions, please note that it's completely fine to ask me! "
    hide msemilyneutral at bottom
    show msemilyangry at center
    mse " ...Just, don't ask the same question. "
    mse " It reall ticks me off whenever someone asks me that same thing over and over again. "
    hide msemilyangry at bottom
    show msemilyneutral at center
    mse " Anyway, let's get on with the lesson! "
    scene black with dissolve
    " You spent the rest of class hours trying your best not to fall asleep. "
    " The topic was just really that boring, but you had to pay attention otherwise Miss Emily's going to whack you on the head. "
    " You most certainly didn't want that happening. "
    " Oh, and hey...looks like you're about to survive the class. "
    play sound "audio/bellring.mp3"
    " The bell rings, snapping you out of your sleepiness. "
    " You then walked to the hallways so that you could get on with your break. "
    pause 2.0
    jump thursbreak4

label thursbreak4:
    scene hallway with dissolve
    if oligangjoin == True:
        jump thursoligang4
    else:
        pass
    " Where do you wanna go for this break? "
    menu:
        " {image=lanaicon} The front of the school {image=bubbleicon} ":
            jump thursfrontschool4
        " {image=engelicon} The back of the school {image=popularicon} ":
            jump thursbackschool4
        " {image=skellicon} The gym {image=rileyicon} ":
            jump thursgym4
        " {image=claireicon} The cafeteria {image=rubyicon} ":
            jump thurscafeteria4
        " {image=abbieicon} The rooftop {image=cubbieicon} ":
            jump thursrooftop4
        " {image=robbyicon} The library {image=kevinicon} ":
            jump thurslibrary4

label thursfrontschool4:
    # lana and bubble
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of the school and spotted two of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if lanaknow == True and bubbleknow == True:
        menu:
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump goomball
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump koomball
    elif lanaknow == True and bubbleknow == True:
        menu:
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump goomball
            " {image=bubbleicon} A girl made up of bubbles {image=bubbleicon} ":
                jump koomball
    elif lanaknow == False and bubbleknow == True:
        menu:
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump goomball
            " {image=bubbleicon} Bubble {image=bubbleicon} ":
                jump koomball
    else:
        menu:
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump goomball
            " {image=bubbleicon} A girl made up of bubbles {image=bubbleicon} ":
                jump koomball
    label goomball:
        show lananeutral at center with easeinright
        if lanaknow == True:
            " You walked up to her and greeted her, "
            " Then asked what she was doing. "
            hide lananeutral at bottom
            show lanahappy at center
            l " Hi, [name]!! "
            l " Just doing...basically nothing. "
            hide lanahappy at bottom
            show lananeutral at center
            l " I have no idea what to do this break...other than look at bunny photos. "
            l " Bunnies are really cute, honestly! "
            l " Though, I don't know if I'd be a good owner, hehehhh... "
            l " I think I'll just stick onto watching videos for now. "
            l " Anyywayyy, were you thinking of doing anything else this break? "
            l " I'm out of ideas... "
            " You shrugged. You were kinda expecting for her to be doing something right now. "
            " You then had an idea. She talked about bunnies earlier.. "
            " Not really an idea, just a question you're about to ask her. "
            if popularknow == True:
                " You asked her what she did when she first saw Petunia. "
            else:
                " You asked her what she did when she first saw that one rabbit popular girl. "
            l " Oh geez, Petunia?? "
            hide lananeutral at bottom
            show lanahappy at center
            l " Well, to be honest... "
            l " I may or may not have freaked out a little when I first saw her. "
            l " Look, she was a rabbit! of course I would freak out just a LITTLE! "
            l " Good thing Engel noticed I was looking and he held me back. "
            l " The urge to pet her was STRONG...but I can't be weird... "
            l " I don't want to make myself look weird infront of one of the popular girls! "
            hide lanahappy at bottom
            show lananeutral at center
            l" Thankfully Engel held me back at the time... "
            l " Otherwise I don't know how I would've controlled myself. "
            l " I wonder if she ever noticed that I was looking... "
            l " Probably not, since she was looking at her phone at the time. "
            l " But still, there's a possibility that she noticed... "
            l " And that's not good for me at all. "
            scene black with dissolve
            " You spent the rest of the break talking about bunnies with Lana. "
            " Huh...I'm wondering if this whole part of the game was because the programmer got a bunny recently. "
            " Interesting. Bunnies are really cute though, so we can't complain. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, time for your next class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump musicclassthurs
        else:
            " You walked up to her and greeted her, "
            " Then asked what she was doing. "
            hide lananeutral at bottom
            show lanahappy at center
            x " Hi, [name]!! "
            x " Just doing...basically nothing. "
            $ lanaknow = True
            l " I'm Lana, by the way! Nice to meet you! "
            hide lanahappy at bottom
            show lananeutral at center
            l " I have no idea what to do this break...other than look at bunny photos. "
            l " Bunnies are really cute, honestly! "
            l " Though, I don't know if I'd be a good owner, hehehhh... "
            l " I think I'll just stick onto watching videos for now. "
            l " Anyywayyy, were you thinking of doing anything else this break? "
            l " I'm out of ideas... "
            " You shrugged. You were kinda expecting for her to be doing something right now. "
            " You then had an idea. She talked about bunnies earlier.. "
            " Not really an idea, just a question you're about to ask her. "
            if popularknow == True:
                " You asked her what she did when she first saw Petunia. "
            else:
                " You asked her what she did when she first saw that one rabbit popular girl. "
            l " Oh geez, Petunia?? "
            hide lananeutral at bottom
            show lanahappy at center
            l " Well, to be honest... "
            l " I may or may not have freaked out a little when I first saw her. "
            l " Look, she was a rabbit! of course I would freak out just a LITTLE! "
            l " Good thing Engel noticed I was looking and he held me back. "
            l " The urge to pet her was STRONG...but I can't be weird... "
            l " I don't want to make myself look weird infront of one of the popular girls! "
            hide lanahappy at bottom
            show lananeutral at center
            l" Thankfully Engel held me back at the time... "
            l " Otherwise I don't know how I would've controlled myself. "
            l " I wonder if she ever noticed that I was looking... "
            l " Probably not, since she was looking at her phone at the time. "
            l " But still, there's a possibility that she noticed... "
            l " And that's not good for me at all. "
            scene black with dissolve
            " You spent the rest of the break talking about bunnies with Lana. "
            " Huh...I'm wondering if this whole part of the game was because the programmer got a bunny recently. "
            " Interesting. Bunnies are really cute though, so we can't complain. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, time for your next class. "
            " You walked back into the school and went to your classroom. "
            pause 2.0
            jump musicclassthurs
    label koomball:
        show bubbleneutral at center with easeinleft
        if bubbleknow == True:
            b " Hello there, [name]! "
            b " I was just looking at the grass.. "
            b " And noticed that a few ants have made a few ant mounds! "
            b " I'm not really the type to crush them... "
            b " I mean, they've worked hard on it, sure! "
            b " But they can also be a little annoying - ants, I mean. "
            b " I look away for ONE second, and guess what I see? "
            hide bubbleneutral at bottom
            show bubbleangry at center
            b " An ant biting my leg. "
            b " And it's not a normal ant, no - "
            b " It's one of those red ants! "
            b " You know? the ones with the very painful bites? "
            b " God I hate those things... "
            b " I know it's just a small animal, but I can't help but feel so annoyed!! "
            b " Like jeez, you could've bit someone else! "
            b " Besides, I'm literally just made up of bubbles - "
            hide bubbleangry at bottom
            show bubbleconfuse at center
            b " Wait, how does that work?? "
            b " An ant bit me and I'm literally made out of bubbles... "
            b " How do I still feel pain?? "
            b " And isn't my blood going to be, like...soap and water? "
            b " Don't ants not like water??? and soap??? "
            hide bubbleconfuse at bottom
            show bubbleneutral at center
            b " Man, life confuses me sometimes. "
            b " But I guess we just have to deal with how life is... "
            b " Still doesn't help that a few things are confusing though. "
            scene black with dissolve
            " You spent the rest of the break talking with Bubble. "
            " I agree, ants ARE pretty annoying. "
            " Especially when you look away for one moment and there's already ants on it. "
            " Annoying as hell. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You then went back inside the school and went to your classroom. "
            pause 2.0
            jump musicclassthurs
        else:
            x " Hello there, [name]! "
            x " Oh! I don't think I've introduced myself before to you... "
            x " Sorry, silly me... "
            $ bubbleknow = True
            b " I'm Bubble! It's nice to meet you! "
            b " Anywho... "
            b " I was just looking at the grass.. "
            b " And noticed that a few ants have made a few ant mounds! "
            b " I'm not really the type to crush them... "
            b " I mean, they've worked hard on it, sure! "
            b " But they can also be a little annoying - ants, I mean. "
            b " I look away for ONE second, and guess what I see? "
            hide bubbleneutral at bottom
            show bubbleangry at center
            b " An ant biting my leg. "
            b " And it's not a normal ant, no - "
            b " It's one of those red ants! "
            b " You know? the ones with the very painful bites? "
            b " God I hate those things... "
            b " I know it's just a small animal, but I can't help but feel so annoyed!! "
            b " Like jeez, you could've bit someone else! "
            b " Besides, I'm literally just made up of bubbles - "
            hide bubbleangry at bottom
            show bubbleconfuse at center
            b " Wait, how does that work?? "
            b " An ant bit me and I'm literally made out of bubbles... "
            b " How do I still feel pain?? "
            b " And isn't my blood going to be, like...soap and water? "
            b " Don't ants not like water??? and soap??? "
            hide bubbleconfuse at bottom
            show bubbleneutral at center
            b " Man, life confuses me sometimes. "
            b " But I guess we just have to deal with how life is... "
            b " Still doesn't help that a few things are confusing though. "
            scene black with dissolve
            " You spent the rest of the break talking with Bubble. "
            " I agree, ants ARE pretty annoying. "
            " Especially when you look away for one moment and there's already ants on it. "
            " Annoying as hell. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for your next class. "
            " You then went back inside the school and went to your classroom. "
            pause 2.0
            jump musicclassthurs
label thursbackschool4:
    # engel dealing with petunia...again.
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    " You walked to the back of the school and spotted two of your classmates talking with eachother. "
    " Curious on what they're talking about, you decided to join in their conversation. "
    show engelneutral at left with easeinright
    show petuniaangry at right with easeinright
    if engelknow == True and popularknow == True:
        e " ...Petunia, you've got to calm down. "
        p " CALM DOWN?! "
        p " Why should I calm down, Engel. "
        " Well damn, looks like someone's mad. "
        " You're curious on what she's mad about though... "
        e " Uh...um... "
        e " Because...???? "
        p " BECAUSE WHAT, ENGEL!! " with vpunch
        p " How can I be calm when I know I'm in a school with a BITCH. "
        e " Petunia, I really think you should stop talking about Lizzy like that... "
        e " I know that you two can be friends again... "
        e " You two have gotten in misunderstandings before, but you both managed to come back together just fine! "
        e " I don't think I've talked to you about this before, but... "
        e " What's your problem with Lizzy? Just a few days ago, you two were fine... "
        p " ...What's my problem with her? "
        p " WHAT'S MY PROBLEM WITH HER?! " with vpunch
        e " uh yeah that's what I said{nw} "
        p " My problem with her is that she's horrible at communication! "
        p " I ask her why she's being mad - she ignores me! "
        p " Like, hello? I ask you what's going on with you, and you respond with nothing but silence! "
        p " How am I supposed to fix things if you don't tell me what's going wrong with you?! "
        p " God, it just pisses me off really bad! "
        hide engelneutral at bottom
        show engelsad at left
        e " Hmm...you're right - she kind of needs to communicate with you, "
        e " But that doesn't mean that she should just immediately spit out the reason why she isn't talking. "
        p " ...What do you mean by that. "
        hide engelsad at bottom
        show engelneutral at left
        e " What if she isn't comfortable with sharing yet? "
        e " Maybe you just need to give her some time alone so that she could get herself some confidence to tell you. "
        e " The thing she might be going through - it's probably embarrassing to her... "
        e " ...And you just need a little patience to wait for her to say what she needs to say. "
        p " Well what if I want her to say it now???? "
        menu:
            " Maybe you should listen to what Engel says ":
                $ engellv += 10
                $ popularlv += 10
                hide engelneutral at bottom
                show engelhappy at left
                e " ([name]? I didn't know that you were here...) "
                e " (Thanks for agreeing with me though.) "
                e " (Petunia needs to hear this, even though she's being a little stubborn right now.) "
                hide engelhappy at bottom
                show engelneutral at left
                e " Ahem...it's not like you can force her to just say it. "
                e " Infact, that's just gonna worsen the situation. "
                e " I know that you don't want that to happen... "
                e " ...Don't you? "
                hide petuniaangry at bottom
                show petuniasad at right
                p " ...Sigh...no I don't. "
                p " Thanks for listening and giving me advice, Engel. "
                p " I'll give her some time to think it out. "
                e " No problem, Petunia. "
                scene black with dissolve
                " You spent the rest of the break talking with Engel and Petunia after their conversation. "
                " Petunia looked a little down after the whole thing, but you managed to make her laugh by making a joke. "
                " Thankfully...you didn't like her with a frown. "
                " You're glad to make her happy. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your clasroom. "
                pause 2.0
                jump musicclassthurs
            " *Stay silent* ":
                " Yeah, let's just stay silent. "
                " You don't really wanna be a part of this. "
                e " ...It's not like you can force her to just say it. "
                e " Infact, that's just gonna worsen the situation. "
                e " I know that you don't want that to happen... "
                e " ...Don't you? "
                hide petuniaangry at bottom
                show petuniasad at right
                p " ...Sigh...no I don't. "
                p " Thanks for listening and giving me advice, Engel. "
                p " I'll give her some time to think it out. "
                e " No problem, Petunia. "
                scene black with dissolve
                " You spent the rest of the break talking with Engel and Petunia after their conversation. "
                " Petunia looked a little down after the whole thing, but you managed to make her laugh by making a joke. "
                " Thankfully...you didn't like her with a frown. "
                " You're glad to make her happy. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your clasroom. "
                pause 2.0
                jump musicclassthurs
    elif engelknow == True and popularknow == False:
        e " ...Petunia, you've got to calm down. "
        $ popularknow = True
        p " CALM DOWN?! "
        p " Why should I calm down, Engel. "
        " Well damn, looks like someone's mad. "
        " You're curious on what she's mad about though... "
        e " Uh...um... "
        e " Because...???? "
        p " BECAUSE WHAT, ENGEL!! " with vpunch
        p " How can I be calm when I know I'm in a school with a BITCH. "
        e " Petunia, I really think you should stop talking about Lizzy like that... "
        e " I know that you two can be friends again... "
        e " You two have gotten in misunderstandings before, but you both managed to come back together just fine! "
        e " I don't think I've talked to you about this before, but... "
        e " What's your problem with Lizzy? Just a few days ago, you two were fine... "
        p " ...What's my problem with her? "
        p " WHAT'S MY PROBLEM WITH HER?! " with vpunch
        e " uh yeah that's what I said{nw} "
        p " My problem with her is that she's horrible at communication! "
        p " I ask her why she's being mad - she ignores me! "
        p " Like, hello? I ask you what's going on with you, and you respond with nothing but silence! "
        p " How am I supposed to fix things if you don't tell me what's going wrong with you?! "
        p " God, it just pisses me off really bad! "
        hide engelneutral at bottom
        show engelsad at left
        e " Hmm...you're right - she kind of needs to communicate with you, "
        e " But that doesn't mean that she should just immediately spit out the reason why she isn't talking. "
        p " ...What do you mean by that. "
        hide engelsad at bottom
        show engelneutral at left
        e " What if she isn't comfortable with sharing yet? "
        e " Maybe you just need to give her some time alone so that she could get herself some confidence to tell you. "
        e " The thing she might be going through - it's probably embarrassing to her... "
        e " ...And you just need a little patience to wait for her to say what she needs to say. "
        p " Well what if I want her to say it now???? "
        menu:
            " Maybe you should listen to what Engel says ":
                $ engellv += 10
                $ popularlv += 10
                hide engelneutral at bottom
                show engelhappy at left
                e " ([name]? I didn't know that you were here...) "
                e " (Thanks for agreeing with me though.) "
                e " (Petunia needs to hear this, even though she's being a little stubborn right now.) "
                hide engelhappy at bottom
                show engelneutral at left
                e " Ahem...it's not like you can force her to just say it. "
                e " Infact, that's just gonna worsen the situation. "
                e " I know that you don't want that to happen... "
                e " ...Don't you? "
                hide petuniaangry at bottom
                show petuniasad at right
                p " ...Sigh...no I don't. "
                p " Thanks for listening and giving me advice, Engel. "
                p " I'll give her some time to think it out. "
                e " No problem, Petunia. "
                scene black with dissolve
                " You spent the rest of the break talking with Engel and Petunia after their conversation. "
                " Petunia looked a little down after the whole thing, but you managed to make her laugh by making a joke. "
                " Thankfully...you didn't like her with a frown. "
                " You're glad to make her happy. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your clasroom. "
                pause 2.0
                jump musicclassthurs
            " *Stay silent* ":
                " Yeah, let's just stay silent. "
                " You don't really wanna be a part of this. "
                e " ...It's not like you can force her to just say it. "
                e " Infact, that's just gonna worsen the situation. "
                e " I know that you don't want that to happen... "
                e " ...Don't you? "
                hide petuniaangry at bottom
                show petuniasad at right
                p " ...Sigh...no I don't. "
                p " Thanks for listening and giving me advice, Engel. "
                p " I'll give her some time to think it out. "
                e " No problem, Petunia. "
                scene black with dissolve
                " You spent the rest of the break talking with Engel and Petunia after their conversation. "
                " Petunia looked a little down after the whole thing, but you managed to make her laugh by making a joke. "
                " Thankfully...you didn't like her with a frown. "
                " You're glad to make her happy. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your clasroom. "
                pause 2.0
                jump musicclassthurs
    elif engelknow == False and popularknow == True:
        x " ...Petunia, you've got to calm down. "
        p " CALM DOWN?! "
        $ engelknow = True
        p " Why should I calm down, Engel. "
        " Well damn, looks like someone's mad. "
        " You're curious on what she's mad about though... "
        e " Uh...um... "
        e " Because...???? "
        p " BECAUSE WHAT, ENGEL!! " with vpunch
        p " How can I be calm when I know I'm in a school with a BITCH. "
        e " Petunia, I really think you should stop talking about Lizzy like that... "
        e " I know that you two can be friends again... "
        e " You two have gotten in misunderstandings before, but you both managed to come back together just fine! "
        e " I don't think I've talked to you about this before, but... "
        e " What's your problem with Lizzy? Just a few days ago, you two were fine... "
        p " ...What's my problem with her? "
        p " WHAT'S MY PROBLEM WITH HER?! " with vpunch
        e " uh yeah that's what I said{nw} "
        p " My problem with her is that she's horrible at communication! "
        p " I ask her why she's being mad - she ignores me! "
        p " Like, hello? I ask you what's going on with you, and you respond with nothing but silence! "
        p " How am I supposed to fix things if you don't tell me what's going wrong with you?! "
        p " God, it just pisses me off really bad! "
        hide engelneutral at bottom
        show engelsad at left
        e " Hmm...you're right - she kind of needs to communicate with you, "
        e " But that doesn't mean that she should just immediately spit out the reason why she isn't talking. "
        p " ...What do you mean by that. "
        hide engelsad at bottom
        show engelneutral at left
        e " What if she isn't comfortable with sharing yet? "
        e " Maybe you just need to give her some time alone so that she could get herself some confidence to tell you. "
        e " The thing she might be going through - it's probably embarrassing to her... "
        e " ...And you just need a little patience to wait for her to say what she needs to say. "
        p " Well what if I want her to say it now???? "
        menu:
            " Maybe you should listen to what Engel says ":
                $ engellv += 10
                $ popularlv += 10
                hide engelneutral at bottom
                show engelhappy at left
                e " ([name]? I didn't know that you were here...) "
                e " (Thanks for agreeing with me though.) "
                e " (Petunia needs to hear this, even though she's being a little stubborn right now.) "
                hide engelhappy at bottom
                show engelneutral at left
                e " Ahem...it's not like you can force her to just say it. "
                e " Infact, that's just gonna worsen the situation. "
                e " I know that you don't want that to happen... "
                e " ...Don't you? "
                hide petuniaangry at bottom
                show petuniasad at right
                p " ...Sigh...no I don't. "
                p " Thanks for listening and giving me advice, Engel. "
                p " I'll give her some time to think it out. "
                e " No problem, Petunia. "
                scene black with dissolve
                " You spent the rest of the break talking with Engel and Petunia after their conversation. "
                " Petunia looked a little down after the whole thing, but you managed to make her laugh by making a joke. "
                " Thankfully...you didn't like her with a frown. "
                " You're glad to make her happy. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your clasroom. "
                pause 2.0
                jump musicclassthurs
            " *Stay silent* ":
                " Yeah, let's just stay silent. "
                " You don't really wanna be a part of this. "
                e " ...It's not like you can force her to just say it. "
                e " Infact, that's just gonna worsen the situation. "
                e " I know that you don't want that to happen... "
                e " ...Don't you? "
                hide petuniaangry at bottom
                show petuniasad at right
                p " ...Sigh...no I don't. "
                p " Thanks for listening and giving me advice, Engel. "
                p " I'll give her some time to think it out. "
                e " No problem, Petunia. "
                scene black with dissolve
                " You spent the rest of the break talking with Engel and Petunia after their conversation. "
                " Petunia looked a little down after the whole thing, but you managed to make her laugh by making a joke. "
                " Thankfully...you didn't like her with a frown. "
                " You're glad to make her happy. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your clasroom. "
                pause 2.0
                jump musicclassthurs
    else:
        x " ...Petunia, you've got to calm down. "
        $ popularknow = True
        p " CALM DOWN?! "
        p " Why should I calm down, Engel. "
        $ engelknow = True
        " Well damn, looks like someone's mad. "
        " You're curious on what she's mad about though... "
        e " Uh...um... "
        e " Because...???? "
        p " BECAUSE WHAT, ENGEL!! " with vpunch
        p " How can I be calm when I know I'm in a school with a BITCH. "
        e " Petunia, I really think you should stop talking about Lizzy like that... "
        e " I know that you two can be friends again... "
        e " You two have gotten in misunderstandings before, but you both managed to come back together just fine! "
        e " I don't think I've talked to you about this before, but... "
        e " What's your problem with Lizzy? Just a few days ago, you two were fine... "
        p " ...What's my problem with her? "
        p " WHAT'S MY PROBLEM WITH HER?! " with vpunch
        e " uh yeah that's what I said{nw} "
        p " My problem with her is that she's horrible at communication! "
        p " I ask her why she's being mad - she ignores me! "
        p " Like, hello? I ask you what's going on with you, and you respond with nothing but silence! "
        p " How am I supposed to fix things if you don't tell me what's going wrong with you?! "
        p " God, it just pisses me off really bad! "
        hide engelneutral at bottom
        show engelsad at left
        e " Hmm...you're right - she kind of needs to communicate with you, "
        e " But that doesn't mean that she should just immediately spit out the reason why she isn't talking. "
        p " ...What do you mean by that. "
        hide engelsad at bottom
        show engelneutral at left
        e " What if she isn't comfortable with sharing yet? "
        e " Maybe you just need to give her some time alone so that she could get herself some confidence to tell you. "
        e " The thing she might be going through - it's probably embarrassing to her... "
        e " ...And you just need a little patience to wait for her to say what she needs to say. "
        p " Well what if I want her to say it now???? "
        menu:
            " Maybe you should listen to what Engel says ":
                $ engellv += 10
                $ popularlv += 10
                hide engelneutral at bottom
                show engelhappy at left
                e " ([name]? I didn't know that you were here...) "
                e " (Thanks for agreeing with me though.) "
                e " (Petunia needs to hear this, even though she's being a little stubborn right now.) "
                hide engelhappy at bottom
                show engelneutral at left
                e " Ahem...it's not like you can force her to just say it. "
                e " Infact, that's just gonna worsen the situation. "
                e " I know that you don't want that to happen... "
                e " ...Don't you? "
                hide petuniaangry at bottom
                show petuniasad at right
                p " ...Sigh...no I don't. "
                p " Thanks for listening and giving me advice, Engel. "
                p " I'll give her some time to think it out. "
                e " No problem, Petunia. "
                scene black with dissolve
                " You spent the rest of the break talking with Engel and Petunia after their conversation. "
                " Petunia looked a little down after the whole thing, but you managed to make her laugh by making a joke. "
                " Thankfully...you didn't like her with a frown. "
                " You're glad to make her happy. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your clasroom. "
                pause 2.0
                jump musicclassthurs
            " *Stay silent* ":
                " Yeah, let's just stay silent. "
                " You don't really wanna be a part of this. "
                e " ...It's not like you can force her to just say it. "
                e " Infact, that's just gonna worsen the situation. "
                e " I know that you don't want that to happen... "
                e " ...Don't you? "
                hide petuniaangry at bottom
                show petuniasad at right
                p " ...Sigh...no I don't. "
                p " Thanks for listening and giving me advice, Engel. "
                p " I'll give her some time to think it out. "
                e " No problem, Petunia. "
                scene black with dissolve
                " You spent the rest of the break talking with Engel and Petunia after their conversation. "
                " Petunia looked a little down after the whole thing, but you managed to make her laugh by making a joke. "
                " Thankfully...you didn't like her with a frown. "
                " You're glad to make her happy. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked back into the school and went to your clasroom. "
                pause 2.0
                jump musicclassthurs
label thursgym4:
    # skell and riley
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked to the gym and spotted two of your classmates talking with eachother. "
    " Wondering what they might be talking about, you decided to walk over to them. "
    show skellneutral at right with easeinleft
    show rileyangry at left with easeinleft
    if skellknow == True and rileyknow == True:
        sk " ...So I take it that the conversation didn't go well? "
        ri " Oh boy, do I have a lot to tell you. "
        " Ohohooo, looks like we've got some drama here. "
        " Now that I think about it, a lot of drama has been happening... "
        " I mean, there's a thing going on with the popular girls, so uh...yeah. "
        " Back to the content! "
        ri " First off - I was admiring an Oliver picture, right? "
        ri " Just hanging out on the rooftop, doing my own thing... "
        ri " Don't you go and open up your phone, Skell! "
        sk " Sorry Riley, was just checking a notification from Ruby. "
        sk " Continue... "
        ri " ANYWAYS - Robby then starts walking up to me, right? "
        ri " Starts talking about 'something that he wants to talk to me about'... "
        ri " I know that you know me well - and I know that you thought that I thought he was going to talk about Olibot! "
        ri " But nooo, he starts talking about how he's tired on making Oliver stuff! "
        ri " And that if I want to make Oliver content for myself, then I should just make it myself! "
        ri " Like hellooooo? I was asking you about Olibot, not how you're doing? "
        ri " I told him that - and then he started going all angry on me! "
        ri " What did I do other than say that he should be working on Olibot? "
        ri " Nothing! I did absolutely nothing! "
        ri " Geez, sometimes I can't understand him... "
        menu:
            " Maybe you should give him time to rest ":
                $ skelllv += 10
                $ robbrileylv += 10
                sk " (Oh, [name]? you're here?) "
                sk " (Sorry that I didn't notice you a bit earlier.) "
                sk " (Thanks for stepping in though.) "
                sk " (Kind of tired of having to deal with these two's arguments...) "
                ri " Eh. What do you mean by that, [name]. "
                " You told her that sometimes, people needs breaks. "
                " Considering that Riley has a fixation on Oliver, you decided to use him as an example... "
                " You then said: 'what if Oliver just didn't feel like going to school one day?' "
                " That's because he's tired. And people need rest. "
                " Oliver needs rest, everyone needs rest. "
                " You also told her that she might be going a bit overboard with all of the Oliver stuff. "
                " From what you could tell - this Robby person has been getting real tired with all of the Oliver stuff Riley's been mentioning. "
                " You told her that maybe she could tone that down too. "
                ri " ... "
                hide rileyangry at bottom
                show rileymurder at left
                ri " ... "
                hide skellneutral at bottom
                show skellsurprised at right
                sk " Holy shit, Riley, no. "
                sk " You know I'm telling Ruby if you're actually gonna try to... "
                ri " ... "
                sk " Riley. "
                scene black with dissolve
                " You spent the rest of the break being chased down by Riley. "
                " You were just trying to get some sense into her... "
                " ...And somehow you managed to make her more insane than she already is. "
                " Skell eventually managed to hold her back after a bit. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You got out of the gym and went back to your classroom. "
                pause 2.0
                jump musicclassthurs
            " *Stay silent* ":
                $ skelllv += 10
                $ robbrileylv += 10
                " Best to stay out of this, then. "
                " Let's be silent... "
                sk " Well, uh... "
                sk " Maybe he's tired about doing stuff for you? "
                sk " You know, the whole Oliver thing... "
                sk " You should probably give him some time to rest or just leave him alone. "
                ri " What. What do you mean. "
                sk " You keep on asking him to make a lot of stuff for you. "
                sk " Whether it's Oliver stuff or not - you always go to him. "
                sk " I'm sure it's been getting tiring for him. "
                sk " Let me give you an example...after a long day, Oliver goes home. "
                sk " Oliver is very tired after everyone kept asking him to do something he doesn't want to do. "
                sk " People keep asking him to do their homework. "
                sk " People keep bothering him. "
                sk " Of course he would be tired - and when he's tired, he needs some rest. "
                sk " So, think of Oliver as Robby in that situation. "
                sk " You should also start toning down on the whole Oliver thing. "
                sk " Robby doesn't really like when you talk about him... "
                sk " ...Considering that you talk about him every single day without a single break. "
                hide rileyneutral at bottom
                show rileysad at left
                ri " ... "
                ri " Okay, finee... "
                ri " I'll talk to him in VC when we get home. "
                sk " Good. "
                scene black with dissolve
                " You spent the rest of the break talking with Skell and Riley after their conversation. "
                " Huh. To be honest, you'd get really exhausted if someone kept asking you to make stuff about Oliver. "
                " Like, imagine if someone saw you making a whole lot of things based off of Oliver... "
                " ...Then you'd have to explain if you had a crush on him or not. Euughh... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked out of the gym and then went to your classroom. "
                pause 2.0
                jump musicclassthurs
    elif skellknow == True and rileyknow == False:
        sk " ...So I take it that the conversation didn't go well? "
        x " Oh boy, do I have a lot to tell you. "
        " Ohohooo, looks like we've got some drama here. "
        " Now that I think about it, a lot of drama has been happening... "
        " I mean, there's a thing going on with the popular girls, so uh...yeah. "
        " Back to the content! "
        x " First off - I was admiring an Oliver picture, right? "
        x " Just hanging out on the rooftop, doing my own thing... "
        x " Don't you go and open up your phone, Skell! "
        $ rileyknow = True
        sk " Sorry Riley, was just checking a notification from Ruby. "
        sk " Continue... "
        ri " ANYWAYS - Robby then starts walking up to me, right? "
        ri " Starts talking about 'something that he wants to talk to me about'... "
        ri " I know that you know me well - and I know that you thought that I thought he was going to talk about Olibot! "
        ri " But nooo, he starts talking about how he's tired on making Oliver stuff! "
        ri " And that if I want to make Oliver content for myself, then I should just make it myself! "
        ri " Like hellooooo? I was asking you about Olibot, not how you're doing? "
        ri " I told him that - and then he started going all angry on me! "
        ri " What did I do other than say that he should be working on Olibot? "
        ri " Nothing! I did absolutely nothing! "
        ri " Geez, sometimes I can't understand him... "
        menu:
            " Maybe you should give him time to rest ":
                $ skelllv += 10
                $ robbrileylv += 10
                sk " (Oh, [name]? you're here?) "
                sk " (Sorry that I didn't notice you a bit earlier.) "
                sk " (Thanks for stepping in though.) "
                sk " (Kind of tired of having to deal with these two's arguments...) "
                ri " Eh. What do you mean by that, [name]. "
                " You told her that sometimes, people needs breaks. "
                " Considering that Riley has a fixation on Oliver, you decided to use him as an example... "
                " You then said: 'what if Oliver just didn't feel like going to school one day?' "
                " That's because he's tired. And people need rest. "
                " Oliver needs rest, everyone needs rest. "
                " You also told her that she might be going a bit overboard with all of the Oliver stuff. "
                " From what you could tell - this Robby person has been getting real tired with all of the Oliver stuff Riley's been mentioning. "
                " You told her that maybe she could tone that down too. "
                ri " ... "
                hide rileyangry at bottom
                show rileymurder at left
                ri " ... "
                hide skellneutral at bottom
                show skellsurprised at right
                sk " Holy shit, Riley, no. "
                sk " You know I'm telling Ruby if you're actually gonna try to... "
                ri " ... "
                sk " Riley. "
                scene black with dissolve
                " You spent the rest of the break being chased down by Riley. "
                " You were just trying to get some sense into her... "
                " ...And somehow you managed to make her more insane than she already is. "
                " Skell eventually managed to hold her back after a bit. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You got out of the gym and went back to your classroom. "
                pause 2.0
                jump musicclassthurs
            " *Stay silent* ":
                $ skelllv += 10
                $ robbrileylv += 10
                " Best to stay out of this, then. "
                " Let's be silent... "
                sk " Well, uh... "
                sk " Maybe he's tired about doing stuff for you? "
                sk " You know, the whole Oliver thing... "
                sk " You should probably give him some time to rest or just leave him alone. "
                ri " What. What do you mean. "
                sk " You keep on asking him to make a lot of stuff for you. "
                sk " Whether it's Oliver stuff or not - you always go to him. "
                sk " I'm sure it's been getting tiring for him. "
                sk " Let me give you an example...after a long day, Oliver goes home. "
                sk " Oliver is very tired after everyone kept asking him to do something he doesn't want to do. "
                sk " People keep asking him to do their homework. "
                sk " People keep bothering him. "
                sk " Of course he would be tired - and when he's tired, he needs some rest. "
                sk " So, think of Oliver as Robby in that situation. "
                sk " You should also start toning down on the whole Oliver thing. "
                sk " Robby doesn't really like when you talk about him... "
                sk " ...Considering that you talk about him every single day without a single break. "
                hide rileyneutral at bottom
                show rileysad at left
                ri " ... "
                ri " Okay, finee... "
                ri " I'll talk to him in VC when we get home. "
                sk " Good. "
                scene black with dissolve
                " You spent the rest of the break talking with Skell and Riley after their conversation. "
                " Huh. To be honest, you'd get really exhausted if someone kept asking you to make stuff about Oliver. "
                " Like, imagine if someone saw you making a whole lot of things based off of Oliver... "
                " ...Then you'd have to explain if you had a crush on him or not. Euughh... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked out of the gym and then went to your classroom. "
                pause 2.0
                jump musicclassthurs
    elif skellknow == False and rileyknow == True:
        x " ...So I take it that the conversation didn't go well? "
        ri " Oh boy, do I have a lot to tell you. "
        " Ohohooo, looks like we've got some drama here. "
        " Now that I think about it, a lot of drama has been happening... "
        " I mean, there's a thing going on with the popular girls, so uh...yeah. "
        " Back to the content! "
        ri " First off - I was admiring an Oliver picture, right? "
        ri " Just hanging out on the rooftop, doing my own thing... "
        ri " Don't you go and open up your phone, Skell! "
        $ skellknow = True
        sk " Sorry Riley, was just checking a notification from Ruby. "
        sk " Continue... "
        ri " ANYWAYS - Robby then starts walking up to me, right? "
        ri " Starts talking about 'something that he wants to talk to me about'... "
        ri " I know that you know me well - and I know that you thought that I thought he was going to talk about Olibot! "
        ri " But nooo, he starts talking about how he's tired on making Oliver stuff! "
        ri " And that if I want to make Oliver content for myself, then I should just make it myself! "
        ri " Like hellooooo? I was asking you about Olibot, not how you're doing? "
        ri " I told him that - and then he started going all angry on me! "
        ri " What did I do other than say that he should be working on Olibot? "
        ri " Nothing! I did absolutely nothing! "
        ri " Geez, sometimes I can't understand him... "
        menu:
            " Maybe you should give him time to rest ":
                $ skelllv += 10
                $ robbrileylv += 10
                sk " (Oh, [name]? you're here?) "
                sk " (Sorry that I didn't notice you a bit earlier.) "
                sk " (Thanks for stepping in though.) "
                sk " (Kind of tired of having to deal with these two's arguments...) "
                ri " Eh. What do you mean by that, [name]. "
                " You told her that sometimes, people needs breaks. "
                " Considering that Riley has a fixation on Oliver, you decided to use him as an example... "
                " You then said: 'what if Oliver just didn't feel like going to school one day?' "
                " That's because he's tired. And people need rest. "
                " Oliver needs rest, everyone needs rest. "
                " You also told her that she might be going a bit overboard with all of the Oliver stuff. "
                " From what you could tell - this Robby person has been getting real tired with all of the Oliver stuff Riley's been mentioning. "
                " You told her that maybe she could tone that down too. "
                ri " ... "
                hide rileyangry at bottom
                show rileymurder at left
                ri " ... "
                hide skellneutral at bottom
                show skellsurprised at right
                sk " Holy shit, Riley, no. "
                sk " You know I'm telling Ruby if you're actually gonna try to... "
                ri " ... "
                sk " Riley. "
                scene black with dissolve
                " You spent the rest of the break being chased down by Riley. "
                " You were just trying to get some sense into her... "
                " ...And somehow you managed to make her more insane than she already is. "
                " Skell eventually managed to hold her back after a bit. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You got out of the gym and went back to your classroom. "
                pause 2.0
                jump musicclassthurs
            " *Stay silent* ":
                $ skelllv += 10
                $ robbrileylv += 10
                " Best to stay out of this, then. "
                " Let's be silent... "
                sk " Well, uh... "
                sk " Maybe he's tired about doing stuff for you? "
                sk " You know, the whole Oliver thing... "
                sk " You should probably give him some time to rest or just leave him alone. "
                ri " What. What do you mean. "
                sk " You keep on asking him to make a lot of stuff for you. "
                sk " Whether it's Oliver stuff or not - you always go to him. "
                sk " I'm sure it's been getting tiring for him. "
                sk " Let me give you an example...after a long day, Oliver goes home. "
                sk " Oliver is very tired after everyone kept asking him to do something he doesn't want to do. "
                sk " People keep asking him to do their homework. "
                sk " People keep bothering him. "
                sk " Of course he would be tired - and when he's tired, he needs some rest. "
                sk " So, think of Oliver as Robby in that situation. "
                sk " You should also start toning down on the whole Oliver thing. "
                sk " Robby doesn't really like when you talk about him... "
                sk " ...Considering that you talk about him every single day without a single break. "
                hide rileyneutral at bottom
                show rileysad at left
                ri " ... "
                ri " Okay, finee... "
                ri " I'll talk to him in VC when we get home. "
                sk " Good. "
                scene black with dissolve
                " You spent the rest of the break talking with Skell and Riley after their conversation. "
                " Huh. To be honest, you'd get really exhausted if someone kept asking you to make stuff about Oliver. "
                " Like, imagine if someone saw you making a whole lot of things based off of Oliver... "
                " ...Then you'd have to explain if you had a crush on him or not. Euughh... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked out of the gym and then went to your classroom. "
                pause 2.0
                jump musicclassthurs
    else:
        x " ...So I take it that the conversation didn't go well? "
        x " Oh boy, do I have a lot to tell you. "
        " Ohohooo, looks like we've got some drama here. "
        " Now that I think about it, a lot of drama has been happening... "
        " I mean, there's a thing going on with the popular girls, so uh...yeah. "
        " Back to the content! "
        x " First off - I was admiring an Oliver picture, right? "
        x " Just hanging out on the rooftop, doing my own thing... "
        x " Don't you go and open up your phone, Skell! "
        $ skellknow = True
        $ rubyknow = True
        sk " Sorry Riley, was just checking a notification from Ruby. "
        sk " Continue... "
        ri " ANYWAYS - Robby then starts walking up to me, right? "
        ri " Starts talking about 'something that he wants to talk to me about'... "
        ri " I know that you know me well - and I know that you thought that I thought he was going to talk about Olibot! "
        ri " But nooo, he starts talking about how he's tired on making Oliver stuff! "
        ri " And that if I want to make Oliver content for myself, then I should just make it myself! "
        ri " Like hellooooo? I was asking you about Olibot, not how you're doing? "
        ri " I told him that - and then he started going all angry on me! "
        ri " What did I do other than say that he should be working on Olibot? "
        ri " Nothing! I did absolutely nothing! "
        ri " Geez, sometimes I can't understand him... "
        menu:
            " Maybe you should give him time to rest ":
                $ skelllv += 10
                $ robbrileylv += 10
                sk " (Oh, [name]? you're here?) "
                sk " (Sorry that I didn't notice you a bit earlier.) "
                sk " (Thanks for stepping in though.) "
                sk " (Kind of tired of having to deal with these two's arguments...) "
                ri " Eh. What do you mean by that, [name]. "
                " You told her that sometimes, people needs breaks. "
                " Considering that Riley has a fixation on Oliver, you decided to use him as an example... "
                " You then said: 'what if Oliver just didn't feel like going to school one day?' "
                " That's because he's tired. And people need rest. "
                " Oliver needs rest, everyone needs rest. "
                " You also told her that she might be going a bit overboard with all of the Oliver stuff. "
                " From what you could tell - this Robby person has been getting real tired with all of the Oliver stuff Riley's been mentioning. "
                " You told her that maybe she could tone that down too. "
                ri " ... "
                hide rileyangry at bottom
                show rileymurder at left
                ri " ... "
                hide skellneutral at bottom
                show skellsurprised at right
                sk " Holy shit, Riley, no. "
                sk " You know I'm telling Ruby if you're actually gonna try to... "
                ri " ... "
                sk " Riley. "
                scene black with dissolve
                " You spent the rest of the break being chased down by Riley. "
                " You were just trying to get some sense into her... "
                " ...And somehow you managed to make her more insane than she already is. "
                " Skell eventually managed to hold her back after a bit. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You got out of the gym and went back to your classroom. "
                pause 2.0
                jump musicclassthurs
            " *Stay silent* ":
                $ skelllv += 10
                $ robbrileylv += 10
                " Best to stay out of this, then. "
                " Let's be silent... "
                sk " Well, uh... "
                sk " Maybe he's tired about doing stuff for you? "
                sk " You know, the whole Oliver thing... "
                sk " You should probably give him some time to rest or just leave him alone. "
                ri " What. What do you mean. "
                sk " You keep on asking him to make a lot of stuff for you. "
                sk " Whether it's Oliver stuff or not - you always go to him. "
                sk " I'm sure it's been getting tiring for him. "
                sk " Let me give you an example...after a long day, Oliver goes home. "
                sk " Oliver is very tired after everyone kept asking him to do something he doesn't want to do. "
                sk " People keep asking him to do their homework. "
                sk " People keep bothering him. "
                sk " Of course he would be tired - and when he's tired, he needs some rest. "
                sk " So, think of Oliver as Robby in that situation. "
                sk " You should also start toning down on the whole Oliver thing. "
                sk " Robby doesn't really like when you talk about him... "
                sk " ...Considering that you talk about him every single day without a single break. "
                hide rileyneutral at bottom
                show rileysad at left
                ri " ... "
                ri " Okay, finee... "
                ri " I'll talk to him in VC when we get home. "
                sk " Good. "
                scene black with dissolve
                " You spent the rest of the break talking with Skell and Riley after their conversation. "
                " Huh. To be honest, you'd get really exhausted if someone kept asking you to make stuff about Oliver. "
                " Like, imagine if someone saw you making a whole lot of things based off of Oliver... "
                " ...Then you'd have to explain if you had a crush on him or not. Euughh... "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for your next class. "
                " You walked out of the gym and then went to your classroom. "
                pause 2.0
                jump musicclassthurs
label thurscafeteria4:
    # claire and ruby
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    if clairebeatup == True and clairesorry == False:
        " You can't interact with someone here because you didn't apologize. "
        " Sorry not sorry. "
        scene black
        pause 2.0
        jump musicclassthurs
    else:
        pass
    " You walked to the cafeteria and spotted your two classmates talking about something. "
    " Wondering what they're doing, you decided to talk up to them. "
    show claireneutral at left with easeinright
    show rubyneutral at right with easeinright
    if claireknow == True and rubyknow == True:
        ru " Hi [name]! Hi Claire! "
        c " Hey there, Ruby! "
        " You greeted the both of them. "
        ru " You know... "
        hide rubyneutral at bottom
        show rubysad at right
        ru " Riley and Robby have been fighting lately. "
        hide claireneutral at bottom
        show claireconfused at left
        c " What? Why? "
        c " It's not really like them to fight... "
        c " Well, as far as I know. "
        ru " Apparently, Riley wanted to make something Oliver related... "
        c " Oliver related? I think I see where this is going... "
        c " Of course she would want to make something Oliver related. "
        c " It's common knowledge that she's obsessed with him. "
        ru " Well - this time it's not really something as simple as a love letter or anything like that... "
        ru " She decided that she wanted to make an Oliver bot that would help him in bullying. "
        c " Jesus christ, really? "
        c " Never knew she was THAT down bad to the point she would want to make something like that... "
        c " The things I learn from my classmates... huh. "
        ru " She didn't know anything about robotics - so she asked Robby for help. "
        ru " And you know that Robby's been getting real tired recently over making things! "
        ru " Riley asking him to make something Oliver related just made his mood worse... "
        ru " Skell talked with Robby about it a few breaks earlier and said that he would talk to her about it on the third break of the day... "
        ru " Aaaaand thats when the argument started. "
        c " Mmm...honestly, if Riley wanted to make something Oliver related, she should do it herself. "
        c " Constantly asking Robby for that kind of help is gonna get annoying at some point. "
        c " I can see why Robby's mad at her... "
        c " She should've given Robby atleast a bit of rest. "
        ru " Yeah, I agree with that. "
        ru " It still hurts me that they're arguing like this though... "
        menu:
            " They're gonna be alright ":
                $ rubylv += 10
                $ clairelv += 5
                hide rubysad at bottom
                show rubyneutral at right
                hide claireconfused at bottom
                show claireneutral at left
                c " Yup, [name]'s right. "
                c " Even if they're not fine right now, they'll be fine later. "
                c " Trust us on this one, Ruby. "
                ru " ...Yeah, thanks guys. "
                ru " They'll be fine in the end and they'll be all sunshine and rainbows again! "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Claire. "
                " That whole Riley and Robby thing is getting you curious now... "
                " Maybe you should've watched the whole argument go down. "
                " Nah, wait, no. You don't got that magical popcorn, unfortunately. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and went to your classroom. "
                pause 2.0
                jump musicclassthurs
            " *Say nothing* ":
                hide rubysad at bottom
                show rubyneutral at right
                hide claireconfused at bottom
                show claireneutral at left
                c " Even if they're not fine right now, they'll be fine later. "
                c " Trust us on this one, Ruby. "
                ru " ...Yeah, thanks guys. "
                ru " They'll be fine in the end and they'll be all sunshine and rainbows again! "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Claire. "
                " That whole Riley and Robby thing is getting you curious now... "
                " Maybe you should've watched the whole argument go down. "
                " Nah, wait, no. You don't got that magical popcorn, unfortunately. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and went to your classroom. "
                pause 2.0
                jump musicclassthurs
    elif claireknow == True and rubyknow == False:
        x " Hi [name]! Hi Claire! "
        c " Hey there, Ruby! "
        x " Ooo, wait! I don't think I've introduced myself to [name] yet.. "
        c " Oh shoot - better introduce yourself to [them] now! "
        x " I AM!! Just give me a sec, geez... "
        $ rubyknow = True
        ru " Hello!! I'm Ruby, it's nice to meet you! "
        " You greeted the both of them. "
        ru " You know... "
        hide rubyneutral at bottom
        show rubysad at right
        ru " Riley and Robby have been fighting lately. "
        hide claireneutral at bottom
        show claireconfused at left
        c " What? Why? "
        c " It's not really like them to fight... "
        c " Well, as far as I know. "
        ru " Apparently, Riley wanted to make something Oliver related... "
        c " Oliver related? I think I see where this is going... "
        c " Of course she would want to make something Oliver related. "
        c " It's common knowledge that she's obsessed with him. "
        ru " Well - this time it's not really something as simple as a love letter or anything like that... "
        ru " She decided that she wanted to make an Oliver bot that would help him in bullying. "
        c " Jesus christ, really? "
        c " Never knew she was THAT down bad to the point she would want to make something like that... "
        c " The things I learn from my classmates... huh. "
        ru " She didn't know anything about robotics - so she asked Robby for help. "
        ru " And you know that Robby's been getting real tired recently over making things! "
        ru " Riley asking him to make something Oliver related just made his mood worse... "
        ru " Skell talked with Robby about it a few breaks earlier and said that he would talk to her about it on the third break of the day... "
        ru " Aaaaand thats when the argument started. "
        c " Mmm...honestly, if Riley wanted to make something Oliver related, she should do it herself. "
        c " Constantly asking Robby for that kind of help is gonna get annoying at some point. "
        c " I can see why Robby's mad at her... "
        c " She should've given Robby atleast a bit of rest. "
        ru " Yeah, I agree with that. "
        ru " It still hurts me that they're arguing like this though... "
        menu:
            " They're gonna be alright ":
                $ rubylv += 10
                $ clairelv += 5
                hide rubysad at bottom
                show rubyneutral at right
                hide claireconfused at bottom
                show claireneutral at left
                c " Yup, [name]'s right. "
                c " Even if they're not fine right now, they'll be fine later. "
                c " Trust us on this one, Ruby. "
                ru " ...Yeah, thanks guys. "
                ru " They'll be fine in the end and they'll be all sunshine and rainbows again! "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Claire. "
                " That whole Riley and Robby thing is getting you curious now... "
                " Maybe you should've watched the whole argument go down. "
                " Nah, wait, no. You don't got that magical popcorn, unfortunately. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and went to your classroom. "
                pause 2.0
                jump musicclassthurs
            " *Say nothing* ":
                hide rubysad at bottom
                show rubyneutral at right
                hide claireconfused at bottom
                show claireneutral at left
                c " Even if they're not fine right now, they'll be fine later. "
                c " Trust us on this one, Ruby. "
                ru " ...Yeah, thanks guys. "
                ru " They'll be fine in the end and they'll be all sunshine and rainbows again! "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Claire. "
                " That whole Riley and Robby thing is getting you curious now... "
                " Maybe you should've watched the whole argument go down. "
                " Nah, wait, no. You don't got that magical popcorn, unfortunately. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and went to your classroom. "
                pause 2.0
                jump musicclassthurs
    elif claireknow == False and rubyknow == True:
        ru " Hi [name]! Hi Claire! "
        x " Hey there, Ruby! "
        x " Wait, hey... I don't think I got to introduce myself to [name]. "
        x " Better do that now then! "
        $ claireknow = True
        c " Hi there! I'm Claire, your classmate. "
        c " Real nice to meet you! "
        " You greeted the both of them. "
        ru " You know... "
        hide rubyneutral at bottom
        show rubysad at right
        ru " Riley and Robby have been fighting lately. "
        hide claireneutral at bottom
        show claireconfused at left
        c " What? Why? "
        c " It's not really like them to fight... "
        c " Well, as far as I know. "
        ru " Apparently, Riley wanted to make something Oliver related... "
        c " Oliver related? I think I see where this is going... "
        c " Of course she would want to make something Oliver related. "
        c " It's common knowledge that she's obsessed with him. "
        ru " Well - this time it's not really something as simple as a love letter or anything like that... "
        ru " She decided that she wanted to make an Oliver bot that would help him in bullying. "
        c " Jesus christ, really? "
        c " Never knew she was THAT down bad to the point she would want to make something like that... "
        c " The things I learn from my classmates... huh. "
        ru " She didn't know anything about robotics - so she asked Robby for help. "
        ru " And you know that Robby's been getting real tired recently over making things! "
        ru " Riley asking him to make something Oliver related just made his mood worse... "
        ru " Skell talked with Robby about it a few breaks earlier and said that he would talk to her about it on the third break of the day... "
        ru " Aaaaand thats when the argument started. "
        c " Mmm...honestly, if Riley wanted to make something Oliver related, she should do it herself. "
        c " Constantly asking Robby for that kind of help is gonna get annoying at some point. "
        c " I can see why Robby's mad at her... "
        c " She should've given Robby atleast a bit of rest. "
        ru " Yeah, I agree with that. "
        ru " It still hurts me that they're arguing like this though... "
        menu:
            " They're gonna be alright ":
                $ rubylv += 10
                $ clairelv += 5
                hide rubysad at bottom
                show rubyneutral at right
                hide claireconfused at bottom
                show claireneutral at left
                c " Yup, [name]'s right. "
                c " Even if they're not fine right now, they'll be fine later. "
                c " Trust us on this one, Ruby. "
                ru " ...Yeah, thanks guys. "
                ru " They'll be fine in the end and they'll be all sunshine and rainbows again! "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Claire. "
                " That whole Riley and Robby thing is getting you curious now... "
                " Maybe you should've watched the whole argument go down. "
                " Nah, wait, no. You don't got that magical popcorn, unfortunately. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and went to your classroom. "
                pause 2.0
                jump musicclassthurs
            " *Say nothing* ":
                hide rubysad at bottom
                show rubyneutral at right
                hide claireconfused at bottom
                show claireneutral at left
                c " Even if they're not fine right now, they'll be fine later. "
                c " Trust us on this one, Ruby. "
                ru " ...Yeah, thanks guys. "
                ru " They'll be fine in the end and they'll be all sunshine and rainbows again! "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Claire. "
                " That whole Riley and Robby thing is getting you curious now... "
                " Maybe you should've watched the whole argument go down. "
                " Nah, wait, no. You don't got that magical popcorn, unfortunately. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and went to your classroom. "
                pause 2.0
                jump musicclassthurs
    else:
        x " Hi [name]! Hi Claire! "
        x " Hey there, Ruby! "
        x " Wait, Ruby...have we introduced oursevles to [name] yet? "
        x " No, I don't think so... "
        x " Better to do that now, then! "
        $ claireknow = True
        c " Hi there, I'm Claire! It's nice to meet you! "
        ru " Hellooo, I'm Ruby! Me and Claire are your classmates! "
        " You greeted the both of them. "
        ru " You know... "
        hide rubyneutral at bottom
        show rubysad at right
        ru " Riley and Robby have been fighting lately. "
        hide claireneutral at bottom
        show claireconfused at left
        c " What? Why? "
        c " It's not really like them to fight... "
        c " Well, as far as I know. "
        ru " Apparently, Riley wanted to make something Oliver related... "
        c " Oliver related? I think I see where this is going... "
        c " Of course she would want to make something Oliver related. "
        c " It's common knowledge that she's obsessed with him. "
        ru " Well - this time it's not really something as simple as a love letter or anything like that... "
        ru " She decided that she wanted to make an Oliver bot that would help him in bullying. "
        c " Jesus christ, really? "
        c " Never knew she was THAT down bad to the point she would want to make something like that... "
        c " The things I learn from my classmates... huh. "
        ru " She didn't know anything about robotics - so she asked Robby for help. "
        ru " And you know that Robby's been getting real tired recently over making things! "
        ru " Riley asking him to make something Oliver related just made his mood worse... "
        ru " Skell talked with Robby about it a few breaks earlier and said that he would talk to her about it on the third break of the day... "
        ru " Aaaaand thats when the argument started. "
        c " Mmm...honestly, if Riley wanted to make something Oliver related, she should do it herself. "
        c " Constantly asking Robby for that kind of help is gonna get annoying at some point. "
        c " I can see why Robby's mad at her... "
        c " She should've given Robby atleast a bit of rest. "
        ru " Yeah, I agree with that. "
        ru " It still hurts me that they're arguing like this though... "
        menu:
            " They're gonna be alright ":
                $ rubylv += 10
                $ clairelv += 5
                hide rubysad at bottom
                show rubyneutral at right
                hide claireconfused at bottom
                show claireneutral at left
                c " Yup, [name]'s right. "
                c " Even if they're not fine right now, they'll be fine later. "
                c " Trust us on this one, Ruby. "
                ru " ...Yeah, thanks guys. "
                ru " They'll be fine in the end and they'll be all sunshine and rainbows again! "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Claire. "
                " That whole Riley and Robby thing is getting you curious now... "
                " Maybe you should've watched the whole argument go down. "
                " Nah, wait, no. You don't got that magical popcorn, unfortunately. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and went to your classroom. "
                pause 2.0
                jump musicclassthurs
            " *Say nothing* ":
                hide rubysad at bottom
                show rubyneutral at right
                hide claireconfused at bottom
                show claireneutral at left
                c " Even if they're not fine right now, they'll be fine later. "
                c " Trust us on this one, Ruby. "
                ru " ...Yeah, thanks guys. "
                ru " They'll be fine in the end and they'll be all sunshine and rainbows again! "
                scene black with dissolve
                " You spent the rest of the break talking with Ruby and Claire. "
                " That whole Riley and Robby thing is getting you curious now... "
                " Maybe you should've watched the whole argument go down. "
                " Nah, wait, no. You don't got that magical popcorn, unfortunately. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the cafeteria and went to your classroom. "
                pause 2.0
                jump musicclassthurs
label thursrooftop4:
    # abbie and cubbie
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked to the rooftop and spotted your two classmates talking with eachother. "
    " Wondering what they're talking about, you decided to join their conversation. "
    show abbieneutral at right with easeinleft
    show cubbieneutral at left with easeinleft
    if abbieknow == True and cubbieknow == True:
        a " Hmm, no, that doesn't look very right... "
        a " Maybe you could try putting it in that spot...? "
        a " Like, over here...in the corner... "
        cb " ...? "
        a " Yeah, right there... "
        a " Wait, no...it still doesn't look right... "
        a " ...G..geez, who knew sticker placement could be so difficult..? "
        " You greeted them before asking what they were doing. "
        a " Oh, hey [name]... "
        a " I was actually just relaxing here until Cubbie asked me for help... "
        a " Um...he was asking where he would put this sticker on his ID... "
        a " We don't really use ID's, but the teachers kinda still need them for us... "
        a " Most of the students here just take off their ID's the moment they get inside the school... "
        a " Including me and, um...basically everyone in class. "
        cb " ... "
        a " Erh - Cubbie's trying to say that he just wanted to decorate it for fun... "
        a " ...Even though he isn't going to use it that much... "
        a " Um... [name], do you have an idea on where he could place it...? "
        menu:
            " In the bottom left corner ":
                $ cubbielv += 5
                $ abbielv += 5
                a " Over here...? "
                " Cubbie hovers the sticker over the place you said. "
                " The bottom left corner trick can never go wrong. "
                " It looks just fine. "
                a " Mmm, yeah, it really does look great there... "
                a " Uh...thank you for the help, [name]. "
                cb " !! "
                " Cubbie seems happy for your help. "
                scene black with dissolve
                " You spent the rest of the break talking with Abbie and Cubbie. "
                " Talking about some cool stickers you found in your childhood... "
                " You found a lot of shiny stickers in your childhood. "
                " Why? because you like the shinyness of them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump musicclassthurs
            " In the bottom right corner ":
                $ cubbielv += 5
                $ abbielv += 5
                a " Over here...? "
                " Cubbie hovers the sticker over the place you said. "
                " The bottom right corner trick can never go wrong. "
                " It looks just fine. "
                a " Mmm, yeah, it really does look great there... "
                a " Uh...thank you for the help, [name]. "
                cb " !! "
                " Cubbie seems happy for your help. "
                scene black with dissolve
                " You spent the rest of the break talking with Abbie and Cubbie. "
                " Talking about some cool stickers you found in your childhood... "
                " You found a lot of shiny stickers in your childhood. "
                " Why? because you like the shinyness of them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump musicclassthurs
    elif abbieknow == True and cubbieknow == False:
        a " Hmm, no, that doesn't look very right... "
        a " Maybe you could try putting it in that spot...? "
        a " Like, over here...in the corner... "
        x " ...? "
        a " Yeah, right there... "
        a " Wait, no...it still doesn't look right... "
        a " ...G..geez, who knew sticker placement could be so difficult..? "
        " You greeted them before asking what they were doing. "
        a " Oh, hey [name]... "
        $ cubbieknow = True
        a " I was actually just relaxing here until Cubbie asked me for help... "
        a " Um...he was asking where he would put this sticker on his ID... "
        a " We don't really use ID's, but the teachers kinda still need them for us... "
        a " Most of the students here just take off their ID's the moment they get inside the school... "
        a " Including me and, um...basically everyone in class. "
        cb " ... "
        a " Erh - Cubbie's trying to say that he just wanted to decorate it for fun... "
        a " ...Even though he isn't going to use it that much... "
        a " Um... [name], do you have an idea on where he could place it...? "
        menu:
            " In the bottom left corner ":
                $ cubbielv += 5
                $ abbielv += 5
                a " Over here...? "
                " Cubbie hovers the sticker over the place you said. "
                " The bottom left corner trick can never go wrong. "
                " It looks just fine. "
                a " Mmm, yeah, it really does look great there... "
                a " Uh...thank you for the help, [name]. "
                cb " !! "
                " Cubbie seems happy for your help. "
                scene black with dissolve
                " You spent the rest of the break talking with Abbie and Cubbie. "
                " Talking about some cool stickers you found in your childhood... "
                " You found a lot of shiny stickers in your childhood. "
                " Why? because you like the shinyness of them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump musicclassthurs
            " In the bottom right corner ":
                $ cubbielv += 5
                $ abbielv += 5
                a " Over here...? "
                " Cubbie hovers the sticker over the place you said. "
                " The bottom right corner trick can never go wrong. "
                " It looks just fine. "
                a " Mmm, yeah, it really does look great there... "
                a " Uh...thank you for the help, [name]. "
                cb " !! "
                " Cubbie seems happy for your help. "
                scene black with dissolve
                " You spent the rest of the break talking with Abbie and Cubbie. "
                " Talking about some cool stickers you found in your childhood... "
                " You found a lot of shiny stickers in your childhood. "
                " Why? because you like the shinyness of them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump musicclassthurs
    elif abbieknow == False and cubbieknow == True:
        x " Hmm, no, that doesn't look very right... "
        x " Maybe you could try putting it in that spot...? "
        x " Like, over here...in the corner... "
        cb " ...? "
        x " Yeah, right there... "
        x " Wait, no...it still doesn't look right... "
        x " ...G..geez, who knew sticker placement could be so difficult..? "
        " You greeted them before asking what they were doing. "
        x " Oh, hey [name]... "
        $ abbieknow = True
        x " I don't think we've met before, actually... "
        x " Uh...might as well introduce myself then... "
        a " I'm Abbie...It's nice to meet you...uh... "
        a " I was actually just relaxing here until Cubbie asked me for help... "
        a " Um...he was asking where he would put this sticker on his ID... "
        a " We don't really use ID's, but the teachers kinda still need them for us... "
        a " Most of the students here just take off their ID's the moment they get inside the school... "
        a " Including me and, um...basically everyone in class. "
        cb " ... "
        a " Erh - Cubbie's trying to say that he just wanted to decorate it for fun... "
        a " ...Even though he isn't going to use it that much... "
        a " Um... [name], do you have an idea on where he could place it...? "
        menu:
            " In the bottom left corner ":
                $ cubbielv += 5
                $ abbielv += 5
                a " Over here...? "
                " Cubbie hovers the sticker over the place you said. "
                " The bottom left corner trick can never go wrong. "
                " It looks just fine. "
                a " Mmm, yeah, it really does look great there... "
                a " Uh...thank you for the help, [name]. "
                cb " !! "
                " Cubbie seems happy for your help. "
                scene black with dissolve
                " You spent the rest of the break talking with Abbie and Cubbie. "
                " Talking about some cool stickers you found in your childhood... "
                " You found a lot of shiny stickers in your childhood. "
                " Why? because you like the shinyness of them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump musicclassthurs
            " In the bottom right corner ":
                $ cubbielv += 5
                $ abbielv += 5
                a " Over here...? "
                " Cubbie hovers the sticker over the place you said. "
                " The bottom right corner trick can never go wrong. "
                " It looks just fine. "
                a " Mmm, yeah, it really does look great there... "
                a " Uh...thank you for the help, [name]. "
                cb " !! "
                " Cubbie seems happy for your help. "
                scene black with dissolve
                " You spent the rest of the break talking with Abbie and Cubbie. "
                " Talking about some cool stickers you found in your childhood... "
                " You found a lot of shiny stickers in your childhood. "
                " Why? because you like the shinyness of them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump musicclassthurs
    else:
        x " Hmm, no, that doesn't look very right... "
        x " Maybe you could try putting it in that spot...? "
        x " Like, over here...in the corner... "
        x " ...? "
        x " Yeah, right there... "
        x " Wait, no...it still doesn't look right... "
        x " ...G..geez, who knew sticker placement could be so difficult..? "
        " You greeted them before asking what they were doing. "
        x " Oh, hey [name]... "
        $ abbieknow = True
        x " I don't think we've met before, actually... "
        x " Uh...might as well introduce myself then... "
        a " I'm Abbie...It's nice to meet you...uh... "
        $ cubbieknow = True
        a " I was actually just relaxing here until Cubbie asked me for help... "
        a " Um...he was asking where he would put this sticker on his ID... "
        a " We don't really use ID's, but the teachers kinda still need them for us... "
        a " Most of the students here just take off their ID's the moment they get inside the school... "
        a " Including me and, um...basically everyone in class. "
        cb " ... "
        a " Erh - Cubbie's trying to say that he just wanted to decorate it for fun... "
        a " ...Even though he isn't going to use it that much... "
        a " Um... [name], do you have an idea on where he could place it...? "
        menu:
            " In the bottom left corner ":
                $ cubbielv += 5
                $ abbielv += 5
                a " Over here...? "
                " Cubbie hovers the sticker over the place you said. "
                " The bottom left corner trick can never go wrong. "
                " It looks just fine. "
                a " Mmm, yeah, it really does look great there... "
                a " Uh...thank you for the help, [name]. "
                cb " !! "
                " Cubbie seems happy for your help. "
                scene black with dissolve
                " You spent the rest of the break talking with Abbie and Cubbie. "
                " Talking about some cool stickers you found in your childhood... "
                " You found a lot of shiny stickers in your childhood. "
                " Why? because you like the shinyness of them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump musicclassthurs
            " In the bottom right corner ":
                $ cubbielv += 5
                $ abbielv += 5
                a " Over here...? "
                " Cubbie hovers the sticker over the place you said. "
                " The bottom right corner trick can never go wrong. "
                " It looks just fine. "
                a " Mmm, yeah, it really does look great there... "
                a " Uh...thank you for the help, [name]. "
                cb " !! "
                " Cubbie seems happy for your help. "
                scene black with dissolve
                " You spent the rest of the break talking with Abbie and Cubbie. "
                " Talking about some cool stickers you found in your childhood... "
                " You found a lot of shiny stickers in your childhood. "
                " Why? because you like the shinyness of them. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked down from the rooftop and went to your classroom. "
                pause 2.0
                jump musicclassthurs
label thurslibrary4:
    # robby and kevin
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked into the library and saw two of your classmates talking with eachother. "
    " Wondering what they're talking about, you decided to join their conversation. "
    show robbyangry at left with easeinright
    show kevinneutral at right with easeinright
    if robbyknow == True and kevinknow == True:
        rb " Guess how the conversation went. "
        kv " Horrible?? "
        rb " No, Kevin... even worse than that, somehow. "
        kv " Geez, Robby...tell me how it went. "
        rb " She kept on telling me to work on the Olibot thing - "
        rb " Even though I kept saying that I'm tired! "
        rb " Can this girl let me rest for once??? "
        rb " I'm probably not even going to get a wink of sleep because of her... "
        rb " I swear, the only thing she ever comes up to me for is to talk about Oliver! "
        rb " I'm out there on the rooftop, trying to work... "
        rb " And then suddenly she teleports to my side saying a lot of shit about Oliver! "
        rb " Does it look like I care, Riley? "
        rb " HUH? DOES IT??????? "
        rb " Besides, I'm trying to concentrate here! "
        rb " You and your annoying ass is just getting me distracted and I{nw} "
        hide robbyangry at bottom
        show robbyneutral at left
        kv " Okay, I'm going to have to stop you before you go on and on about this for the entire break. "
        kv " I do agree with you, she should understand that you can't work 24/7. "
        kv " She should understand that you're not a robot, you're a human being... "
        kv " ...But I don't think I can get that into her thick skull. "
        kv " That skull of hers is only filled with Oliver and Oliver only. "
        rb " Yeah, it is. "
        rb " And I'm getting really sick and tired of her mentioning him a lot. "
        rb " Like, is he actually the only thing you talk about? "
        rb " How about you actually find something interesting to talk about? "
        rb " Seriously, how does she manage to talk about the same thing every single day? "
        rb " God, it's insane... "
        kv " Well, we can't really do anything about it. "
        kv " If we tell her something bad about Oliver, she'd most likely try to kill us. "
        kv " And if we tell her about the truth, she's going to throw a tantrum. "
        kv " I think it's best if we just wait this one out... "
        kv " I mean wait this one out until she isn't mad anymore. "
        rb " That's going to be awhile, you know. "
        rb " She's gonna remember what I said about Oliver for a long time... "
        rb " But just maybe she can understand after a bit. "
        kv " Hopefully. "
        scene black with dissolve
        " You spent the rest of the break talking with Robby and Kevin after their conversation. "
        " Huh. Did the conversation with Riley really go that bad? "
        " I mean, not sure if you saw it, but god damn. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You walked out of the library and then went to your classroom. "
        pause 2.0
        jump musicclassthurs
    elif robbyknow == True and kevinknow == False:
        rb " Guess how the conversation went. "
        x " Horrible?? "
        $ kevinknow = True
        rb " No, Kevin... even worse than that, somehow. "
        kv " Geez, Robby...tell me how it went. "
        rb " She kept on telling me to work on the Olibot thing - "
        rb " Even though I kept saying that I'm tired! "
        rb " Can this girl let me rest for once??? "
        rb " I'm probably not even going to get a wink of sleep because of her... "
        rb " I swear, the only thing she ever comes up to me for is to talk about Oliver! "
        rb " I'm out there on the rooftop, trying to work... "
        rb " And then suddenly she teleports to my side saying a lot of shit about Oliver! "
        rb " Does it look like I care, Riley? "
        rb " HUH? DOES IT??????? "
        rb " Besides, I'm trying to concentrate here! "
        rb " You and your annoying ass is just getting me distracted and I{nw} "
        hide robbyangry at bottom
        show robbyneutral at left
        kv " Okay, I'm going to have to stop you before you go on and on about this for the entire break. "
        kv " I do agree with you, she should understand that you can't work 24/7. "
        kv " She should understand that you're not a robot, you're a human being... "
        kv " ...But I don't think I can get that into her thick skull. "
        kv " That skull of hers is only filled with Oliver and Oliver only. "
        rb " Yeah, it is. "
        rb " And I'm getting really sick and tired of her mentioning him a lot. "
        rb " Like, is he actually the only thing you talk about? "
        rb " How about you actually find something interesting to talk about? "
        rb " Seriously, how does she manage to talk about the same thing every single day? "
        rb " God, it's insane... "
        kv " Well, we can't really do anything about it. "
        kv " If we tell her something bad about Oliver, she'd most likely try to kill us. "
        kv " And if we tell her about the truth, she's going to throw a tantrum. "
        kv " I think it's best if we just wait this one out... "
        kv " I mean wait this one out until she isn't mad anymore. "
        rb " That's going to be awhile, you know. "
        rb " She's gonna remember what I said about Oliver for a long time... "
        rb " But just maybe she can understand after a bit. "
        kv " Hopefully. "
        scene black with dissolve
        " You spent the rest of the break talking with Robby and Kevin after their conversation. "
        " Huh. Did the conversation with Riley really go that bad? "
        " I mean, not sure if you saw it, but god damn. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You walked out of the library and then went to your classroom. "
        pause 2.0
        jump musicclassthurs
    elif robbyknow == False and kevinknow == True:
        x " Guess how the conversation went. "
        kv " Horrible?? "
        x " No, Kevin... even worse than that, somehow. "
        $ robbyknow = True
        kv " Geez, Robby...tell me how it went. "
        rb " She kept on telling me to work on the Olibot thing - "
        rb " Even though I kept saying that I'm tired! "
        rb " Can this girl let me rest for once??? "
        rb " I'm probably not even going to get a wink of sleep because of her... "
        rb " I swear, the only thing she ever comes up to me for is to talk about Oliver! "
        rb " I'm out there on the rooftop, trying to work... "
        rb " And then suddenly she teleports to my side saying a lot of shit about Oliver! "
        rb " Does it look like I care, Riley? "
        rb " HUH? DOES IT??????? "
        rb " Besides, I'm trying to concentrate here! "
        rb " You and your annoying ass is just getting me distracted and I{nw} "
        hide robbyangry at bottom
        show robbyneutral at left
        kv " Okay, I'm going to have to stop you before you go on and on about this for the entire break. "
        kv " I do agree with you, she should understand that you can't work 24/7. "
        kv " She should understand that you're not a robot, you're a human being... "
        kv " ...But I don't think I can get that into her thick skull. "
        kv " That skull of hers is only filled with Oliver and Oliver only. "
        rb " Yeah, it is. "
        rb " And I'm getting really sick and tired of her mentioning him a lot. "
        rb " Like, is he actually the only thing you talk about? "
        rb " How about you actually find something interesting to talk about? "
        rb " Seriously, how does she manage to talk about the same thing every single day? "
        rb " God, it's insane... "
        kv " Well, we can't really do anything about it. "
        kv " If we tell her something bad about Oliver, she'd most likely try to kill us. "
        kv " And if we tell her about the truth, she's going to throw a tantrum. "
        kv " I think it's best if we just wait this one out... "
        kv " I mean wait this one out until she isn't mad anymore. "
        rb " That's going to be awhile, you know. "
        rb " She's gonna remember what I said about Oliver for a long time... "
        rb " But just maybe she can understand after a bit. "
        kv " Hopefully. "
        scene black with dissolve
        " You spent the rest of the break talking with Robby and Kevin after their conversation. "
        " Huh. Did the conversation with Riley really go that bad? "
        " I mean, not sure if you saw it, but god damn. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You walked out of the library and then went to your classroom. "
        pause 2.0
        jump musicclassthurs
    else:
        x " Guess how the conversation went. "
        x " Horrible?? "
        $ robbyknow = True
        $ kevinknow = True
        rb " No, Kevin... even worse than that, somehow. "
        kv " Geez, Robby...tell me how it went. "
        rb " She kept on telling me to work on the Olibot thing - "
        rb " Even though I kept saying that I'm tired! "
        rb " Can this girl let me rest for once??? "
        rb " I'm probably not even going to get a wink of sleep because of her... "
        rb " I swear, the only thing she ever comes up to me for is to talk about Oliver! "
        rb " I'm out there on the rooftop, trying to work... "
        rb " And then suddenly she teleports to my side saying a lot of shit about Oliver! "
        rb " Does it look like I care, Riley? "
        rb " HUH? DOES IT??????? "
        rb " Besides, I'm trying to concentrate here! "
        rb " You and your annoying ass is just getting me distracted and I{nw} "
        hide robbyangry at bottom
        show robbyneutral at left
        kv " Okay, I'm going to have to stop you before you go on and on about this for the entire break. "
        kv " I do agree with you, she should understand that you can't work 24/7. "
        kv " She should understand that you're not a robot, you're a human being... "
        kv " ...But I don't think I can get that into her thick skull. "
        kv " That skull of hers is only filled with Oliver and Oliver only. "
        rb " Yeah, it is. "
        rb " And I'm getting really sick and tired of her mentioning him a lot. "
        rb " Like, is he actually the only thing you talk about? "
        rb " How about you actually find something interesting to talk about? "
        rb " Seriously, how does she manage to talk about the same thing every single day? "
        rb " God, it's insane... "
        kv " Well, we can't really do anything about it. "
        kv " If we tell her something bad about Oliver, she'd most likely try to kill us. "
        kv " And if we tell her about the truth, she's going to throw a tantrum. "
        kv " I think it's best if we just wait this one out... "
        kv " I mean wait this one out until she isn't mad anymore. "
        rb " That's going to be awhile, you know. "
        rb " She's gonna remember what I said about Oliver for a long time... "
        rb " But just maybe she can understand after a bit. "
        kv " Hopefully. "
        scene black with dissolve
        " You spent the rest of the break talking with Robby and Kevin after their conversation. "
        " Huh. Did the conversation with Riley really go that bad? "
        " I mean, not sure if you saw it, but god damn. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You walked out of the library and then went to your classroom. "
        pause 2.0
        jump musicclassthurs
label thursoligang4:
    scene black with dissolve
    pause 2.0
    scene oligangclub with dissolve
    " You walked into the room and spotted Zip and Edward just hanging out. "
    " Wondering what they're up to, you decided to walk up to them. "
    show zipneutral at left with easeinright
    show edwardneutral at right with easeinright
    ed " Yo, [name]! take a look at this! "
    " Edward practically shoves his phone into your face the moment you get close. "
    " You take his phone away from his face and you look at the photo he showed you.. "
    " It was a photo of Oliver and some girl with short brown hair and a tiara. "
    " Looks like this photo was taken about...a year ago or so. "
    " Huh, this photo is REAL old then. You weren't even here in this school at the time. "
    " Wonder who that girl is... "
    " That girl looks really familiar for some reason. "
    " Even though you haven't seen her before. "
    ed " We were looking through Oliver's phone and found this piece o' gold! "
    ed " It's Oliver's first day of being in a relationship with Alice! "
    ed " Uh...you know Alice? "
    z " She's Oliver's demon girlfriend. "
    z " Sometimes we like tricking people to get into her room in this school... "
    z " And we would also get her to eat those people. "
    z " Fun, right? "
    " Pretty cruel, but fun nonetheless. "
    " Looks like their behaviour is rubbing off on you... "
    " Great. "
    ed " Aaaanyway - he was practically DROOLING all over her the moment he got to be her boyfriend. "
    ed " We would hear him saying that he misses his girlfriend eeeeveryday... "
    z " Even though he could literally just go and check out his room. "
    z " The amount of idiocy that idiot has, seriously... "
    ed " Heheh - yeah. He still does that until now, too. "
    ed " Just a little bit less intense. "
    ed " Like before - he'd talk about her NONSTOP. "
    ed " Now, he talks about her less due to Alice confronting him about it. "
    ed " Not sure how she knew, but I guess she's been listening? "
    z " Most likely, yeah. "
    z " Yo, you wanna view more of Oliver's old photos? "
    z " Mostly just to make fun of him. "
    menu:
        " lmao sure ":
            $ oliganglv += 10
            hide edwardneutral at bottom
            show edwardhappy at right
            ed " Great! "
            z " Cmere and grab a seat then. "
            " You grabbed a seat and then began looking at Oliver's gallery. "
            scene black with dissolve
            " You spent the rest of the break looking at Oliver's old photos. "
            " Some of them were pretty cute - mostly the ones with his girlfriend in it. "
            " Some of them were just straight up weird... "
            " Annnnd some of them were pictures of him bullying various students. "
            " Very interesting gallery he's got. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You then went to the classroom after a bit. "
            pause 2.0
            jump musicclassthurs
        " Nah not in the mood ":
            z " Zamn, alright. "
            ed " I'll just send pics later, then. "
            scene black with dissolve
            " You spent the rest of the break just chilling in the room. "
            " Doing nothing but chilling in the room. And playing games. "
            " Occasionally, you'd hear some snickering coming from Edward and Zip... "
            " ...Now you're kind of wondering what kind of photos they're looking at. "
            " Edward did say that he would send pics later though. "
            play sound "audio/bellring.mp3"
            " The bell rings after a bit, looks like it's time for another class. "
            " You then went to the classroom after a bit. "
            pause 2.0
            jump musicclassthurs

label musicclassthurs:
    scene classroom with dissolve
    " You walked into the classroom and waited patiently for the music teacher to arrive. "
    " It took him a bit, but he eventually managed to come in. "
    show mrdemineutral at center with easeinright
    msd " I'm so, so sorry class! "
    msd " I have something important to do that Miss Grace tasked me with... "
    msd " But, while I'm gone... "
    msd " I'm going to have you guys do an activity sheet that I made up. "
    msd " E-engel will be watching over you all and making sure that everyone's doing their work... "
    msd " Please take one sheet from my desk and immediately start working... "
    msd " And uh...no distractions, please...! "
    msd " I'll have to get going now, um... "
    msd " M-make sure to behave! "
    hide mrdemineutral at right with easeoutright
    " Aaaand he leaves. "
    " Wonder what that important thing was... "
    " It was none of your business though. "
    " Time to get to work then.. "
    scene black with dissolve
    " You spent the rest of class hours doing the activity sheet that Mister Demi gave you. "
    " You could tell Engel was giving Oliver and the gang a stink eye for not doing their work. "
    " But honestly, it's not that surprising that they're not doing work. "
    " Even if this thing is the most simplest thing to answer... "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for your final break of the day. "
    " You passed your work to Engel and then walked out of the classroom. "
    pause 2.0
    jump thursbreak5

label thursbreak5:
    scene hallway with dissolve
    if oligangjoin == True:
        jump thursoligang5
    else:
        pass
    " Where do you wanna go for this break? "
    menu:
        " {image=engelicon} The front of the school {image=abbieicon} ":
            jump thursfrontschool5
        " {image=claireicon} The back of the school {image=popularicon} ":
            jump thursbackschool5
        " {image=cubbieicon} The gym {image=rileyicon} ":
            jump thursgym5
        " {image=skellicon} The cafeteria {image=lanaicon} ":
            jump thurscafeteria5
        " {image=bubbleicon} The rooftop {image=kevinicon} ":
            jump thursrooftop5
        " {image=rubyicon} The library {image=robbyicon} ":
            jump thurslibrary5

label thursfrontschool5:
    # engel and abbie
    scene black with dissolve
    pause 2.0
    scene paperschoolfront with dissolve
    " You walked to the front of the school and spotted your classmates doing their own things. "
    " You wanted to talk to them...but who do you talk to? "
    if abbieknow == True and engelknow == True:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump doorsdoors900
            " {image=engelicon} Engel {image=engelicon} ":
                jump doorsdoors1
    elif abbieknow == True and engelknow == False:
        menu:
            " {image=abbieicon} Abbie {image=abbieicon} ":
                jump doorsdoors900
            " {image=engelicon} A boy with feathers on his head {image=engelicon} ":
                jump doorsdoors1
    elif abbieknow == False and engelknow == True:
        menu:
            " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                jump doorsdoors900
            " {image=engelicon} Engel {image=engelicon} ":
                jump doorsdoors1
    else:
        menu:
            " {image=abbieicon} A shy looking boy {image=abbieicon} ":
                jump doorsdoors900
            " {image=engelicon} A boy with feathers on his head {image=engelicon} ":
                jump doorsdoors1
    label doorsdoors900:
        show abbieneutral at center with easeinright
        if abbieknow == True:
            " Huh. He looks like he's holding something in his hands. "
            " You're not sure what it is, but maybe you could figure it out. "
            " You then greeted him and asked him what he had in his hands "
            a " Oh, um....hello there, [name]...! "
            a " It's nice to see you here, really... "
            a " I was just looking at the birds that were passing by... "
            a " Um...I thought they were pretty cute... "
            a " ...But I noticed that one of them wasn't moving after the rest flew away... "
            a " I decided to check on it, and... "
            " Abbie opens up his hands and you saw a little injured bird on them. "
            " Pretty sure one of it's wings were damaged, therefore it couldn't fly properly. "
            a " I-I found this little guy... "
            a " I dunno what happened to him...like, how he broke his wing... "
            a " ...And I don't really know what to do with him, but... "
            a " I really wanna help him out... "
            a " ...Seeing hurt animals makes me sad... "
            a " But...I'm no animal expert, so... "
            a " What do you think we should do...? "
            a " ...I really need some help out here... "
            menu:
                " Maybe hand it to the nurse? ":
                    $ abbielv += 5
                    a " That doesn't sound too bad... "
                    a " ...Nurses ARE trained to stay calm in these situations... "
                    a " (I don't really know what that has to do with this oh god why did I say that) "
                    a " They could also just call a wildlife center... "
                    a " Um...could you come with me to take the bird to the nurse...? "
                    a " If you don't mind, that is... "
                    a " I kinda feel a little embarrassed walking in school with a random bird... "
                    a " And...and what if Oliver decides to come out of nowhere and... "
                    hide abbieneutral at bottom
                    show abbiesad at center
                    a " ... "
                    a " G-gosh, I didn't mean to sound like a bother... "
                    a " I'm so sorry... "
                    a " It's okay if you don't want to walk with me, really... "
                    a " If you don't want to, then it's fine... "
                    " You basically had absolutely nothing to do for the rest of the break, "
                    " And yes I have used this excuse multiple times to get you to do something - don't come at me, "
                    " AHEM - You agreed to walk with ABbie because you had absolutely nothing to do. "
                    " You kinda wanted to help anyway since the bird looked really cute. "
                    hide abbiesad at bottom
                    show abbiehappy at center
                    a " Thank you, [name]... "
                    a " Let's go, I don't want to keep this poor bird waiting...! "
                    scene black with dissolve
                    " You spent the rest of the break walking and talking with Abbie. "
                    " Eventually, you guys reached the nurse's office. "
                    " You kinda had to speak for Abbie because his voice was too low for the nurse. "
                    " But, the nurse called a wildlife center and told you guys to leave the bird here. "
                    " You and Abbie then talked about the bird being safe after a bit. "
                    " Abbie seemed a little anxious on leaving it alone... "
                    " You reassured him that it was going to be fine though, and that it was just getting help. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit - looks like it's time for another class. "
                    " You then went to your classroom with Abbie after a bit. "
                    pause 2.0
                    jump artclassthurs
                " I don't know what to do ":
                    a " Oh, um...okay... "
                    a " Hmmm...what should I do...? "
                    a " ...!...Oh right, the nurses office...! "
                    a " I could just take him to the nurses office and let him rest there... "
                    a " That doesn't sound too bad... "
                    a " ...Nurses ARE trained to stay calm in these situations... "
                    a " (I don't really know what that has to do with this oh god why did I say that) "
                    a " They could also just call a wildlife center... "
                    a " Um...could you come with me to take the bird to the nurse...? "
                    a " If you don't mind, that is... "
                    a " I kinda feel a little embarrassed walking in school with a random bird... "
                    a " And...and what if Oliver decides to come out of nowhere and... "
                    hide abbieneutral at bottom
                    show abbiesad at center
                    a " ... "
                    a " G-gosh, I didn't mean to sound like a bother... "
                    a " I'm so sorry... "
                    a " It's okay if you don't want to walk with me, really... "
                    a " If you don't want to, then it's fine... "
                    " You basically had absolutely nothing to do for the rest of the break, "
                    " And yes I have used this excuse multiple times to get you to do something - don't come at me, "
                    " AHEM - You agreed to walk with ABbie because you had absolutely nothing to do. "
                    " You kinda wanted to help anyway since the bird looked really cute. "
                    hide abbiesad at bottom
                    show abbiehappy at center
                    a " Thank you, [name]... "
                    a " Let's go, I don't want to keep this poor bird waiting...! "
                    scene black with dissolve
                    " You spent the rest of the break walking and talking with Abbie. "
                    " Eventually, you guys reached the nurse's office. "
                    " You kinda had to speak for Abbie because his voice was too low for the nurse. "
                    " But, the nurse called a wildlife center and told you guys to leave the bird here. "
                    " You and Abbie then talked about the bird being safe after a bit. "
                    " Abbie seemed a little anxious on leaving it alone... "
                    " You reassured him that it was going to be fine though, and that it was just getting help. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit - looks like it's time for another class. "
                    " You then went to your classroom with Abbie after a bit. "
                    pause 2.0
                    jump artclassthurs
        else:
            " Huh. He looks like he's holding something in his hands. "
            " You're not sure what it is, but maybe you could figure it out. "
            " You then greeted him and asked him what he had in his hands "
            x " Oh, um....hello there, [name]...was that your name...? "
            x " um... It's nice to see you here, really... "
            x " Uh...before I answer your question... "
            x " I don't think we've met before... "
            x " I mean, I recognize you as my new classmate, but... "
            x " I don't think I've ever got to introduce myself to you... "
            x " ...Maybe I should do that now...? "
            $ abbieknow = True
            a " I'm Abbie...it's...um...nice to meet you... "
            a " ...Back to your...q-question... "
            a " I was just looking at the birds that were passing by... "
            a " Um...I thought they were pretty cute... "
            a " ...But I noticed that one of them wasn't moving after the rest flew away... "
            a " I decided to check on it, and... "
            " Abbie opens up his hands and you saw a little injured bird on them. "
            " Pretty sure one of it's wings were damaged, therefore it couldn't fly properly. "
            a " I-I found this little guy... "
            a " I dunno what happened to him...like, how he broke his wing... "
            a " ...And I don't really know what to do with him, but... "
            a " I really wanna help him out... "
            a " ...Seeing hurt animals makes me sad... "
            a " But...I'm no animal expert, so... "
            a " What do you think we should do...? "
            a " ...I really need some help out here... "
            menu:
                " Maybe hand it to the nurse? ":
                    $ abbielv += 5
                    a " That doesn't sound too bad... "
                    a " ...Nurses ARE trained to stay calm in these situations... "
                    a " (I don't really know what that has to do with this oh god why did I say that) "
                    a " They could also just call a wildlife center... "
                    a " Um...could you come with me to take the bird to the nurse...? "
                    a " If you don't mind, that is... "
                    a " I kinda feel a little embarrassed walking in school with a random bird... "
                    a " And...and what if Oliver decides to come out of nowhere and... "
                    hide abbieneutral at bottom
                    show abbiesad at center
                    a " ... "
                    a " G-gosh, I didn't mean to sound like a bother... "
                    a " I'm so sorry... "
                    a " It's okay if you don't want to walk with me, really... "
                    a " If you don't want to, then it's fine... "
                    " You basically had absolutely nothing to do for the rest of the break, "
                    " And yes I have used this excuse multiple times to get you to do something - don't come at me, "
                    " AHEM - You agreed to walk with ABbie because you had absolutely nothing to do. "
                    " You kinda wanted to help anyway since the bird looked really cute. "
                    hide abbiesad at bottom
                    show abbiehappy at center
                    a " Thank you, [name]... "
                    a " Let's go, I don't want to keep this poor bird waiting...! "
                    scene black with dissolve
                    " You spent the rest of the break walking and talking with Abbie. "
                    " Eventually, you guys reached the nurse's office. "
                    " You kinda had to speak for Abbie because his voice was too low for the nurse. "
                    " But, the nurse called a wildlife center and told you guys to leave the bird here. "
                    " You and Abbie then talked about the bird being safe after a bit. "
                    " Abbie seemed a little anxious on leaving it alone... "
                    " You reassured him that it was going to be fine though, and that it was just getting help. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit - looks like it's time for another class. "
                    " You then went to your classroom with Abbie after a bit. "
                    pause 2.0
                    jump artclassthurs
                " I don't know what to do ":
                    a " Oh, um...okay... "
                    a " Hmmm...what should I do...? "
                    a " ...!...Oh right, the nurses office...! "
                    a " I could just take him to the nurses office and let him rest there... "
                    a " That doesn't sound too bad... "
                    a " ...Nurses ARE trained to stay calm in these situations... "
                    a " (I don't really know what that has to do with this oh god why did I say that) "
                    a " They could also just call a wildlife center... "
                    a " Um...could you come with me to take the bird to the nurse...? "
                    a " If you don't mind, that is... "
                    a " I kinda feel a little embarrassed walking in school with a random bird... "
                    a " And...and what if Oliver decides to come out of nowhere and... "
                    hide abbieneutral at bottom
                    show abbiesad at center
                    a " ... "
                    a " G-gosh, I didn't mean to sound like a bother... "
                    a " I'm so sorry... "
                    a " It's okay if you don't want to walk with me, really... "
                    a " If you don't want to, then it's fine... "
                    " You basically had absolutely nothing to do for the rest of the break, "
                    " And yes I have used this excuse multiple times to get you to do something - don't come at me, "
                    " AHEM - You agreed to walk with ABbie because you had absolutely nothing to do. "
                    " You kinda wanted to help anyway since the bird looked really cute. "
                    hide abbiesad at bottom
                    show abbiehappy at center
                    a " Thank you, [name]... "
                    a " Let's go, I don't want to keep this poor bird waiting...! "
                    scene black with dissolve
                    " You spent the rest of the break walking and talking with Abbie. "
                    " Eventually, you guys reached the nurse's office. "
                    " You kinda had to speak for Abbie because his voice was too low for the nurse. "
                    " But, the nurse called a wildlife center and told you guys to leave the bird here. "
                    " You and Abbie then talked about the bird being safe after a bit. "
                    " Abbie seemed a little anxious on leaving it alone... "
                    " You reassured him that it was going to be fine though, and that it was just getting help. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit - looks like it's time for another class. "
                    " You then went to your classroom with Abbie after a bit. "
                    pause 2.0
                    jump artclassthurs
    label doorsdoors1:
        show engelneutral at center with easeinleft
        if engelknow == True:
            e " Hmm...the wind is quite strong today. "
            e " Not that strong, but a good amount of strong. "
            e " I like this...the fresh air... "
            e " Hmhmm...this is a good way to relax. "
            e " Maybe I should take a few walks on the weekends... "
            e " That would be nice. "
            " You greeted him politely, then asked him what he was doing. "
            hide engelneutral at bottom
            show engelhappy at center
            e " Hm? [name], hi! "
            e " I'm happy to see you here. "
            e " I hope you've been doing well. "
            e " I'm just taking a breather... "
            e " The air feels really nice on our skin, doesn't it? "
            e " I like going out and walking for a good bit. "
            e " It always feels nice whenever the wind hits... "
            hide engelhappy at bottom
            show engelneutral at center
            e " Though, the only unpleasant thing is if the sun suddenly decides to make everything hot. "
            e " It's been getting a tad bit hotter recently... "
            e " I mean, nothing wrong with a little sun, but still... "
            e " I think it's been getting bad to the point that I'd have to use two fans... "
            e " Which is a little strange since it's been also raining a bit hard in the nights... "
            e " Guess the sun decided to get a little revenge on the rain for taking the spotlight, huh? "
            hide engelneutral at bottom
            show engelhappy at center
            e " Hehe, I know that's not the case here, but... "
            e " Thinking of everything in a silly way is pretty nice every now and then. "
            e " You've gotta enjoy life a lot after all, hehe. "
            e " [name], would you want to relax with me for a bit? "
            e " It's alright if you don't want to. "
            menu:
                " Hang out with engel ":
                    $ engellv += 10
                    hide engelhappy at bottom
                    show engelcontent at center
                    e " I'm glad that you'd want to spent time with me, [name]. "
                    if engellv >= 15 or engellv == 15:
                        " Looks like Engel's thinking about something. Let's see what he's thinking about... "
                        " Don't worry, I got this. "
                        e " (You being here makes me feel so much better already..) "
                        e " (Your prescence calms me in the bestest of ways...) "
                        e " (I really want to hang out with you more, but I also don't want to bother you...) "
                        e " (I wonder how you'd feel if I told you all this...) "
                        e " (Hhmmm...maybe I'll tell you when the time is right...) "
                        e " (With how things are going so far, it's been great...!!) "
                        e " (I want to continue having fun with you...) "
                        e " It's always nice to have someone hanging out with you. "
                        e " We should probably talk more to get to know eachother better! "
                        e " You seem like quite the fun [person] to talk to, [name]! "
                        e " So, if you don't mind... "
                        e " We could talk more tomorrow, if you want to. "
                    else:
                        e " It's always nice to have someone hanging out with you. "
                        e " We should probably talk more to get to know eachother better! "
                        e " You seem like quite the fun [person] to talk to, [name]! "
                        e " So, if you don't mind... "
                        e " We could talk more tomorrow, if you want to. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Engel. "
                    " You had a lot of fun talking with him, since he was mostly being a chill guy. "
                    " He would often throw in some jokes here and there, too. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your last class. "
                    pause 2.0
                    jump artclassthurs
                " I've got places to be ":
                    hide engelhappy at bottom
                    show engelneutral at center
                    e " Oh! were you just passing by, then? "
                    e " I really didn't mean to distract you... "
                    e " Thought you were here for a long conversation. "
                    e " My apologies... "
                    e " Though, I won't keep you here for too long. "
                    e " Good luck on whatever you're busy with, [name]. "
                    e " If you have any questions about anything, I'm right here. "
                    e " I'll see you later in class. "
                    scene black with dissolve
                    " You spent the rest of the break walking around the school. "
                    " While you were walking around, you saw three students throwing pranks on a random nerd you don't recognize. "
                    " Huh. Interesting. "
                    " You should probably help in that, but you also don't want to get involved and get hurt. "
                    " Plus the pranks seem pretty harmless from what you're seeing. "
                    " Maybe someone else should help that guy... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked to your classroom after a bit of looking at your phone. "
                    pause 2.0
                    jump artclassthurs
        else:
            x " Hmm...the wind is quite strong today. "
            x " Not that strong, but a good amount of strong. "
            x " I like this...the fresh air... "
            x " Hmhmm...this is a good way to relax. "
            x " Maybe I should take a few walks on the weekends... "
            x " That would be nice. "
            " You greeted him politely, then asked him what he was doing. "
            hide engelneutral at bottom
            show engelhappy at center
            x " Hm? [name], hi! "
            x " I'm happy to see you here. "
            x " I hope you've been doing well. "
            x " Oh wait! I don't think I've introduced myself to you before... "
            x " I apologize...this isn't what a star student should do. "
            $ engelknow = True
            e " I'm Engel, it's nice to meet you! as for what I was doing... "
            e " I'm just taking a breather... "
            e " The air feels really nice on our skin, doesn't it? "
            e " I like going out and walking for a good bit. "
            e " It always feels nice whenever the wind hits... "
            hide engelhappy at bottom
            show engelneutral at center
            e " Though, the only unpleasant thing is if the sun suddenly decides to make everything hot. "
            e " It's been getting a tad bit hotter recently... "
            e " I mean, nothing wrong with a little sun, but still... "
            e " I think it's been getting bad to the point that I'd have to use two fans... "
            e " Which is a little strange since it's been also raining a bit hard in the nights... "
            e " Guess the sun decided to get a little revenge on the rain for taking the spotlight, huh? "
            hide engelneutral at bottom
            show engelhappy at center
            e " Hehe, I know that's not the case here, but... "
            e " Thinking of everything in a silly way is pretty nice every now and then. "
            e " You've gotta enjoy life a lot after all, hehe. "
            e " [name], would you want to relax with me for a bit? "
            e " It's alright if you don't want to. "
            menu:
                " Hang out with engel ":
                    $ engellv += 10
                    hide engelhappy at bottom
                    show engelcontent at center
                    e " I'm glad that you'd want to spent time with me, [name]. "
                    if engellv >= 15 or engellv == 15:
                        " Looks like Engel's thinking about something. Let's see what he's thinking about... "
                        " Don't worry, I got this. "
                        e " (You being here makes me feel so much better already..) "
                        e " (Your prescence calms me in the bestest of ways...) "
                        e " (I really want to hang out with you more, but I also don't want to bother you...) "
                        e " (I wonder how you'd feel if I told you all this...) "
                        e " (Hhmmm...maybe I'll tell you when the time is right...) "
                        e " (With how things are going so far, it's been great...!!) "
                        e " (I want to continue having fun with you...) "
                        e " It's always nice to have someone hanging out with you. "
                        e " We should probably talk more to get to know eachother better! "
                        e " You seem like quite the fun [person] to talk to, [name]! "
                        e " So, if you don't mind... "
                        e " We could talk more tomorrow, if you want to. "
                    else:
                        e " It's always nice to have someone hanging out with you. "
                        e " We should probably talk more to get to know eachother better! "
                        e " You seem like quite the fun [person] to talk to, [name]! "
                        e " So, if you don't mind... "
                        e " We could talk more tomorrow, if you want to. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Engel. "
                    " You had a lot of fun talking with him, since he was mostly being a chill guy. "
                    " He would often throw in some jokes here and there, too. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your last class. "
                    pause 2.0
                    jump artclassthurs
                " I've got places to be ":
                    hide engelhappy at bottom
                    show engelneutral at center
                    e " Oh! were you just passing by, then? "
                    e " I really didn't mean to distract you... "
                    e " Thought you were here for a long conversation. "
                    e " My apologies... "
                    e " Though, I won't keep you here for too long. "
                    e " Good luck on whatever you're busy with, [name]. "
                    e " If you have any questions about anything, I'm right here. "
                    e " I'll see you later in class. "
                    scene black with dissolve
                    " You spent the rest of the break walking around the school. "
                    " While you were walking around, you saw three students throwing pranks on a random nerd you don't recognize. "
                    " Huh. Interesting. "
                    " You should probably help in that, but you also don't want to get involved and get hurt. "
                    " Plus the pranks seem pretty harmless from what you're seeing. "
                    " Maybe someone else should help that guy... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked to your classroom after a bit of looking at your phone. "
                    pause 2.0
                    jump artclassthurs
label thursbackschool5:
    # claire and lizzy
    scene black with dissolve
    pause 2.0
    scene paperschoolback with dissolve
    if clairebeatup == True and clairesorry == False:
        " You can't interact with someone here because you didn't apologize. "
        " Sorry not sorry. "
        scene black
        pause 2.0
        jump artclassthurs
    else:
        pass
    " You walked to the back of the school and found two of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if claireknow == True and popularknow == True:
        menu:
            " {image=claireicon} Claire {image=claireicon} ":
                jump odetarirun
            " {image=popularicon} Lizzy {image=popularicon} ":
                jump odetarideserved
    elif claireknow == True and popularknow == False:
        menu:
            " {image=claireicon} Claire {image=claireicon} ":
                jump odetarirun
            " {image=popularicon} A popular girl {image=popularicon} ":
                jump odetarideserved
    elif claireknow == False and popularknow == True:
        menu:
            " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                jump odetarirun
            " {image=popularicon} Lizzy {image=popularicon} ":
                jump odetarideserved
    else:
        menu:
            " {image=claireicon} A girl with a bow on her head {image=claireicon} ":
                jump odetarirun
            " {image=popularicon} A popular girl {image=popularicon} ":
                jump odetarideserved
    label odetarirun:
        show claireneutral at center with easeinleft
        if claireknow == True:
            c " Hmhmmm... "
            c " I wonder what Engel and Bubble are doing right now... "
            c " Maybe I should check out that one show Lana's been making? "
            c " I heard she records the episodes and puts them all on BookFace... "
            c " Yeah, I should probably check it out once I'm free. "
            c " She's pretty good at storytelling, after all. "
            c " Maybe she should get a job that's related to storytelling in the future... "
            c " That would fit her very well. "
            " You greeted her and asked what she was doing. "
            hide claireneutral at bottom
            show clairehappy at center
            c " Hm? [name], hiiii!! "
            c " Just, you know...thinking about life and my friends. "
            c " And also looking at the greenery every now and then. "
            c " They say it rests the eyes! "
            c " I've been kind of looking at my phone a lot recently, so... "
            c " I'm taking this as a break! "
            hide clairehappy at bottom
            show claireneutral at center
            c " I don't really want to be THAT addicted to my phone... "
            c " Otherwise I'm going to end up like those kids who...what's this... "
            hide claireneutral at bottom
            show claireconfused at center
            c " What do they call it? that skibidi toilet thing? "
            c " ...Brainrot...? "
            c " I've been hearing kids say that a lot more often now... "
            c " It's been kind of getting to my head, and I don't want to be addicted to that AI slop! "
            c " Sure it's funny to say, but really.. "
            c " We don't need to rely on AI this much. "
            c " Geez...what's been going on with people nowadays? "
            c " Thinking that a robot would do a better job than you... "
            c " When true quality work comes from human beings. "
            c " Even if it doesn't feel like it, there's truly something special in humans making things instead of robots. "
            c " Guh... I shouldn't talk about this topic for too long. "
            hide claireconfused at bottom
            show claireneutral at center
            c " Anyway! You wanna hang out here for a bit? "
            c " I kinda need someone to talk to... "
            c " Sitting out here alone isn't really a fun thing to do, you know. "
            c " I mean, sure the peace is great - but it also feels a little empty without someone by your side. "
            c " Do you wanna hang out with me just for a little bit? "
            c " Oh, and of course - it's okay if you don't want to! "
            menu:
                " Stay with Claire ":
                    $ clairelv += 10
                    hide claireneutral at bottom
                    show clairehappy at center
                    c " That's great! "
                    c " Come here, sit next to me... "
                    c " We can talk about anything you want! "
                    if clairelv >= 25 or clairelv == 25:
                        " Looks like Claire is thinking about something. "
                        " Don't worry, I've got this. "
                        c " (I don't know why, but everything just feels so easy with [them]...) "
                        c " (It feels like I can just talk to [them] and I'll feel okay...) "
                        c " (Is this what they call having a best friend?) "
                        c " (I mean, Engel is my friend, but he's just a close friend...) "
                        c " (Not the best one, sorry Engel...) "
                        c " (But...I'm glad that [they] [are] with me and talking to me right now.) "
                        c " (I just hope that I won't get too boring for [them]...) "
                        c " Maybe we could talk about eachother? "
                        c " As in, like...to get to know eachother, of course! "
                        c " I'd love to get to know more about you! "
                        c " You seem like an interesting person, after all... "
                        c " And also a fun one! "
                        c " Let's get started then...hm... "
                    else:
                        c " Maybe we could talk about eachother? "
                        c " As in, like...to get to know eachother, of course! "
                        c " I'd love to get to know more about you! "
                        c " You seem like an interesting person, after all... "
                        c " And also a fun one! "
                        c " Let's get started then...hm... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Claire. "
                    " You both got to know a lot about eachother, actually. "
                    " Did you know that she's REAL into pinterest photos? "
                    " Like, all the aesthetic stuff and all that. "
                    " Bet you never knew that, huh? "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump artclassthurs
                " I've got places to be ":
                    c " Oh, were you just stopping by here then? "
                    c " I didn't mean to distract you here for long... "
                    c " You can get going to whatever you have to do though! "
                    c " I'll see you later in class, [name]! "
                    scene black with dissolve
                    " You spent the rest of the break walking around the school. "
                    " While you were walking around, you saw three students throwing pranks on a random nerd you don't recognize. "
                    " Huh. Interesting. "
                    " You should probably help in that, but you also don't want to get involved and get hurt. "
                    " Plus the pranks seem pretty harmless from what you're seeing. "
                    " Maybe someone else should help that guy... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked to your classroom after a bit of looking at your phone. "
                    pause 2.0
                    jump artclassthurs
        else:
            x " Hmhmmm... "
            x " I wonder what Engel and Bubble are doing right now... "
            x " Maybe I should check out that one show Lana's been making? "
            x " I heard she records the episodes and puts them all on BookFace... "
            x " Yeah, I should probably check it out once I'm free. "
            x " She's pretty good at storytelling, after all. "
            x " Maybe she should get a job that's related to storytelling in the future... "
            x " That would fit her very well. "
            " You greeted her and asked what she was doing. "
            hide claireneutral at bottom
            show clairehappy at center
            x " Hm? [name], hiiii!! "
            x " Wait, before I answer your question... "
            x " I don't think I've introduced myself before! "
            x " So sorry, haha... "
            $ claireknow = True
            c " I'm Claire! It's really nice to meet you! "
            c " I'm one of your classmates, if you didn't know that. "
            c " Anyway, about your question... "
            c " Just, you know...thinking about life and my friends. "
            c " And also looking at the greenery every now and then. "
            c " They say it rests the eyes! "
            c " I've been kind of looking at my phone a lot recently, so... "
            c " I'm taking this as a break! "
            hide clairehappy at bottom
            show claireneutral at center
            c " I don't really want to be THAT addicted to my phone... "
            c " Otherwise I'm going to end up like those kids who...what's this... "
            hide claireneutral at bottom
            show claireconfused at center
            c " What do they call it? that skibidi toilet thing? "
            c " ...Brainrot...? "
            c " I've been hearing kids say that a lot more often now... "
            c " It's been kind of getting to my head, and I don't want to be addicted to that AI slop! "
            c " Sure it's funny to say, but really.. "
            c " We don't need to rely on AI this much. "
            c " Geez...what's been going on with people nowadays? "
            c " Thinking that a robot would do a better job than you... "
            c " When true quality work comes from human beings. "
            c " Even if it doesn't feel like it, there's truly something special in humans making things instead of robots. "
            c " Guh... I shouldn't talk about this topic for too long. "
            hide claireconfused at bottom
            show claireneutral at center
            c " Anyway! You wanna hang out here for a bit? "
            c " I kinda need someone to talk to... "
            c " Sitting out here alone isn't really a fun thing to do, you know. "
            c " I mean, sure the peace is great - but it also feels a little empty without someone by your side. "
            c " Do you wanna hang out with me just for a little bit? "
            c " Oh, and of course - it's okay if you don't want to! "
            menu:
                " Stay with Claire ":
                    $ clairelv += 10
                    hide claireneutral at bottom
                    show clairehappy at center
                    c " That's great! "
                    c " Come here, sit next to me... "
                    c " We can talk about anything you want! "
                    if clairelv >= 25 or clairelv == 25:
                        " Looks like Claire is thinking about something. "
                        " Don't worry, I've got this. "
                        c " (I don't know why, but everything just feels so easy with [them]...) "
                        c " (It feels like I can just talk to [them] and I'll feel okay...) "
                        c " (Is this what they call having a best friend?) "
                        c " (I mean, Engel is my friend, but he's just a close friend...) "
                        c " (Not the best one, sorry Engel...) "
                        c " (But...I'm glad that [they] [are] with me and talking to me right now.) "
                        c " (I just hope that I won't get too boring for [them]...) "
                        c " Maybe we could talk about eachother? "
                        c " As in, like...to get to know eachother, of course! "
                        c " I'd love to get to know more about you! "
                        c " You seem like an interesting person, after all... "
                        c " And also a fun one! "
                        c " Let's get started then...hm... "
                    else:
                        c " Maybe we could talk about eachother? "
                        c " As in, like...to get to know eachother, of course! "
                        c " I'd love to get to know more about you! "
                        c " You seem like an interesting person, after all... "
                        c " And also a fun one! "
                        c " Let's get started then...hm... "
                    scene black with dissolve
                    " You spent the rest of the break talking with Claire. "
                    " You both got to know a lot about eachother, actually. "
                    " Did you know that she's REAL into pinterest photos? "
                    " Like, all the aesthetic stuff and all that. "
                    " Bet you never knew that, huh? "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked back into the school and went to your classroom. "
                    pause 2.0
                    jump artclassthurs
                " I've got places to be ":
                    c " Oh, were you just stopping by here then? "
                    c " I didn't mean to distract you here for long... "
                    c " You can get going to whatever you have to do though! "
                    c " I'll see you later in class, [name]! "
                    scene black with dissolve
                    " You spent the rest of the break walking around the school. "
                    " While you were walking around, you saw three students throwing pranks on a random nerd you don't recognize. "
                    " Huh. Interesting. "
                    " You should probably help in that, but you also don't want to get involved and get hurt. "
                    " Plus the pranks seem pretty harmless from what you're seeing. "
                    " Maybe someone else should help that guy... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked to your classroom after a bit of looking at your phone. "
                    pause 2.0
                    jump artclassthurs
    label odetarideserved:
        show lizzyneutral at center with easeinright
        if popularknow == True:
            " You walked up to her and noticed that she seemed a little quiet. "
            " Out of the two popular girls in this school, you knew she was kinda the quiet one... "
            " ...But never really thought of her as the REALLY REALLY quiet one. "
            " Since usually popular girls are talkative to know all the hot gossip. "
            " You asked her if she was doing alright. "
            lz " ...? Oh, you. "
            lz " Sorry, I was just thinking about a few things... "
            lz " Like thinking about apologizing to Petunia. "
            lz " I'm sure you know about me and Petunia's situation right now. "
            lz " I'd say you don't know, so...let's say me and Petunia had a disagreement. "
            lz " I've been taking other people's words into consideration, "
            lz " After asking everyone what I should do... "
            lz " I didn't really want to tell her the truth at first, but I know she has to know at some point. "
            lz " But now I think I'm ready to tell her how I really feel. "
            lz " I just...don't know the right words to tell her. "
            lz " What if I say the wrong thing and I mess things up even more? "
            lz " I don't want that to happen. "
            lz " And I can't exactly just...use AI to generate an apology. "
            lz " AI shit is dumb. "
            lz " Plus, using AI would just make it sound insincere. "
            lz " So...I might need some help here, [name]. "
            lz " I know that we don't know eachother that much, but I really need your help. "
            lz " So...could you help me, just this once? "
            lz " If you're not busy right now, that is. "
            menu:
                " Help Lizzy ":
                    $ popularlv += 10
                    hide lizzyneutral at bottom
                    show lizzyhappy at center
                    lz " ...I'm glad that you're helping me then. "
                    lz " I really don't want me and Petunia's relationship to be stained for the rest of our lives... "
                    lz " It's sad, don't you think? "
                    lz " Two best friends parting... "
                    lz " Even though we do this sometimes, it still pains me a lot. "
                    lz " That's why I always try to get our relationship to be fixed. "
                    lz " Like right now, actually. "
                    if popularlv >= 20 or popularlv == 20:
                        " Looks like Lizzy is thinking about something. "
                        " Here, I'll let you hear what she's thinking. I've got this. "
                        lz " (Huh...despite everything [name] has seen from us...) "
                        lz " ([they] really do want me and Petunia to be together again.) "
                        lz " (Even if [they] didn't know me and her for long...) "
                        lz " (Maybe I was wrong to think of [them] that way.) "
                        lz " (Maybe I can still fix this later...) "
                        lz " (I just hope both [name] and Petunia will forgive me for what I thought.) "
                        lz " Anyways, we shouldn't waste time. "
                        lz " We should start thinking on what I need to say to her. "
                        lz " I'm planning to tell her once school is over, so... "
                        lz " Let's get on with it. "
                    else:
                        lz " Anyways, we shouldn't waste time. "
                        lz " We should start thinking on what I need to say to her. "
                        lz " I'm planning to tell her once school is over, so... "
                        lz " Let's get on with it. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Lizzy. "
                    " You helped her with finding some words so that she could talk to Petunia properly... "
                    " ...And not completely and utterly fuck up royally. "
                    " You guys eventually got something together and Lizzy thanked you for it. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked to your classroom after a bit of looking at your phone. "
                    pause 2.0
                    jump artclassthurs
                " I've got places to be ":
                    hide lizzyneutral at bottom
                    show lizzyconfused at center
                    lz " Oh shit, you had somewhere to go? "
                    lz " Dang, my bad then. "
                    lz " Didn't mean to keep you away from whatever you were doing. "
                    hide lizzyconfused at bottom
                    show lizzyneutral at center
                    lz " You can go now though. "
                    lz " I'll figure out a way to get my words working. "
                    lz " See you in class. "
                    scene black with dissolve
                    " You spent the rest of the break walking around the school. "
                    " While you were walking around, you saw three students throwing pranks on a random nerd you don't recognize. "
                    " Huh. Interesting. "
                    " You should probably help in that, but you also don't want to get involved and get hurt. "
                    " Plus the pranks seem pretty harmless from what you're seeing. "
                    " Maybe someone else should help that guy... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked to your classroom after a bit of looking at your phone. "
                    pause 2.0
                    jump artclassthurs
        else:
            " You walked up to her and noticed that she seemed a little quiet. "
            " Out of the two popular girls in this school, you knew she was kinda the quiet one... "
            " ...But never really thought of her as the REALLY REALLY quiet one. "
            " Since usually popular girls are talkative to know all the hot gossip. "
            " You asked her if she was doing alright. "
            x " ...? Oh, you. "
            $ popularknow = True
            lz " I'm uh...Lizzy. And... "
            lz " ... "
            lz " Sorry, I was just thinking about a few things... "
            lz " Like thinking about apologizing to Petunia. "
            lz " I'm sure you know about me and Petunia's situation right now. "
            lz " I'd say you don't know, so...let's say me and Petunia had a disagreement. "
            lz " I've been taking other people's words into consideration, "
            lz " After asking everyone what I should do... "
            lz " I didn't really want to tell her the truth at first, but I know she has to know at some point. "
            lz " But now I think I'm ready to tell her how I really feel. "
            lz " I just...don't know the right words to tell her. "
            lz " What if I say the wrong thing and I mess things up even more? "
            lz " I don't want that to happen. "
            lz " And I can't exactly just...use AI to generate an apology. "
            lz " AI shit is dumb. "
            lz " Plus, using AI would just make it sound insincere. "
            lz " So...I might need some help here, [name]. "
            lz " I know that we don't know eachother that much, but I really need your help. "
            lz " So...could you help me, just this once? "
            lz " If you're not busy right now, that is. "
            menu:
                " Help Lizzy ":
                    $ popularlv += 10
                    hide lizzyneutral at bottom
                    show lizzyhappy at center
                    lz " ...I'm glad that you're helping me then. "
                    lz " I really don't want me and Petunia's relationship to be stained for the rest of our lives... "
                    lz " It's sad, don't you think? "
                    lz " Two best friends parting... "
                    lz " Even though we do this sometimes, it still pains me a lot. "
                    lz " That's why I always try to get our relationship to be fixed. "
                    lz " Like right now, actually. "
                    lz " Anyways, we shouldn't waste time. "
                    lz " We should start thinking on what I need to say to her. "
                    lz " I'm planning to tell her once school is over, so... "
                    lz " Let's get on with it. "
                    scene black with dissolve
                    " You spent the rest of the break talking with Lizzy. "
                    " You helped her with finding some words so that she could talk to Petunia properly... "
                    " ...And not completely and utterly fuck up royally. "
                    " You guys eventually got something together and Lizzy thanked you for it. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked to your classroom after a bit of looking at your phone. "
                    pause 2.0
                    jump artclassthurs
                " I've got places to be ":
                    hide lizzyneutral at bottom
                    show lizzyconfused at center
                    lz " Oh shit, you had somewhere to go? "
                    lz " Dang, my bad then. "
                    lz " Didn't mean to keep you away from whatever you were doing. "
                    hide lizzyconfused at bottom
                    show lizzyneutral at center
                    lz " You can go now though. "
                    lz " I'll figure out a way to get my words working. "
                    lz " See you in class. "
                    scene black with dissolve
                    " You spent the rest of the break walking around the school. "
                    " While you were walking around, you saw three students throwing pranks on a random nerd you don't recognize. "
                    " Huh. Interesting. "
                    " You should probably help in that, but you also don't want to get involved and get hurt. "
                    " Plus the pranks seem pretty harmless from what you're seeing. "
                    " Maybe someone else should help that guy... "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You walked to your classroom after a bit of looking at your phone. "
                    pause 2.0
                    jump artclassthurs
label thursgym5:
    # cubbie and riley
    scene black with dissolve
    pause 2.0
    scene gym with dissolve
    " You walked to the gym and found two of your classmates talking with eachother. "
    " Wondering what they're talking about, you decided to walk over to them. "
    show cubbieneutral at left with easeinright
    show rileyneutral at right with easeinright
    if cubbieknow == True and rileyknow == True:
        ri " Cubster! [name]ster! "
        cb " ...? "
        " The other guy seems to be a little confused with the nickname. "
        " You honestly don't mind your nickname. "
        " It was a little unique, and you liked being unique. "
        " Maybe you should give yourself a nickname... "
        " mc[name]coolster. "
        " Banger, right? "
        ri " I've been thinking lately... "
        ri " Maybe I should bring Oliver more stuff! "
        ri " I know that he likes them! "
        ri " Even though he...kind of throws them in the trash. "
        ri " That just means that he appreciates them a lot! "
        ri " Trash can have valuable things in it, after all! "
        ri " Like what they say - one mans treasure is another mans gold... "
        ri " I guess that kind of applies to Oliver??? I don't know what I'm getting at, HEHEHAHAHaaa... "
        cb " ... "
        " Cubbie seems to have the expression of: not this again. "
        " Looks like Riley's been going extra Oliver-mode today. "
        " It's honestly a little bit concerning and you should probably help her "
        " Though, what should you say? "
        " You don't want to accidentally hurt her, after all. "
        " Let's think... "
        menu:
            " Calm Riley down ":
                $ robbrileylv += 10
                " Before RIley could say anything about Oliver, you stopped her. "
                " You told her that she's been talking about Oliver way too much recently... "
                " And that she should probably tone it down a little. "
                " You told her that even Cubbie's looking a bit uncomfortable right now. "
                ri " ...Wait, really? "
                ri " Have I been going overboard...? "
                hide rileyneutral at bottom
                show rileysad at right
                ri " Oh geez, I didn't mean to upset you guys... "
                ri " I guess I've just been too focused on Oliver to notice that you guys felt upset. "
                ri " Maybe this is why Robby was upset at me earlier. "
                ri " (Good job Riley, when can you learn to shut up...?) "
                ri " (Probably never, with how I'm acting...) "
                ri " (I'm too pathetic over Oliver, I swear...) "
                " You told her that it's alright to talk about Oliver. "
                " It's just that you've got to tone it down just a bit. "
                " Sometimes people aren't gonna like what you talk about. "
                " So, if they say that they aren't interested, then... "
                " You should probably just talk about something else. "
                " To prevent making them feel uncomfortable, of course. "
                ri " Hmm... "
                hide rileysad at bottom
                show rileyneutral at right
                ri  " ...Okay!! I'll take your advice, [name]! "
                ri " Thanks for teaching me this stuff! "
                if robbrileylv >= 20 or robbrileylv == 20:
                    " Looks like Riley's thinking about something. "
                    " Let's see what she's thinking about... "
                    ri " (Huh...this is weird.) "
                    ri " (It feels like [name] kinda understands me in a way...) "
                    ri " (Makes me feel all safe and nice...) "
                    ri " (Huh! This feeling is interesting!) "
                    ri " (Maybe I should talk to [them] more...) "
                    ri " Do you have anymore advice for me, actually? "
                    ri " I need to learn from the best, after all! "
                    ri " Come on, come on! Give me more advice! "
                else:
                    ri " Do you have anymore advice for me, actually? "
                    ri " I need to learn from the best, after all! "
                    ri " Come on, come on! Give me more advice! "
                scene black with dissolve
                " You spent the rest of the break talking with Riley. "
                " You were just giving her some advice and more stuff. "
                " You weren't sure if she was actually going to improve, but atleast she said she was gonna try. "
                " Keyword: try. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your final class. "
                pause 2.0
                jump artclassthurs
            " Distract Cubbie from Riley's yapping! ":
                $ cubbielv += 10
                " You nudged Cubbie's shoulder so that you could get his attention. "
                " You wanted to distract him from the rambling that's gonna happen. "
                cb " ...?? "
                " You grabbed your phone from your pocket and gave it to him. "
                " Your phone pretty much has a lot of games in it. "
                " You told him to play any kinds of games in there because you didn't want him to listen to Riley's rambling. "
                " You'll just deal with the nodding and going 'ooh' and 'aah' for the rambling. "
                " You were pretty good at doing that, as far as you've been told. "
                hide cubbieneutral at bottom
                show cubbiehappy at left
                cb " ...!! "
                " Cubbie gives you a thankful smile, and he starts playing a game on his phone. "
                if cubbielv >= 20 or cubbielv == 20:
                    " Looks like Cubbie's thinking about something. "
                    " Don't worry, I'll let you listen. "
                    cb " (...With [name] around, I feel just a bit safer...) "
                    cb " ([they] [are] always so nice towards me...) "
                    cb " (I don't know why [they] [are] nice, but...I like them. A lot.) "
                    cb " (I wanna talk with them more...) "
                    cb " (Maybe I could even let [them] hear my voice for the first time...?) "
                    cb " (Only when I get more comfortable though...) "
                    " Cubbie seems concentrated on the game he's playing. "
                    " Best to not disturb him, and time to focus on Riley's rambling. "
                    " You have a feeling that this one is going to be a long one... "
                    " Not that you minded. You could just play ping pong in your mind for the entire thing. "
                else:
                    " Cubbie seems concentrated on the game he's playing. "
                    " Best to not disturb him, and time to focus on Riley's rambling. "
                    " You have a feeling that this one is going to be a long one... "
                    " Not that you minded. You could just play ping pong in your mind for the entire thing. "
                scene black with dissolve
                " You spent the rest of the break talking with Riley. "
                " You were just giving her some advice and more stuff. "
                " You weren't sure if she was actually going to improve, but atleast she said she was gonna try. "
                " Keyword: try. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your final class. "
                pause 2.0
                jump artclassthurs
    elif cubbieknow == True and rileyknow == False:
        x " Cubster! [name]ster! "
        cb " ...? "
        " Huh, you heardof that insane little kid before. "
        $ rileyknow = True
        " You've heard her name was Riley and she liked talking about Oliver. "
        " An extremely obsessed fangirl, in short. "
        " The other guy seems to be a little confused with the nickname she gave him. "
        " You honestly don't mind your nickname. "
        " It was a little unique, and you liked being unique. "
        " Maybe you should give yourself a nickname... "
        " mc[name]coolster. "
        " Banger, right? "
        ri " I've been thinking lately... "
        ri " Maybe I should bring Oliver more stuff! "
        ri " I know that he likes them! "
        ri " Even though he...kind of throws them in the trash. "
        ri " That just means that he appreciates them a lot! "
        ri " Trash can have valuable things in it, after all! "
        ri " Like what they say - one mans treasure is another mans gold... "
        ri " I guess that kind of applies to Oliver??? I don't know what I'm getting at, HEHEHAHAHaaa... "
        cb " ... "
        " Cubbie seems to have the expression of: not this again. "
        " Looks like Riley's been going extra Oliver-mode today. "
        " It's honestly a little bit concerning and you should probably help her "
        " Though, what should you say? "
        " You don't want to accidentally hurt her, after all. "
        " Let's think... "
        menu:
            " Calm Riley down ":
                $ robbrileylv += 10
                " Before RIley could say anything about Oliver, you stopped her. "
                " You told her that she's been talking about Oliver way too much recently... "
                " And that she should probably tone it down a little. "
                " You told her that even Cubbie's looking a bit uncomfortable right now. "
                ri " ...Wait, really? "
                ri " Have I been going overboard...? "
                hide rileyneutral at bottom
                show rileysad at right
                ri " Oh geez, I didn't mean to upset you guys... "
                ri " I guess I've just been too focused on Oliver to notice that you guys felt upset. "
                ri " Maybe this is why Robby was upset at me earlier. "
                ri " (Good job Riley, when can you learn to shut up...?) "
                ri " (Probably never, with how I'm acting...) "
                ri " (I'm too pathetic over Oliver, I swear...) "
                " You told her that it's alright to talk about Oliver. "
                " It's just that you've got to tone it down just a bit. "
                " Sometimes people aren't gonna like what you talk about. "
                " So, if they say that they aren't interested, then... "
                " You should probably just talk about something else. "
                " To prevent making them feel uncomfortable, of course. "
                ri " Hmm... "
                hide rileysad at bottom
                show rileyneutral at right
                ri  " ...Okay!! I'll take your advice, [name]! "
                ri " Thanks for teaching me this stuff! "
                if robbrileylv >= 20 or robbrileylv == 20:
                    " Looks like Riley's thinking about something. "
                    " Let's see what she's thinking about... "
                    ri " (Huh...this is weird.) "
                    ri " (It feels like [name] kinda understands me in a way...) "
                    ri " (Makes me feel all safe and nice...) "
                    ri " (Huh! This feeling is interesting!) "
                    ri " (Maybe I should talk to [them] more...) "
                    ri " Do you have anymore advice for me, actually? "
                    ri " I need to learn from the best, after all! "
                    ri " Come on, come on! Give me more advice! "
                else:
                    ri " Do you have anymore advice for me, actually? "
                    ri " I need to learn from the best, after all! "
                    ri " Come on, come on! Give me more advice! "
                scene black with dissolve
                " You spent the rest of the break talking with Riley. "
                " You were just giving her some advice and more stuff. "
                " You weren't sure if she was actually going to improve, but atleast she said she was gonna try. "
                " Keyword: try. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your final class. "
                pause 2.0
                jump artclassthurs
            " Distract Cubbie from Riley's yapping! ":
                $ cubbielv += 10
                " You nudged Cubbie's shoulder so that you could get his attention. "
                " You wanted to distract him from the rambling that's gonna happen. "
                cb " ...?? "
                " You grabbed your phone from your pocket and gave it to him. "
                " Your phone pretty much has a lot of games in it. "
                " You told him to play any kinds of games in there because you didn't want him to listen to Riley's rambling. "
                " You'll just deal with the nodding and going 'ooh' and 'aah' for the rambling. "
                " You were pretty good at doing that, as far as you've been told. "
                hide cubbieneutral at bottom
                show cubbiehappy at left
                cb " ...!! "
                " Cubbie gives you a thankful smile, and he starts playing a game on his phone. "
                if cubbielv >= 20 or cubbielv == 20:
                    " Looks like Cubbie's thinking about something. "
                    " Don't worry, I'll let you listen. "
                    cb " (...With [name] around, I feel just a bit safer...) "
                    cb " ([they] [are] always so nice towards me...) "
                    cb " (I don't know why [they] [are] nice, but...I like them. A lot.) "
                    cb " (I wanna talk with them more...) "
                    cb " (Maybe I could even let [them] hear my voice for the first time...?) "
                    cb " (Only when I get more comfortable though...) "
                    " Cubbie seems concentrated on the game he's playing. "
                    " Best to not disturb him, and time to focus on Riley's rambling. "
                    " You have a feeling that this one is going to be a long one... "
                    " Not that you minded. You could just play ping pong in your mind for the entire thing. "
                else:
                    " Cubbie seems concentrated on the game he's playing. "
                    " Best to not disturb him, and time to focus on Riley's rambling. "
                    " You have a feeling that this one is going to be a long one... "
                    " Not that you minded. You could just play ping pong in your mind for the entire thing. "
                scene black with dissolve
                " You spent the rest of the break talking with Riley. "
                " You were just giving her some advice and more stuff. "
                " You weren't sure if she was actually going to improve, but atleast she said she was gonna try. "
                " Keyword: try. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your final class. "
                pause 2.0
                jump artclassthurs
    elif cubbieknow == False and rileyknow == True:
        ri " Cubster! [name]ster! "
        $ cubbieknow = True
        cb " ...? "
        " The other guy seems to be a little confused with the nickname. "
        " You honestly don't mind your nickname. "
        " It was a little unique, and you liked being unique. "
        " Maybe you should give yourself a nickname... "
        " mc[name]coolster. "
        " Banger, right? "
        ri " I've been thinking lately... "
        ri " Maybe I should bring Oliver more stuff! "
        ri " I know that he likes them! "
        ri " Even though he...kind of throws them in the trash. "
        ri " That just means that he appreciates them a lot! "
        ri " Trash can have valuable things in it, after all! "
        ri " Like what they say - one mans treasure is another mans gold... "
        ri " I guess that kind of applies to Oliver??? I don't know what I'm getting at, HEHEHAHAHaaa... "
        cb " ... "
        " Cubbie seems to have the expression of: not this again. "
        " Looks like Riley's been going extra Oliver-mode today. "
        " It's honestly a little bit concerning and you should probably help her "
        " Though, what should you say? "
        " You don't want to accidentally hurt her, after all. "
        " Let's think... "
        menu:
            " Calm Riley down ":
                $ robbrileylv += 10
                " Before RIley could say anything about Oliver, you stopped her. "
                " You told her that she's been talking about Oliver way too much recently... "
                " And that she should probably tone it down a little. "
                " You told her that even Cubbie's looking a bit uncomfortable right now. "
                ri " ...Wait, really? "
                ri " Have I been going overboard...? "
                hide rileyneutral at bottom
                show rileysad at right
                ri " Oh geez, I didn't mean to upset you guys... "
                ri " I guess I've just been too focused on Oliver to notice that you guys felt upset. "
                ri " Maybe this is why Robby was upset at me earlier. "
                ri " (Good job Riley, when can you learn to shut up...?) "
                ri " (Probably never, with how I'm acting...) "
                ri " (I'm too pathetic over Oliver, I swear...) "
                " You told her that it's alright to talk about Oliver. "
                " It's just that you've got to tone it down just a bit. "
                " Sometimes people aren't gonna like what you talk about. "
                " So, if they say that they aren't interested, then... "
                " You should probably just talk about something else. "
                " To prevent making them feel uncomfortable, of course. "
                ri " Hmm... "
                hide rileysad at bottom
                show rileyneutral at right
                ri  " ...Okay!! I'll take your advice, [name]! "
                ri " Thanks for teaching me this stuff! "
                if robbrileylv >= 20 or robbrileylv == 20:
                    " Looks like Riley's thinking about something. "
                    " Let's see what she's thinking about... "
                    ri " (Huh...this is weird.) "
                    ri " (It feels like [name] kinda understands me in a way...) "
                    ri " (Makes me feel all safe and nice...) "
                    ri " (Huh! This feeling is interesting!) "
                    ri " (Maybe I should talk to [them] more...) "
                    ri " Do you have anymore advice for me, actually? "
                    ri " I need to learn from the best, after all! "
                    ri " Come on, come on! Give me more advice! "
                else:
                    ri " Do you have anymore advice for me, actually? "
                    ri " I need to learn from the best, after all! "
                    ri " Come on, come on! Give me more advice! "
                scene black with dissolve
                " You spent the rest of the break talking with Riley. "
                " You were just giving her some advice and more stuff. "
                " You weren't sure if she was actually going to improve, but atleast she said she was gonna try. "
                " Keyword: try. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your final class. "
                pause 2.0
                jump artclassthurs
            " Distract Cubbie from Riley's yapping! ":
                $ cubbielv += 10
                " You nudged Cubbie's shoulder so that you could get his attention. "
                " You wanted to distract him from the rambling that's gonna happen. "
                cb " ...?? "
                " You grabbed your phone from your pocket and gave it to him. "
                " Your phone pretty much has a lot of games in it. "
                " You told him to play any kinds of games in there because you didn't want him to listen to Riley's rambling. "
                " You'll just deal with the nodding and going 'ooh' and 'aah' for the rambling. "
                " You were pretty good at doing that, as far as you've been told. "
                hide cubbieneutral at bottom
                show cubbiehappy at left
                cb " ...!! "
                " Cubbie gives you a thankful smile, and he starts playing a game on his phone. "
                if cubbielv >= 20 or cubbielv == 20:
                    " Looks like Cubbie's thinking about something. "
                    " DOn't worry, I'll let you listen. "
                    cb " (...With [name] around, I feel just a bit safer...) "
                    cb " ([they] [are] always so nice towards me...) "
                    cb " (I don't know why [they] [are] nice, but...I like them. A lot.) "
                    cb " (I wanna talk with them more...) "
                    cb " (Maybe I could even let [them] hear my voice for the first time...?) "
                    cb " (Only when I get more comfortable though...) "
                    " Cubbie seems concentrated on the game he's playing. "
                    " Best to not disturb him, and time to focus on Riley's rambling. "
                    " You have a feeling that this one is going to be a long one... "
                    " Not that you minded. You could just play ping pong in your mind for the entire thing. "
                else:
                    " Cubbie seems concentrated on the game he's playing. "
                    " Best to not disturb him, and time to focus on Riley's rambling. "
                    " You have a feeling that this one is going to be a long one... "
                    " Not that you minded. You could just play ping pong in your mind for the entire thing. "
                scene black with dissolve
                " You spent the rest of the break talking with Riley. "
                " You were just giving her some advice and more stuff. "
                " You weren't sure if she was actually going to improve, but atleast she said she was gonna try. "
                " Keyword: try. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your final class. "
                pause 2.0
                jump artclassthurs
    else:
        x " Cubster! [name]ster! "
        $ cubbieknow = True
        cb " ...? "
        " Huh, you heardof that insane little kid before. "
        $ rileyknow = True
        " You've heard her name was Riley and she liked talking about Oliver. "
        " An extremely obsessed fangirl, in short. "
        " The other guy seems to be a little confused with the nickname she gave him. "
        " You honestly don't mind your nickname. "
        " It was a little unique, and you liked being unique. "
        " Maybe you should give yourself a nickname... "
        " mc[name]coolster. "
        " Banger, right? "
        ri " I've been thinking lately... "
        ri " Maybe I should bring Oliver more stuff! "
        ri " I know that he likes them! "
        ri " Even though he...kind of throws them in the trash. "
        ri " That just means that he appreciates them a lot! "
        ri " Trash can have valuable things in it, after all! "
        ri " Like what they say - one mans treasure is another mans gold... "
        ri " I guess that kind of applies to Oliver??? I don't know what I'm getting at, HEHEHAHAHaaa... "
        cb " ... "
        " Cubbie seems to have the expression of: not this again. "
        " Looks like Riley's been going extra Oliver-mode today. "
        " It's honestly a little bit concerning and you should probably help her "
        " Though, what should you say? "
        " You don't want to accidentally hurt her, after all. "
        " Let's think... "
        menu:
            " Calm Riley down ":
                $ robbrileylv += 10
                " Before RIley could say anything about Oliver, you stopped her. "
                " You told her that she's been talking about Oliver way too much recently... "
                " And that she should probably tone it down a little. "
                " You told her that even Cubbie's looking a bit uncomfortable right now. "
                ri " ...Wait, really? "
                ri " Have I been going overboard...? "
                hide rileyneutral at bottom
                show rileysad at right
                ri " Oh geez, I didn't mean to upset you guys... "
                ri " I guess I've just been too focused on Oliver to notice that you guys felt upset. "
                ri " Maybe this is why Robby was upset at me earlier. "
                ri " (Good job Riley, when can you learn to shut up...?) "
                ri " (Probably never, with how I'm acting...) "
                ri " (I'm too pathetic over Oliver, I swear...) "
                " You told her that it's alright to talk about Oliver. "
                " It's just that you've got to tone it down just a bit. "
                " Sometimes people aren't gonna like what you talk about. "
                " So, if they say that they aren't interested, then... "
                " You should probably just talk about something else. "
                " To prevent making them feel uncomfortable, of course. "
                ri " Hmm... "
                hide rileysad at bottom
                show rileyneutral at right
                ri  " ...Okay!! I'll take your advice, [name]! "
                ri " Thanks for teaching me this stuff! "
                if robbrileylv >= 20 or robbrileylv == 20:
                    " Looks like Riley's thinking about something. "
                    " Let's see what she's thinking about... "
                    ri " (Huh...this is weird.) "
                    ri " (It feels like [name] kinda understands me in a way...) "
                    ri " (Makes me feel all safe and nice...) "
                    ri " (Huh! This feeling is interesting!) "
                    ri " (Maybe I should talk to [them] more...) "
                    ri " Do you have anymore advice for me, actually? "
                    ri " I need to learn from the best, after all! "
                    ri " Come on, come on! Give me more advice! "
                else:
                    ri " Do you have anymore advice for me, actually? "
                    ri " I need to learn from the best, after all! "
                    ri " Come on, come on! Give me more advice! "
                scene black with dissolve
                " You spent the rest of the break talking with Riley. "
                " You were just giving her some advice and more stuff. "
                " You weren't sure if she was actually going to improve, but atleast she said she was gonna try. "
                " Keyword: try. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your final class. "
                pause 2.0
                jump artclassthurs
            " Distract Cubbie from Riley's yapping! ":
                $ cubbielv += 10
                " You nudged Cubbie's shoulder so that you could get his attention. "
                " You wanted to distract him from the rambling that's gonna happen. "
                cb " ...?? "
                " You grabbed your phone from your pocket and gave it to him. "
                " Your phone pretty much has a lot of games in it. "
                " You told him to play any kinds of games in there because you didn't want him to listen to Riley's rambling. "
                " You'll just deal with the nodding and going 'ooh' and 'aah' for the rambling. "
                " You were pretty good at doing that, as far as you've been told. "
                hide cubbieneutral at bottom
                show cubbiehappy at left
                cb " ...!! "
                " Cubbie gives you a thankful smile, and he starts playing a game on his phone. "
                if cubbielv >= 20 or cubbielv == 20:
                    " Looks like Cubbie's thinking about something. "
                    " Don't worry, I'll let you listen. "
                    cb " (...With [name] around, I feel just a bit safer...) "
                    cb " ([they] [are] always so nice towards me...) "
                    cb " (I don't know why [they] [are] nice, but...I like them. A lot.) "
                    cb " (I wanna talk with them more...) "
                    cb " (Maybe I could even let [them] hear my voice for the first time...?) "
                    cb " (Only when I get more comfortable though...) "
                    " Cubbie seems concentrated on the game he's playing. "
                    " Best to not disturb him, and time to focus on Riley's rambling. "
                    " You have a feeling that this one is going to be a long one... "
                    " Not that you minded. You could just play ping pong in your mind for the entire thing. "
                else:
                    " Cubbie seems concentrated on the game he's playing. "
                    " Best to not disturb him, and time to focus on Riley's rambling. "
                    " You have a feeling that this one is going to be a long one... "
                    " Not that you minded. You could just play ping pong in your mind for the entire thing. "
                scene black with dissolve
                " You spent the rest of the break talking with Riley. "
                " You were just giving her some advice and more stuff. "
                " You weren't sure if she was actually going to improve, but atleast she said she was gonna try. "
                " Keyword: try. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You walked out of the gym and went to your final class. "
                pause 2.0
                jump artclassthurs
label thurscafeteria5:
    # skell and lana
    scene black with dissolve
    pause 2.0
    scene cafeteria with dissolve
    " You walked into the cafeteria and spotted two of your classmates doing their own things. "
    " You wanted to talk to one of them...but who do you talk to? "
    if skellknow == True and lanaknow == True:
        menu:
            " {image=skellicon} Skell {image=skellicon} ":
                jump funkadicklexi
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump funkapussi
    elif skellknow == True and lanaknow == False:
        menu:
            " {image=skellicon} Skell {image=skellicon} ":
                jump funkadicklexi
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump funkapussi
    elif skellknow ==  False and lanaknow == True:
        menu:
            " {image=skellicon} An emo guy {image=skellicon} ":
                jump funkadicklexi
            " {image=lanaicon} Lana {image=lanaicon} ":
                jump funkapussi
    else:
        menu:
            " {image=skellicon} An emo guy {image=skellicon} ":
                jump funkadicklexi
            " {image=lanaicon} A girl with sock puppets on her hands {image=lanaicon} ":
                jump funkapussi
    label funkadicklexi:
        show skellneutral at center with easeinleft
        if skellknow == True:
            sk " Hmhmmm... "
            sk " There's a new song for Zatsune Ziku... "
            sk " I should check that out later. "
            sk " I don't have enough data to view that right now... "
            sk " Sighhh... "
            sk " I should've given myself data earlier. "
            sk " Then I could've seen the video early. "
            " You sat next to him and asked him what he was doing. "
            sk " Oh, [name]??? hi there. "
            sk " Was just talking about the new...Zatzune Ziku video. "
            hide skellneutral at bottom
            show skellsad at center
            sk " I know it's embarrassing for me to like something like that, shut uuup... "
            sk " I mean, seeing a guy like Zatsune's content is really rare around here... "
            sk " Could see why you look a little weirded out... "
            " ...You haven't even said anything yet. "
            " He already thinks that you're not gonna like him for liking what he likes. "
            " That's not really true...unless if you don't like Zatsune. "
            " You should probably say something to make him feel better. "
            " Or not, your choice. "
            " What should you say or do? "
            menu:
                " I like Zatsune too dw bro ":
                    $ skelllv += 10
                    hide skellsad at bottom
                    show skellsurprised at center
                    sk " Hold on, really? "
                    sk " I didn't expect you to like her... "
                    hide skellsurprised at bottom
                    show skellneutral at center
                    sk " What's your favorite song from her? "
                    sk " Mine has to be nonmonitoring. "
                    sk " What about you? you have any favorites? "
                    sk " Or do you like any kind of Zatsune song? "
                    if kind == True:
                        " You told him that you liked that one wher she's a magical girl. "
                        sk " Oh, that went really popular at one point. "
                        sk " Like other vocaloid songs, but it's a little bit more iconic than them. "
                        sk " Specifically with that one BEAAAMM line in there. "
                        sk " A good choice, really. "
                    elif calm == True:
                        " You told him that you liked any kind of song from Zatsune. "
                        sk " Ah, cool, cool. "
                        sk " All songs from Zatsune are pretty good in my opinion. "
                        sk " Though there are some weird songs, they somehow make it good... "
                        sk " Doesn't mean that you should like them though. "
                    elif mean == True:
                        " You told him that you liked the creepy ones. "
                        sk " Oooh, cool, cool. "
                        sk " The creepy songs are honestly the one of the ones that hit really hard. "
                        sk " It's got that special charm to them. "
                        sk " While there's others who hate it for how creepy it is, there's some who enjoys it. "
                    else:
                        pass
                    sk " You've got pretty good taste, in my opinion. "
                    sk " It's nice having someone who knows who Zatsune is here in this school... "
                    sk " I feel like I could go on a whole rambling session about her right now. "
                    sk " Like dude...have you noticed her hair keeps getting thicker with each new redesign? "
                    sk " Wonder why they do that... "
                    sk " I mean I get that they want to add more floof, but sometimes... "
                    sk " More floof is a little too much. You get what I'm saying? "
                    if skelllv >= 20 or skelllv == 20:
                        " Looks like Skell is thinking about something. "
                        " Let's see what's in that skull of his. "
                        sk " (...For some reason...[name] keeps talking to me...) "
                        sk " (Not that I mind it, [they] make me feel...seen.) "
                        sk " (In the best way ever...) "
                        sk " (Most people would think that I'm weird for how I act...) "
                        sk " (...But [name]...[they] stayed.) "
                        sk " (No matter what I talked about. No matter what I was doing.) "
                        sk " (...How could they like someone like me...?) "
                        sk " ...Uh, anyway... "
                        sk " I've got a few Zatsune songs on my playlist. "
                        sk " We could go ahead and listen to them... "
                        sk " ...If you want to, of course. "
                        " You had nothing else to do, so you decided to listen to some songs. "
                        sk " Alright, here... you can pick the first song. "
                    else:
                        sk " ...Uh, anyway... "
                        sk " I've got a few Zatsune songs on my playlist. "
                        sk " We could go ahead and listen to them... "
                        sk " ...If you want to, of course. "
                        " You had nothing else to do, so you decided to listen to some songs. "
                        sk " Alright, here... you can pick the first song. "
                    scene black with dissolve
                    " You spent the rest of the break listening to songs in Skell's playlist. "
                    " You even caught him singing to some of them - and his singing skills were pretty good. "
                    " Though everytime you complimented him for his singing, "
                    " He would deny that he even sung in the first place. "
                    " He seems a little embarrassed about singing, huh? "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You got out of the cafeteria and went to your classroom after a bit. "
                    pause 2.0
                    jump artclassthurs
                " Her music's kinda not for me ":
                    hide skellsad at bottom
                    show skellneutral at center
                    sk " Oh, uh... "
                    sk " That's alright if her music isn't your thing. "
                    sk " People have different tastes, after all. "
                    sk " I like what I like, and you like what you like. "
                    sk " Not really gonna force you to listen to the same music as me. "
                    sk " That would be kinda weird, in all honesty. "
                    sk " On another hand, since you're here... "
                    sk " You had something to talk to me about? "
                    " You asked about the whole situation with the popular girls. "
                    sk " Uhhh...Petunia and Lizzy? "
                    sk " Yeah, they argue a lot. "
                    sk " Though they've never really argued that much to the point they insult eachother. "
                    sk " That's what they're doing right now, by the way... "
                    sk " But, they DO get back together as a duo after a good bit, usually a day. "
                    sk " So they should be fine tomorrow. Nothing to worry about, really. "
                    scene black with dissolve
                    " You spent the rest of the break hanging out with Skell. "
                    " Just talking about the situation with the popular girls... "
                    " Even if Skell says that they're gonna be alright, you kinda doubt that. "
                    " But, you're gonna pray that they're gonna be fine. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You got out of the cafeteria and went to your classroom for your final class of the day. "
                    pause 2.0
                    jump artclassthurs
        else:
            x " Hmhmmm... "
            x " There's a new song for Zatsune Ziku... "
            x " I should check that out later. "
            x " I don't have enough data to view that right now... "
            x " Sighhh... "
            x " I should've given myself data earlier. "
            x " Then I could've seen the video early. "
            " You sat next to him and asked him what he was doing. "
            x " Oh, [name]??? hi there. "
            x " Uh, before I asnwer yor question, "
            x " I don't think we've ever met before. "
            x " Either we actually did and I never got to introduce myself... "
            x " ...Or I just completely forgot that I did. "
            x " Either way, I should still probably do the whole introduction thingy.. "
            $ skellknow = True
            sk " I'm Skell. It's nice to meet you. And uh, for your question... "
            sk " Was just talking about the new...Zatzune Ziku video. "
            hide skellneutral at bottom
            show skellsad at center
            sk " I know it's embarrassing for me to like something like that, shut uuup... "
            sk " I mean, seeing a guy like Zatsune's content is really rare around here... "
            sk " Could see why you look a little weirded out... "
            " ...You haven't even said anything yet. "
            " He already thinks that you're not gonna like him for liking what he likes. "
            " That's not really true...unless if you don't like Zatsune. "
            " You should probably say something to make him feel better. "
            " Or not, your choice. "
            " What should you say or do? "
            menu:
                " I like Zatsune too dw bro ":
                    $ skelllv += 10
                    hide skellsad at bottom
                    show skellsurprised at center
                    sk " Hold on, really? "
                    sk " I didn't expect you to like her... "
                    hide skellsurprised at bottom
                    show skellneutral at center
                    sk " What's your favorite song from her? "
                    sk " Mine has to be nonmonitoring. "
                    sk " What about you? you have any favorites? "
                    sk " Or do you like any kind of Zatsune song? "
                    if kind == True:
                        " You told him that you liked that one wher she's a magical girl. "
                        sk " Oh, that went really popular at one point. "
                        sk " Like other vocaloid songs, but it's a little bit more iconic than them. "
                        sk " Specifically with that one BEAAAMM line in there. "
                        sk " A good choice, really. "
                    elif calm == True:
                        " You told him that you liked any kind of song from Zatsune. "
                        sk " Ah, cool, cool. "
                        sk " All songs from Zatsune are pretty good in my opinion. "
                        sk " Though there are some weird songs, they somehow make it good... "
                        sk " Doesn't mean that you should like them though. "
                    elif mean == True:
                        " You told him that you liked the creepy ones. "
                        sk " Oooh, cool, cool. "
                        sk " The creepy songs are honestly the one of the ones that hit really hard. "
                        sk " It's got that special charm to them. "
                        sk " While there's others who hate it for how creepy it is, there's some who enjoys it. "
                    else:
                        pass
                    sk " You've got pretty good taste, in my opinion. "
                    sk " It's nice having someone who knows who Zatsune is here in this school... "
                    sk " I feel like I could go on a whole rambling session about her right now. "
                    sk " Like dude...have you noticed her hair keeps getting thicker with each new redesign? "
                    sk " Wonder why they do that... "
                    sk " I mean I get that they want to add more floof, but sometimes... "
                    sk " More floof is a little too much. You get what I'm saying? "
                    if skelllv >= 20 or skelllv == 20:
                        " Looks like Skell is thinking about something. "
                        " Let's see what's in that skull of his. "
                        sk " (...For some reason...[name] keeps talking to me...) "
                        sk " (Not that I mind it, [they] make me feel...seen.) "
                        sk " (In the best way ever...) "
                        sk " (Most people would think that I'm weird for how I act...) "
                        sk " (...But [name]...[they] stayed.) "
                        sk " (No matter what I talked about. No matter what I was doing.) "
                        sk " (...How could they like someone like me...?) "
                        sk " ...Uh, anyway... "
                        sk " I've got a few Zatsune songs on my playlist. "
                        sk " We could go ahead and listen to them... "
                        sk " ...If you want to, of course. "
                        " You had nothing else to do, so you decided to listen to some songs. "
                        sk " Alright, here... you can pick the first song. "
                    else:
                        sk " ...Uh, anyway... "
                        sk " I've got a few Zatsune songs on my playlist. "
                        sk " We could go ahead and listen to them... "
                        sk " ...If you want to, of course. "
                        " You had nothing else to do, so you decided to listen to some songs. "
                        sk " Alright, here... you can pick the first song. "
                    scene black with dissolve
                    " You spent the rest of the break listening to songs in Skell's playlist. "
                    " You even caught him singing to some of them - and his singing skills were pretty good. "
                    " Though everytime you complimented him for his singing, "
                    " He would deny that he even sung in the first place. "
                    " He seems a little embarrassed about singing, huh? "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for your next class. "
                    " You got out of the cafeteria and went to your classroom after a bit. "
                    pause 2.0
                    jump artclassthurs
                " Her music's kinda not for me ":
                    hide skellsad at bottom
                    show skellneutral at center
                    sk " Oh, uh... "
                    sk " That's alright if her music isn't your thing. "
                    sk " People have different tastes, after all. "
                    sk " I like what I like, and you like what you like. "
                    sk " Not really gonna force you to listen to the same music as me. "
                    sk " That would be kinda weird, in all honesty. "
                    sk " On another hand, since you're here... "
                    sk " You had something to talk to me about? "
                    " You asked about the whole situation with the popular girls. "
                    sk " Uhhh...Petunia and Lizzy? "
                    sk " Yeah, they argue a lot. "
                    sk " Though they've never really argued that much to the point they insult eachother. "
                    sk " That's what they're doing right now, by the way... "
                    sk " But, they DO get back together as a duo after a good bit, usually a day. "
                    sk " So they should be fine tomorrow. Nothing to worry about, really. "
                    scene black with dissolve
                    " You spent the rest of the break hanging out with Skell. "
                    " Just talking about the situation with the popular girls... "
                    " Even if Skell says that they're gonna be alright, you kinda doubt that. "
                    " But, you're gonna pray that they're gonna be fine. "
                    play sound "audio/bellring.mp3"
                    " The bell rings after a bit, looks like it's time for another class. "
                    " You got out of the cafeteria and went to your classroom for your final class of the day. "
                    pause 2.0
                    jump artclassthurs
    label funkapussi:
        show lananeutral at center with easeinright
        if lanaknow == True:
            l " Hheeeyy there, [name]! "
            l " You know, about that thing Petunia and Lizzy are having right now... "
            l " Their beef - I heard from a little birdie... "
            l " That Lizzy's planning to apologize after school ends! "
            l " That's great, isn't it? "
            l " But then again, the apology could still go horrible... "
            l " We can only hope for the best for them! "
            l " Right...? "
            " Lana stays silent for a bit. "
            " She looks as if she doesn't know what to say... "
            " If we were in a cartoon movie right now, you could see her sweating bullets. "
            " Too bad we don't have enough budget for that. "
            " Lana coughs and after a bit, she speaks up again. "
            if lanalv >= 15 or lanalv == 15:
                " This time, she looks sadder. "
                " Huh...she was so happy just a moment ago. "
                " You wonder what happened. "
                l " [name]...I know we haven't known eachother for too long... "
                l " But sometimes, I feel like I'm too energetic, you know? "
                l " I feel like sometimes people just can't put up with my energy. "
                l " I always try to make the worse things look better. "
                l " Someone getting a low grade? I tell them that it'll get better. "
                l " It's a good thing, but there's always this nagging feeling that I shouldn't have said certain things... "
                l " Maybe they didn't need the reassurance and I'm making myself look like a fool. "
                l " ...I don't exactly know what I'm getting at right now, this is really stupid, heheh... "
                l " Probably annoying you right at this moment... "
                l " I know Abbie somehow can tolerate me - but what about you? "
                l " What about everyone else? "
                l " What if they're just pretending that I enjoy their company? "
                l " I've loved the times you've tuned into my shows, but... "
                l " Were you even listening when I acted them out? "
                l " Or were you just zoning out? "
                l " Can you tell me what you really think of me? "
                l " Am I annoying you too much whenever I talk to you? "
                l " ...I just need you to tell me something so that I can improve. "
                l " I don't want to be a chatterbox that everyone hates. "
                menu:
                    " You're perfect the way you are ":
                        $ lanalv += 10
                        l " Really...? "
                        l " You don't feel annoyed? "
                        l " And are you sure that I don't need changing...? "
                        l " ...Maybe I am. Maybe I am perfect the way I am. "
                        l " Sorry if I ruined the mood, [name]. "
                        l " I just needed to get a few thoughts out. "
                        l " Thanks for listening though. "
                        l " It was nice finally voicing out my thoughts for once... "
                        l " It's usually a little hard for me to open up like this... "
                        l " Especially if it's something about my emotions... "
                        l " But, still... "
                        hide lanasad at bottom
                        show lananeutral at center
                        l " I'm glad you listened. "
                        l " Thank you. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Lana. "
                        " You didn't know Lana was suffering like thoughts like those... "
                        " It breaks your heart that she thinks like that. "
                        " In your opinion, she's fine the way she is. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the cafeteria and then went to your classroom. "
                        pause 2.0
                        jump artclassthurs
                    " You're okay ":
                        $ lanalv += 5
                        l " You really sure I don't need any changing...? "
                        l " ...Maybe I am. Maybe I am okay. "
                        l " Sorry if I ruined the mood, [name]. "
                        l " I just needed to get a few thoughts out. "
                        l " Thanks for listening though. "
                        l " It was nice finally voicing out my thoughts for once... "
                        l " It's usually a little hard for me to open up like this... "
                        l " Especially if it's something about my emotions... "
                        l " But, still... "
                        hide lanasad at bottom
                        show lananeutral at center
                        l " I'm glad you listened. "
                        l " Thank you. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Lana. "
                        " You didn't know Lana was suffering like thoughts like those... "
                        " It breaks your heart that she thinks like that. "
                        " In your opinion, she's fine the way she is. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the cafeteria and then went to your classroom. "
                        pause 2.0
                        jump artclassthurs
            else:
                l " Errhhh... "
                l " Now that I think about it, I gotta go! "
                l " Sorry [name], haha... "
                l " Looks like Abbie's calling me for help with his uh... "
                l " Math assignment, yeah! "
                l " SEE YOU LATER IN CLASS!!! "
                hide lananeutral at right with easeoutright
                " ...And she leaves. "
                " You knew damn well there was no math assignment. "
                " And you also knew that Lana wasn't smart enough to do something like math. "
                " Something's off, but you don't wanna push her into telling you what's going on with her. "
                " Boundaries are boundaries, after all. "
                " You spent the rest of the break hanging out with Skell. "
                " Just talking about the situation with the popular girls... "
                " Even if Skell says that they're gonna be alright, you kinda doubt that. "
                " But, you're gonna pray that they're gonna be fine. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You got out of the cafeteria and went to your classroom for your final class of the day. "
                pause 2.0
                jump artclassthurs
        else:
            x " Hheeeyy there, [name]! "
            x " Oh, oh!! wait, I don't think we've met before! "
            x " So sorry that I didn't introduce mysaelf to you earlier, hhh... "
            x " Enough of the talking though! LETS GET INTRODUCING!! "
            $ lanaknow = True
            l " I'm Lana! one of your classmates! "
            l " I know that we're gonna be the greatest friends ever! "
            l " But being a great friend means that we should talk about something interesting! "
            l " Like, erh... "
            l " You know, about that thing Petunia and Lizzy are having right now... "
            l " Their beef - I heard from a little birdie... "
            l " That Lizzy's planning to apologize after school ends! "
            l " That's great, isn't it? "
            l " But then again, the apology could still go horrible... "
            l " We can only hope for the best for them! "
            l " Right...? "
            " Lana stays silent for a bit. "
            " She looks as if she doesn't know what to say... "
            " If we were in a cartoon movie right now, you could see her sweating bullets. "
            " Too bad we don't have enough budget for that. "
            " Lana coughs and after a bit, she speaks up again. "
            if lanalv >= 15 or lanalv == 15:
                " This time, she looks sadder. "
                " Huh...she was so happy just a moment ago. "
                " You wonder what happened. "
                l " [name]...I know we haven't known eachother for too long... "
                l " But sometimes, I feel like I'm too energetic, you know? "
                l " I feel like sometimes people just can't put up with my energy. "
                l " I always try to make the worse things look better. "
                l " Someone getting a low grade? I tell them that it'll get better. "
                l " It's a good thing, but there's always this nagging feeling that I shouldn't have said certain things... "
                l " Maybe they didn't need the reassurance and I'm making myself look like a fool. "
                l " ...I don't exactly know what I'm getting at right now, this is really stupid, heheh... "
                l " Probably annoying you right at this moment... "
                l " I know Abbie somehow can tolerate me - but what about you? "
                l " What about everyone else? "
                l " What if they're just pretending that I enjoy their company? "
                l " I've loved the times you've tuned into my shows, but... "
                l " Were you even listening when I acted them out? "
                l " Or were you just zoning out? "
                l " Can you tell me what you really think of me? "
                l " Am I annoying you too much whenever I talk to you? "
                l " ...I just need you to tell me something so that I can improve. "
                l " I don't want to be a chatterbox that everyone hates. "
                menu:
                    " You're perfect the way you are ":
                        $ lanalv += 10
                        l " Really...? "
                        l " You don't feel annoyed? "
                        l " And are you sure that I don't need changing...? "
                        l " ...Maybe I am. Maybe I am perfect the way I am. "
                        l " Sorry if I ruined the mood, [name]. "
                        l " I just needed to get a few thoughts out. "
                        l " Thanks for listening though. "
                        l " It was nice finally voicing out my thoughts for once... "
                        l " It's usually a little hard for me to open up like this... "
                        l " Especially if it's something about my emotions... "
                        l " But, still... "
                        hide lanasad at bottom
                        show lananeutral at center
                        l " I'm glad you listened. "
                        l " Thank you. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Lana. "
                        " You didn't know Lana was suffering like thoughts like those... "
                        " It breaks your heart that she thinks like that. "
                        " In your opinion, she's fine the way she is. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the cafeteria and then went to your classroom. "
                        pause 2.0
                        jump artclassthurs
                    " You're okay ":
                        $ lanalv += 5
                        l " You really sure I don't need any changing...? "
                        l " ...Maybe I am. Maybe I am okay. "
                        l " Sorry if I ruined the mood, [name]. "
                        l " I just needed to get a few thoughts out. "
                        l " Thanks for listening though. "
                        l " It was nice finally voicing out my thoughts for once... "
                        l " It's usually a little hard for me to open up like this... "
                        l " Especially if it's something about my emotions... "
                        l " But, still... "
                        hide lanasad at bottom
                        show lananeutral at center
                        l " I'm glad you listened. "
                        l " Thank you. "
                        scene black with dissolve
                        " You spent the rest of the break talking with Lana. "
                        " You didn't know Lana was suffering like thoughts like those... "
                        " It breaks your heart that she thinks like that. "
                        " In your opinion, she's fine the way she is. "
                        play sound "audio/bellring.mp3"
                        " The bell rings after a bit, looks like it's time for another class. "
                        " You walked out of the cafeteria and then went to your classroom. "
                        pause 2.0
                        jump artclassthurs
            else:
                l " Errhhh... "
                l " Now that I think about it, I gotta go! "
                l " Sorry [name], haha... "
                l " Looks like Abbie's calling me for help with his uh... "
                l " Math assignment, yeah! "
                l " SEE YOU LATER IN CLASS!!! "
                hide lananeutral at right with easeoutright
                " ...And she leaves. "
                " You knew damn well there was no math assignment. "
                " And you also knew that Lana wasn't smart enough to do something like math. "
                " Something's off, but you don't wanna push her into telling you what's going on with her. "
                " Boundaries are boundaries, after all. "
                " You spent the rest of the break hanging out with Skell. "
                " Just talking about the situation with the popular girls... "
                " Even if Skell says that they're gonna be alright, you kinda doubt that. "
                " But, you're gonna pray that they're gonna be fine. "
                play sound "audio/bellring.mp3"
                " The bell rings after a bit, looks like it's time for another class. "
                " You got out of the cafeteria and went to your classroom for your final class of the day. "
                pause 2.0
                jump artclassthurs
label thursrooftop5:
    # bubble and kevin
    $ bubblelv += 10
    $ kevinlv += 10
    scene black with dissolve
    pause 2.0
    scene rooftop with dissolve
    " You walked to the rooftop and found two of your classmates talking with eachother. "
    " Wondering what they're talking about, you decided to walk over to them. "
    show bubbleneutral at right with easeinleft
    show kevinneutral at left with easeinleft
    if bubbleknow == True and kevinknow == True:
        b " I'm sorry, you what? "
        " You greeted the both of them and asked them what they were doing. "
        kv " Bubble - [name]'s here. "
        b " Oh hey, [name]! "
        b " I'm just talking to Kevin over here... "
        b " ...About his very interesting theories. "
        hide bubbleneutral at bottom
        show bubbleconfused at right
        b " Anyway - Kevin, how did you end up on the thought that she killed everyone? "
        " You have absolutely no idea what they're talking about, but you're all in for it. "
        kv " I mean, think about it... "
        kv " Think about all of the evidences that were left behind! "
        kv " You can't tell me that it isn't her. "
        kv " Besides - she gives the MC this weird look at the end of episode 108! "
        b " Weird...? now that I think about it... "
        kv " And also, one of the evidences was LITERALLY a strand of pink hair. "
        kv " And who else has pink hair? ZIMI. "
        " Hold on, that name sounds familiar... "
        " Not sure where you've heard it before though. "
        b " Huh...but there was this other character with pink hair though! "
        b " How do you know that it's her? "
        kv " Well, she probably knew that they were going to figure everything out with that single piece of hair. "
        kv " And you know how that other character has the EXACT same hair color as her? "
        kv " It would be a little hard to distinguish who is who's... "
        kv " But, with a little bit of good acting then she could put the blame on that girl! "
        kv " That's the reason why they arrested that girl instead of her! "
        kv " And also, she even has her face as her icon in a future episode... "
        kv " Don't tell me that's NOT the smell of a theory being true. "
        kv " You finally see where I'm getting at? "
        b " Actually, yeah... "
        hide bubbleconfused at bottom
        show bubbleamazed at right
        b " Everything makes sense now! "
        b " No way you figured all this on your own, Kevin... "
        b " How'd you do it? "
        hide kevinneutral at bottom
        show kevinhappy at left
        kv " Let's just say I was paying close attention to the details. "
        kv " Can't be a die hard fan if I'm not pushing out theories! "
        scene black with dissolve
        " You spent the rest of the break talking with Bubble and Kevin. "
        " Knowing absolutely nothing about what they were talking about - you just nodded every now and then. "
        " The thing they were talking about was interesting though... "
        " Some sort of murder mystery? very interesting. "
        " You've gotta ask them what kind of peak they're looking at. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You went down from the rooftop and then went to your classroom. "
        pause 2.0
        jump artclassthurs
    elif bubbleknow == True and kevinknow == False:
        b " I'm sorry, you what? "
        " You greeted the both of them and asked them what they were doing. "
        x " Bubble - [name]'s here. "
        b " Oh hey, [name]! "
        $ kevinknow = True
        b " I'm just talking to Kevin over here... "
        b " ...About his very interesting theories. "
        hide bubbleneutral at bottom
        show bubbleconfused at right
        b " Anyway - Kevin, how did you end up on the thought that she killed everyone? "
        " You have absolutely no idea what they're talking about, but you're all in for it. "
        kv " I mean, think about it... "
        kv " Think about all of the evidences that were left behind! "
        kv " You can't tell me that it isn't her. "
        kv " Besides - she gives the MC this weird look at the end of episode 108! "
        b " Weird...? now that I think about it... "
        kv " And also, one of the evidences was LITERALLY a strand of pink hair. "
        kv " And who else has pink hair? ZIMI. "
        " Hold on, that name sounds familiar... "
        " Not sure where you've heard it before though. "
        b " Huh...but there was this other character with pink hair though! "
        b " How do you know that it's her? "
        kv " Well, she probably knew that they were going to figure everything out with that single piece of hair. "
        kv " And you know how that other character has the EXACT same hair color as her? "
        kv " It would be a little hard to distinguish who is who's... "
        kv " But, with a little bit of good acting then she could put the blame on that girl! "
        kv " That's the reason why they arrested that girl instead of her! "
        kv " And also, she even has her face as her icon in a future episode... "
        kv " Don't tell me that's NOT the smell of a theory being true. "
        kv " You finally see where I'm getting at? "
        b " Actually, yeah... "
        hide bubbleconfused at bottom
        show bubbleamazed at right
        b " Everything makes sense now! "
        b " No way you figured all this on your own, Kevin... "
        b " How'd you do it? "
        hide kevinneutral at bottom
        show kevinhappy at left
        kv " Let's just say I was paying close attention to the details. "
        kv " Can't be a die hard fan if I'm not pushing out theories! "
        scene black with dissolve
        " You spent the rest of the break talking with Bubble and Kevin. "
        " Knowing absolutely nothing about what they were talking about - you just nodded every now and then. "
        " The thing they were talking about was interesting though... "
        " Some sort of murder mystery? very interesting. "
        " You've gotta ask them what kind of peak they're looking at. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You went down from the rooftop and then went to your classroom. "
        pause 2.0
        jump artclassthurs
    elif bubbleknow == False and kevinknow == True:
        x " I'm sorry, you what? "
        " You greeted the both of them and asked them what they were doing. "
        $ bubbleknow = True
        kv " Bubble - [name]'s here. "
        b " Oh hey, [name]! "
        b " I'm just talking to Kevin over here... "
        b " ...About his very interesting theories. "
        hide bubbleneutral at bottom
        show bubbleconfused at right
        b " Anyway - Kevin, how did you end up on the thought that she killed everyone? "
        " You have absolutely no idea what they're talking about, but you're all in for it. "
        kv " I mean, think about it... "
        kv " Think about all of the evidences that were left behind! "
        kv " You can't tell me that it isn't her. "
        kv " Besides - she gives the MC this weird look at the end of episode 108! "
        b " Weird...? now that I think about it... "
        kv " And also, one of the evidences was LITERALLY a strand of pink hair. "
        kv " And who else has pink hair? ZIMI. "
        " Hold on, that name sounds familiar... "
        " Not sure where you've heard it before though. "
        b " Huh...but there was this other character with pink hair though! "
        b " How do you know that it's her? "
        kv " Well, she probably knew that they were going to figure everything out with that single piece of hair. "
        kv " And you know how that other character has the EXACT same hair color as her? "
        kv " It would be a little hard to distinguish who is who's... "
        kv " But, with a little bit of good acting then she could put the blame on that girl! "
        kv " That's the reason why they arrested that girl instead of her! "
        kv " And also, she even has her face as her icon in a future episode... "
        kv " Don't tell me that's NOT the smell of a theory being true. "
        kv " You finally see where I'm getting at? "
        b " Actually, yeah... "
        hide bubbleconfused at bottom
        show bubbleamazed at right
        b " Everything makes sense now! "
        b " No way you figured all this on your own, Kevin... "
        b " How'd you do it? "
        hide kevinneutral at bottom
        show kevinhappy at left
        kv " Let's just say I was paying close attention to the details. "
        kv " Can't be a die hard fan if I'm not pushing out theories! "
        scene black with dissolve
        " You spent the rest of the break talking with Bubble and Kevin. "
        " Knowing absolutely nothing about what they were talking about - you just nodded every now and then. "
        " The thing they were talking about was interesting though... "
        " Some sort of murder mystery? very interesting. "
        " You've gotta ask them what kind of peak they're looking at. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You went down from the rooftop and then went to your classroom. "
        pause 2.0
        jump artclassthurs
    else:
        x " I'm sorry, you what? "
        " You greeted the both of them and asked them what they were doing. "
        x " Bubble - [name]'s here. "
        $ bubbleknow = True
        $ kevinlv = True
        b " Oh hey, [name]! "
        b " I'm just talking to Kevin over here... "
        b " ...About his very interesting theories. "
        hide bubbleneutral at bottom
        show bubbleconfused at right
        b " Anyway - Kevin, how did you end up on the thought that she killed everyone? "
        " You have absolutely no idea what they're talking about, but you're all in for it. "
        kv " I mean, think about it... "
        kv " Think about all of the evidences that were left behind! "
        kv " You can't tell me that it isn't her. "
        kv " Besides - she gives the MC this weird look at the end of episode 108! "
        b " Weird...? now that I think about it... "
        kv " And also, one of the evidences was LITERALLY a strand of pink hair. "
        kv " And who else has pink hair? ZIMI. "
        " Hold on, that name sounds familiar... "
        " Not sure where you've heard it before though. "
        b " Huh...but there was this other character with pink hair though! "
        b " How do you know that it's her? "
        kv " Well, she probably knew that they were going to figure everything out with that single piece of hair. "
        kv " And you know how that other character has the EXACT same hair color as her? "
        kv " It would be a little hard to distinguish who is who's... "
        kv " But, with a little bit of good acting then she could put the blame on that girl! "
        kv " That's the reason why they arrested that girl instead of her! "
        kv " And also, she even has her face as her icon in a future episode... "
        kv " Don't tell me that's NOT the smell of a theory being true. "
        kv " You finally see where I'm getting at? "
        b " Actually, yeah... "
        hide bubbleconfused at bottom
        show bubbleamazed at right
        b " Everything makes sense now! "
        b " No way you figured all this on your own, Kevin... "
        b " How'd you do it? "
        hide kevinneutral at bottom
        show kevinhappy at left
        kv " Let's just say I was paying close attention to the details. "
        kv " Can't be a die hard fan if I'm not pushing out theories! "
        scene black with dissolve
        " You spent the rest of the break talking with Bubble and Kevin. "
        " Knowing absolutely nothing about what they were talking about - you just nodded every now and then. "
        " The thing they were talking about was interesting though... "
        " Some sort of murder mystery? very interesting. "
        " You've gotta ask them what kind of peak they're looking at. "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for another class. "
        " You went down from the rooftop and then went to your classroom. "
        pause 2.0
        jump artclassthurs
label thurslibrary5:
    $ rubylv += 5
    $ robbrileylv += 5
    # ruby and robby
    scene black with dissolve
    pause 2.0
    scene library with dissolve
    " You walked to the library and spotted two of your classmates talking with eachother. "
    " Wondering what they're talking about, you decided to join their conversation. "
    show rubyneutral at right with easeinleft
    show robbyneutral at left with easeinleft
    if rubyknow == True and robbyknow == True:
        " Oh hey, looks like they're talking about something important. "
        " I'll give you some free points for listening in, don't worry. "
        ru " You think you can handle talking to Riley again? "
        rb " Probably not for the time being, no... "
        rb " Would be good if she sent me an apology later. "
        rb " But I don't think she can even manage to to an apology if she thinks about Oliver so much. "
        rb " Oliver's practically the only thing she thinks about day and night. "
        rb " I wouldn't be surprised if she would accidentally call me Oliver at one point. "
        rb " Geez... atleast I'm getting a break from her. "
        ru " Robby...I know things are gonna get better. "
        ru " Besides, Skell talked to her earlier and she told me that she's going to send you an apology! "
        ru " I'm sure everything's going to be fine after that. "
        rb " ...She's actually sending me an apology? "
        rb " That's real surprising. "
        rb " Skell probably just bribed her with Oliver pictures just to get her attention. "
        rb " I'm sure it's just going to be an insincere apology... "
        hide rubyneutral at bottom
        show rubysad at right
        ru " Oh, Robby... "
        ru " I made sure Skell wouldn't bait her with things like that! "
        ru " He knows better than to do that, I promise. "
        ru " You wanna talk about something else to cheer you up? "
        rb " I guess. "
        rb " Better than talking about Oliver. "
        rb " I don't think I ever wanna hear that name again, honestly... "
        rb " Let's just talk about something else, please? "
        hide rubysad at bottom
        show rubyhappy at right
        ru " Okay! "
        ru " I'll generate a conversation based off of our interests, then! "
        ru " I'm sure you're going to feel better afterwards! "
        hide robbyneutral at bottom
        show robbyhappy at left
        rb " Hah...thanks, Ruby. "
        rb " You always know how to make me feel better. "
        rb " Even through the darkest of times. "
        ru " It's my duty as a friend to make you smile! "
        ru " A frown on your face doesn't suit you! "
        rb " Oh, shut up. "
        scene black with dissolve
        " After listening into their conversation, you decided to walk around the school for a bit. "
        " Huh...seems like one of them had a disagreement with someone. "
        " Not at Oliver specifically, but at someone else who keeps talking about him. "
        " You really do wonder who it could be... "
        " It's totally not so obvious... "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your final class of the day. "
        " You continued walking around for a bit before going to your classroom. "
        pause 2.0
        jump artclassthurs
    elif rubyknow == True and robbyknow == False:
        " Oh hey, looks like they're talking about something important. "
        " I'll give you some free points for listening in, don't worry. "
        ru " You think you can handle talking to Riley again? "
        x " Probably not for the time being, no... "
        x " Would be good if she sent me an apology later. "
        x " But I don't think she can even manage to to an apology if she thinks about Oliver so much. "
        x " Oliver's practically the only thing she thinks about day and night. "
        x " I wouldn't be surprised if she would accidentally call me Oliver at one point. "
        x " Geez... atleast I'm getting a break from her. "
        $ robbyknow = True
        ru " Robby...I know things are gonna get better. "
        ru " Besides, Skell talked to her earlier and she told me that she's going to send you an apology! "
        ru " I'm sure everything's going to be fine after that. "
        rb " ...She's actually sending me an apology? "
        rb " That's real surprising. "
        rb " Skell probably just bribed her with Oliver pictures just to get her attention. "
        rb " I'm sure it's just going to be an insincere apology... "
        hide rubyneutral at bottom
        show rubysad at right
        ru " Oh, Robby... "
        ru " I made sure Skell wouldn't bait her with things like that! "
        ru " He knows better than to do that, I promise. "
        ru " You wanna talk about something else to cheer you up? "
        rb " I guess. "
        rb " Better than talking about Oliver. "
        rb " I don't think I ever wanna hear that name again, honestly... "
        rb " Let's just talk about something else, please? "
        hide rubysad at bottom
        show rubyhappy at right
        ru " Okay! "
        ru " I'll generate a conversation based off of our interests, then! "
        ru " I'm sure you're going to feel better afterwards! "
        hide robbyneutral at bottom
        show robbyhappy at left
        rb " Hah...thanks, Ruby. "
        rb " You always know how to make me feel better. "
        rb " Even through the darkest of times. "
        ru " It's my duty as a friend to make you smile! "
        ru " A frown on your face doesn't suit you! "
        rb " Oh, shut up. "
        scene black with dissolve
        " After listening into their conversation, you decided to walk around the school for a bit. "
        " Huh...seems like one of them had a disagreement with someone. "
        " Not at Oliver specifically, but at someone else who keeps talking about him. "
        " You really do wonder who it could be... "
        " It's totally not so obvious... "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your final class of the day. "
        " You continued walking around for a bit before going to your classroom. "
        pause 2.0
        jump artclassthurs
    elif rubyknow == False and robbyknow == True:
        " Oh hey, looks like they're talking about something important. "
        " I'll give you some free points for listening in, don't worry. "
        x " You think you can handle talking to Riley again? "
        rb " Probably not for the time being, no... "
        rb " Would be good if she sent me an apology later. "
        rb " But I don't think she can even manage to to an apology if she thinks about Oliver so much. "
        rb " Oliver's practically the only thing she thinks about day and night. "
        rb " I wouldn't be surprised if she would accidentally call me Oliver at one point. "
        rb " Geez... atleast I'm getting a break from her. "
        x " Robby...I know things are gonna get better. "
        x " Besides, Skell talked to her earlier and she told me that she's going to send you an apology! "
        x " I'm sure everything's going to be fine after that. "
        rb " ...She's actually sending me an apology? "
        rb " That's real surprising. "
        rb " Skell probably just bribed her with Oliver pictures just to get her attention. "
        rb " I'm sure it's just going to be an insincere apology... "
        hide rubyneutral at bottom
        show rubysad at right
        x " Oh, Robby... "
        x " I made sure Skell wouldn't bait her with things like that! "
        x " He knows better than to do that, I promise. "
        x " You wanna talk about something else to cheer you up? "
        rb " I guess. "
        rb " Better than talking about Oliver. "
        rb " I don't think I ever wanna hear that name again, honestly... "
        rb " Let's just talk about something else, please? "
        hide rubysad at bottom
        show rubyhappy at right
        x " Okay! "
        x " I'll generate a conversation based off of our interests, then! "
        x " I'm sure you're going to feel better afterwards! "
        hide robbyneutral at bottom
        show robbyhappy at left
        $ rubyknow = True
        rb " Hah...thanks, Ruby. "
        rb " You always know how to make me feel better. "
        rb " Even through the darkest of times. "
        ru " It's my duty as a friend to make you smile! "
        ru " A frown on your face doesn't suit you! "
        rb " Oh, shut up. "
        scene black with dissolve
        " After listening into their conversation, you decided to walk around the school for a bit. "
        " Huh...seems like one of them had a disagreement with someone. "
        " Not at Oliver specifically, but at someone else who keeps talking about him. "
        " You really do wonder who it could be... "
        " It's totally not so obvious... "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your final class of the day. "
        " You continued walking around for a bit before going to your classroom. "
        pause 2.0
        jump artclassthurs
    else:
        " Oh hey, looks like they're talking about something important. "
        " I'll give you some free points for listening in, don't worry. "
        x " You think you can handle talking to Riley again? "
        x " Probably not for the time being, no... "
        x " Would be good if she sent me an apology later. "
        x " But I don't think she can even manage to to an apology if she thinks about Oliver so much. "
        x " Oliver's practically the only thing she thinks about day and night. "
        x " I wouldn't be surprised if she would accidentally call me Oliver at one point. "
        x " Geez... atleast I'm getting a break from her. "
        $ robbyknow = True
        x " Robby...I know things are gonna get better. "
        x " Besides, Skell talked to her earlier and she told me that she's going to send you an apology! "
        x " I'm sure everything's going to be fine after that. "
        rb " ...She's actually sending me an apology? "
        rb " That's real surprising. "
        rb " Skell probably just bribed her with Oliver pictures just to get her attention. "
        rb " I'm sure it's just going to be an insincere apology... "
        hide rubyneutral at bottom
        show rubysad at right
        x " Oh, Robby... "
        x " I made sure Skell wouldn't bait her with things like that! "
        x " He knows better than to do that, I promise. "
        x " You wanna talk about something else to cheer you up? "
        rb " I guess. "
        rb " Better than talking about Oliver. "
        rb " I don't think I ever wanna hear that name again, honestly... "
        rb " Let's just talk about something else, please? "
        hide rubysad at bottom
        show rubyhappy at right
        x " Okay! "
        x " I'll generate a conversation based off of our interests, then! "
        x " I'm sure you're going to feel better afterwards! "
        hide robbyneutral at bottom
        show robbyhappy at left
        $ rubyknow = True
        rb " Hah...thanks, Ruby. "
        rb " You always know how to make me feel better. "
        rb " Even through the darkest of times. "
        ru " It's my duty as a friend to make you smile! "
        ru " A frown on your face doesn't suit you! "
        rb " Oh, shut up. "
        scene black with dissolve
        " After listening into their conversation, you decided to walk around the school for a bit. "
        " Huh...seems like one of them had a disagreement with someone. "
        " Not at Oliver specifically, but at someone else who keeps talking about him. "
        " You really do wonder who it could be... "
        " It's totally not so obvious... "
        play sound "audio/bellring.mp3"
        " The bell rings after a bit, looks like it's time for your final class of the day. "
        " You continued walking around for a bit before going to your classroom. "
        pause 2.0
        jump artclassthurs
label thursoligang5:
    # oliver and edward
    scene black with dissolve
    pause 2.0
    scene oligangclub with dissolve
    " You walked into the room and spotted Edward hanging out with Oliver. "
    " Wait, nah. Oliver looks a little bit pissed off. "
    " Huh, wonder what happened here. "
    " You haven't seen Oliver be mad at one of his goons... "
    " Interesting. Let's go see what's up. "
    show oliverangry at left with easeinright
    show edwardangry at right with easeinright
    o " I told you not to use the soap from my bag, Ed. "
    ed " Where else was I supposed t' look?! "
    ed " You just told me to look for a bar of soap! "
    ed " No direction whatsoever! "
    ed " If ya didn't want me touching yer bag soap, then ya could've told me so! "
    ed " Then I wouldn't have checked your bag in the first place! "
    o " Ergh...I know I should've given you instructions. "
    o " I guess I can forgive you for now. "
    o " You've gotta bring me a shit ton of soap tomorrow though. "
    ed " WHAT?! come on! "
    ed " Ya know I can't afford a shit ton of soap! "
    ed " What am I, made of money?! "
    hide oliverangry at bottom
    show oliverhappy at left
    o " No, you're made off of human skin, idiot. "
    ed " THAT'S WHAT - "
    ed " Ergh... "
    ed " For gods sake, Oliver. Sometimes I can't understand ya. "
    o " Heheh. "
    o " I was just messing with ya on the whole soap thing, though. "
    o " I know you can't afford allat. "
    o " Though, you could give me one dollar. "
    hide edwardangry at bottom
    show edwardconfused at right
    ed " ...What are ya gunna do with a dollar? "
    o " Things, Edward. Things. "
    o " A whole lot of things. "
    scene black with dissolve
    " You spent the rest of the break just chilling in the room. "
    " You looked at Oliver and Edward every now and then, before looking back at your phone. "
    " Now that you think about it... "
    " You kinda just now realized how tall Oliver was. "
    " Maybe it would be worse if you compared him to Zip. "
    " Yeah, no. A lot worse. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, looks like it's time for your next class. "
    " You waited for about 5 minutes before going to your classroom. "
    pause 2.0
    jump artclassthurs

label artclassthurs:
    scene classroom with dissolve
    " You walked to the arts classroom and sat down onto your seat. "
    " You then waited patiently for the arts teacher to arrive... "
    " And drew a few things in your art notebook. "
    " It's pretty fitting, really. "
    " The teacher then walked into class after a bit. "
    show sashaneutral at center with easeinright
    mss " Heellooo, class! "
    mss " We won't really be doing anything important today... "
    mss " Fo a fact, I'm only going to show you guys examples of the stuff we talked about in our last lesson! "
    mss " To give you guys something to do, I'd like for you all to draw the examples in your notebooks. "
    mss " Don't make the examples too big - "
    mss " - Otherwise, you'd run out of space for the others! "
    mss " Anyway, let's begin! "
    scene black with dissolve
    " You spent the rest of the break drawing out the examples that Miss Sasha was giving the class. "
    " You kinda just lazily drew them and labelled them, but it looked alright. "
    play sound "audio/bellring.mp3"
    " The bell rings after a bit, time for you to go home. "
    " You packed your things and you then went out of school. "
    pause 2.0
    jump thursendday

label thursendday:
    scene paperschoolfront with dissolve
    " You walked out of the school, taking in the nice fresh air. "
    " Before you went home, you decided to look around for anything interesting. "
    if popularknow == True:
        " Huh, looks like the popular girls are going up to eachother now. "
        " Let's go and see what they're doing. "
        " Maybe they're actually apologizing to eachother. "
        show lizzyneutral at right with easeinleft
        show petuniasad at left with easeinleft
        p " ...What do you want, Lizzy... "
        p " I'm already in a bad mood, I don't need you to make it worse. "
        p " Just tell me before I go home. "
        lz " ... "
        hide lizzyneutral at bottom
        show lizzysad at right
        lz " ...Look, I wanted to say sorry for... "
        lz " Everything I did and said. "
        lz " Lend me an ear and listen to my explanation? "
        lz " Please, I need you to hear this. "
        lz " I don't want you to be making jokes about this either. "
        lz " This is something serious. "
        p " Okay.. "
        lz " Look, the reason I got upset with you yesterday was because... "
        if populartiktok == True or populartiktoklater == True:
            $ popularlv += 10
            lz " ...I got jealous of [name]. "
            hide petuniasad at bottom
            show petuniaconfused at left
            p " Wait, what? "
            p " Why? "
            lz " It's just that... "
            lz " People were kind of talking about you and [name] more. "
            lz " They said that you and [them] would be a much better duo... "
            lz " And everyone slowly started forgetting about me. "
            lz " ...And I thought...in time... "
            lz " You would forget about me too. I didn't like that thought. "
            lz " So I kind of got mad at you thinking that you actually would... "
            hide petuniaconfused at bottom
            show petunianeutral at left
            p " ...Lizzy, darling! "
            p " Why didn't you tell me this sooner? "
            p " Of course I won't forget about you, silly. "
            p " Besides, you're too iconic. "
            lz " ... (really...?) "
            p " So what if they want me and [name]? "
            p " We're just going to have to show them us as a trio! "
            p " Until we get too iconic to the point that you're back in! "
            p " Remember, darling... "
            p " We're STARS. and stars don't forget eachother. "
            hide lizzysad at bottom
            show lizzyneutral at right
            lz " ...Yeah...yeah! "
            hide lizzyneutral at bottom
            show lizzyhappy at right
            lz " Thanks guys...I really needed to hear all of this. "
            p " No problem! you guys wanna hang out at my house for a bit? "
            lz " I'm down. "
            " You told Petunia that you weren't really in the mood to. "
            p " That's fine, [name], we understand! "
            p " That just means that I could get some bonding time with Lizzy. "
            p " We could also come up with new videos too! "
            lz " Yeah! "
            lz " We'll see you tomorrow, [name]! "
            " You waved both of them goodbye. "
            hide lizzyhappy at right with easeoutright
            hide petunianeutral at right with easeoutright
            " And with that, you went back to your own home. "
            scene black with dissolve
            pause 2.0
            jump normalhomedadada
        else:
            lz " ...I got jealous of your friend. "
            hide petuniasad at bottom
            show petuniaconfused at left
            p " Wait, what? "
            p " Why? "
            lz " It's just that... "
            lz " You've been talking about them so much recently. "
            lz " Everyone's been getting curious on who they were... "
            lz " It's all: 'Oh, who's that?' 'When can we meet them?' "
            lz " I was starting to see less comments about me... "
            lz " ...And everyone was slowly forgetting about me. "
            lz " ...And I thought...in time... "
            lz " You would forget about me too. I didn't like that thought. "
            lz " So I kind of got mad at you thinking that you actually would... "
            hide petuniaconfused at bottom
            show petunianeutral at left
            p " ...Lizzy, darling! "
            p " Why didn't you tell me this sooner? "
            p " Of course I won't forget about you, silly. "
            p " Besides, you're too iconic. "
            lz " ... (really...?) "
            p " So what if they want me to show who that friend is? "
            p " We just don't give a single flying fuck about those guys and ignore them! "
            p " Remember, darling... "
            p " We're STARS. and stars don't forget eachother. "
            hide lizzysad at bottom
            show lizzyneutral at right
            lz " ...Yeah...yeah! "
            hide lizzyneutral at bottom
            show lizzyhappy at right
            lz " Thanks guys...I really needed to hear all of this. "
            p " No problem! you guys wanna hang out at my house for a bit? "
            lz " I'm down. "
            " You told Petunia that you weren't really in the mood to. "
            p " That's fine, [name], we understand! "
            p " That just means that I could get some bonding time with Lizzy. "
            p " We could also come up with new videos too! "
            lz " Yeah! "
            lz " We'll see you tomorrow, [name]! "
            " You waved both of them goodbye. "
            hide lizzyhappy at right with easeoutright
            hide petunianeutral at right with easeoutright
            " And with that, you went back to your own home. "
            scene black with dissolve
            pause 2.0
            jump normalhomedadada
    elif abbieteach == True:
        " As you were looking around, you felt a buzzing in your pockets. "
        " You opened up your phone and turns out it was a message from Abbie. "
        " Here's what it read... "
        a " Hi [name]!! ^_^ "
        a " I decided to come home a little bit earlier than you today... "
        a " That's because I wanted to do some more self training!! "
        a " It's been going really well recently, so I wanna see if I can improve more! "
        a " Hope you understand, have a good night! "
        " ...Sweet. What should you respond with? "
        menu:
            " 'Okay, have fun training and have a good night! <3' ":
                $ abbielv += 10
                " Sent that to him... "
                " and he immediately reacted to your message with a heart emoji. "
                " Cute. Hope his training goes well. "
                " You put your phone back into your pocket... "
                " And with that, you went back to your own home. "
                scene black with dissolve
                pause 2.0
                jump normalhomedadada
            " React to his message with a heart emoji ":
                " Sent that to him. "
                " Nice. Hope his training goes well. "
                " You put your phone back into your pocket... "
                " And with that, you went back to your own home. "
                scene black with dissolve
                pause 2.0
                jump normalhomedadada
    else:
        pass
    " Looks like nothing interesting is happenning. "
    " Guess you're gonna have to go home now... "
    " You took one last glance at your school before you headed off home. "
    scene black with dissolve
    pause 2.0
    jump normalhomedadada
label normalhomedadada:
    stop music fadeout 1.5
    pause 2.0
    play music "audio/home.mp3" fadein 1.5
    scene mcroom with dissolve
    " You got out of your schoolwear and you went back to your comfy homewear. "
    " You put your bag somewhere near your bed... "
    " ...Then, you satdown on your bed to make sure there were no assignments. "
    " Of course, everything's due next week. "
    " You could just procrastinate on these on sunday. "
    " You closed your phone, and put it on your desk. "
    " ..Before you then went to your bed and tucked yourself in. "
    " Time for a good night's rest. "
    scene black with dissolve
    " Good night. "
    pause 2.0
    jump friday
