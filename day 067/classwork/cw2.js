

// 2) შექმენით ფუნქცია სახელად compare რომელსაც 
// გადაეცემა ორი ობიექტი, ორივე ობიექტი იქნება 
// შემდეგნაირ ფორმატში -> {name: სტრინგი, id: რიცხვი, grade: რიცხვი},
//  შეადარეთ ორი ობიექტი grade-თ, თუ ერთი და იგივეა, 
// მაშინ იდ-თ შეადარეთ, დააბრუნეთ სახელი იმ მოსწავლის რომელიც ჯობია.




const compare = (one, two) => {
    
    if (one.grade === two.grade) {
        if (one.id > two.id) {
            return one.name
        } else {
            return two.name
        }
    } else {
        if (one.grade > two.grade) {
            return one.name
        } else {
            return two.name
        }
    }
    
}



console.log(compare({name: "nika", id: 17, grade: 11}, {name: "vaxo", id: 16, grade: 11}))