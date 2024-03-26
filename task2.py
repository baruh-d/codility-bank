'''
There is an array A that consists of N integers. In one move you can select
a number from A and replace it by the sum of its digits. One number can
be selected multiple times. You can apply at most tWO moves. What is the
minimum sum of the array you can achieve?
Write a function:
def solution (A)
that, qiven an array A, returns the minimum sum of the array you can
achieve after applying at most two moves.
'''
def solution(A):
    #iterating through the array of numbers
    for i in range(len(A)):
        #converting the numbers that are greater than or equal to 10 into strings to access the digits
        if A[i] >= 10:
            #converting to string
            digits = str(A[i]) 
            #converting the string back to integers and summing the individual digits of those numbers
            digit_sum = sum(int(digit) for digit in digits)
            # replace the original number in the array with the sum of its digits
            A[i] = digit_sum 
    return A
        

'''
# Examples:
1. Given A= [1, 10, 12, 3], you can apply the move on the second and third
elements. Then A= [1, 1,3, 3] and the function shouid return 8.
2. Given A = [2, 29, 3] you can apply the move twice on the second
element. Then A= [2,2,3] and the function should return 7.
3. Given A = [100, 101, 102, 103] you can apply the move on the first and
second elements. Then A= [1,2, 102, 103] and the function should return 208.
4. Given A= 55, you can apply the move twice on the first element. Then
A=[1] and the function should return 1.
Write an efficient algorithm for the following assumptions:
•N is an integer within the range [1..50,000]:
•each element of array A is an integer within the range
[1..10,000].
'''
print(solution([1, 10, 12, 3]))
print(solution([55]))
print(solution([100, 101, 102, 103]))