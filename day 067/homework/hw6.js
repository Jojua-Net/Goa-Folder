

// 6) შექმენი ობიექტების სია users, სადაც თითოეულს 
// ექნება name და age. დაბეჭდე ყველა მომხმარებლის სახელი და ასაკი.


let users = [
    {
        name: "Vaxtang",
        age: 16,
    },
    {
        name: "Davit",
        age: 14,
    },
    {
        name: "Lasha",
        age: 37,
    }
]


for (let i = 0; i < users.length; i++) {
    console.log(users[i].name, users[i].age)
}