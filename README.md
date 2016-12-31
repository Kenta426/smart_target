#Smart Target

Simple genetic algorithm project

![](image/screenshot.jpg)

##Background
I was inspired to try out genetic algorithm by myself after watching this [video](https://www.youtube.com/watch?v=qv6UVOQ0F44&t=176s) on YouTube. My initial idea was to install self-driving cars that learn how to avoid collisions; however, in order to decide actions based on the environment where I cannot define fixed length genes, I needed to pass down the weights of neural network as gene. Before tackling with self-driving cars, I decided to practice genetic algorithm on lower complexity.

For this project, this [website](http://www.blprnt.com/smartrockets/) and this [tutorial](https://www.youtube.com/watch?v=bGz7mv2vD6g) were very helpful.



##Objective
Shoot balls from the launcher (bottom left corner in the image above) and try to hit 2 randomly generated targets. The ball will bounce off the first target vertically drawn in the 1st quadrant, and try to hit the second target which is draw horizontally in the 3rd quadrant.

>![](image/target.jpg)



##Design
Gene includes three information:
* Mass of the ball
* The initial x velocity
* The initial y velocity

Therefore the gene is represented by a vector of length 3, and store type float value in each element.

Each generation is a sequence of gene (in default, it is 15)
>![](image/gene.jpg)





##Fitness Function
Here is the pseudo code for the fitness function of this project

```
if the ball does not hit the first target:
  fitness = 1 / distance_from_target1
elif the ball does not hit the second target:
  fitness = 1 + 1 / distance_from_target2
else:
  fitness = 2
```

As shown above, the fitness is 0 - 1 if it does not hit the first target, 1 - 2 if only hits the first target, 2 if the ball hits 2 targets.


##Natural Selection
Usually genes in genetic algorithm are far more complex than the list with the length of 3. Thus, I ran into the issue by the lack of diversity in early generation, meaning, after a few iterations, all value in genes converge to same value and stopped evolving. In order to increase variety in each generation, I took following methods.

####Method 1
#####Step:
1. After each generation, evaluate fitness of each balls.
2. Use Cumulative Distribution Function to pick 2 genes with the best fitness as parents of the next generation. (The bigger the fitness is, the more likely to be picked)
3. Randomly pick a new value from the range of 2 parents. For example, if the mass of parents gene is 5 and 10, pick a random float value in between 5 and 10.
4. Keep this until it creates a new generation

#####Result:
The gene pool will converge to a wrong value and stop evolving after 3 - 5 generations.

####Method 2
#####Step:
1. After each generation, evaluate fitness of each balls.
2. Use Cumulative Distribution Function to pick 2 genes with the best fitness as parents of the next generation. (The bigger the fitness is, the more likely to be picked)
3. Now implement mutation. Randomly generate a number (0 - 1) and if the number is lower than global variable, MUTATION, then create a new random gene with random values of mass, vx, and vy.
3. If it does not mutate, pick a child value from 1 parent with 50% of chance, meaning, if the mass of parents gene is 5 and 10, pick 5 or 10 randomly.
4. Keep this until it creates a new generation

#####Result:
The evolution speed drastically decreased. After hitting the first target, the evolution stops completely. Also, sometimes, the new generation performs worse than the previous one.

####Method 3 (Best method for this project)
#####Step:
1. After each generation, evaluate fitness of each balls.
2. Use Cumulative Distribution Function to pick 2 genes with the best fitness as parents of the next generation. (The bigger the fitness is, the more likely to be picked)
3. Pass down the best performed gene without altering the information (elite gene)
4. Now implement mutation. Randomly generate a number (0 - 1) and if the number is lower than global variable, MUTATION, then create a new random gene with random values of mass, vx, and vy.
5. If it does not mutate, pick a child value from 1 parent with 50% of chance, meaning, if the mass of parents gene is 5 and 10, pick 5 or 10 randomly.
6. Instead of simply using the same value from the parents genes, I added noise to the children, meaning after picking 5 or 10, I added random value from 0 to 1, resulting the child gene to be slightly different from the parents gene.
7. Keep this until it creates a new generation

#####Result:
Due to the step 3, I was able to prevent the model from performing worse than the previous generation. Also by adding a small noise to the parents gene, the generation will adjust to evolve after hitting the first target and keep evolving until they hit the second target as well.

>![](image/selection.jpg)
