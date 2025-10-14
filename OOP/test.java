public class GarbageCollectionDemo {
    public static void main(String[] args) {
        // Membuat objek yang tidak lagi diakses
        TestClass obj = new TestClass();

        // Menyisipkan objek ke dalam daftar
        System.gc(); // Memanggil garbage collector

        System.out.println("Garbage collection completed");
    }
}

class TestClass {
    // Mengganti finalize() dengan close() karena finalize() deprecated pada Java 9
    public void close() {
        System.out.println("Object destroyed");
    }
}