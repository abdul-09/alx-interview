#!/usr/bin/python3

def isWinner(x, nums):
    # Define a nested function to calculate the winner for each round
    def calculateWinner(n):
        # If only one number is left, Ben wins
        if n == 1:
            return "Ben"

        # Use the Sieve of Eratosthenes to mark primes up to n
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        p = 2
        # Mark non-prime numbers
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1

        # Simulate the game to determine the winner
        maria_turn = True
        while True:
            can_remove = False
            for i in range(2, n + 1):
                if primes[i] and n % i == 0:
                    can_remove = True
                    n -= i
                    break
            if not can_remove:
                break
            maria_turn = not maria_turn

        # Return the winner of the game
        if maria_turn:
            return "Ben"  # If Maria can't make a move, Ben wins
        else:
            return "Maria"

    # Initialize counters for Maria and Ben's wins
    maria_wins = 0
    ben_wins = 0

    # Loop through each round specified in nums
    for n in nums:
        # Calculate the winner for the current round
        winner = calculateWinner(n)
        # Update the wins counter based on the winner
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    # Determine the overall winner based on the number of wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # If the winner cannot be determined
