### lv

define clairelv = 0
define engellv = 0
define bubblelv = 0
define lanalv = 0
define abbielv = 0
define oliganglv = 0
define popularlv = 0
define cubbielv = 0
define kevinlv = 0
define robbrileylv = 0
define rubylv = 0
define skelllv = 0

define circlelv = 0
define thavellv = 0
define bloomielv = 0
define gracelv = 0
define sashalv = 0
define demilv = 0
define emilylv = 0

# ocs
define disklv = 0
define quinnlv = 0
define temerolv = 0
define sparklv = 0
define noxlv = 0
define koalv = 0
define jacoblv = 0
define yinhuilv = 0
define yangyilv = 0
define carmenlv = 0
define jamlv = 0
define mattelv = 0
define orchidlv = 0

# endings

define claireending = False
define engelending = False
define bubbleending = False
define lanaending = False
define abbieending = False
define oligangending = False
define circlending = False
define thravelending = False
define bloomieending = False
define lonelyending = False

# personality

define kind = False
define mean = False
define calm = False

# friends

define claireknow = False
define engelknow = False
define abbieknow = False
define lanaknow = False
define bubbleknow = False
define oligangknow = False
define skellknow = False
define rubyknow = False
define robbyknow = False
define rileyknow = False
define popularknow = False
define cubbieknow = False
define kevinknow = False

define diskknow = False
define quinnknow = False
define temeroknow = False
define sparkknow = False
define noxknow = False
define koaknow = False
define miaknow = False
define jexknow = False
define pythonknow = False
define carmenknow = False
define jamknow = False
define matteknow = False
define jacobknow = False
define notiveknow = False
define orchidknow = False
define yinhuiknow = False
define yangyiknow = False

define pythonchallenge = False
define pythoncode4 = False
define pythoncode2 = False
define pythoncode0 = False
define diskparty = False

define yinhuiparty = False
define yangyiparty = False
define yinyangparty = False
define yinhuiend = False
define yangyiend = False

define quinnshowsee = False

define diqutte = False
define spatemnox = False
define jamorcar = False
define koamiajex = False
define jacnotyinyang = False

define jamsnitch = False
define jamcomfort = False
define carmencomfort = False
define temerolistenin = False
define sparklistenin = False
define temeroformseen = False
define sparkformseen = False

define circleknow = False
define thavelknow = False
define bloomieknow = False
define emilyknow = False
define demiknow = False
define sashaknow = False

define oliganghangout = False

define abbiehomework = False
define lanacraft = False
define clairestudy = False
define engelstudy = False
define bubblestudy = False
define popularfriends = False

define warning1 = False
define warning2 = False
define warning3 = False
define warning4 = False
define warning5 = False

define sciencetest = 0

define abbiemeandefend = False
define abbieteach = False
define abbiehelp = False
define abbiehomework = False

define oligangtry = False
define oligangjoin = False

define populartiktok = False
define populartiktoklater = False

define askedcircle = False
define askedthavel = False
define askedbloomie = False

define circleinvite = False
define thavelinvite = False
define bloomieinvite = False
define emilyinvite = False
define demiinvite = False
define sashainvite = False

# seating

define claengbub = False
define abblana = False
define oligang = False
define alone = False

define clairesorry = False
define clairebeatup = False
define clairedefend = False

# route stuff

define normalroute = False
define ocroute = False
define teacherroute = False

# teacher mad count
define circlemad1 = False
define circlemad2 = False
define circlemad3 = False

define thavelmad1 = False
define thavelmad2 = False
define thavelmad3 = False

define bloomiemad1 = False
define bloomiemad2 = False
define bloomiemad3 = False

# timer
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.
init:
    $ timer_range = 0
    $ timer_jump = 0

# other thing
