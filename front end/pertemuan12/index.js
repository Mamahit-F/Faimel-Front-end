//Asynchronous JavaScript

//Synchronous -> single thread -> blocking
// console.log("proses 1");
// console.log("proses 2");
// console.log("proses 3"); //Jika proses memakan waktu yang lama maka akan terblock
// console.log("proses 4");

//Asynchronous -> mullti thread -> non blocking
//1. Parallel
// setTimeout(() => {
//   console.log("proses 1");
// }, 5000);
// setTimeout(() => {
//   console.log("proses 2");
// }, 3000);
// setTimeout(() => {
//   console.log("proses 3");
// }, 4000); //Jika proses memakan waktu yang lama maka akan terblock
// setTimeout(() => {
//   console.log("proses 4");
// }, 1000);

//2. Concurrent
//ES5
// setTimeout(() => {
//   console.log("proses 1");
//   setTimeout(() => {
//     console.log("proses 2");
//     setTimeout(() => {
//       console.log("proses 3");
//       setTimeout(() => {
//         console.log("proses 4");
//       }, 1000);
//     }, 4000);
//   }, 3000);
// }, 5000);

//Promise
// let condition = true;
// const newPromise = new Promise((resolve, reject) => {
//   if (condition) {
//     resolve("berhasil");
//   } else {
//     reject("Gagal");
//   }
// });

//Cara menggunakan promise
//1. then -> catch
// newPromise
//   .then((result) => `${result} !!!`)
//   .then((result2) => console.log(result2))
//   .catch((error) => console.log(error));

//2. Async/await
// Harus  buat didalam fungsi

// const getPromise = async () => {
//   const result = await newPromise;
//   console.log(result);
// };
// getPromise();

// Simulasi fetch data API dar JSONPla
// fetch("https://jsonplaceholder.typicode.com/users")
//   .then((response) => response.json())
//   .then((json) => console.log(json));

//mini exercise
//Ganti fetch then-catch majadi async/await
const getDataJson = async () => {
  const response = await fetch("https://jsonplaceholder.typicode.com/users");
  const json = await response.json();
  json.forEach(({ address }) => console.log(address));
};
getDataJson();
