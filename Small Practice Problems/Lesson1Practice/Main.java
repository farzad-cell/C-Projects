
// By Farzad Darwazi

import java.util.Objects;
import java.util.Scanner;

class Lesson1Practice {

    // !!!!!! MAIN METHOD !!!!!!!!
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // PRACTICE #1: Variable Practice
            // Whole numbers only
            byte practiceForByte = 98;
            short practiceForShort = 2000;
            int practiceForInt = -122976;
            long practiceForLong = 0;

            // Decimal numbers only
            float practiceForFloat = 2e9f;
            double practiceForDouble = -0.88176;

            // Boolean value
            boolean practiceForBoolean = true;

            // Character value
            char practiceForChar = '$';

        boolean isUserIn = false;
        String userPick;
        String choice;

        while(true){
            System.out.println("\nWelcome to the Lesson 1 practice\n" +
                    "------------------------------------\n" +
                    "1. Variable Practice Outputs\n" +
                    "2. Rectangle Calculator\n" +
                    "3. Temperature Converter\n" +
                    "4. Casting Challenge\n" +
                    "5. Tip Calculator\n" +
                    "0. Exit\n" +
                    "------------------------------------");
            System.out.print("Enter Your Choice (0-5): ");
            userPick = sc.next();
            System.out.println("\n");

            if(Objects.equals(userPick, "0")){
                System.out.print("*************\n** GoodBye **\n*************");
                break;
            }
            if (Objects.equals(userPick, "1") || Objects.equals(userPick, "2") ||
                    Objects.equals(userPick, "3") || Objects.equals(userPick, "4") ||
                    Objects.equals(userPick, "5")) {
                isUserIn = true;
            }else{
                isUserIn = false;
                System.out.println("Invalid Input (0-5)");
                continue;
            }


            switch (userPick){
                case "1":             // PRACTICE #1
                    System.out.println("PRACTICE #1: Variable Practice\n" +
                            "------------------------------------\n" +
                            "1. Byte: " + practiceForByte + "\n" +
                            "2. Short: " + practiceForShort + "\n" +
                            "3. Int: " + practiceForInt + "\n" +
                            "4. Long: " + practiceForLong + "\n" +
                            "5. Float: " + practiceForFloat + "\n" +
                            "6. Double: " + practiceForDouble + "\n" +
                            "7. Char: " + practiceForChar + "\n" +
                            "8. Boolean: " + practiceForBoolean + "\n" +
                            "------------------------------------");
                    // Holds page
                    System.out.println("Press Any Key To EXIT");
                    choice = sc.next();

                    break;

                case "2":             // PRACTICE #2
                    System.out.println("PRACTICE #2: Rectangle Calculator\n" +
                            "------------------------------------");

                    // Prompt and Read
                    System.out.print("Enter Width: ");
                    double width = sc.nextDouble();
                    System.out.print("\n");
                    System.out.print("Enter Height: ");
                    double height = sc.nextDouble();
                    System.out.print("\n");

                    //Area Calculation
                    double area = width * height;

                    // Perimeter Calculation
                    double perimeter = 2 * (width + height);

                    System.out.println("Area: " + area + "\n" +
                            "Perimeter: " + perimeter);
                    System.out.println("------------------------------------");

                    // Holds page
                    System.out.println("Press Any Key To EXIT");
                    choice = sc.next();

                    break;

                case "3":           // PRACTICE #3
                    System.out.println("PRACTICE #3: Temperature Converter\n" +
                            "------------------------------------");

                    // Prompt and Read
                    System.out.print("Enter Degree In Fahrenheit (F) : ");
                    double fahrenheit = sc.nextDouble();
                    System.out.print("\n");

                    double celsius = (fahrenheit - 32) * 5 / 9;

                    System.out.printf("%.2f°F is %.2f°C%n", fahrenheit, celsius);

                    // Holds page
                    System.out.println("------------------------------------\n" +
                            "Press Any Key To EXIT");
                    choice = sc.next();

                    break;

                case "4":           // PRACTICE #4
                    System.out.println("PRACTICE #4: Casting Challenge\n" +
                            "------------------------------------");
                    System.out.print("Enter a Value for Casting: ");
                    double numberForCasting = sc.nextDouble();
                    System.out.print("\n");

                    // Explanation Part: Taking a value in decimal and using
                    // (int) on a double cause the decimal become a whole number
                    // and java removing and decimal part
                    int castedNumber = (int)numberForCasting;

                    System.out.println("Original Value: " + numberForCasting + " | Casted Value: " +
                            castedNumber);
                    System.out.println("------------------------------------");

                    // Holds page
                    System.out.println("Press Any Key To EXIT");
                    choice = sc.next();

                    break;

                case "5":           // PRACTICE #5
                    System.out.println("PRACTICE #5: Tip Calculator\n" +
                            "------------------------------------");
                    System.out.print("Enter bill amount: ");
                    double billAmount = sc.nextDouble();
                    System.out.print("\n");
                    System.out.print("Enter tip percentage Ex. 20: ");
                    double tipPercent = sc.nextDouble();
                    System.out.print("\n");

                    double decimalTip = tipPercent / 100;
                    double tipAmount = billAmount * decimalTip;
                    double total = tipAmount + billAmount;


                    System.out.println("Tip : $" + tipAmount + " | Total: $" +
                            total);
                    System.out.println("------------------------------------");

                    // Holds page
                    System.out.println("Press Any Key To EXIT");
                    choice = sc.next();

                    break;
            }
        }
    }
}
