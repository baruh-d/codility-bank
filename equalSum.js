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
//solution
function solution(A) {
    let sumsArray = [];
    let maxValue = -1;

    // Calculate sum of digits for each number in A
    A.forEach(num => {
        let sumOfDigits = 0;
        while (num > 0) {
            sumOfDigits += num % 10;
            num = Math.floor(num / 10);
        }
        sumsArray.push(sumOfDigits);
    });

    // Find pairs with the same sum of digits
    for (let i = 0; i < sumsArray.length; i++) {
        for (let j = i + 1; j < sumsArray.length; j++) {
            if (sumsArray[i] === sumsArray[j]) {
                let pairSum = A[i] + A[j];
                maxValue = Math.max(maxValue, pairSum);
            }
        }
    }
    
    return maxValue;
}

// Example usage
console.log(solution([51, 71, 17, 42])); // Output should be 93
console.log(solution([51, 32, 43]));     // Output should be -1
console.log(solution([42, 33, 60]));     // Output should be 102
