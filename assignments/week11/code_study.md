### Template for Code Reading Exercise

#### 1. Where did you find the code and why did you choose it? (Provide the link)

I found the code on github.com, when looking for pygame code, as Im planning to da an action game using the library myself. 
It stood out to me as it was highly rated, well organized and met the requirement of 100 lines. 

https://github.com/attreyabhatt/Space-Invaders-Pygame/blob/master/main.py

#### 1. What does the program do? What's the general structure of the program? 

This is a 2D game, where you control a spacecraft at the bottom of the screen and are able to move it around and shoot bullets at enemies. 
You score when hitting them and the program keeps track of your score. You move using your arrow keys and shoot bullets with the space bar. 

The general structure looks the following:
1. Initialization: Importing libraries, creating the background screen and sound.
2. Loading assets: images of player and enemies, bullet. 
3. Functions: Shooting bullets, detecting colliions, keeping score
4. Main loop: movement input, enemy movement, collision animation. 


#### 1. Function analysis: pick one function and analyze it in detail:
I choose the Collision function

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

- What does this function do? 
  - The function detects whether there has been an collision between a bullet and the enemy. 
- What are the inputs and outputs?
  - Inputs are the current locations of both the enemies and bullets in XY-Coordinates. 
- How does it work (step by step)?
  - 1. The distance is measured by adding the difference between both the X-Coordinates (enemyX, bulletX) and the Y-coordinates (enemyY, bulletY)
  - 2. the function decides by using a simple if-else function. If the result is under 27, the value is set to True, meaning it detects a collision. Otherwise if it is over 27, the value is set to False and we do not have a collision. 


---

#### Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)

- definetly structure. Because the code was so well structured, it was rather easy to follow and helped understanding the ideas. 
- The Use of all the Helper Functions was a good way of keeping it organized and reusing parts of the code. 
- The use of lists to handle several enemies at the same time was a very smart way of doing so. I will probably use this as well in my project. 

#### What parts of the code were confusing or difficult at the beginning to understand?
#### Were you able to understand what it is doing after your own research?

- I struggled to understand, why the data on the enemies was stored in lists in the beginning. It took me a while to understand the possibilities to better scale for more enemies at the same time. 

---

Extra notes