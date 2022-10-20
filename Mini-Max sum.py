Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example
array [1,2,3,4,5]
The minimum sum is 10 and the maximum sum is 14 . The function prints
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

Input Format

A single line of five space-separated integers.

Constraints


Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14

Steps:
1. Get input in the array
2. Get the minimum value 
3. Give the for condition
4. Calculate the array sum
5. Subtract the min value from the array sum and same as the max value
6. print the output

Code:
n=list(map(int,input().split()))
a=min(n)
b=max(n)
x=sum(n)
y=x-b
z=x-a
print(y,z)
