Aim: 
The aim of this program is to implement three different approaches to solving the knapsack problem and analyze their time complexity for different input sizes.

Description
	Problem Statement
The knapsack problem is a classic optimization problem where the goal is to maximize the total value of items that can be included in a knapsack without exceeding its capacity. This program implements three different approaches to solving the knapsack problem:
1.	Sorting items based on weights and filling the knapsack.

	Method Used
The methods used are variations of the greedy algorithm for the knapsack problem. Each approach sorts the items differently before selecting items to include in the knapsack based on specific criteria.
Algorithm
knapsack(values, weights, W):
    n = len(values)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

Time Complexity: 
Approach 1: Sorting items based on weights
o	Best Case: O(n log n)
o	Average Case: O(n log n)
o	Worst Case: O(n log n)





