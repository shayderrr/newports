################################################################################
##
## Achievements for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
##
################################################################################
## This file contains code for an achievement system in Ren'Py. It is designed
## as a wrapper to the built-in achievement system, so it hooks into the
## Steam backend as well if you set up your achievement IDs the same as in
## the Steam backend.
##
## You don't have to register the achievements or anything with the backend,
## or worry about syncing - that's all automatically done for you when the
## achievements are declared and granted.
##
## To get started, declare a few achievements below. Some samples are included.
## You may also replace the `image locked_achievement` image with something
## appropriate - this image is used as the default "Locked" image for all your
## achievements unless you specify something else.
##
## Then you can make a button to go to your achievement gallery screen, e.g.
# textbutton _("Achievements") action ShowMenu("achievement_gallery")
## This will show the achievement gallery screen, declared below. You can
## further customize it however you like.
## If you click on an achievement in the gallery during development (this will
## not happen in a release build), it will toggle the achievement on/off.
## This will also let you see the achievement popup screen, similarly declared
## below. It can be customized however you like.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## Leave a comment on the tool page on itch.io or an issue on the GitHub
## if you run into any issues.
################################################################################

################################################################################
## CONFIGURATION
################################################################################
## This is a configuration value which determines whether the in-game
## achievement popup should appear when Steam is detected. Since Steam
## already has its own built-in popup, you may want to set this to False
## if you don't want to show the in-game popup alongside it.
## The in-game popup will still work on non-Steam builds, such as builds
## released DRM-free on itch.io.
define myconfig.INGAME_POPUP_WITH_STEAM = True
## The length of time the in-game popup spends hiding itself (see
## transform achievement_popout below).
define myconfig.ACHIEVEMENT_HIDE_TIME = 1.1
## True if the game should show in-game achievement popups when an
## achievement is earned. You can set this to False if you just want an
## achievement gallery screen and don't want any popups.
define myconfig.SHOW_ACHIEVEMENT_POPUPS = False
## This can be set to a sound that plays when the achievement popup appears.
## None does not play a sound.
define myconfig.ACHIEVEMENT_SOUND = None # "audio/sfx/achievement.ogg"
## If the sound plays, this sets the channel it will play on. The audio
## channel plays on the sfx mixer, and can play overlapping sounds if multiple
## achievements are earned at once.
define myconfig.ACHIEVEMENT_CHANNEL = "audio"

## A callback, or list of callbacks, which are called when an achievement
## is granted. It is called with one argument, the achievement which
## was granted. It is only called if the achievement has not previously
## been earned. See the README for more information.
define myconfig.ACHIEVEMENT_CALLBACK = [
    ## This first example is an achievement which unlocks after two other
    ## achievements have been granted ("hidden_achievement" and
    ## "hidden_description").
    LinkedAchievement(hidden3=['hidden_achievement', 'hidden_description']),
    ## The second example is an achievement which unlocks after all achievements
    ## have been granted. This is a special case.
    LinkedAchievement(platinum_achievement='all'),
]

init python:
    ## This is a built-in configuration value. It will set the position of
    ## the Steam popup. You can change this to any of the following:
    ## "top_left", "top_right", "bottom_left", "bottom_right"
    ## You may want to use this to ensure any Steam notifications don't conflict
    ## with the position of the built-in notification, if you're using both.
    achievement.steam_position = None

################################################################################
## DEFINING ACHIEVEMENTS
################################################################################
## Replace this with whatever locked image you want to use as the default
## for a locked achievement.
image locked_achievement = Text("Can't get this yet!")

## Example 1 ###################################################################
## This is how you declare achievements. You will use `define` and NOT
## `default`, so you can update the achievements later (you wouldn't want the
## description to be tied to a specific save file, for example).
## The order you declare achievements in is the order they will appear in the
## achievement gallery, by default.
define welcome_achievement = Achievement(
    ## The human-readable name, as it'll appear in the popup and in the gallery.
    name=_("Welcome!"),
    ## The id is used for Steam integration, and should match whatever ID
    ## you have set up in the Steam backend (if using).
    id="welcome_achievement",
    ## Description.
    description=_("{color=#F8F8FF}Another dating sim? Nah!{/color}"),
    ## The image used in the popup and in the gallery once this achievement
    ## is unlocked.
    unlocked_image="gui/window_icon.png",
    ## By default all achievements use the "locked_achievement" image (declared
    ## above), but if you wanted to provide a different image, this is how
    ## you would specify it. It's used in the achievement gallery when the
    ## achievement is locked.
    locked_image="locked_achievement",
    ## All achievements are hidden=False by default, but you can change it to
    ## hidden=True if you'd like the title/description to show as ??? in the
    ## achievement gallery. See Examples 3 and 4 for examples of this.
    hidden=False,
)

