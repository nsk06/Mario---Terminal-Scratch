# Mario---Terminal-Scratch
"Hey Welcome to my game."
This game is written in python3 and uses only core packages along with numpy and colorama
Controls:
To start you should run start.py where it greets you with intro sound.
On pressing "p" it takes you to main game which is in play.py 
The controls are:
a:left move
d:right move
q:quit
sw:vertical jump
dw:right jump
aw:left jump
Feautres:
The game has 2 levels each with obstacles,colours,sounds,coins,lifeadders,different enemies and extreme fun.
Sound has been added using os module and it is done in background using &.
Colors on start screen using colorama rest are done through ansi escape characters.
Mario can jump as per control and identical to gravity situations.
Mario can collect coins from "$" symbols upto a fixed no. of times.
There are two type of enemies one simple and another boss(in level 2).
Simple enemies can be killed using bullets or by stomping them while boss can be killed only by bullets.
Both have different speed and lives.
The boss enemy and some simple enemies have feauture of following the Mario(smart)
Each enemy is spawned on the visible screen only.
Boss enemy cant fall in pit and is represented differently also.
The background is moving identical to original game.
Different levels have different enemy speed and movement
Files:
sounds consist of sounds used
start is start screen
board contains the description of board
people consist of various persons in game
objects consist of various objects in game
takeinput is used for taking input from user
color is used for color ansi characters
getch is also used for taking inputs
play consist of main game
requirement consist of requirements for running the game
