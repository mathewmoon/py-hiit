#!/usr/bin/env python3.8
from pyhiit import speak, rest, ropes, core, strength, bag


def ropes_bag_strength_core():
    speak("Lets start!. First is the ropes!")
    rest(5, msg=False)
    ropes(5)  # 15 minutes
    rest(180, "Rest for 3 minutes! Next is core!")
    core(3)  # 6 minutes
    rest(60, "Rest for 1 minute! Next up is strength training!")
    strength(3)  # 5.5 minutes
    rest(120, "Rest for two minutes! Next is the bag!")
    bag(5)  # 13.5 minutes
    speak("Finished!!")


def punch():
    bag(5)  # 13.5 minutes
    speak("Finished!!")


punch()

# 39 minute workout
# ropes_bag_strength_core()
