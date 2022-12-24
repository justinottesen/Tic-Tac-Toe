# Tic-Tac-Toe
by Justin Ottesen

Recreation of my first ever coding project, which was a Tic-Tac-Toe game,
which had multiple gamemodes (Singleplayer, Multiplayer, and Simulation),
and multiple difficulties, ranging from random choice, to mathematical
perfection.

The first version of this project was completed over March and April of 2021.
It was much more thorough than this one, however I did not save my code online,
and it was lost when my computer died. I got bored over Winter Break of 2022,
and decided to recreate it, which only took a few hours of messing around.

The implementation of the game itself is rather straightforward, players choose
open squares to go in until either of them win, or there are no squares left.
The part where this gets interesting is the opponent. I only decided to
implement the perfect bot for this project.

This uses the MiniMax algorithm, which recursively generates all possible
outcomes from the current position, and assumes perfect play from each player.
It assigns a score to each position, with one player maximizing and one player
minimizing, and chooses the next move which generates the best outcome score
based on the player's goal.

This algorithm is incredibly slow especially at the beginning of the game, so
I implemented some easy optimizations. First, if a win is found for a player,
it stops searching, because it doesn't need to know multiple ways to win. 

This has some slight performance boost, but the biggest timesave was by
implemeting a dictionary to store the positions and their scores. This got rid
of many repeated calculations, espcecially when running multiple games through
the simulation. On my machine, the first game takes about 0.04 seconds, while 
the second game only takes 0.0003 seconds, which is about 10 times faster.

The Menu and gamemodes were scrapped together rather quickly, I didn't feel
like spending that much time on them, this is really just me trying to start
puting my projects on GitHub, because I have many incomplete projects sitting
on my computer.
