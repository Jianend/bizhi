public class hi {
    public static void main(String[] args) {
        for (int a = 10000; a <= 99999; a++) {
            int g, s, b, q, w;
            g = a % 10;
            s = a / 10 % 10;
            b = a / 100 % 10;
            q = a / 1000 % 10;
            w = a / 10000 % 10;
            if (Math.pow(g, 5) + Math.pow(s, 5) + Math.pow(b, 5) + Math.pow(q, 5) + Math.pow(w, 5) == a) {
                System.out.println(a);
            }

        }

    }
}
