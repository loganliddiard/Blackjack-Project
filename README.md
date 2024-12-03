# Blackjack

## Team Members:
* Kaden Hart
* Logan Liddiard


## Project Overview

This project focuses on applying the algorithms focusing on uncertainty across the game Blackjack scenarios. There were three main parts:

1. Exploring the use of optimal stopping algorithms in blackjack
2. Determining if epsilon-greedy algorithm can find the optimal table to play at
3. Seeing if reinforcement learning algorithms can find improved strategies

## Requirements:

* Python 3.x
* Required packages: `numpy`, `scipy`, `matplotlib`, `seaborn`
These can be installed by running:
```
pip install numpy scipy matplotlib seaborn
```

## How to run:

The main python file for submission is `main.py`



## Optimal Stop

### When to stop hitting?

We had this algorithm play 100,000 rounds of blackjack for each point it could stop on (1-20) using an optimal strategy and tried to find the optimal point to hitting on was

Through the different runs of this algoritm most often it was a fight between 15 and 16. This disproves the beleive that  some people think the optimal point to stop hitting on is, which is 12 in a lot of cases

<p align="center">
  <img src="figures/simple_optimal_stophit.png" alt="optimal_hit">
</p>


### When to leave the table?

We had this algorithm play 1000 rounds of blackjack using an optimal strategy and tried to find the optimal point to stop exploring was.

Across different runs of this algorithm the common theme amongst them is to stop exploring sooner rather than later. The optimal point to stop exploring and leave when you either break even or surpass your maximum amount seems to be around round 50-100. The longer you play the more you ned up losing on average as seen in the graph below.


<p align="center">
  <img src="figures/simple_optimal_leave.png" alt="optimal_leave">
</p>


