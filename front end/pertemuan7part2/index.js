// // //JavaScript Conditional & Loop

// // //1. JavaScript Conditional
// // let suhu = 30;
// // if (suhu >= 38) {
// //   console.log("Suhu diluar panas");
// // } else {
// //   console.log("Suhu diluar normal");
// // }

// //if - else if - elif
// //juka umuur 0 - 5 tampilkan balita
// //jika umur 6 - 11 tampilkkan anak anak
// //juka umur 12 - 17 tampilkan remaja
// //jika umur 18 - 23 tampilkan anak muda
// //jika umur 24 - 40 tampilkan dewasa
// //jika umur 41 keatas tamplika orang tua

// // umur = 16;
// // if (umur >= 0 && umur <= 5) {
// //   console.log("umur termasuk kategori balita");
// // } else if (umur >= 6 && umur <= 11) {
// //   console.log("termasuk kategori anak anak");
// // } else if (umur >= 12 && umur <= 17) {
// //   console.log("termasuk kategori remaja");
// // } else if (umur >= 18 && umur <= 23) {
// //   console.log("termasuk kategori anak muda");
// // } else if (umur >= 24 && umur <= 40) {
// //   console.log("termasuk kategori dewasa");
// // } else if (umur >= 41) {
// //   console.log("termasuk kategori dewasa");
// // } else {
// //   console.log("tidak termasuk dalam range");
// // }

// // Switch case
// let umur = 5;
// switch (umur) {
//   case 1:
//     console.log("hari minggu");
//     break;
//   case 2:
//     console.log("hari senin");
//     break;
//   case 3:
//     console.log("hari selasa");
//     break;
//   case 4:
//     console.log("hari rabu");
//     break;
//   case 5:
//     console.log("kamis");
//     break;
//   case 6:
//     console.log("jumat");
//     break;
//   case 7:
//     console.log("sabtu");
//     break;
// }

// //2. JavaScript Loop
// //1. for loop
// for (let i = 1; i <= 10; i++) {
//   console.log(i);
// }

// //2. while loop
// let i = 1;
// while (i <= 10) {
//   console.log(i);
//   i++;
// }

//3. do while
// let i = 1;
// do {
//   console.log(i);
//   i++;
// } while (i <= 10);

//Array built-in method
let numbers = [1, 2, 3, 4, 5];
console.log(numbers); //tampilkan semua sekaligus
//menapilkan isi aray satu per satu
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}

//Built-in methode
//1. forEach()
// numbers.forEach(function (value) {
//   console.log(value);
// });

//map()
let output = numbers.map(function (value) {
  return value + 2; //data bisa diolah contohnya di tambah
});
console.log(output);

//3. filter()
// let output = numbers.map(function (value) {
//   return value + 2;
// });
// console.log(output);
