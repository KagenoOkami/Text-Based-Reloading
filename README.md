Text-Based-Reloading

A little script inspired by games such as Receiver and VR games like Pavlov and H3VR

Uses Python 3.7
Uses Pynput

Bit of a mess as of right now.
Things might still break.

Todo:

Implement an actual inventory system
Implement better ways to interact/look at the weapons. (visuals(?))
Implement a few game like features like a random inventory.




press 1,2,3,4,5 for the weapons:
- Revolver
- Double Barrel Shotgun
- Bolt Action Rifle
- Pump Action Shotgun
- Pistol (Self chambering)

Revolver:
Open the cylinder with "R"
Load a cardrigde with "K" (up to 6 times)
Close the cylinder with "V"
Cock the hammer with "U"
Fire with "J"
To extract all cardridges (fired or not) with "," when the cylinder is open
cylinder can be rotated with "I" and "O"

Double Barrel Shotgun:
Open the action with "R"
Load a cardrige in the left barrel with "N" and in the right with "M"
Close the action with "V"
Fire twice with "J"
Open the action again
To extract press "U" for the left barrel and "I" for the right barrel or "Y" for both

Bolt Action:
Unlock the bolt (rotate up) with "R"
Draw the bolt with "V"
Load a single round into the magazine with "K"
Load a single round into the chamber with "I"
Load a clip into the magazine with ","
Push the bolt with "R"
Lock the bolt (rotate down) with "T"
Fire with "J"
Unlock the bolt, draw, push, lock, fire, repeat

Pump Action:
Open the bolt with "V"
Load a single round into the tube with "K"
Load a single round into the chamber with "I"
Close the bolt with "R"
Fire with "J"
Open, close, fire, repeat

Pistol:
Load a magazine with "K"
Rack the slide with "V"
Fire with "J"
Eject magazine with ","