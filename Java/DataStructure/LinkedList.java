import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.ListIterator;

//ArrayList
//LinkedList -> 객체를 생성하고 주소를 Reference
//Date 단위 : Node (Data field, Link field(Variable , next Node))
//Head : 누가 노드의 시작인가?
//Tail : 누가 노드의 끝인가?
//배열의 끝 값부터 직접 채운다.
public class LinkedList{
    private Node head;
    private Node tail;
    private int nodeSize = 0;
    class Node{
        Object data;
        Node next;
        Node(Object data){
            this.data = data;
            this.next = null;
        }
    }
    //instance method
    public void addFirst(Object data){
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
        //listSize = 0 -> 1
        if(head.next == null) tail = head;
        nodeSize ++;
    }
    public void addLast(Object data){
        Node newNode = new Node(data);
        if(nodeSize == 0) addFirst(data);
        tail.next = newNode;
        tail = newNode;
        nodeSize ++;
    }
    //java collection frameWork , 삭제된 노드의 값을 출력
    public Object removeFirst(){
        Node start = head;
        head = head.next;
        Object returnData = start.data;
        nodeSize --;
        return returnData;
    }
    public Object removeLast(){
        return remove(nodeSize-1);
    }
    public Object remove(int index){
        if(index == 0) return removeFirst();
        else{
            Node preNode = node(index-1);
            Node removeNode = preNode.next;
            preNode.next = removeNode.next;
            Object returnData = removeNode.data;
            if(removeNode.next == null) tail = preNode;
            nodeSize --;
            return returnData;
        }
    }
    //Node where i find
    public Node node (int index){
        Node x = head;
        for(int i=0; i<index; i++) x = x.next;
        return x;
    }
    //add Node
    public void add(int index, Object data){
        if(index ==0) addFirst(data);
        else{
            Node newNode = new Node(data);
            Node nodeRoom = node(index -1);
            Node nextRoom = nodeRoom.next;
            nodeRoom.next = newNode;
            newNode.next = nextRoom;
            nodeSize++;
            if(newNode.next == null) tail = newNode;
        }
    }
    //print Node
    public String toString(){
        if(head == null){
            return "[]";
        }
        Node start = head;
        String str = "[";
        while (start.next != null) {
            str += start.data + ", ";
            start = start.next;
        }
            str += start.data;
            return str + "]";

    }
    //get Node
    public Node get(int index){
        Node getNode = node(index);
        return getNode;
    }
    //size 값을 private로 선언, 외부에서 마음대로 변경하지 못하기 떄문
    public int nodeSize(){
       return nodeSize;
    }
    public int indexOf(Object data){
        int index = 0;
        //비교노드
        Node compareNode = node(0);
        while(compareNode.data != data){
            index++;
            compareNode = compareNode.next;
            if(compareNode.next == null) {
                System.out.print("Doesn't Exist ");
                index = -1;
                break;
            }
        }
        return index;
    }
    public ListIterator listIterator(){
        return new ListIterator();
    }

    public class ListIterator{
        private Node next;
        private Node returnNode;
        private int nextIndex ;
        ListIterator(){
            next = head;
        }
        //Local method -> next method in public class ListIterator
        public Object next(){
            returnNode = next;
            next = returnNode.next;
            nextIndex++;
            return returnNode.data;
        }
        //nextIndex < size
        //if(true) => return true
        //return (Condition of true)
        public boolean hasNext() {
            return /*if*/nextIndex < nodeSize();
        }
        public void add(Object input){
            Node newNode = new Node(input);
            if(returnNode == null)head = newNode;
            else returnNode.next = newNode;

            newNode.next = next;
            returnNode = newNode;
            nextIndex++;
            nodeSize++;
        }
        public void remove(){
            if(returnNode == null) head = next.next;
            else returnNode.next = next.next;
            next = next.next;
            nodeSize--;
        }
    }
    public static void main (String[] args){
        LinkedList list = new LinkedList();
        list.addFirst(10);
        list.addFirst(20);
        //마지막에 추가한 값이 head.
        list.addFirst(30);
        list.addFirst(40);
        list.addFirst(50);
        list.addFirst(60);
        //변수가 아닌 함수로 접근하는 이유,
//        for(int i=0; i<list.nodeSize(); i++){
//            System.out.println(list.get(i).data);
//        }
        //iterator
        //LinkedList inner class => ListIterator
        //                 list li = new list();
        LinkedList.ListIterator li = list.listIterator();
        li.remove();
        li.remove();
        li.next();
        li.remove();
        System.out.println(list);
    }
}
