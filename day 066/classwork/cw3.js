


// 3) შექმენით ფუნქცია isEven, რომელიც იღებს ერთ ნუმერიკულ 
// პარამეტრს და აბრუნებს true, თუ რიცხვი ლუწია,
//  წინააღმდეგ შემთხვევაში false.


function isEven(num) {
    if (num % 2 === 0) {
        return true
    } else {
        return false
    }
}


console.log(isEven(10))
console.log(isEven(5))