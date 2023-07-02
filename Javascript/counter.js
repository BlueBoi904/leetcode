// Create a counter using closure.
/*
Approach
The inner function returned by createCounter uses a closure to maintain access to the count variable defined in the outer function. When the inner function is called, it increments count by 1 and returns its new value.

Complexity
Time complexity:
The time complexity of the inner function is O(1) because it performs a constant number of operations (incrementing and returning count). The time complexity of the outer function is also O(1) because it performs a constant number of operations (defining a variable and returning the inner function).

Space complexity:
The space complexity of the createCounter function is O(1) because it only defines one variable count. The space complexity of the inner function is also O(1) because it does not create any additional variables.
*/
createCounter = function (n) {
    let count = n - 1
    return function () {
        count++
        return count
    };
};

// One liner

createCounter = n => () => n++;
