import random 

with open("hangman\sowpods.txt", mode="r") as file:
    words = list(file.readlines())
    random_word = random.choice(words)
    print(random_word)
    mixed_random_word = "".join(random.sample(random_word, len(random_word)))
    chances = 6
    while True:
        print(mixed_random_word)
        guess = str(input() + "\n").upper()
        if chances == 1:
            print("Haha you lost")
            break
        elif guess == random_word:
            print("Wow you found it")
            break 
        else:
            guess = str(input("Try again") + "\n").upper()
            chances -=1
        
    
    # 
    # if guess == words[120]:
    #     print("Worked")
    # else:
    #     print("oh no")
