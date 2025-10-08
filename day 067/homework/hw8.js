

// 8) შექმენი სია cars, სადაც თითოეულ 
// ობიექტს ექნება brand და year.
// დაბეჭდე მხოლოდ ახალი მანქანები


const cars = [
    {
        brand: "ford",
        model: "mustang",
        year: 2025,
    },
    {
        brand: "bmw",
        model: "e39",
        year: 2000,
    },
    {
        brand: "bmw",
        model: "e34",
        year: 1995,
    }
]


for (let i = 0; i < cars.length; i++) {
    if (cars[i].year === 2025) {
        console.log(cars[i].brand, cars[i].model, cars[i].year)
    }
}