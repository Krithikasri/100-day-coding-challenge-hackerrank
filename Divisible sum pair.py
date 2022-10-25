Given an array of integers and a positive integer , determine the number of  pairs where  and  +  is divisible by k.



Complete the divisibleSumPairs function in the editor below.

divisibleSumPairs has the following parameter(s):

int n: the length of array 
int ar[n]: an array of integers
int k: the integer divisor
Returns
- int: the number of pairs

Input Format

The first line contains  space-separated integers,  and .
The second line contains  space-separated integers, each a value of .

Constraints

Sample Input

STDIN           Function
-----           --------
6 3             n = 6, k = 3
1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]
Sample Output

 5
 

Code: 
n,k=input().split()
ar=list(map(int,input().split()))
y=int(k)
c=0
for i in range (0,len(ar)):
    for j in range(i+1,len(ar)):
        if (ar[i] + ar[j]) % y==0:
            c=c+1
print(c)
