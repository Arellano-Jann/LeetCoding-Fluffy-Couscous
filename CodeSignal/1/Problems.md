# Problem 1
You are given an array of integers numbers and two integers left and right. You task is to calculate a boolean array result, where result[i] = true if there exists an integer x, such that numbers[i] = (i + 1) * x and left ≤ x ≤ right. Otherwise, result[i] should be set to false.

Example

For numbers = [8, 5, 6, 16, 5], left = 1, and right = 3, the output should be solution(numbers, left, right) = [false, false, true, false, true].

For numbers[0] = 8, we need to find a value of x such that 1 * x = 8, but the only value that would work is x = 8 which doesn't satisfy the boundaries 1 ≤ x ≤ 3, so result[0] = false.

For numbers[1] = 5, we need to find a value of x such that 2 * x = 5, but there is no integer value that would satisfy this equation, so result[1] = false.

For numbers[2] = 6, we can choose x = 2 because 3 * 2 = 6 and 1 ≤ 2 ≤ 3, so result[2] = true.

For numbers[3] = 16, there is no an integer 1 ≤ x ≤ 3, such that 4 * x = 16, so result[3] = false.

For numbers[4] = 5, we can choose x = 1 because 5 * 1 = 5 and 1 ≤ 1 ≤ 3, so result[4] = true.

# Problem 2
Given two strings s and t, both consisting of lowercase English letters and digits, your task is to calculate how many ways exactly one digit could be removed from one of the strings so that s is lexicographically smaller than t after the removal. Note that we are removing only a single instance of a single digit, rather than all instances (eg: removing 1 from the string a11b1c could result in a1b1c or a11bc, but not abc).

Also note that digits are considered lexicographically smaller than letters.

Example

For s = "ab12c" and t = "1zz456", the output should be solution(s, t) = 1.

Here are all the possible removals:

We can remove the first digit from s, obtaining "ab2c". "ab2c" > "1zz456", so we don't count this removal

We can remove the second digit from s, obtaining "ab1c". "ab1c" > "1zz456", so we don't count this removal

We can remove the first digit from t, obtaining "zz456". "ab12c" < "zz456", so we count this removal

We can remove the second digit from t, obtaining "1zz56". "ab12c" > "1zz56", so we don't count this removal

We can remove the third digit from t, obtaining "1zz46". "ab12c" > "1zz46", so we don't count this removal

We can remove the fourth digit from t, obtaining "1zz45". "ab12c" > "1zz45", so we don't count this removal

The only valid case where s < t after removing a digit is "ab12c" < "zz456". Therefore, the answer is 1.

For s = "ab12c" and t = "ab24z", the output should be solution(s, t) = 3.

There are 4 possible ways of removing the digit:

"ab1c" < "ab24z"
"ab2c" > "ab24z"
"ab12c" < "ab4z"
"ab12c" < "ab2z"

Three of these cases match the requirement that s < t, so the answer is 3.

# Problem 3
Minesweeper is a popular single-player computer game. The goal is to locate mines within a rectangular grid of cells. At the start of the game, all of the cells are concealed. On each turn, the player clicks on a blank cell to reveal its contents, leading to the following result:

If there's a mine on this cell, the player loses and the game is over;

Otherwise, a number appears on the cell, representing how many mines there are within the 8 neighbouring cells (up, down, left, right, and the 4 diagonal directions);

If the revealed number is 0, each of the 8 neighbouring cells are automatically revealed in the same way.

You are given a boolean matrix field representing the distribution of bombs in the rectangular field. You are also given integers x and y, representing the coordinates of the player's first clicked cell - x represents the row index, and y represents the column index, both of which are 0-based.

Your task is to return an integer matrix of the same dimensions as field, representing the resulting field after applying this click. If a cell remains concealed, the corresponding element should have a value of -1.

It is guaranteed that the clicked cell does not contain a mine.

# Problem 4
Given an array of unique integers numbers, your task is to find the number of pairs of indices (i, j) such that i ≤ j and the sum numbers[i] + numbers[j] is equal to some power of 2.

Note: numbers 20 = 1, 21 = 2, 22 = 4, 23 = 8, etc. are considered to be powers of 2.

Example

For numbers = [1, -1, 2, 3], the output should be solution(numbers) = 5.

There is one pair of indices where the corresponding elements sum up to 20 = 1:
(1, 2): numbers[1] + numbers[2] = -1 + 2 = 1

There are two pairs of indices where the corresponding elements sum up to 21 = 2:
(0, 0): numbers[0] + numbers[0] = 1 + 1 = 2
(1, 3): numbers[1] + numbers[3] = -1 + 3 = 2

There are two pairs of indices where the corresponding elements sum up to 22 = 4:
(0, 3): numbers[0] + numbers[3] = 1 + 3 = 4
(2, 2): numbers[2] + numbers[2] = 2 + 2 = 4

In total, there are 1 + 2 + 2 = 5 pairs summing up to powers of two.

For numbers = [2], the output should be solution(numbers) = 1.

The only pair of indices is (0, 0) and the sum of corresponding elements is equal to 22 = 4. So, the answer is 1.

For numbers = [-2, -1, 0, 1, 2], the output should be solution(numbers) = 5.

There are two pairs of indices where the corresponding elements sum up to 20 = 1: (2, 3) and (1, 4)

There are two pairs of indices where the corresponding elements sum up to 21 = 2: (2, 4) and (3, 3)

There is one pair of indices where the corresponding elements sum up to 22 = 4: (4, 4)

In total, there are 2 + 2 + 1 = 5 pairs summing up to powers of 2

