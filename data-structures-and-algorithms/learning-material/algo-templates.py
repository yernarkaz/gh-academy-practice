from collections import deque

# Common patterns and templates for medium-level LeetCode problems

# 1. Two Pointers (e.g., for array, string processing)


def two_pointers_template(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None


# 2. Sliding Window (e.g., for subarray problems)


def sliding_window_template(nums, k):
    window_sum = 0
    start = 0
    max_sum = float("-inf")
    for end in range(len(nums)):
        window_sum += nums[end]
        if end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[start]
            start += 1
    return max_sum


# 3. Depth-First Search (DFS) for Graph or Tree (recursive approach)


def dfs_template(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_template(graph, neighbor, visited)
    return visited


# 4. Breadth-First Search (BFS) for Graph or Tree (iterative approach)


def bfs_template(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


# 5. Dynamic Programming (e.g., for classic DP problems)


def dp_template(n):
    dp = [0] * (n + 1)
    # Initialize base cases
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# 6. Binary search


def binary_search_template(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


"How can we handle edge cases for each template?",
"Which data structures pair best with these approaches?",
"How can each template be optimized further?",
"When might we choose a recursive versus an iterative approach?",
"How do we handle large inputs or memory constraints in these patterns?",


"""
1. Two Pointers: Check if the array has fewer than two elements.
2. Sliding Window: Ensure k <= len(nums) and handle empty input.
3. DFS: Handle empty graph or a start node not in the graph.
4. BFS: Same as DFS, plus check if start node exists.
5. DP: Validate n >= 0 and handle large n carefully.
"""

{
    "Two Pointers": ["Arrays", "Lists"],
    "Sliding Window": ["Arrays", "Lists", "Deque"],
    "DFS": ["Stacks", "Recursion", "Adjacency List/Table"],
    "BFS": ["Queues", "Deque", "Adjacency List/Table"],
    "DP": ["Arrays", "2D Tables"],
}


{
    "Two Pointers": "Sort if needed, break early when conditions are met.",
    "Sliding Window": "Use prefix sums or a deque to handle complex shifts efficiently.",
    "DFS": "Consider iterative DFS to avoid recursion overhead; use adjacency lists.",
    "BFS": "Use an adjacency list and mark visited efficiently to prevent repeats.",
    "DP": "Reduce space by only storing recent states if possible, or memoize selectively.",
}


"""
Use recursion when the problem has a natural tree or divide-and-conquer structure
and code clarity is prioritized. Use iteration when memory constraints or
large input sizes make recursion depth a concern, or when performance optimizations
like tail recursion elimination aren't available.
"""


"""
Tips for handling large inputs or memory constraints in common patterns:
    1) Use streaming or chunked data processing with two-pointer or sliding
        window approaches to avoid loading the entire dataset at once.
    2) For graph traversals, use adjacency lists and iterative methods where
        possible to reduce recursion depth and memory usage.
    3) In DP, optimize by storing only the states needed at each step and
        consider space-saving techniques like rolling arrays.
"""


"Process data in smaller chunks to limit memory usage."
"Explore iterative solutions over recursive ones to avoid stack limits."
"Use lazy evaluation and data streaming where relevant."
"Adopt space-optimized DP or specialized data structures for large data."
