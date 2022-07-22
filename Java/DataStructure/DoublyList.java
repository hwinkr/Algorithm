public class DoublyList {
    private Node head;
    private Node tail;
    private int nodeSize;
    class Node{
        Object data;
        Node prev;
        Node next;

        Node(Object data){
            this.data = data;
            this.next = null;
            this.prev = null;
        }
    }
    public void addFirst(Object input){
        Node newNode = new Node(input);
        newNode.next = head;
        if(head != null) head.prev = newNode;
        head = newNode;
        nodeSize++;
        if(head.next == null) tail = head;
    }

    public void addLast(Object input){
        Node newNode = new Node(input);
        if(nodeSize == 0) addFirst(input);
        else{
            tail.next = newNode;
            newNode.prev= tail;
            tail = newNode;
            nodeSize ++;
        }
    }


}
