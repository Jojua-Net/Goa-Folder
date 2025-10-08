

// 7) იგივე სიიდან დაბეჭდე მხოლოდ ის მომხმარებლები,
//  რომლების ასაკი მეტია 18-ზე. გამოიყენე if ან filter().


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
    if (users[i].age > 18) {
        console.log(users[i].name, users[i].age)
    }
}