define playedonce = Achievement(
    name=_("It begins..."),
    id="playedonce",
    description=_("{color=#F8F8FF} Finish an ending for the first time! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define lonelyend = Achievement(
    name=_("Eternal Loneliness"),
    id="lonelyend",
    description=_("{color=#F8F8FF} I thought I taught you how the game works... {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define clairesend = Achievement(
    name=_("Claires Joy"),
    id="clairesjoy",
    description=_("{color=#F8F8FF} Get Claire's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define engelsend = Achievement(
    name=_("Two birds on a wire"),
    id="engelsend",
    description=_("{color=#F8F8FF} Get Engel's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define bubblesend = Achievement(
    name=_("Bubbling Friendship"),
    id="bubblesend",
    description=_("{color=#F8F8FF} Get Bubble's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define lanasend = Achievement(
    name=_("Not a player, a puppeteer!"),
    id="lanasend",
    description=_("{color=#F8F8FF} Get Lana's ending!...wait, an epic the musical reference in the title? {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define abbiesend = Achievement(
    name=_("Strong in the real way!"),
    id="abbiesend",
    description=_("{color=#F8F8FF} Get Abbie's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define oligangsend = Achievement(
    name=_("Trouble Quartet!"),
    id="oligangsend",
    description=_("{color=#F8F8FF} Get Oliver and the gang's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define cubbiesend = Achievement(
    name=_("Cat kitty cat cat!"),
    id="cubbiesend",
    description=_("{color=#F8F8FF} Get Cubbie's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define kevinsend = Achievement(
    name=_("Nerding out together"),
    id="kevinsend",
    description=_("{color=#F8F8FF} Get Kevin's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define popularsend = Achievement(
    name=_("Soon-to-be Celebrities!"),
    id="popularsend",
    description=_("{color=#F8F8FF} Get Petunia and Lizzy's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define robrileysend = Achievement(
    name=_("Chaos ensues..."),
    id="robrileysend",
    description=_("{color=#F8F8FF} Get Robby and Riley's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define rubysend = Achievement(
    name=_("Machine Love"),
    id="rubysend",
    description=_("{color=#F8F8FF} Get Ruby's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define skellsend = Achievement(
    name=_("Secretly a Miku fan"),
    id="skellsend",
    description=_("{color=#F8F8FF} Get Skell's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define circlesend = Achievement(
    name=_("Oreo consumer"),
    id="circlesend",
    description=_("{color=#F8F8FF} Get Miss Circle's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define thavelsend = Achievement(
    name=_("Mi Amor"),
    id="thavelsend",
    description=_("{color=#F8F8FF} Get Miss Thavel's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define bloomiesend = Achievement(
    name=_("Scientists Together"),
    id="bloomiesend",
    description=_("{color=#F8F8FF} Get Miss Bloomie's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define emilysend = Achievement(
    name=_("Bestest Friendship In History"),
    id="emilysend",
    description=_("{color=#F8F8FF} Get Miss Emily's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define demisend = Achievement(
    name=_("Music To My Ears"),
    id="demisend",
    description=_("{color=#F8F8FF} Get Mister Demi's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define sashasend = Achievement(
    name=_("Aortic Work Of Art"),
    id="sashasend",
    description=_("{color=#F8F8FF} Get Miss Sasha's Ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define disksend = Achievement(
    name=_("Life of the party!"),
    id="disksend",
    description=_("{color=#F8F8FF} Get Disk's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define quinnsend = Achievement(
    name=_("Romeo and Juliet"),
    id="quinnsend",
    description=_("{color=#F8F8FF} Get Quinn's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define mattesend = Achievement(
    name=_("Artist's Assistant"),
    id="mattesend",
    description=_("{color=#F8F8FF} Get Matte's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define jamsend = Achievement(
    name=_("GameJammed"),
    id="jamsend",
    description=_("{color=#F8F8FF} Get Jam's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define sparksend = Achievement(
    name=_("Color and Electricity"),
    id="sparksend",
    description=_("{color=#F8F8FF} Get Spark's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define temerosend = Achievement(
    name=_("Insane Scientists"),
    id="temeroend",
    description=_("{color=#F8F8FF} Get Temero's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define yinhuisend = Achievement(
    name=_("The good side of bad"),
    id="playedonce",
    description=_("{color=#F8F8FF} Get Yinhui's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define yangyisend = Achievement(
    name=_("The bad side of good...?"),
    id="yangyisend",
    description=_("{color=#F8F8FF} Get Yangyi's ending!...okay that title doesnt really make sense {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define yinyangend = Achievement(
    name=_("Balance"),
    id="yinyangend",
    description=_("{color=#F8F8FF} Get BOTH of the twin's endings! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define noxsend = Achievement(
    name=_("Sleepy Little Creatures"),
    id="noxsend",
    description=_("{color=#F8F8FF} Get Nox's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define carmensend = Achievement(
    name=_("Sweet Music"),
    id="carmensend",
    description=_("{color=#F8F8FF} Get Carmen's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define koasend = Achievement(
    name=_("Unexpected Friendship"),
    id="koasend",
    description=_("{color=#F8F8FF} Get Koa's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define orchidsend = Achievement(
    name=_("Despite everything..."),
    id="orchidsend",
    description=_("{color=#F8F8FF} ... You still got Orchid's ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define jacobsend = Achievement(
    name=_("Through strong walls"),
    id="jacobsend",
    description=_("{color=#F8F8FF} Melt through Jacob's walls and get his ending! {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

define pythonsend = Achievement(
    name=_("Yay, you got my ending!"),
    id="playedonce",
    description=_("{color=#F8F8FF} Finish Python's quest! - consider this as an ending. <3 {/color}"),
    unlocked_image="gui/window_icon.png", # temporary
    locked_image="locked_achievement",
    hidden=False,
)

# ERROR: failed to apply 'hyacinthus ending'.

# add other endings later

## You can grant an achievement in-game with `$ sample_achievement.grant()`

## Example 2 ###################################################################
## define progress_achievement = Achievement(
    ## name=_("Progress Achievement"),
    ## id="progress_achievement",
    ## description=_("This is an achievement with a progress bar."),
    ## unlocked_image=Transform("gui/window_icon.png", matrixcolor=InvertMatrix()),
    ## To record progress, you need to specify a stat_max. This means you can
    ## show a progress bar with % completion towards the achievement. It is
    ## useful if, for example, you have an achievement counting how many
    ## chapters the player has completed which unlocks when they have seen all
    ## the chapters.
    ## stat_max=12,
    ## You can also provide a stat_modulo, which means the achievement is only
    ## updated in the Steam backend every time the stat reaches a multiple of
    ## the modulo.
    ## Alternatively, this system also lets you set stat_update_percent instead,
    ## so if you want it to update every 10% it progresses, you can set
    ## stat_update_percent=10
    ## This is most useful for achievements with a large number of steps,
    ## like a general % completion achievement. Maybe there are 600 things to
    ## complete for the achievement, but obviously 0.1% increments are pretty
    ## meaningless so you can either set stat_modulo=6 or stat_update_percent=1
    ## and it will update Steam every 6 steps or every 1%.
##)
## To update progress towards completion of this achievement, you can use
# $ progress_achievement.add_progress(1)
## where 1 is how much progress is added to the stat (so, the first time it
## is called for the above example it'd be 1/12, the second it'd be 2/12, etc).
##
## Alternatively, you can directly set the progress like:
# $ progress_achievement.progress(5)
## This will directly set progress to 5, making the above example 5/12 for
## example. This can be useful if you're doing something like using a set to
## track unique progress towards the achievement e.g.
# $ persistent.seen_endings.add("end1")
# $ ending_achievement.progress(len(persistent.seen_endings))
## This will prevent the achievement from being added to multiple times if the
## player sees the same ending multiple times.

## Example 3 ###################################################################
## This achievement is "hidden", that is, its name and description appear as
## ??? in the achievement gallery until it is unlocked.
##define hidden_achievement = Achievement(
    ##name=_("Hidden Achievement"),
    ##id="hidden_achievement",
    ##description=_("This hidden achievement hides both the name and description."),
    ##unlocked_image=Transform("gui/window_icon.png", matrixcolor=BrightnessMatrix(-1.0)),
    ##hidden=True, ## The important bit that hides the name and description
##)

## Example 4 ###################################################################
##define hidden_description = Achievement(
    ##name=_("Hidden Description"),
    ##id="hidden_description",
    ##description=_("This hidden achievement hides only the description."),
    ##unlocked_image=Transform("gui/window_icon.png", matrixcolor=SepiaMatrix()),
    ##hide_description=True, ## The important bit that hides only the description
##)

## Example 5 ###################################################################
## This achievement unlocks automatically when the other two hidden achievements
## are unlocked. This is set up via myconfig.ACHIEVEMENT_CALLBACK earlier in
## the file.
##define hidden_double_unlock = Achievement(
    ##name=_("You found it"),
    ##id="hidden3",
    ##description=_("This achievement unlocks automatically when the other two hidden achievements are unlocked."),
    ##unlocked_image=Transform("gui/window_icon.png", matrixcolor=ContrastMatrix(0.0)),
    ##hidden=True,
    ## Besides just setting hide_description=True to set it to "???", you can
    ## optionally provide your own custom description here, which is only
    ## shown until the achievement is unlocked.
    ##hide_description=_("Try unlocking the other two hidden achievements before this one."),
##)
## Example 6 ###################################################################
## This -2 makes sure it's declared before the other achievements. This is
## so it shows up first in the list even though it's defined all the way down
## here.
define -2 all_achievements = Achievement(
    name=_("Achievement Collector"),
    id="platinum_achievement",
    description=_("You unlocked every achievement... how long did this take you?"),
    unlocked_image=Transform("gui/window_icon.png", matrixcolor=BrightnessMatrix(1.0)),
    hide_description=_("Get all other achievements."),
)

################################################################################
## SCREENS
################################################################################
## POPUP SCREEN
################################################################################
## A screen which shows a popup for an achievement the first time
## it is obtained. You may modify this however you like.
## The relevant information is:
## a.name = the human-readable name of the achievement
## a.description = the description
## a.unlocked_image = the image of the achievement, now that it's unlocked
## a.timestamp = the time the achievement was unlocked at
screen achievement_popup(a, tag, num):

    zorder 190

    ## Allows multiple achievements to be slightly offset from each other.
    ## This number should be at least as tall as one achievement.
    default achievement_yoffset = num*170

    frame:
        style_prefix 'achieve_popup'
        ## The transform that makes it pop out
        at achievement_popout()
        ## Offsets the achievement down if there are multiple
        yoffset achievement_yoffset
        has hbox
        add a.unlocked_image:
            ## Make sure the image is within a certain size. Useful because
            ## often popups are smaller than the full gallery image.
            ## In this case it will not exceed 95 pixels tall but will retain
            ## its dimensions.
            fit "contain" ysize 95 align (0.5, 0.5)
        vbox:
            text a.name
            text a.description size 25

    ## Hide the screen after 5 seconds. You can change the time but shouldn't
    ## change the action.
    timer 5.0 action [Hide("achievement_popup"),
            Show('finish_animating_achievement', num=num, _tag=tag+"1")]

style achieve_popup_frame:
    is confirm_frame
    align (0.0, 0.0)
style achieve_popup_hbox:
    spacing 10
style achieve_popup_vbox:
    spacing 2


## A transform that pops the achievement out from the left side of
## the screen and bounces it slightly into place, then does the
## reverse when the achievement is hidden.
transform achievement_popout():
    ## The `on show` event occurs when the screen is first shown.
    on show:
        ## Align it off-screen at the left. Note that no y information is
        ## given, as that is handled on the popup screen.
        xpos 0.0 xanchor 1.0
        ## Ease it on-screen
        easein_back 1.0 xpos 0.0 xanchor 0.0
    ## The `on hide, replaced` event occurs when the screen is hidden.
    on hide, replaced:
        ## Ease it off-screen again.
        ## This uses the hide time above so it supports displaying multiple
        ## achievements at once.
        # easeout_back myconfig.ACHIEVEMENT_HIDE_TIME xpos 0.0 xanchor 1.0
        easeout_back myconfig.ACHIEVEMENT_HIDE_TIME xpos 0.0 xanchor 1.0

################################################################################
## ACHIEVEMENT GALLERY SCREEN
################################################################################
## The screen displaying a list of the achievements the player has earned.
## Feel free to update the styling for this however you like; this is just one
## way to display the various information.
screen achievement_gallery():
    tag menu

    add VBox(Transform("#292835", ysize=110), "#21212db2") # Background

    ############################################################################
    ## Version 1 ###############################################################
    ## If you're using a default template/typical Ren'Py layout, uncomment
    ## the following:
    # use game_menu(_("Achievement Gallery"), scroll='viewport'):
    ############################################################################
    ## Version 2 ###############################################################
    ## Otherwise, if you'd like this to be independent of the game menu,
    ## use the following:
    textbutton _("Return") action Return() align (1.0, 1.0)
    viewport:
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"
        xalign 0.5 yalign 0.5
        xsize int(config.screen_width*0.6) ysize int(config.screen_height*0.7)
        xfill False yfill False
        has vbox
        spacing 20
    ############################################################################
    ## Version 3 ###############################################################
    ## You might also consider a vpgrid layout like so:
    # textbutton _("Return") action Return() align (1.0, 1.0)
    # vpgrid:
    #     cols 2
    #     mousewheel True draggable True pagekeys True
    #     scrollbars "vertical"
    #     xalign 0.5 yalign 0.5
    #     xsize 1500 ysize int(config.screen_height*0.7)
    #     yspacing 70 xspacing 50
    ############################################################################
        ## This list contains every achievement you declared. You can also
        ## create your own lists to iterate over, if desired. That would be
        ## useful if you wanted to group achievements by category, for example.
        for a in Achievement.all_achievements:
            button:
                style_prefix 'achievement'
                ## During development, you can click on achievements in the
                ## gallery and they will toggle on/off.
                if config.developer:
                    action a.Toggle()
                has hbox
                if a.idle_img:
                    fixed:
                        align (0.5, 0.5)
                        xysize (155, 155)
                        add a.idle_img fit "scale-down" ysize 155 align (0.5, 0.5)
                else:
                    null width -10
                vbox:
                    label a.name
                    text a.description
                    if a.has():
                        ## There are two ways to display the timestamp. The
                        ## first is automatically formatted like
                        ## Unlocked Sep 14, 2023 @ 6:45 PM
                        text a.timestamp size 22
                        ## If you want to format it yourself, you can use
                        ## the get_timestamp method:
                        # text __("Achieved at ") + a.get_timestamp(__("%H:%M on %Y/%m/%d"))
                        ## The above example would display the timestamp like:
                        ## Achieved at 18:45 on 2023/09/14
                        ## See https://strftime.org/ for formatting
                        ## Note also the double underscores for translation.
                    elif a.stat_max:
                        # Has a bar to show stat progress.
                        ## NOTE: If you don't want to show the progress *bar*,
                        ## you can remove this entire block (or potentially just
                        ## keep the text and not the bar if you like).
                        fixed:
                            fit_first True
                            bar value a.stat_progress range a.stat_max:
                                style 'achievement_bar'
                            text "[a.stat_progress]/[a.stat_max]":
                                style_suffix "progress_text"

        ## So there's a bit of space at the bottom after scrolling all the way.
        null height 100

    ## A header that shows how many achievements you've earned, out of
    ## the total number of achievements in the game. Feel free to remove
    ## or relocate this.
    label __("Achievements: ") + "{earned}/{total}".format(
            earned=Achievement.num_earned(), total=Achievement.num_total()):
        text_size 52 xalign 0.5 text_color "#f93c3e" top_padding 15

    ## This is an example of a button you might have during development which
    ## will reset all achievement progress at once. It can also be provided
    ## to players if you'd like them to be able to reset their achievement
    ## progress.
    # textbutton "Reset All" action Achievement.Reset() align (1.0, 0.0)

style achievement_button:
    size_group 'achievement'
    xmaximum 750
style achievement_label:
    padding (2, 2)
style achievement_label_text:
    size 40 color "#ff8335"
style achievement_hbox:
    spacing 10
style achievement_vbox:
    spacing 2
style achievement_bar:
    xmaximum 600
