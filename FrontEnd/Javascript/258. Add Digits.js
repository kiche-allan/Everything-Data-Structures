// # Given an integer num, repeatedly add all its digits until the result has only one digit, and return it

var addDigits = function(num) {
    while (num > 9) {
        num = num.toString().split('').reduce(function(sum, digit){
            return sum + parseInt(digit)
        }, 0)
    }
    return num;
    
};

// This line declares a function addDigits using the var keyword, which takes an integer num as an argument.
// This line starts a while loop that will continue as long as the given number num is greater than 9.
// This line converts the given number num to a string using the .toString() method, then splits the resulting string into an array of individual digits using the .split('') method. We then use the .reduce() method to add up all the digits in the array, using the sum variable to keep track of the running total.
// This line returns the final result of the function, which should be a single-digit number.

// I hope this helps! Let me know if you have any further questions.