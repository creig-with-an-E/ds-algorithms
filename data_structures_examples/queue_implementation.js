class Node {
    constructor(value){
        this.value = value
        this.next = null
    }
}

class Queue{
    // first and last
    // length
    // first in first out
    constructor(){
        this.first = null
        this.last = null
        this.length = 0
    }

    peek(){
        if(this.first === null){
            return None
        }
        return this.first
    }

    enqueue(value){
        // make new_node
        // check if empty
        // if empty make first and last
        // else: keep record of our last element
        //      make last.next = last
        //      make new_node the last 
        // update the counter
        const node = new Node(value)
        if(this.first === null){
            this.first = node
            this.last = node
        }else{
            this.last.next = node
            this.last = node
        }

        this.length++
    }   
    
    deque(){
        // check if empty queue
        // remove the first
        // if only one remains make to set first and last to null too

    }   
}


const queue = new Queue()
queue.enqueue('page1')
queue.enqueue('page2')
queue.enqueue('queue3')
console.log(queue.peek().next);
console.log(queue.last)