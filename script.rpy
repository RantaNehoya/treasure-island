
define flash = Fade(0.1, 0.0, 0.3, color="#fff")

define e = Character("", image="elliot")
define d = Character("", image="doll")

transform slightright:
    xalign 0.65
    yalign 1.0

transform slightleft:
    xalign 0.35
    yalign 1.0


# The game starts here.
label start:

    "Welcome to your adventure!!!!" 
    with flash

    scene bg path1

    "After years of living in poverty on the island of NuNu, you've grown tired.{p=1}{cps=50}
    In an effort to rid yourself of this suffering, you leave home in search of the bear's gold.{/cps}"

    scene bg bridge with dissolve
    "You make your way to the Bridge of Souls.{p=1}{cps=50}
    It is rumoured to carry the souls of all the people who died trying to cross it.{/cps}{p=1}{cps=50}
    Do you wish to cross the bridge and leave the island?{/cps}"

    menu:
        "Yes, I do":
            jump path1

        "No, I do not":
            jump end4


label path1:
    
    show elliot excited

    "Well HIIIIII!{p=1}
    {cps=50}I see you want to cross this bridge.{/cps}"

    show elliot excited blushing
    "{cps=50}No worries, I won't stand in your way.{/cps}"

    hide elliot excited blushing

    e excited "{cps=50}In fact, I'll narrate your story from here on.{/cps}"
    e happy "While crossing the bridge you begin to feel anxious.{p=1}
    {cps=50}What do yo do?{/cps}"

    menu:
        "Look down":
            jump path2

        "Look straight ahead":
            jump end3



label path2:
    e shocked "{cps=50}You look down and manage to calm yourself by taking deep breaths.{/cps}"
    e excited "{cps=50}Maybe this wasn't such a bad idea after all.{/cps}"

    scene bg forest1

    show doll happy
    show vamp neutral at slightleft behind doll
    show monster neutral at slightright behind vamp


    e shocked "{cps=50}You make it to the end of the bridge where you see a gang of very scary looking criminals waiting for you.{p=1}{/cps}"
    e angry "{cps=50}They ask you what you're doing so far away from home.{/cps}"
    e "{cps=50}What do you do?{/cps}"

    menu:
        "Lie":
            jump end1

        "Tell them you're going searching for the bear's gold":
            jump path3


label path3:
    e excited "Very satisfied with your answer, the criminals decide to join you on your quest."

    scene bg forest2

    e happy "You make your way to the Whispering Woods to find the spirit that guards it.{p=2}
    {cps=50}What do you do?{/cps}"

    menu:
        "Demand the spirit lets you through":
            jump path4

        "Ask the criminals to handle it":
            jump path6


label path4:

    scene bg forest3

    e shocked "Wow... that spirit was quite docile.{p=1}
    Makes you wonder why it was even there to begin with..."

    show influencer neutral

    e excited blushing "While on your journey, you see a social media influencer livestreaming.{p=1}
    {cps=50}What do you do?{/cps}"

    menu:
        "Say wassup to the chat":
            jump end2

        "Not my business. Keep it moving":
            jump path5


label path5:

    scene bg cave

    e happy "{cps=50}You remain focused and continue with your journey to the bear's cave.{/cps}"
    e "{cps=50}You enter the cave in search for the bear's rumoured treasures while the criminals stand guard for you.{/cps}"
    e excited "Eventually...{p=1}
    {cps=50}You find the bear's treasure. Lucky you.{/cps}"
    e excited blushing "{cps=50}What do you do?{/cps}"

    menu:
        "Take it all":
            jump end5

        "Share the riches":
            jump end6


label path6:

    show doll angry
    show vamp neutral at slightleft behind doll
    show monster neutral at slightright behind vamp

    d "With pleasure"

    hide doll angry
    hide monster neutral
    hide vamp neutral

    scene bg forest3

    e shocked "{cps=50}Your criminal friends attempt to slay the spirit and end up severly injured.{/cps}"
    e frown blushing "{cps=50}You will have to progress without them.{/cps}"

    show influencer neutral

    e frown "{cps=50}As you journey through the Whispering Woods, you see a social media influencer livestreaming.{/cps}{p=1}
    {cps=50}What do you do?{/cps}"

    menu:
        "VIDEOBOMB!!! duuuhhh":
            jump end7

        "Not my business. Move along":
            jump end8

