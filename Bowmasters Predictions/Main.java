
// By Farzad Darwazi

import java.util.Scanner;

class BowmasterPrediction{

    // Method for fixedPower
    public static void fixedPower(double m){
        float constK =0.003370f;

        double argA = 2 * constK * m;
        double flatArkRad = 0.5 * Math.asin(argA);
        double flatArk = Math.toDegrees(flatArkRad);

        double lobArk = 90 - flatArk;

        System.out.println("--------------------------------------------------------\n" +
                "Different Ground Level:");
        System.out.printf("\tFlat Ark: %.2f°\t\tFLAT ONLY\n\tLob Ark: %.2f°\n", flatArk, lobArk);
        }

    // Method for variablePower
    public static void variablePower(double m){
        float constC = 0.01618f;  // 0.007950f for IPhone version  // 0.01618f YouTube

        double powerMin;
        double powerForList;
        double angleForList;
        int numOfList = 5;
        System.out.println("--------------------------------------------------------\n" +
                "Same Ground Level:");
        for(int i = 0; i < numOfList; i++){
            powerMin = Math.sqrt(m / constC);
            powerForList = powerMin + ((double)i / (numOfList - 1) * (100.0 - powerMin));
            angleForList = 0.5 * Math.asin(Math.min(1.0, m /
                    (constC * Math.pow(powerForList, 2)))) *
                    (180 / Math.PI);
            System.out.printf("\tPower: %.2f%%\t\tAngle: %.2f°%n", powerForList, angleForList);
        }
        System.out.println("--------------------------------------------------------");

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("\033[1;32m╔══════════════════════════════════════════════════════╗");
        System.out.println("║ \033[1;36m \uD83C\uDFF9\uD83C\uDFAF Welcome to Farzad's " +
                "Bowmaster Predictor " +
                "\uD83C\uDFF9\uD83C\uDFAF \033[0m\033[1;32m ║");
        System.out.println("╠══════════════════════════════════════════════════════╣");
        System.out.println("║  When READY, please enter the distance shown in the  ║");
        System.out.println("║  game screen (in meters) to get your predictions.    ║");
        System.out.println("╠══════════════════════════════════════════════════════╣");
        System.out.println("║  Enter 0 at any time to exit.                        ║");
        System.out.println("╚══════════════════════════════════════════════════════╝");

        double enterMeters;
        do{
            System.out.print("Enter Distance: ");
            enterMeters = sc.nextDouble();

            if(enterMeters == 0){
                System.out.println("\033[1;32m╔═════════════════════════════════════════" +
                        "═════════════╗\033[0m");
                System.out.println("\033[1;32m║\033[1;36m     Thanks for using Bowmaster " +
                        "Predictor — Bye!  \033[0m\033[1;32m    ║\033[0m");
                System.out.println("\033[1;32m╚════════════════════════════════════════════" +
                        "══════════╝\033[0m");
                break;
            }

            fixedPower(enterMeters);


            variablePower(enterMeters);


        }while (true);

    }
}
