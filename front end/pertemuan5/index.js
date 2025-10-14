// IIFE & Callback Function

//1. IIFE (Immediately Invoked Funtioan Expression)
// self-executing anonymous function

// (function () {
//   console.log("Hello World");
// })();

// // With parameter & return value

// (function (fullName, sister) {
//   console.log("Hello " + fullName + sister);
// })("John Doe ", "April ");

// //

// let output = (function (fullName) {
//   return "Hello " + fullName;
// })("John Doe");
// console.log(output);

//2. Callback Function
//function passed into another fundtion as an argument

// function greetings(callback) {
//   callback();
// }

// //Function as argunmen must be a anononyus function
// greetings(function () {
//   console.log("Hello Callback");
// });
// //

//Callback function with parameter & return value
function greetings(callback) {
  let output = callback("John Doe");
  return output;
}

//Function as argunmen must be a anononyus function
let output2 = greetings(function (fullName) {
  return "Hello " + fullName;
});
console.log(output2);

//Exercise 01
//buatlah program untuk menghitung BMI dengan menggunakan
//IIFE & Callback function (with parameter & return value)
