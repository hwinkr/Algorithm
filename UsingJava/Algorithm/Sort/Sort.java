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

//class BinarySort{
//    static int[] arr = new int[10];
//    static Scanner sc = new Scanner(System.in);
//    public static void main (String[] args){
//        for(int i=0; i<arr.length; i++) arr[i] = sc.nextInt();
//        for(int i=1; i<arr.length; i++){
//            for (int j=i-1; j>=0; j--){
//                if(arr[j]>arr[i]){
//                    int changeBox = arr[i];
//                    arr[i] = arr[j];
//                    arr[j] = changeBox;
//                    i -=1;
//                }
//            }
//        }
//        System.out.println(Arrays.toString(arr));
//    }
//}

//Both of Bubble Sort and Insertion Sort Time Complexity is O(N^2)
//QuickSort Algorithm Time Complexity is O(N*logN)
//정렬이 한번 종료 될 때마다, 탐색구간 -> 1/2
class QuickSort{
    static int[] arr = new int[10];
    static Scanner sc = new Scanner(System.in);
    public static void main (String[] args){
        for (int i=0; i<arr.length; i++) arr[i] = sc.nextInt();
        quickSort(arr, 0,arr.length-1);
        System.out.println(Arrays.toString(arr));
    }
    static void quickSort(int[] data , int start ,int end){
        int part2 = partition (data,start,end);
        //재귀함수 사용.
        if (start < part2-1) quickSort(data,start,part2-1);
        if (part2 < end) quickSort(data,part2,end);
    }
    static int partition(int[] data, int start , int end) {
        int pivot = data[(start + end) / 2];
        while(start <=end) {
            while (data[start] < pivot) start++;
            while (data[end] > pivot) end--;
            if (start <= end) {
                swap(data, start, end);
                start++;
                end--;
            }
        }
        return start;
    }
    static void swap (int[] data, int start , int end){
        int changeBox = data[start];
        data[start] = data[end];
        data[end] = changeBox;
    }
}
class QuickSort1{
    static int[] arr = new int[10];
    static Scanner sc = new Scanner(System.in);
    public static void main (String[] args){
        for (int i=0; i<arr.length; i++) arr[i] = sc.nextInt();
        quickSort(arr, 0,arr.length-1);
        System.out.println(Arrays.toString(arr));
    }
    static void quickSort(int[] data , int start ,int end){
        int part2 = partition (data,start,end);
        //재귀함수 사용.
        if (start < part2-1) quickSort(data,start,part2-1);
        if (part2 < end) quickSort(data,part2,end);
    }
    static int partition(int[] data, int start , int end) {
        int pivot = data[(start + end) / 2];
        while(start <=end) {
            while (data[start] < pivot) start++;
            while (data[end] > pivot) end--;
            if (start <= end) {
                swap(data, start, end);
                start++;
                end--;
            }
        }
        return start;
    }
    static void swap (int[] data, int start , int end){
        int changeBox = data[start];
        data[start] = data[end];
        data[end] = changeBox;
    }
}