Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

Input Format

The first line contains an integer,n , the size of the array.
The second line contains  space-separated integers that describe .

Constraints



Output Format

Print the following  lines, each to  decimals:

proportion of positive values
proportion of negative values
proportion of zeros

Steps:
1. Get input n to define array size
2. Enter the elements in array
3. Then define 3 characters with o value (eg: p=0)
4. Give the condition
5. Then divide them with array size

Code: 
n=int(input())
x=list(map(int,input().split()[:n]))
p=0
q=0
r=0
for i in range(0,n):
    if x[i]>0:
        p+=1
    if x[i]<0:
        q+=1
    if x[i]==0:
        r+=1
print(p/n)
print(q/n)
print(r/n)
