

// 9) შექმენი სია products (name, price). იპოვე ყველაზე ძვირი პროდუქტი.


let products = [
    {
        name: "xinkali",
        price: 300,
    },
    {
        name: "darbaidzes coca-cola",
        price: 1000000,
    },
    {
        name: "shota napoleoni :d",
        price: 2000000,
    }
]

let max = 0

for (let i = 1; i < products.length; i++) {
    max = products[0].price

    if (max < products[i].price) {
        max = products[i].price
    } else if (max > products[i].price) {
        continue
    }
}


console.log(max)

