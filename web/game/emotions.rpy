transform happy:
    yoffset 16.0
    yzoom 16.0
    linear 0.125 yzoom 0.95
    linear 0.1 yzoom 1.025
    linear 0.1 yzoom 1.075
    linear 0.25 yzoom 0.99
    linear 0.25 yzoom 16.0

transform worried:
    yoffset 16.0
    xoffset 415  # Start slightly to the left of the new estimated center
    linear 0.05 xoffset 425  # Move right slightly
    linear 0.1 xoffset 405  # Move left slightly
    linear 0.15 xoffset 425  # Move right further
    linear 0.15 xoffset 405  # Move left further
    linear 0.1 xoffset 425  # Move right slightly
    linear 0.2 xoffset 415  # Return to the new center

transform appearleft:
    xalign 0
    yalign 1.0
    alpha 0 xoffset -30
    easein .5 alpha 1.0 xoffset 0
    on hide:
        alpha 1.0 xoffset 0
        easein .5 alpha 0 xoffset -30
transform appearright:
    xalign 1.0
    yalign 1.0
    alpha 0 xoffset 30
    easein .5 alpha 1.0 xoffset 0
    on hide:
        alpha 1.0 xoffset 0
        easein .5 alpha 0 xoffset 30

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

transform credit:
    alpha 0.0
    easein 1.0 alpha 1.0
    pause 3.0
    easein 1.0 alpha 0.0
