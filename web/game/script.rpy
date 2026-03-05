### MC

define mc = Character("[name]")
define x = Character("???")

### students

define c = Character("Claire")
define e = Character("Engel")
define b = Character("Bubble")
define l = Character("Lana")
define a = Character("Abbie")
define o = Character("Oliver")
define z = Character("Zip")
define ed = Character("Edward")
define p = Character("Petunia")
define lz = Character("Lizzy")
define cb = Character("Cubbie")
define kv = Character("Kevin")
define rb = Character("Robby")
define ri = Character("Riley")
define ru  = Character("Ruby")
define sk = Character("Skell")
define al = Character("Alice")

### teachers + principal

define msc = Character("Miss Circle")
define mst = Character("Miss Thavel")
define msb = Character("Miss Bloomie")
define mse = Character("Miss Emily")
define msg = Character("Miss Grace")
define msd = Character("Mister Demi")
define mss = Character("Miss Sasha")
define mscl = Character("Mister Clio") # history
define msa = Character("Mister Altrix") # health
define msso = Character("Mister Sol") # pe
define msac = Character("Mister Ace") # ghost
define msl = Character("Miss Lua") #physics
define msw = Character("Miss Wisteria") # gardening
define msx = Character("Miss Jiayu")
define msh = Character("Miss Hyacinthus")

### OCS for OC ROUTE

define d = Character("Disk")
define q = Character("Quinn")
define yi = Character("Yinhui") # mean brother
define ya = Character("Yangyi") # nice brother
define sp = Character("Spark")
define tm = Character("Temero NEO")
define n = Character("Nox Cesso")
define j = Character("Jex")
define k = Character("Koa") # owned by blaze1953 on toyhouse
define m = Character("Mia") # owned by Felow_thetherianYT
define py = Character("Python")
define ca = Character("Carmen")
define ja = Character("Jam")
define ma = Character("Matte")
define jac = Character("Jacob")
define no = Character("Notive")
define oc = Character("Orchid")

define xx = Character(None)
define ju = Character("Juliana")
define pe = Character("Pedro")

# timer
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

init:
    $ timer_range = 0
    $ timer_jump = 0

label splashscreen:
    if persistent.playedgame != True:
        show aliceneutral at center with dissolve
        al " You're out here to look for a dating sim, aren't you. "
        al " A dating sim for FPE characters...how interesting. "
        al " Too bad a dating sim for ALL fpe characters doesn't exist. "
        al " It's always just the teachers, is it not? "
        al " You wished you could have one of the students as your lover... "
        al " ...I can make that happen. "
        al " Let's just say that I'd have to make a new universe for it though. "
        al " And with a new universe, comes complications. "
        al " Due to limitations, I'll only have you BEFRIEND fpe characters. "
        al " No complaints, no problems. "
        al " Without a further a-do...let's get befriending. "
        hide aliceneutral at bottom with easeoutbottom
        pause 2.0
        pass
    else:
        pass
    $ renpy.movie_cutscene("movies/intro.ogv")
    return

