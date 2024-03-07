import java.util.Scanner;


class Main {
    public static void main(String[] args) {
      double phpToUsd = 1;
      double phpToEuro =  0.734719;
      double phpToYuan = 6.346934;
      double phpToKoruna = 18.77263;
      double phpToKrone = 5.449007;
      double phpToSheqel = 3.726334;
      double phpToDinar = 0.274588;

      Scanner myObj = new Scanner(System.in);

      System.out.println("Enter Philippine Peso: ");

      double Php = myObj.nextDouble();

      double Dollar = Php * phpToUsd / 43.33089;
      double Euro = Php * phpToEuro / 43.33089;
      double Yuan = Php * phpToYuan / 43.33089;
      double Koruna = Php * phpToKoruna / 43.33089;
      double Krone = Php * phpToKrone / 43.33089;
      double Sheqel = Php * phpToSheqel / 43.33089;
      double Dinar = Php * phpToDinar / 43.33089;

      System.out.println("The amount's equivalent to:");
      System.out.println("US Dollar is: " + String.format("%.6f", Dollar));
      System.out.println("Euro        : " + String.format("%.6f", Euro));
      System.out.println("Yuan        : " + String.format("%.6f",Yuan));
      System.out.println("Koruna      : " + String.format("%.6f",Koruna));
      System.out.println("Krone       : " + String.format("%.6f",Krone));
      System.out.println("Sheqel      : " + String.format("%.6f",Sheqel));
      System.out.println("Dinar       : " + String.format("%.6f",Dinar));



    }  }