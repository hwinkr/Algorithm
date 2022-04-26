//ArrayList
//LinkedList -> 객체를 생성하고 주소를 Reference
//Date 단위 : Node (Data field, Link field(Variable , next Node))
//Head : 누가 노드의 시작인가?
//Tail : 누가 노드의 끝인가?
//배열의 끝 값부터 직접 채운다.
public class LinkedList{
    Node head;
    Node tail;
    int nodeSize = 0;
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
    public Object removeLast(){
        return remove(nodeSize-1);
    }
    public Node node (int index){
        Node x = head;
        for(int i=0; i<index; i++) x = x.next;
        return x;
    }
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
    public static void main (String[] args){
        LinkedList list = new LinkedList();
        list.addFirst(10);
        list.addFirst(20);
        //마지막에 추가한 값이 head.
        list.addFirst(30);
        list.addFirst(40);
        list.addFirst(50);
        list.addFirst(60);
        System.out.println(list.removeLast());
        System.out.println(list);
    }
}
