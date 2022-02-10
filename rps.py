#rps.py
# rock paper scissors made by ttheholyone

import random



def main():
    items = ['rock', 'paper', 'scissors']
    items = random.choice(items)
    print("Choose a item:\nRock = r\nPaper = p\nScissors = s")
    item = input("Which item? ")




    if items == 'rock' and item == 's':
        print("Loser! Computer chose rock!")

    elif items == 'paper' and item == 'r':
        print("Loser! Computer chose paper!")

    elif items == 'scissors' and item == 'p':
        print("Loser! Computer chose scissors!")
    elif items == 'rock' and item == 'p':
        print("Winner! Computer chose rock!")

    elif items == 'paper' and item == 's':
        print("Winner! Computer chose paper!")

    elif items == 'scissors' and item == 'r':
        print("Winner! Computer chose scissors!")

    elif items == 'rock' and item == 'r':
        print("Tie! Computer chose rock!")

    elif items == 'paper' and item == 'p':
        print("Tie! Computer chose paper!")

    elif items == 'scissors' and item == 's':
        print("Tie! Computer chose scissors;")


main()

while True:
    qr = input("1: Quit\n2: Restart\n")
    if qr == '1':
        quit()
    elif qr == '2':
        main()
