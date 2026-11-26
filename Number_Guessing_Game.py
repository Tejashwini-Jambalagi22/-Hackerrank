'''Build a number guessing game

Program requirements:
1. Store a secret number, such as 7.
2. Ask the user to guess the number.
3. If the guess is too high, display Too high.
4. If it is too low, display Too low.
5. If correct, display Congratulations!.
6. Count the number of attempts.


Example:'''



secret = 7
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Congratulations!")
        print("Attempts:", attempts)
        break
