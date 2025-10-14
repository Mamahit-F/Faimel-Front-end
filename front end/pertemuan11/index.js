//Destructuring & Module
//1. Destructuring Array
// const numbers = [1, 2, 3, 4, 5]; //Structuring

// let num1 = numbers[0];
// let num2 = numbers[1];
// let num3 = numbers[2];
// let num4 = numbers[3];
// let num5 = numbers[4];

//Destructuring ES6
// const [num1, num2, num3, num4, num5] = numbers;
// console.log(num1, num2, num3, num4, num5);

//Destructuring Array sebagian item saja
// const [, , num3, ,] = numbers;
// console.log(num3);

//Destructuring menggunakan rest parameter
// const [num1, num2, ...rest] = numbers;
// console.log(num1, num2, rest);

//Destructuring Object
// const student = {
//   fullName: "John",
//   age: 25,
//   status: "active",
// };

// const fullName = student.fullName;
// const age = student.age;
// const status = student.status;

// const { fullName, age, status } = student;
// console.log(fullName, age, status);

//Destructuring object sebagian item
// const { age } = student;
// console.log(age);

//Destructuring object dengan rest parameter
// const { fullName, ...rest } = student;
// console.log(fullName, rest);

//Mini Exercise
//Cari di Exercise 4 di bagian mana kita dapat melakukan
//destructuring

// 1
// function calculateAge(birthYear) {
//   return 2019 - birthYear;
// }

// function yearUntilRetirement({ year, firstName }) {
//   var age = calculateAge(year);
//   var retirement = 60 - age;

//   if (retirement > 0) {
//     console.log(firstName + " retires in " + retirement + " years");
//   } else {
//     console.log(firstName + " is already retired.");
//   }
// }

// yearUntilRetirement({ year: 1987, firstName: "John" });

// //3.
// var phi = 3.14;
// var power = 2;
// var radius = 0;

// var calculateArea = function ({ radius, power }) {
//   return phi * Math.pow(radius, power);
// };

// radius = 21;
// var area21 = calculateArea({ radius: radius, power: 2 });

// radius = 7;
// var area7 = calculateArea({ radius: radius, power: 2 });

// console.log(
//   "area with 21 radius: " + area21 + ", and area with 7 radius: " + area7
// );

//Module
import { student as mahasiswa, angka } from "./data.js";
import ucapkanSalam from "./sayGreetings.js";

console.log(mahasiswa);
console.log(angka);
ucapkanSalam();
index.js;
// Displaying index.js.