label start:
    stop music fadeout 0.5
    if persistent.playedgame == True:
        " Looks like you've played this game before. You've unlocked some other routes. "
        menu:
            " OC route ":
                $ ocroute = True
                " Enter your character's name, gender, and personality. "
                $ name = renpy.input(_("My name was..."), allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", length=30)
                $ name = name.strip()
                while(name in notusablenames):
                    $ name = renpy.input(_("MY name was...(previous name is unusable, darling!) "), allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", length=30)
                if name == "":
                    $ name = _("oreo")
                elif name == "johnbobette":
                    " hi rudie "
                elif name == "myballshurt" or name == "mbh":
                    " you need to go to lavie for ball surgery "
                elif name == "lavie" or name == "tundrox":
                    " what are you doing here "
                    " you need to go back to work "
                    return
                elif name == "anthonybassie":
                    " haha nice try "
                    return
                elif name == "roro" or name == "neolotus7":
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                elif name == "yaku" or name == "yakubell":
                    " THATS ME "
                    return
                elif name == "sample":
                    pause 1
                    scene hallway with dissolve
                    show oliverhappy at center
                    o " your mom "
                    return
                elif name == "aiden":
                    " That name sounds familiar... "
                    " Eh, nevermind...it's probably nothing. "
                elif name == "hyacinthus":
                    " ... "
                    $ renpy.quit()
                elif name == "katie":
                    " [name]...? What a familiar name. "
                    " Could it be you? The real one? "
                    " ...No, it's impossible. No way the {i}true{/i} one is here. "
                    " And if they were... "
                    " ...I wonder what they would think of this simulation. "
                elif name == "Katie":
                    " [name]...? What a familiar name. "
                    " Could it be you? The real one? "
                    " ...No, it's impossible. No way the {i}true{/i} one is here. "
                    " And if they were... "
                    " ...I wonder what they would think of this simulation. "
                elif name == "kaaatie":
                    " [name]...? What a familiar name. "
                    " Could it be you? The real one? "
                    " ...No, it's impossible. No way the {i}true{/i} one is here. "
                    " And if they were... "
                    " ...I wonder what they would think of this simulation. "
                elif name == "Kaaatie":
                    " [name]...? What a familiar name. "
                    " Could it be you? The real one? "
                    " ...No, it's impossible. No way the {i}true{/i} one is here. "
                    " And if they were... "
                    " ...I wonder what they would think of this simulation. "
                menu:
                    "I'm a girl. (She/Her) ":
                        #english pronouns
                        $ person = "girl"
                        $ they = "she"
                        $ are = "is"
                        $ arent = "isn't"
                        $ were = "was"
                        $ werent = "wasn't"
                        $ do = "does"
                        $ dont = "doesn't"
                        $ s = "s"
                        $ them = "her"
                        $ their = "her"
                        $ theirs = "hers"
                        $ mr = "mrs"
                        $ fancy = "ma'am"
                    "I'm a boy. (He/him) ":
                        $ person = "guy"
                        $ they = "he"
                        $ are = "is"
                        $ arent = "isn't"
                        $ were = "was"
                        $ werent = "wasnt"
                        $ do = "does"
                        $ dont = "doesn't"
                        $ s = "s"
                        $ them = "him"
                        $ their = "his"
                        $ theirs = "his"
                        $ mr = "mr"
                        $ fancy = "sir"
                    "I'm just some lil silly guy (they/them)":
                        $ person = "person"
                        $ they = "they"
                        $ are = "are"
                        $ arent = "arent"
                        $ were = "were"
                        $ werent = "weren't"
                        $ do = "do"
                        $ s = ""
                        $ dont = "don't"
                        $ them = "them"
                        $ their = "their"
                        $ theirs = "theirs"
                        $ mr = "mx"
                        $ fancy = "mx"
                " How about your personality? "
                menu:
                    " Kind ":
                        $ kind = True
                    " Mean ":
                        $ mean = True
                    " Chill/Calm ":
                        $ calm = True
                jump ocmonday
            " Teacher route ":
                $ teacherroute = True
                " Enter your character's name, gender, and personality. "
                $ name = renpy.input(_("My name was..."), allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", length=30)
                $ name = name.strip()
                while(name in notusablenames):
                    $ name = renpy.input(_("MY name was...(previous name is unusable, darling!) "), allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", length=30)
                if name == "":
                    $ name = _("oreo")
                elif name == "sample":
                    pause 1
                    scene hallway with dissolve
                    show oliverhappy at center
                    o " your mom "
                    return
                elif name == "johnbobette":
                    " hi rudie "
                elif name == "myballshurt" or name == "mbh":
                    " you need to go to lavie for ball surgery "
                elif name == "lavie" or name == "tundrox":
                    " what are you doing here "
                    " you need to go back to work "
                    return
                elif name == "anthonybassie":
                    " haha nice try "
                    return
                elif name == "roro" or name == "neolotus7":
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                elif name == "yaku" or name == "yakubell":
                    " THATS ME "
                    return
                elif name == "hyacinthus":
                    " You're not ready yet. "
                    $ renpy.quit()
                elif name == "katie":
                    " [name]...? What a familiar name. "
                    " Could it be you? The real one? "
                    " ...No, it's impossible. No way the {i}true{/i} one is here. "
                    " And if they were... "
                    " ...I wonder what they would think of this simulation. "
                elif name == "Katie":
                    " [name]...? What a familiar name. "
                    " Could it be you? The real one? "
                    " ...No, it's impossible. No way the {i}true{/i} one is here. "
                    " And if they were... "
                    " ...I wonder what they would think of this simulation. "
                elif name == "kaaatie":
                    " [name]...? What a familiar name. "
                    " Could it be you? The real one? "
                    " ...No, it's impossible. No way the {i}true{/i} one is here. "
                    " And if they were... "
                    " ...I wonder what they would think of this simulation. "
                elif name == "Kaaatie":
                    " [name]...? What a familiar name. "
                    " Could it be you? The real one? "
                    " ...No, it's impossible. No way the {i}true{/i} one is here. "
                    " And if they were... "
                    " ...I wonder what they would think of this simulation. "
                menu:
                    "I'm a girl. (She/Her) ":
                        #english pronouns
                        $ person = "girl"
                        $ they = "she"
                        $ are = "is"
                        $ arent = "isn't"
                        $ were = "was"
                        $ werent = "wasn't"
                        $ do = "does"
                        $ dont = "doesn't"
                        $ s = "s"
                        $ them = "her"
                        $ their = "her"
                        $ theirs = "hers"
                        $ mr = "mrs"
                        $ fancy = "ma'am"
                    "I'm a boy. (He/him) ":
                        $ person = "guy"
                        $ they = "he"
                        $ are = "is"
                        $ arent = "isn't"
                        $ were = "was"
                        $ werent = "wasnt"
                        $ do = "does"
                        $ dont = "doesn't"
                        $ s = "s"
                        $ them = "him"
                        $ their = "his"
                        $ theirs = "his"
                        $ mr = "mr"
                        $ fancy = "sir"
                    "I'm just some lil silly guy (they/them)":
                        $ person = "person"
                        $ they = "they"
                        $ are = "are"
                        $ arent = "arent"
                        $ were = "were"
                        $ werent = "weren't"
                        $ do = "do"
                        $ s = ""
                        $ dont = "don't"
                        $ them = "them"
                        $ their = "their"
                        $ theirs = "theirs"
                        $ mr = "mx"
                        $ fancy = "mx"
                " How about your personality? "
                menu:
                    " Kind ":
                        $ kind = True
                    " Mean ":
                        $ mean = True
                    " Chill/Calm ":
                        $ calm = True
                jump teachermonday
            " Normal FPE route. ":
                $ normalroute = True
                " Enter your character's name, gender, and personality. "
                $ name = renpy.input(_("My name was..."), allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", length=30)
                $ name = name.strip()
                while(name in notusablenames):
                    $ name = renpy.input(_("MY name was...(previous name is unusable, darling!) "), allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", length=30)
                if name == "":
                    $ name = _("oreo")
                elif name == "sample":
                    pause 1
                    scene hallway with dissolve
                    show oliverhappy at center
                    o " your mom "
                    return
                elif name == "johnbobette":
                    " hi rudie "
                elif name == "myballshurt" or name == "mbh":
                    " you need to go to lavie for ball surgery "
                elif name == "lavie" or name == "tundrox":
                    " what are you doing here "
                    " you need to go back to work "
                    return
                elif name == "anthonybassie":
                    " haha nice try "
                    return
                elif name == "roro" or name == "neolotus7":
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                    " hey roro hey roro hey roro hey roro hey roro "
                elif name == "yaku" or name == "yakubell":
                    " THATS ME "
                    return
                elif name == "hyacinthus":
                    " You're not ready yet. "
                    $ renpy.quit()
                elif name == "katie":
                    " [name]...? What a familiar name. "
                    " Could it be you? The real one? "
                    " ...No, it's impossible. No way the {i}true{/i} one is here. "
                    " And if they were... "
                    " ...I wonder what they would think of this simulation. "
                elif name == "Katie":
                    " [name]...? What a familiar name. "
                    " Could it be you? The real one? "
                    " ...No, it's impossible. No way the {i}true{/i} one is here. "
                    " And if they were... "
                    " ...I wonder what they would think of this simulation. "
                elif name == "kaaatie":
                    " [name]...? What a familiar name. "
                    " Could it be you? The real one? "
                    " ...No, it's impossible. No way the {i}true{/i} one is here. "
                    " And if they were... "
                    " ...I wonder what they would think of this simulation. "
                elif name == "Kaaatie":
                    " [name]...? What a familiar name. "
                    " Could it be you? The real one? "
                    " ...No, it's impossible. No way the {i}true{/i} one is here. "
                    " And if they were... "
                    " ...I wonder what they would think of this simulation. "
                menu:
                    "I'm a girl. (She/Her) ":
                        #english pronouns
                        $ person = "girl"
                        $ they = "she"
                        $ are = "is"
                        $ arent = "isn't"
                        $ were = "was"
                        $ werent = "wasn't"
                        $ do = "does"
                        $ dont = "doesn't"
                        $ s = "s"
                        $ them = "her"
                        $ their = "her"
                        $ theirs = "hers"
                        $ mr = "mrs"
                        $ fancy = "ma'am"
                    "I'm a boy. (He/him) ":
                        $ person = "guy"
                        $ they = "he"
                        $ are = "is"
                        $ arent = "isn't"
                        $ were = "was"
                        $ werent = "wasnt"
                        $ do = "does"
                        $ dont = "doesn't"
                        $ s = "s"
                        $ them = "him"
                        $ their = "his"
                        $ theirs = "his"
                        $ mr = "mr"
                        $ fancy = "sir"
                    "I'm just some lil silly guy (they/them)":
                        $ person = "person"
                        $ they = "they"
                        $ are = "are"
                        $ arent = "arent"
                        $ were = "were"
                        $ werent = "weren't"
                        $ do = "do"
                        $ s = ""
                        $ dont = "don't"
                        $ them = "them"
                        $ their = "their"
                        $ theirs = "theirs"
                        $ mr = "mx"
                        $ fancy = "mx"
                " ... "
                " {nw}"
                menu:
                    " Kind ":
                        $ kind = True
                    " Mean ":
                        $ mean = True
                    " Chill/Calm ":
                        $ calm = True
                jump monday
    else:
        $ welcome_achievement.grant()
        $ normalroute = True
        " Hello, before we start the game, I'd like for you to put in your character's name. "
        " I'll kindly ask for you not to use your real name. "
        $ name = renpy.input(_("My name was..."), allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", length=30)
        $ name = name.strip()
        while(name in notusablenames):
            $ name = renpy.input(_("MY name was...(previous name is unusable, darling!) "), allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", length=30)
        if name == "":
            $ name = _("oreo")
        elif name == "sample":
            pause 1
            scene hallway with dissolve
            show oliverhappy at center
            o " your mom "
            return
        elif name == "johnbobette":
            " hi rudie "
        elif name == "myballshurt" or name == "mbh":
            " you need to go to lavie for ball surgery "
        elif name == "lavie" or name == "tundrox":
            " what are you doing here "
            " you need to go back to work "
            return
        elif name == "anthonybassie":
            " haha nice try "
            return
        elif name == "roro" or name == "neolotus7":
            " hi my bf "
        elif name == "yaku" or name == "yakubell":
            " THATS ME "
            return
        elif name == "hyacinthus":
            " You're not ready yet. "
            $ renpy.quit()
        elif name == "katie":
            " [name]...? What a familiar name. "
            " Could it be you? The real one? "
            " ...No, it's impossible. No way the {i}true{/i} one is here. "
            " And if they were... "
            " ...I wonder what they would think of this simulation. "
        elif name == "Katie":
            " [name]...? What a familiar name. "
            " Could it be you? The real one? "
            " ...No, it's impossible. No way the {i}true{/i} one is here. "
            " And if they were... "
            " ...I wonder what they would think of this simulation. "
        elif name == "kaaatie":
            " [name]...? What a familiar name. "
            " Could it be you? The real one? "
            " ...No, it's impossible. No way the {i}true{/i} one is here. "
            " And if they were... "
            " ...I wonder what they would think of this simulation. "
        elif name == "Kaaatie":
            " [name]...? What a familiar name. "
            " Could it be you? The real one? "
            " ...No, it's impossible. No way the {i}true{/i} one is here. "
            " And if they were... "
            " ...I wonder what they would think of this simulation. "
        " Ooh, [name]. Right, right. Gotcha. Now... Your gender. "
        menu:
            "I'm a girl. (She/Her) ":
                #english pronouns
                $ person = "girl"
                $ they = "she"
                $ are = "is"
                $ arent = "isn't"
                $ were = "was"
                $ werent = "wasn't"
                $ do = "does"
                $ dont = "doesn't"
                $ s = "s"
                $ them = "her"
                $ their = "her"
                $ theirs = "hers"
                $ mr = "mrs"
                $ fancy = "ma'am"
            "I'm a boy. (He/him) ":
                $ person = "guy"
                $ they = "he"
                $ are = "is"
                $ arent = "isn't"
                $ were = "was"
                $ werent = "wasnt"
                $ do = "does"
                $ dont = "doesn't"
                $ s = "s"
                $ them = "him"
                $ their = "his"
                $ theirs = "his"
                $ mr = "mr"
                $ fancy = "sir"
            "I'm just some lil silly guy (they/them)":
                $ person = "person"
                $ they = "they"
                $ are = "are"
                $ arent = "arent"
                $ were = "were"
                $ werent = "weren't"
                $ do = "do"
                $ s = ""
                $ dont = "don't"
                $ them = "them"
                $ their = "their"
                $ theirs = "theirs"
                $ mr = "mx"
                $ fancy = "mx"
        " Alrighty...{w} Now, your choice on this will change how you'll act in-game, and it'll unlock endings depending on which one you pick. "
        " Of course, some endings won'be available if you pick a certain choice. So... "
        " Pick your personality. This really matters for which ending you'll get. "
        menu:
            " Kind ":
                $ kind = True
                jump pickpersonalityend
            " Mean ":
                $ mean = True
                jump pickpersonalityend
            " Chill/Calm ":
                $ calm = True
                jump pickpersonalityend
        label pickpersonalityend:
            " Good. Good, you've just caused pain for the programmer now just by picking this. "
            " Thank you, [name]. You'll wake up for school shortly. "
            " Another quick thing I'd like to note before you go. "
            " To get a character's ending, you must spend time with them. A lot. "
            "...Which means you're going to have to interact with them a lot. Like talk with them and no one else. "
            " On the options bar on each break, there will be little icons to indicate which character is there. "
            " The icons usually are an item or thing that's related to the character. "
            " If there are no icons, it means that there are multiple characters are there. "
            " That's all I'd like to say. Now, goodluck. "
            jump monday
