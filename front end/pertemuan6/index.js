//Array & Object in JavaScript

//array
//Cara 1. Array Literal
let students = ["John", "bob", "jane", "jack"];
let john = ["John", 30, true[(30, 40)]]; //bisa beda tipe data
//Cara 2. Kata kunci "New"
let employees = new Array("John", "bob", "jane", "jack");
console.log(students, john); //menampilkan semua array sekaligus
students[1] = "rayden";
console.log(students[1]); //menampilan element dala array melalui index
console.log(students.length); //menampilkan panjang array

//Akses element terakhir dalam array
console.log(students[students.length - 2]);

//Array Method
let array = [1, 2, 3, "hello", false, true];
//1. toString
console.log(array.toString());
//2. Join()
console.log(array.join("-"));
console.log(array.join(" "));
console.log(array.join("#"));

//3.pop() == menghapus element terakhir
array.pop();
console.log(array);

//4. Push == tambah element terakhir
array.push("Boku no chincin wa chisai");
console.log(array);

//5. shift == menghapus elemnt di depan
array.shift();
console.log(array);

//6. unshift == menambah element diawal atau dipertama
array.unshift("danny rantung");
console.log(array);

//7. splice == menambahkan sesuai kemauan
array.splice(2, 0, "cuki", 5);
console.log(array);

//8. slice()
let numbers = array.slice(1, 5);
console.log(numbers);

//9. concat() == menggabungkan array
let num1 = [1, 2, 3];
let num2 = [4, 5, 6];
let num3 = [7, 8, 9];
let combineNum = num1.concat(num2, num3);
console.log(combineNum);

//

// Object
// Cara deklarasi object
let johnObj = {
  fullName: "John Doe",
  age: 30,
  isActive: true,
  grade: [90, 80, 100],
  address: {
    street: "Jl. Arnold Mononutu",
    city: "minahasa utara",
    province: "Sulawesi Utara",
  },
  sayHello: function () {
    console.log("Hello World");
  },
};
console.log(johnObj);

//caara akses element dalam object
//cara 1,
console.log(johnObj.fullName);
johnObj.sayHello();
console.log(johnObj.address.street);
console.log(johnObj.grade[1]);

//cara 2. Bracket notation
// s
console.log(johnObj["grade"[1]]);
console.log(johnObj["address"]["street"]);
johnObj["sayHello"]();

johnObj.job = "Programmer";
console.log(johnObj);

delete johnObj.isActive; //menhapus properti dalam object
console.log(johnObj);
