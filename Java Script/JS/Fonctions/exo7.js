let fact = function(n) {
    if ((n==0) || (n==1)) {
        return 1;
    } else {
        return n*fact(n-1);
    }
}

console.log(fact(0))
console.log(fact(1))
console.log(fact(5))