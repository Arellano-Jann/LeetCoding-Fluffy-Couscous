# Problem 1
Given an array a, your task is to apply the following mutation to it:

Array a mutates into a new array b of the same length

For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]

If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it is considered to be 0
For example, b[0] equals 0 + a[0] + a[1]

Example

For a = [4, 0, 1, -2, 3], the output should be solution(a) = [4, 5, -1, 2, 1].

Explanation:

b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4

b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5

b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1

b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2

b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1

So, the mutated answer array is [4, 5, -1, 2, 1].


# Problem 2

Given an array of integers a, your task is to count the number of pairs i and j (where 0 ≤ i < j < a.length), such that a[i] and a[j] are digit anagrams.

Two integers are considered to be digit anagrams if they contain the same digits. In other words, one can be obtained from the other by rearranging the digits (or trivially, if the numbers are equal). 

For example, 54275 and 45572 are digit anagrams, but 321 and 782 are not (since they don't contain the same digits). 220 and 22 are also not considered as digit anagrams, since they don't even have the same number of digits.

Example

For a = [25, 35, 872, 228, 53, 278, 872], the output should be solution(a) = 4.

There are 4 pairs of digit anagrams:

a[1] = 35 and a[4] = 53 (i = 1 and j = 4),

a[2] = 872 and a[5] = 278 (i = 2 and j = 5),

a[2] = 872 and a[6] = 872 (i = 2 and j = 6),

a[5] = 278 and a[6] = 872 (i = 5 and j = 6).

Input/Output

[execution time limit] 6 seconds (py3)


# Problem 3

You are given a matrix of integers field of size n × m representing a game field, and also a matrix of integers figure of size 3 × 3 representing a figure. Both matrices contain only 0s and 1s, where 1 means that the cell is occupied, and 0 means that the cell is free.

You choose a position at the top of the game field where you put the figure and then drop it down. The figure falls down until it either reaches the ground (bottom of the field) or lands on an occupied cell, which blocks it from falling further. After the figure has stopped falling, some of the rows in the field may become fully occupied.

demonstration

Your task is to find the dropping position such that at least one full row is formed. As a dropping position you should consider the column index of the cell in game field which matches the top left corner of the figure 3 × 3 matrix. If there are multiple dropping positions satisfying the condition, feel free to return any of them. If there are no such dropping positions, return -1.

Note: When falling, the 3 × 3 matrix of the figure must be entirely inside the game field, even if the figure matrix is not totally occupied.

Example

For
```
field =  [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [1, 0, 0],
          [1, 1, 0]]
and

figure = [[0, 0, 1],
          [0, 1, 1],
          [0, 0, 1]]
```
the output should be solution(field, figure) = 0.

The figure can be dropped only from position 0. When the figure stops falling, two fully occupied rows are formed, so dropping position 0 satisfies the condition.

example 1

For
```
field =  [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [1, 1, 0, 1, 0],
          [1, 0, 1, 0, 1]]
and

figure = [[1, 1, 1],
          [1, 0, 1],
          [1, 0, 1]]
```
the output should be solution(field, figure) = 2.

The figure can be dropped from three positions - 0, 1, and 2. As you can see below, a fully occupied row will be formed only when dropping from position 2:

example 2

For
```
field =  [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 1],
          [1, 1, 0, 1]]
and

figure = [[1, 1, 0],
          [1, 0, 0],
          [1, 0, 0]]

```
the output should be solution(field, figure) = -1.

The figure can be dropped from two positions - 0 and 1, and in both cases, a fully occupied line won't be obtained:

example 3

Note that the figure could technically form a full row if it was dropped one position further to the right, but in that case the figure matrix wouldn't be fully contained with the field.

# Problem 4

Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. Return the array of these digits in ascending order.

Example

For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2, 3, 5].