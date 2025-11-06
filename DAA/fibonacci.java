import java.util.Scanner;

class fibonacci{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int target = input.nextInt();
        System.out.println("The " + target +"th fibonacci number is: "+fiboSeries(target));
    }

    static int fiboSeries(int val){
            // resursive fibonacci series        
            if (val == 0) {
                return 0;
            } else if (val == 1) {
                return 1;
            }
            return fiboSeries(val - 1) + fiboSeries(val - 2);
        
    }
}

// tc is O(n ^ n)

