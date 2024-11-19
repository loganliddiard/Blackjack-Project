import blackjack
import strategy

import matplotlib.pyplot as plt

## Runs optimal stopping algorithms.

def optimal_hit(game):
    print("Running simulation to find point to stop hitting...")
    results=0
    rounds = 1_000_000
    max_win_streak = 0
    win_counts = []

    for val in range(0,20):
        player = strategy.CustomPlaystyle(val)
        results = 0
        streak = 0
        max_win_streak = 0
        for i in range(0,rounds):
            #print(f"Game number: {i}")
            result = game.play_blackjack(player)
            results += result
            
            if result == 1:
                streak +=1
            else: streak = 0
            max_win_streak = max(streak,max_win_streak)

        print(f"max win streak: {max_win_streak}")    

        win_counts.append(results)

    # Plot the data
    plt.plot(win_counts)
    plt.show()


    print(f"Here are the results after {rounds} rounds: {results}")

def optimal_leave(game, player, rounds=1_000):
    print("Running simulation to find the best point to leave the table...")
    
    results = []
    
    for stop_exploring in range(rounds):
        max_wins = 0
        wins = 0
        for j in range(rounds):
            result = game.play_blackjack(player)  # Simulate a blackjack round
            wins += result
            
            if j < stop_exploring:  # Exploration phase
                max_wins = max(max_wins, wins)
            else:  # Exploitation phase
                if wins > max_wins:  # Found a better stopping point
                    results.append(wins)
                    break
        else:
            # Append the final result if no better stopping point was found
            results.append(wins)
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(range(rounds), results, label="Winnings at Optimal Stop", color="blue")
    plt.axhline(y=0, color="red", linestyle="--", label="Break Even")
    plt.xlabel("Exploration Rounds")
    plt.ylabel("Total Winnings")
    plt.title("Optimal Stopping Simulation for Blackjack")
    plt.legend()
    plt.grid(True)
    plt.show()



# Determines if the game prints to console or not
def run_optimalstop():
    mute = True
    game = blackjack.BlackJackGame(mute)

    #optimal_hit(game)

    player = strategy.CustomPlaystyle(15)
    optimal_leave(game,player)




    