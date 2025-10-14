function helloWorld() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("Hello World!");
    }, 2000);
  });
}

export default helloWorld;

// Mengapa kita perlu menambahkan await di dalam messages?
// Apa yang terjadi jika await dihapus?
// Mengapa kita perlu menggunakan export dan import di sini?

// supaya kita dapat hasil string, bukan Promise.
// hasilnya masih berupa Promise pending.
// export dan import dipakai supaya kita bisa memecah kode ke beberapa file dan tetap saling terhubung.
