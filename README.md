#Smart Target

Simple genetic algorithm project

<<<<<<< HEAD
![](image/screenshot.jpg)

##Background
I was inspired to try out genetic algorithm by myself after watching this [video](https://www.youtube.com/watch?v=qv6UVOQ0F44&t=176s) on YouTube. My initial idea was to install self-driving cars that learn how to avoid collisions; however, in order to decide actions based on the environment where I cannot define fixed length genes, I needed to pass down the weights of neural network as gene. Before tackling with self-driving cars, I decided to practice genetic algorithm on lower complexity.

For this project, this [website](http://www.blprnt.com/smartrockets/) and this [tutorial](https://www.youtube.com/watch?v=bGz7mv2vD6g) were very helpful.

##Objective
Shoot balls from the launcher (bottom left corner in the image) and try to hit 2 randomly generated targets.

##Design
Gene includes three information:
* Mass of the ball
* The initial x velocity
* The initial y velocity

Therefore the gene is represented by a vector of length 3, and store type float value in each element.
=======
![Screen Shot](image/screenshot.jpg)
>>>>>>> 56a364abd779506364070cad58c2cdadd3b39a9c
