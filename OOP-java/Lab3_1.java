import java.util.Scanner;

public class Lab3_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter Month: ");
        int month = scanner.nextInt();

        System.out.print("Enter Day: ");
        int day = scanner.nextInt();
        
        scanner.close();

        try {
            String sign = ZodiacSignCalculator.getZodiacSign(month, day);
            String monthName = getMonthName(month);
            System.out.println("Zodiac sign for " + monthName + " " + day + " is " + sign);
        } catch (InvalidDateException e) {
            System.out.println(e.getMessage());
        }
    }
    
    static String getMonthName(int month) {
        String[] monthNames = {
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        };
        return monthNames[month - 1];
    }
}

class ZodiacSignCalculator {
    static String getZodiacSign(int month, int day) throws InvalidDateException {
        if ((month == 1 && day >= 20) || (month == 2 && day <= 18)) {
            return "Aquarius";
        } else if ((month == 2 && day >= 19) || (month == 3 && day <= 20)) {
            return "Pisces";
        } else if ((month == 3 && day >= 21) || (month == 4 && day <= 19)) {
            return "Aries";
        } else if ((month == 4 && day >= 20) || (month == 5 && day <= 20)) {
            return "Taurus";
        } else if ((month == 5 && day >= 21) || (month == 6 && day <= 20)) {
            return "Gemini";
        } else if ((month == 6 && day >= 21) || (month == 7 && day <= 22)) {
            return "Cancer";
        } else if ((month == 7 && day >= 23) || (month == 8 && day <= 22)) {
            return "Leo";
        } else if ((month == 8 && day >= 23) || (month == 9 && day <= 22)) {
            return "Virgo";
        } else if ((month == 9 && day >= 23) || (month == 10 && day <= 22)) {
            return "Libra";
        } else if ((month == 10 && day >= 23) || (month == 11 && day <= 21)) {
            return "Scorpio";
        } else if ((month == 11 && day >= 22) || (month == 12 && day <= 21)) {
            return "Sagittarius";
        } else if ((month == 12 && day >= 22) || (month == 1 && day <= 19)) {
            return "Capricorn";
        } else {
            throw new InvalidDateException("Invalid Date!");
        }
    }
}

class InvalidDateException extends Exception {
    InvalidDateException(String message) {
        super(message);
    }
}
