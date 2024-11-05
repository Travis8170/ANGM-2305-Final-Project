# Title
Snake Game Recreation
## Repository
<Link to your project's public GitHub respository>
https://github.com/Travis8170/ANGM-2305-Final-Project

## Description
Aims to be a faithful recreation of the classic Snake game.
I believe it will be a great way to incorporate all the skills I've learned 
this semester.

## Features
- Snake Trail
	- I will take inspiration from the class rain lab to develop the trail.
It should be similar to the particle system that was developed.
The only difference is that it can freely move in any direction.
- Growing Size
	- I will need to implement an apple object in a random spot on the
field. If the head of the trail lands on the same spot as the apple then the
trail should grow. I will also need to make sure the apple doesn't spawn on
an existing part of the trail.
- Score
	- I will keep a counter every time the apple is collected and will
 display it on the screen. The score should grow exponentially.
- Menus
	- Using a counter the player can cycle through menus. Main Menu,
Game Loop, and Game Over. The counter will change depening on key presses.
ie. 0 = Main Menu. Any key press makes counter = 1, and 1 = Game Loop. etc.

## Challenges
- I will need to learn how to create a trail that grows in size.
- I will need to learn how to spawn in an object at a random spot on the grid
  without it spawning on something that already exists.
- I will need to learn how to display text on the screen.

## Outcomes
Ideal Outcome:
- The game will run with all of the aforementioned features. Ideally the game
  should be optimized and bug free. If possible I would like to add powerups
  or other ways that could reimagine the retro game, but is not what I am
  aiming for in this project.

Minimal Viable Outcome:
- A working game loop where the snake moves around based on button inputs.
  The snake should reset when it runs into itself.

## Milestones

- Week 1
  1. Get the snake to exist.
  2. Snake should be able to move around in the grid.

- Week 2
  1. Get the snake to grow. Can be as simple as growing based on button input.
  2. Also implement and display score based on snake size.
  3. Get the Apple to spawn in.

- Week 3 (Final)
  1. Make snake grow on apple contact.
  2. Make apple not spawn where trail already exists.
  3. Implement menu and finalize score system.
  4. General Bug Fixing.
