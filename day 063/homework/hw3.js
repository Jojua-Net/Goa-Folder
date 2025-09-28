// 3 )დაწერე პროგრამა, რომელიც შეამოწმებს ასაკს:
// 0–12 → "ბავშვი"
// 13–19 → "მოზარდი"
// 20 და მეტი → "ზრდასრული"

function ageStatus(a) {
    if (a > 0 && a <= 12 ) {
        return "ბავშვი"
    } else if (a >= 13 && a <= 19) {
        return "მოზარდი"
    } else {
        return "ზრდასრული"
    }
}

console.log(ageStatus(5))
console.log(ageStatus(13))
console.log(ageStatus(35))