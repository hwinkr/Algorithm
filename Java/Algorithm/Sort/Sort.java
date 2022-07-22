import java.util.Arrays;
import java.util.Scanner;

//public class Sort {
//}
//class BubbleSort {
//    static int[] arr = new int[10];
//    static Scanner sc = new Scanner(System.in);
//    public static void main(String[] args){
//        for (int i=0; i<arr.length; i++) arr[i] = sc.nextInt();
//        for (int i=arr.length-1; i>0; i--){
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
    static Scanner sc = new Scanner(System.in);
    static int[] arr = new int[7];
    public static void main(String[] args) {
        for (int i = 0; i < arr.length; i++) arr[i] = sc.nextInt();
        quickSort(arr, 0, arr.length - 1);
        System.out.println(Arrays.toString(arr));
    }
    static void quickSort(int[] data,int start,int end){
        int partition = partition(data,start,end);
        if(start<partition-1) quickSort(data,start,partition-1);
        if(partition<end) quickSort(data,partition,end);
    }
    static int partition(int[] data,int start,int end){
        int pivot = data[(start+end)/2];
        while(start <= end){
            while(data[start]<pivot) start++;
            while(data[end]>pivot) end --;
            if(start<=end){
               swap(data,start,end);
               start++;
               end--;
            }
        }
        return start;
    }
    static void swap(int[]data,int start,int end){
        int tmp = data[start];
        data[start] = data[end];
        data[end] = tmp;
    }
}

class MergeSort{
     static int[] arr = {4,8,3,5,1,2,7,6};
     static int[] tmp = new int[arr.length];
     public static void main(String[] args){
        mergeSort(arr,tmp,0, arr.length-1);
         System.out.println(Arrays.toString(arr));
     }
     static void mergeSort(int[]data,int[]tmp,int start,int end){
         if(start<end) {
             int mid = (start + end) / 2;
             mergeSort(data,tmp,start, mid);
             mergeSort(data,tmp,mid + 1, end);
             merge(data,tmp,start,mid,end);
         }
     }
     static void merge(int[]data,int[]tmp,int start,int mid,int end){
         for(int i=start; i<=end; i++){
             tmp[i] = data[i];
         }
         int part1 = start;
         int part2 = mid+1;
         int index = start;
         while(part1<=mid && part2<=end){
             if(tmp[part1]>=tmp[part2]){
                 data[index] = tmp[part2];
                 part2++;
                 index++;
             }
             else{
                 data[index] = tmp[part1];
                 part1++;
                 index++;
             }
             if(part2>end){
                 for(int i=0;i<=mid-part1; i++){
                     data[index+i] = tmp[part1+i];
                 }
             } else{
                 for(int j=0;j<=end-part2; j++){
                     data[index+j] = tmp[part2+j];
                 }
             }
         }
     }
}

