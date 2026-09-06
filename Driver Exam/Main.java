import java.util.Objects;
import java.util.Scanner;



// Main class
public class Main {

    /**
     * Requests the student to enter their answers for all 20 questions.
     * Verifies the input by ensuring that only 'a', 'b', 'c', and 'd' are entered.
     * Discards any invalid entry and requests the student to enter again.
     * return char[] an array holding the answers entered by the student
     */
    public static char[] getStuAnswers(){
        Scanner sc = new Scanner(System.in);
        // student input char array
        char[] inputArr = new char[20];

        int answerNum = 0;
        int questionInc = 1;
        do{
            System.out.println("Input answer #" + questionInc);

            String choice = sc.next();
            choice = choice.toLowerCase();

            if(Objects.equals(choice, "a") || Objects.equals(choice, "b")
                    || Objects.equals(choice, "c") || Objects.equals(choice, "d")){

                char choiceToChar = choice.charAt(0);

                inputArr[answerNum] = choiceToChar;

                ++answerNum;
                questionInc++;
            }else
                System.out.println("Invalid Input use (a, b, c, or d)");

        }while (answerNum < 20);

        return inputArr;
    }

    /**
     * Compares the correct answers array against the answers array submitted by the student.
     * Outputs whether the student passed (15+ correct from 20), the total number of correct answers,
     * and the number of questions that the student failed.
     * parameter corrAns the array containing the correct answers to the test
     * parameter stuAnswer the answers array submitted by the student
     */
    public  static void checkExam(char[] corrAns, char[] stuAnswer){
        int corrChoice = 0;
        for(int i = 0; i < 20; ++i){
            if(corrAns[i] == stuAnswer[i]){
                corrChoice++;
            }
        }

        if(corrChoice >= 15){
            System.out.println("****Congrats You Passed****");
        }else {
            System.out.println("----Sorry You Failed----");
        }
        System.out.println("Your Scored: " + corrChoice + "/20");
        System.out.println("Missed question(s): ");
        for(int i = 0; i < 20; ++i){
            if(corrAns[i] != stuAnswer[i]){

                System.out.print("  #" + (i+1));
            }
        }
        System.out.println("\n--------------------------------------------");

    }

    // Main method
    public static void main(String[] args) {
        char[] correctAnswers = {'b','d','a','a','c','a','b','a','c','d'
                ,'b','c','d','a','d','c','c','b','d','a'};
        char[] studentAnswer = getStuAnswers();
        checkExam(correctAnswers,studentAnswer );


        }


    }
