# Blackjack

## Team Members:
* Kaden Hart
* Logan Liddiard


## Project Overview

This project focuses on applying the algorithms focusing on uncertainty across the game Blackjack scenarios. There were three main parts:

1. Exploring the use of optimal stopping algorithms in blackjack
2. Determining if the epsilon-greedy and thompson sampling algorithm can find the optimal table to play at (with different #decks)
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

While inside the same directory as `main.py` run:

`python main.py`


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

### Which table is the best? Do different amounts of decks matter?

We used Thompson sampling and an epsilon greedy algorithm to explore tables with different amounts of decks. We tested epsilon values of [0.01, 0.05, 0.1, 0.4], and deck sizes of [1, 2, 4, 6, 8]. We let it run for 1000 episodes/games, and then averaged the results over 1000 iterations.

<p align="center">
  <img src="figures/overall_performance.png" alt="comparing_all_strats">
</p>

Every epsilon value/thompson sampling and deck combination converged in similar amounts of time and to very similar win ratios. Thompson sampling seems to have converged the fastest. There is about a ~0.5% spread in win ratios in all of the deck and technique combinations. Our plot indicates that the epsilon of 0.4 seems to have the highest converged win ratio, whole e=0.1 was the lowest. thompson sampling did the same as e=.05 & e=.1. However, most if not all of this variability could be explained by not running enough iterations, but it would take a very long time to run significantly higher amounts.

<p align="center">
  <img src="figures/deck_performance.png" alt="strategy convergence">
</p>

We averaged the amount of wins for each deck across all runs. Each deck performed exactly the same. It is apparent that having different amounts of decks does not effect winning chances by typical strategies. Higher amounts of decks are most likely just to discourage card counting, which is considered cheating. These results aren't surprising to us, because each deck count will have the same proportion of all cards.

### How many decks is most profitable? Which strategy for exploring is best?

The results are all very close, it seems like the number of decks doesn't effect profitability with typical strategies, but probably make card counting much harder to do. Our plot shows the epsilon greedy e=.4 is the best strategy, however, this is almost certainly an artifact of not doing enough runs, because the win probabilities of each table seem to be exactly the same. Using higher iterations would make each technique converge to closer values, but this would take forever to run, at least on our cpus single-threaded.