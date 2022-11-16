https://stackoverflow.com/questions/5218895/python-nested-functions-variable-scoping

# Problem 1

Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.

Given an array of integers numbers, your task is to check all the triples of its consecutive elements for being a zigzag. More formally, your task is to construct an array of length numbers.length - 2, where the ith element of the output array equals 1 if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.

Example

For numbers = [1, 2, 1, 3, 4], the output should be solution(numbers) = [1, 1, 0].

(numbers[0], numbers[1], numbers[2]) = (1, 2, 1) is a zigzag, because 1 < 2 > 1;

(numbers[1], numbers[2] , numbers[3]) = (2, 1, 3) is a zigzag, because 2 > 1 < 3;

(numbers[2], numbers[3] , numbers[4]) = (1, 3, 4) is not a zigzag, because 1 < 3 < 4;

For numbers = [1, 2, 3, 4], the output should be solution(numbers) = [0, 0];

Since all the elements of numbers are increasing, there are no zigzags.

For numbers = [1000000000, 1000000000, 1000000000], the output should be solution(numbers) = [0].

Since all the elements of numbers are the same, there are no zigzags.


# Problem 2

You are given two arrays of integers a and b of the same length, and an integer k. We will be iterating through array a from left to right, and simultaneously through array b from right to left, and looking at pairs (x, y), where x is from a and y is from b. Such a pair is called tiny if the concatenation xy is strictly less than k.

Your task is to return the number of tiny pairs that you'll encounter during the simultaneous iteration through a and b.

Example

For a = [1, 2, 3], b = [1, 2, 3], and k = 31, the output should be

solution(a, b, k) = 2.

We're considering the following pairs during iteration:

(1, 3). Their concatenation equals 13, which is less than 31, so the pair is tiny;

(2, 2). Their concatenation equals 22, which is less than 31, so the pair is tiny;

(3, 1). Their concatenation equals 31, which is not less than 31, so the pair is not tiny.

As you can see, there are 2 tiny pairs during the iteration, so the answer is 2.


For a = [16, 1, 4, 2, 14], b = [7, 11, 2, 0, 15], and k = 743, the output should be

solution(a, b, k) = 4.

We're considering the following pairs during iteration:

(16, 15). Their concatenation equals 1615, which is greater than 743, so the pair is not tiny;

(1, 0). Their concatenation equals 10, which is less than 743, so the pair is tiny;

(4, 2). Their concatenation equals 42, which is less than 743, so the pair is tiny.

(2, 11). Their concatenation equals 211, which is less than 743, so the pair is tiny;

(14, 7). Their concatenation equals 147, which is less than 743, so the pair is tiny.

There are 4 tiny pairs during the iteration, so the answer is 4.



# Problem 3
You are given an array of arrays a. Your task is to group the arrays a[i] by their mean values, so that arrays with equal mean values are in the same group, and arrays with different mean values are in different groups.

Each group should contain a set of indices (i, j, etc), such that the corresponding arrays (a[i], a[j], etc) all have the same mean. Return the set of groups as an array of arrays, where the indices within each group are sorted in ascending order, and the groups are sorted in ascending order of their minimum element.

Example

For
```
a = [[3, 3, 4, 2],
     [4, 4],
     [4, 0, 3, 3],
     [2, 3],
     [3, 3, 3]]
```
the output should be
```
solution(a) = [[0, 4],
                 [1],
                 [2, 3]]
mean(a[0]) = (3 + 3 + 4 + 2) / 4 = 3;
mean(a[1]) = (4 + 4) / 2 = 4;
mean(a[2]) = (4 + 0 + 3 + 3) / 4 = 2.5;
mean(a[3]) = (2 + 3) / 2 = 2.5;
mean(a[4]) = (3 + 3 + 3) / 3 = 3.
```
There are three groups of means: those with mean 2.5, 3, and 4. And they form the following groups:

Arrays with indices 0 and 4 form a group with mean 3;

Array with index 1 forms a group with mean 4;

Arrays with indices 2 and 3 form a group with mean 2.5.

Note that neither

```
solution(a) = [[0, 4],
                 [2, 3],
                 [1]]
nor

solution(a) = [[0, 4],
                 [1],
                 [3, 2]]
```
will be considered as a correct answer:

In the first case, the minimal element in the array at index 2 is 1, and it is less then the minimal element in the array at index 1, which is 2.
In the second case, the array at index 2 is not sorted in ascending order.
For
```
a = [[-5, 2, 3],
     [0, 0],
     [0],
     [-100, 100]]
```
the output should be

solution(a) = [[0, 1, 2, 3]]

The mean values of all of the arrays are 0, so all of them are in the same group.




# Problem 4

You've created a new programming language, and now you've decided to add hashmap support to it. Actually you are quite disappointed that in common programming languages it's impossible to add a number to all hashmap keys, or all its values. So you've decided to take matters into your own hands and implement your own hashmap in your new language that has the following operations:

insert x y - insert an object with key x and value y.

get x - return the value of an object with key x.

addToKey x - add x to all keys in map.

addToValue y - add y to all values in map.

To test out your new hashmap, you have a list of queries in the form of two arrays: queryTypes contains the names of the methods to be called (eg: insert, get, etc), and queries contains the arguments for those methods (the x and y values).

Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations.

Example

For queryType = ["insert", "insert", "addToValue", "addToKey", "get"] and query = [[1, 2], [2, 3], [2], [1], [3]], the output should be solution(queryType, query) = 5.

The hashmap looks like this after each query:

1 query: {1: 2}

2 query: {1: 2, 2: 3}

3 query: {1: 4, 2: 5}

4 query: {2: 4, 3: 5}

5 query: answer is 5

The result of the last get query for 3 is 5 in the resulting hashmap.



For queryType = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"] and query = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]], the output should be solution(queryType, query) = 6.

The hashmap looks like this after each query:

1 query: {1: 2}

2 query: {1: 4}

3 query: answer is 4

4 query: {1: 4, 2: 3}

5 query: {2: 4, 3: 3}

6 query: {2: 3, 3: 2}

7 query: answer is 2

The sum of the results for all the get queries is equal to 4 + 2 = 6.