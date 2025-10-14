// function ambilDataUser() {
//   return fetch("https://jsonplaceholder.typicode.com/users")
//     .then((response) => response.json()) // ubah response ke JSON
//     .then((data) => {
//       // tampilkan hanya username dan email
//       data.forEach(({ username, email }) => {
//         console.log(username, email);
//       });
//     })
//     .catch((error) => {
//       console.error("Terjadi error:", error);
//     });
// }

// export default ambilDataUser;

async function ambilDataUser() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/users");
    const data = await response.json();

    // Tampilkan data user dengan format yang diminta
    data.forEach(({ name }) => {
      console.log(`Nama Lengkap: ${name}`);
    });
  } catch (error) {
    console.error("Terjadi error:", error);
  }
}

export default ambilDataUser;

// Mengapa kita butuh .json() setelah fetch()?
// Jika API gagal merespons, bagaimana cara menambahkan error handling?
// 1. .json() → untuk mengubah response body menjadi object JS.
// 2. try...catch + cek response.ok → untuk menangani error jaringan atau HTTP.

// Apa perbedaan pendekatan Promise chaining dengan async/await?
// Promise chaining → bagus untuk kasus sederhana.
// Async/await → lebih readable, cocok untuk banyak step asynchronous
