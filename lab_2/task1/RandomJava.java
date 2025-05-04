import java.security.SecureRandom;

public class RandomJava {
    public static void main(String[] args) {
        int length = 128;
        String binarySequence = generateRandomBinarySequence(length);

        System.out.println("Сгенерированная последовательность:");
        System.out.println(binarySequence);
        System.out.println("Длина: " + binarySequence.length());
    }

    public static String generateRandomBinarySequence(int length) {
        SecureRandom random = new SecureRandom();
        StringBuilder binaryString = new StringBuilder(length);

        for (int i = 0; i < length; i++) {
            // Генерируем 0 или 1
            binaryString.append(random.nextInt(2));
        }

        return binaryString.toString();
    }
}