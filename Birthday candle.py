You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Function Description

Complete the function birthdayCakeCandles in the editor below.

birthdayCakeCandles has the following parameter(s):



int: the number of candles that are tallest
Input Format

The first line contains a single integer,n, the size of the array.
The second line contains  space-separated integers, where each integer is  describes the height of array .

Constraints

Sample Input 0

4
3 2 1 3
Sample Output 0

2
Explanation 0

Candle heights are 3. The tallest candles are 2 units, and there are 2 of them.

Steps:
1. Get the input
2. Assign count value to 0
3. Take the max value in the array
4. Then sort the array
5. Give the for loop condition and check the max and sorted array values.

Code:
n=int(input())
x=list(map(int,input().split()[:n]))
p=0
q=max(x)
y=sorted(x)
for i in range(0,n):
    if (q==y[i]):
        p+=1
print(p)
