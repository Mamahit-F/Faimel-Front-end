// //JavaScript Function

// //Cara 1. function declaration
// function greetings() {
//   console.log("Hello World");
// }

// greetings(); //call function

// //cara 2. Function expression
// let greetings2 = function () {
//   console.log("Hello world 2");
// };

// // greetings2();

// //Function with retunrn value (output) and argument (input)
// function greetings(fullName) {
//   return "hello " + fullName;
// }

// //.        argument
// let output = greetings("John doe");
// console.log(output);

// const greetings2 = function (fullName) {
//   return "Hello " + fullName;
// };
// let output2 = greetings2("John Doe");
// console.log(output);

// //Global, local, block scope variable
// let x = 10;
// console.log(x);
// function func1() {
//   let y = 20;
//   console.log(x);
//   console.log(y);
//   if (true) {
//     let z = 30;
//     console.log(x);
//     console.log(y);
//     console.log(z);
//   }
// }
// func1();

// //mini exersice
// //buatlah fungsi yang menghitung BMI dimana input adalah berat & tinggi dan outputnya adalah bmi

function hitungbmi(berat, tinggi) {
  return berat / (tinggi * tinggi);
}
let bmi = hitungbmi(70, 164);
let hasil = bmi > 25 ? "kelebihan berat badan" : "berat badan anda normal";
console.log(hasil);

//Pelajari dirumah tentang IIFE & Callback Function
