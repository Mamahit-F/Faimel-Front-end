//Ubahlah syntax ES5 berikut ke dalam ES6

// // 1
// const calculateAge = (birthYear) => 2019 - birthYear;

// const yearUntilRetirement = ({ year, firstName }) => {
//   const age = calculateAge(year);
//   const retirement = 60 - age;

//   if (retirement > 0) {
//     console.log(`${firstName} retires in ${retirement} years`);
//   } else {
//     console.log(`${firstName} is already retried`);
//   }
// };
// yearUntilRetirement({ year: 1987, firstName: "John" });

// 2;
// const addNumber = (a, b, c, d, e, f, g) => {
//   let numbers = [a, b, c, d, e, f, g];
//   let sum = 0;
//   //Change to map function
//   numbers.map((num) => (sum += num));
//   return sum;
//   //   for (let i = 0; i < numbers.length; i++) {
//   //     sum += numbers[i];
//   //   }
//   //   return sum;
// };
// console.log(addNumber(1, 2, 3, 4, 5, 6, 7));
// 3.

// const phi = 3.14;

// const calculateArea = ({ radius, power }) => phi * Math.pow(radius, power);

// let radius = 21;
// const area21 = calculateArea({ radius, power: 2 });

// radius = 7;
// const area7 = calculateArea({ radius, power: 2 });

// console.log(`area with 21 radius: ${area21}, and area with 7 radius: ${area7}`);

// 4.
// const makeAjaxRequest = (url, method = "GET") => {
//   console.log(url, method);
// };

// makeAjaxRequest("www.google.com");
