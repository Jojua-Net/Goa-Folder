

// 4) დაწერე პროგრამა, რომელიც 
// შეამოწმებს ორ რიცხვს და გამოიტანს რომელია უფრო დიდი.


function big(a, b) {
    if (a > b) {
        return `${a} მეტია ${b}-ზე`
    } else {
        return `${b} მეტია ${a}-ზე`
    }
}

console.log(big(10, 5))
console.log(big(20, 35))