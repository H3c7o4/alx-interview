#!/usr/bin/python3

makeChange = __import__('0-making_change').makeChange
import time

# Test 1
coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 100000
start_time = time.time()
result = makeChange(coins, total)
end_time = time.time()
execution_time = end_time - start_time
print(f"The fewest number of coins needed to make change for {total} is: {result}")
print(f"Execution time: {execution_time} seconds")

# Test 2
coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 1000000
start_time = time.time()
result = makeChange(coins, total)
end_time = time.time()
execution_time = end_time - start_time
print(f"The fewest number of coins to make change for {total} is: {result}")
print(f"Execution time: {execution_time} seconds")

# Test 3
coins = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
total = 2000000
start_time = time.time()
result = makeChange(coins, total)
end_time = time.time()
execution_time = end_time - start_time
print(f"The fewest number of coins needed to make change for {total} is: {result}")
print(f"Execution time: {execution_time} seconds")
