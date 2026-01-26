import java.util.Scanner;

public class LuasSegitiga {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Input alas
        System.out.print("Masukkan alas segitiga: ");
        double alas = input.nextDouble();

        // Input tinggi
        System.out.print("Masukkan tinggi segitiga: ");
        double tinggi = input.nextDouble();

        // Perhitungan luas segitiga
        double luas = 0.5 * alas * tinggi;

        // Output hasil
        System.out.println("Luas segitiga adalah: " + luas);

        input.close();
    }
}
