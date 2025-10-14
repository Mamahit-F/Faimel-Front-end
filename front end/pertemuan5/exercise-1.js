//1.
(function (berat2, tinggi2) {
  saya2 = berat2 / tinggi2 ** 2;
  if ((saya2 >= 20) & (saya2 <= 25)) console.log("berat badan normal");
  else console.log("berat badan anda tidak normal");
})(70, 1.65);

//2.
function output(callback) {
  let hasil = callback(70 / 1.65 ** 2);
  if ((hasil >= 20) & (hasil <= 25)) console.log("berat badan normal");
  else console.log("berat badan tidak normal");
  return hasil;
}

let output2 = output(function (BMI) {
  return BMI;
});

console.log("hasil BMI anda adalah: ", output2);
