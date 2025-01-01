/**
 * @param {number} num
 * @return {number[]}
 */
var sumOfThree = function(num) {
    let x = num/3

    if (x == Math.floor(x)){
        return [x-1, x, x+1]
    }
    else {
        return []
    }
};