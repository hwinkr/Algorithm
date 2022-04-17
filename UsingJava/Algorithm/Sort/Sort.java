import java.util.Arrays;
import java.util.Scanner;

public class Sort {
}
//class BubbleSort {
//    static int[] arr = new int[10];
//    static Scanner sc = new Scanner(System.in);
//    public static void main(String[] args){
//        for (int i=0; i<arr.length; i++) arr[i] = sc.nextInt();
//        for (int i=arr.length-1; i>0; i++){
//            for(int j=0; j<i; j++){
//                if(arr[j]>arr[j+1]){
//                    int changeBox = arr[j+1];
//                    arr[j+1] = arr[j];
//                    arr[j] = changeBox;
//                }
//            }
//        }
//        System.out.println(Arrays.toString(arr));
//    }
//}

class BinarySort{
    static int[] arr = new int[10];
    static Scanner sc = new Scanner(System.in);
    public static void main (String[] args){
        for(int i=0; i<arr.length; i++) arr[i] = sc.nextInt();
        for(int i=1; i<arr.length; i++){
            for (int j=i-1; j>=0; j--){
                if(arr[j]>arr[i]){
                    int changeBox = arr[i];
                    arr[i] = arr[j];
                    arr[j] = changeBox;
                    i -=1;
                }
            }
        }
        System.out.println(Arrays.toString(arr));
    }
}
class BinarySort1{
    static int[] arr = new int[10];
    static Scanner sc = new Scanner(System.in);
    public static void main (String[] args){
        for(int i=0; i<arr.length; i++) arr[i] = sc.nextInt();
        for(int i=1; i<arr.length; i++){
            for (int j=i-1; j>=0; j--){
                if(arr[j]>arr[i]){
                    int changeBox = arr[i];
                    arr[i] = arr[j];
                    arr[j] = changeBox;
                    i -=1;
                }
            }
        }
        System.out.println(Arrays.toString(arr));
    }
}