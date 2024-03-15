'''
/*
function solution(A);

that, given an array A consisting of N integers, returns the maximum sum of two numbers whose digits add up to an equal sum. 
If there are no two numbers whose digits have an equal sum, the function should return -1.

Examples: 

Given A = [51, 71, 17, 42], the function should return 93. There are two pairs of numbers whose digits add up to an equal sum: (51, 42) and (17, 71). The first pair sums up to 93.
Given A = [42, 33, 60], the function should return 102. The digits of all numbers in A add up to the same sum, and choosing to add 42 and 60 gives the result 102.
Given A = [51, 32, 43], the function should return -1, since all numbers in A have digits that add up to different, unique sums.
*/
/*
Given an array(A) of integers(N) find a pair of elements in the array with digits that add up to an equal sum
When a pair(s) is found, find the pair(s) and add up the sum of the digits that make up the integer
Then return the biggest pair with the same sum of digits maximum sum
*/
'''
def solution(A):
    sumsArray = []
    maxValue = -1
    for num in A:
        sumOfDigits = 0
        for digit in str(num):
            sumOfDigits+=int(digit)
        sumsArray.append(sumOfDigits)
    print(sumsArray)
    for i in range(len(sumsArray)): #i=0  -> j=i+1->min(i+1,len(array)-1)
        for j in range(i+1, len(sumsArray)): #j=1 
            if sumsArray[i] == sumsArray[j]:
                # print(f"the similar sums are, {sumsArray[i]} at index {i}, {sumsArray[j]} at index {j}")
                # print(f"the original values are, {A[i]} at index {i}, {A[j]} at index {j}")
                pairSum = A[i] + A[j] 
                maxValue = max(maxValue, pairSum)
    return maxValue
            
print(solution([51,17,71,42]))
print(solution([51, 32, 43]))
print(solution([42, 33, 60]))