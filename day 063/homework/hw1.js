

// 1)  დაწერე პროგრამა, რომელიც შეამოწმებს რიცხვს:
// თუ რიცხვი მეტია 0-ზე → გამოიტანოს "დადებითი".
// თუ ნაკლებია 0-ზე → "უარყოფითი".
// თუ უდრის 0-ს → "ნულის ტოლია".


function abamidi(a) {

    if (a == 0) {
        return "ნულის ტოლია"
    } else if (a > 0) {
        return "დადებითი"
    } else {
        return "უარყოფითი"
    }
}

console.log(abamidi(10))
console.log(abamidi(0))
console.log(abamidi(-10))