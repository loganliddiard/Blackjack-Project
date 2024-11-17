import blackjack
import strategy

import matplotlib.pyplot as plt
# Run the game

# Determines if the game prints to console or not
mute = True
game = blackjack.BlackJackGame(mute)



results=0

rounds = 1_000_000

max_win_streak = 0
win_counts = []

for val in range(0,20):
    player = strategy.Classic_Playstyle(val)
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