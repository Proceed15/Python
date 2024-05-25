#Time & Pyplot
import random
import time
import matplotlib.pyplot as plt

def typing_game():
    print("Welcome to the Typing Speed Game!")
    input("Press Enter to start...")
    round_number = 1
    all_round_times = []
    mistakes = 0

    while round_number in range(1, 6):
        word_list = ["python", "programming", "challenge", "keyboard", "speed", "accuracy", "coding", "practice", "learning", "fun"]
        round_times = []
        target_word = random.choice(word_list)
        print("\nRound", round_number)
        print("Type the word", target_word, "5 times.")

        for sequence_number in range(1, 6):
            print(f"\nSequence Number {sequence_number}. ")
            
            start_time = time.time()
            user_input = input("Your typing: ")
            end_time = time.time()

            round_time = end_time - start_time
            round_times.append(round_time)
            print(f"Done! Time taken: {round_time:.2f} seconds")
            if(user_input.lower() != target_word):
                mistakes += 1

        total_time = sum(round_times)
        print(f"Total time for this round: {total_time:.2f} seconds")
        all_round_times.append(round_times)
        round_number += 1
        

    print("\nGame Over! You made " + str(mistakes) + " mistakes(s).")
    print("\nHere's a chart about your evolution during these rounds.")
    time.sleep(3)
    
    # Create a bar chart
    for i, round_times in enumerate(all_round_times, start=1):
        plt.bar(range(1, 6), round_times, label=f"Round {i}")

    plt.xlabel('Sequence Number')
    plt.ylabel('Time (seconds)')
    plt.title('Typing Speed Evolution')
    plt.legend()
    plt.xticks(range(1, 6), [f"Sequence {j}" for j in range(1, 6)])
    plt.show()

# Run the game
typing_game()
'''
import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0

print("This program will help you type faster.")
print("You will have to type the word 'programming' as fast as you can for five times.")
input("Press enter to continue.")

while len(times) < 5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if(word.lower() != "programming"):
        mistakes += 1

print("You made " + str(mistakes) + " mistake(s).")
print("Now let's see your evolution.")
t.sleep(3)

x = [1,2,3,4,5]
y = times
plt.plot(x,y)
legend = ["1", "2", "3", "4", "5"]
plt.xticks(x,legend)
plt.ylabel('Time in seconds')
plt.xlabel('Attempts')
plt.title('Your typing evolution')
plt.show()
'''
'''
#Time & Pyplot
import random
import time
import matplotlib.pyplot as plt

def typing_game():
    word_list = ["python", "programming", "challenge", "keyboard", "speed", "accuracy", "coding", "practice", "learning", "fun"]
    print("Welcome to the Typing Speed Game!")
    input("Press Enter to start...")
    round_number = 1

    while round_number in range(1, 6):
        word_list = ["python", "programming", "challenge", "keyboard", "speed", "accuracy", "coding", "practice", "learning", "fun"]
        total_time = 0
        target_word = random.choice(word_list)
        print("\nRound", round_number)
        print("Type the word", {target_word}, "5 times.")

        for sequence_number in range(1, 6):
            print(f"\nSequence Number {sequence_number}. ")
            
            start_time = time.time()
            user_input = input("Your typing: ")
            end_time = time.time()

            round_time = end_time - start_time
            total_time += round_time
            #print(f"Done! Time taken: {round_time:.2f} seconds")
        print(f"Total time for this round: {total_time:.2f} seconds")
        round_number+=1

# Run the game
typing_game()
print("\nGame Over!")
'''
