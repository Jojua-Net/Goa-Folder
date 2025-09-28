


// 2) დაწერე პროგრამა, რომელიც შეამოწმებს, 
// არის თუ არა რიცხვი ლუწი თუ კენტი.


function oddOrEven(a) {
    if (a % 2 === 0) {
        return "ლუწია"
    } else {
        return "კენტია"
    }
}

console.log(oddOrEven(10))
console.log(oddOrEven(5))