# Prime Game

This project involves solving a competitive game scenario where the winner is determined by strategically removing prime numbers and their multiples from a set of consecutive integers.

## Concepts Needed

To successfully tackle this project, you will need to have a solid understanding of the following concepts:

- Prime Numbers: Understanding what prime numbers are and efficient algorithms for identifying them within a range.
- Sieve of Eratosthenes: An efficient algorithm for finding all prime numbers up to a given limit.
- Game Theory: Basic principles of competitive games, optimal play, and win conditions.
- Dynamic Programming/Memoization: Using previous results to make future calculations faster.
- Python Programming: Loops, conditional statements, arrays, and lists for implementing game logic and algorithms.

## Resources

To enhance your understanding of the concepts mentioned above, you can refer to the following resources:

- [Khan Academy: Prime Numbers](https://www.khanacademy.org/math/cc-fourth-grade-math/imp-factors-multiples-and-patterns/imp-prime-and-composite-numbers/v/prime-numbers): Introduction to prime numbers.
- [Sieve of Eratosthenes in Python](https://www.geeksforgeeks.org/sieve-of-eratosthenes/): A step-by-step guide to implementing the sieve algorithm in Python.
- [Game Theory Introduction](https://www.investopedia.com/terms/g/gametheory.asp): A simple explanation of game theory and strategic decision-making.
- [Dynamic Programming with Python Examples](https://skerritt.blog/dynamic-programming/): An introduction to dynamic programming with Python examples.
- Python Official Documentation: Useful for managing lists in Python, which is important for tracking the game state.

## Task: Prime Game

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

Your task is to implement the function `isWinner(x, nums)` which takes the number of rounds `x` and an array of `n` values. The function should return the name of the player that won the most rounds. If the winner cannot be determined, return `None`. You can assume that `n` and `x` will not be larger than 10000, and you cannot import any packages in this task.

### Example

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
Example:

x = 3, nums = [4, 5, 1]
First round: 4

Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose
Second round: 5

Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose
Third round: 1

Ben wins because there are no prime numbers for Maria to choose
Result: Ben has the most wins
