label credits:
    scene creditbg with dissolve
    stop music fadeout 0.5
    menu:
        "Skip the credits":
            scene black with dissolve
            pause 2.0
            return
        "Let them roll":
            play music "audio/credits.wav" fadein 0.5
            pause 2.0
    show text " Programming + Writing + Music ;; - Yakubell " at credit
    pause 5.5
    show text " Art (Sprites) ;; - Yakubell, D'dits :D " at credit
    pause 5.5
    show text " Art (Backgrounds) ;; - @ling.png, @blaze.1953 on Discord " at credit
    pause 5.5
    show text " Bug testers // Playtesters ;; - Tundrox (Lavie), Dandy//Jello.world " at credit
    pause 5.5
    show text " SPECIAL MENTIONS!! (Ocs) " at credit
    pause 5.5
    show text " Disk, Quinn, Spark, Temero NEO, Nox Cesso, Python, Carmen, Jam, Matte, Orchid, + ALL THE TEACHERS IN THE OC ROUTE EXCEPT FOR THE COOKING CLASS ONE ;; - yakubell " at credit
    pause 5.5
    show text " Yinhui and Yangyi ;; - D'dits :D " at credit
    pause 5.5
    show text " Koa ;; - blaze.1953 " at credit
    pause 5.5
    show text " Jex ;; - inseo._.zero " at credit
    pause 5.5
    show text " Mia ;; - Fellow_thetherianYT " at credit
    pause 5.5
    show text " Jacob ;; - Jakub596 " at credit
    pause 5.5
    show text " Notive ;; - some_nonexistentchocobar " at credit
    pause 5.5
    show text " MORE SPECIAL MENTIONS... (extra) " at credit
    pause 5.5
    show text " D'dits ;; - the one who said 'hell yeah lets do fpe visual novel' " at credit
    pause 5.5
    show text " ling.png ;; - having to deal with my background shenanigangs " at credit
    pause 5.5
    show text " And you, dear player ;; - for playing! " at credit
    pause 5.5
    show text " {a=https://www.youtube.com/@yakubell} Youtube {/a}, {a=https://www.tiktok.com/@yaku.frog} Tiktok {/a}, {a=https://x.com/yakustudios}Twitter{/a} " at credit # add links later
    pause 5.5
    show text " Thank you for playing once more! This game was a pain to make. " at credit
    pause 5.5
    scene black with dissolve
    stop music fadeout 0.5
    if persistent.playedgame == True:
        if normalroute == True and persistent.playedgame == True:
            pause 2.0
            return
        elif normalroute == True and persistent.playedgame != True:
            $ persistent.playedgame = True
            $ playedonce.grant()
            " Seems like you unlocked new features... "
            " You should check them out once you play again. "
            " Bye for now. "
            pause 2.0
            return
        elif ocroute == True and persistent.ocplayed != True:
            $ persistent.ocplayed = True
            pause 2.0
            return
        elif ocroute == True and persistent.ocplayed == True:
            pause 2.0
            return
        elif teacherroute == True and persistent.teacherplayed != True:
            $ persistent.teacherplayed = True
            pause 2.0
            return
        elif teacherroute == True and persistent.teacherplayed == True:
            pause 2.0
            return
        else:
            pause 2.0
            return
    elif persistent.playedgame != True:
        $ persistent.playedgame = True
        $ playedonce.grant()
        " Seems like you unlocked new features... "
        " You should check them out once you play again. "
        " Bye for now. "
        pause 2.0
        return
    else:
        $ persistent.playedgame = True
        $ playedonce.grant()
        " Seems like you unlocked new features... "
        " You should check them out once you play again. "
        " Bye for now. "
        pause 2.0
        return
