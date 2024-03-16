import java.util.Scanner;

public class Lab3_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the watts of the light bulb: ");
        int watts = scanner.nextInt();

        int lumens;

        switch (watts) {
            case 15:
                lumens = 125;
                break;
            case 25:
                lumens = 215;
                break;
            case 40:
                lumens = 500;
                break;
            case 60:
                lumens = 880;
                break;
            case 75:
                lumens = 1000;
                break;
            case 100:
                lumens = 1675;
                break;
            default:
                lumens = -1;
                break;
        }

        if (lumens != -1) {
            System.out.println("Lumens: " + lumens);
        } else {
            System.out.println("Invalid input for watts.");
        }
        scanner.close();
    }
}
