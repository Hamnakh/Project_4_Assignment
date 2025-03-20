import random  # random module ko import karna zaroori hai

DONE_LIKELIHOOD = 0.2  # Ek probability value (0 to 1 ke beech)

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # Function ko yahin rok dena agar done() True return kare
        print(curr_num)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:  # DONE_LIKELIHOOD ka use
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
