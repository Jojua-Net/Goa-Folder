

// 5) შექმენი car ობიექტი, დაბეჭდე ყველა key და value

const car = {
    brand: "ford",
    model: "mustang",
    year: 2025,
}


// პირველი გზა
console.log("keys: ", Object.keys(car))
console.log("values: ", Object.values(car))

// მეორე გზა
for (const [key, value] of Object.entries(car)) {
    console.log(key, ":", value)
}