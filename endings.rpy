label end1:

    show doll angry
    show monster neutral at slightright behind doll
    show vamp angry at slightleft behind doll

    e shocked "{cps=50}I don't think they liked that answer very much...{/cps}"

    e angry "{cps=50}Not satisfied with your answer, the criminals vote to kill you and go rampaging on your island.{/cps}"

    e frown "Achieved Ending 1: What a shame. Maybe don't lie"

    return


label end2:

    hide influencer neutral

    e shocked "Well...{p=1}
    {cps=50}Who would've guessed criminals don't like to be on camera.{/cps}"
    
    e frown "To absolutely NO ONE'S surprise{p=1}
    {cps=50}the criminals do what they do best and slaughter her on live...{p=2}{/cps}
    {cps=50}in front of thousands of people.{/cps}"
    
    e angry "{cps=50}That wasn't a very good idea... now you're a criminal by association...{/cps}"

    e frown blushing "{cps=50}Achieved Ending 2: One of them now, I guess{/cps}"

    return


label end3:

    e shocked "In an attempt to cross the bridge as quickly as you can, your hasty movements cause the ties to snap...{p=3}
    {cps=50}resulting in you falling to your death.{/cps}"

    e frown "{cps=50}Achieved Ending 3: Maybe you should'nt have crossed the bridge{/cps}"

    return


label end4:

    "Overtaken by the fear of possibly falling to your death,"

    scene bg house2

    "{cps=50}You decide to make the conscious decision to turn back and go home.{/cps}"
    "{cps=50}No good ending for you.{/cps}{p=1.5}

    {cps=50}Achieved Ending 4: Coward{/cps}"

    return


label end5:

    e frown "Those pesky criminals exhausted their usefulness to you anyways."

    scene bg house

    e excited "{cps=50}You take all the gold for yourself and sneak out of the cave without them seeing you,{p=1}{/cps}
    {cps=50}making your way back home where you now intend to live a life of luxury.{/cps}"

    e happy "Achieved Ending 5: You never have to work again"

    return


label end6:

    e happy "{cps=50}You call the criminals into the cave to behold your discovery.{/cps}"

    show doll happy with dissolve
    show monster neutral at slightright behind doll with dissolve
    show vamp neutral at slightleft behind doll with dissolve

    e frown "{cps=50}Naturally, you decide to share the gold with the criminals as appreciation for their help.{/cps}"
    e "{cps=50}If you didn't they would've forcefully taken it from you anyways.{/cps}"

    e frown blushing "Achieved Ending 6: There are better endings out there"

    return


label end7:

    e excited "{cps=50}Amused, the influencer invites you back to their place.{/cps}"

    scene bg house

    e happy "{cps=50}After hearing your sad story of suffering, the influencer introduces you to the world of social media and sponsorships where you now make plenty of money.{/cps}"
    e shocked blushing "That's how it works right?"

    e excited blushing "{cps=50}Achieved Ending 7: Social Media Star{/cps}"

    return


label end8:

    scene bg forest4

    e frown "Your search for the bear's treasures through the Whispering Woods proved to be futile as you came across..."
    e angry "{cps=50}NOTHING!{/cps}"

    e frown "Welp...{p=2}
    {cps=50}Checkers is always hiring.{/cps}"

    e "Achieved Ending 8: It's a hard knock life"

    return