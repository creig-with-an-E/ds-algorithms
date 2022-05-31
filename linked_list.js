class Node{
    constructor(val){
        this.value = val
        this.next = null
    }
}


class LinkedList{
    constructor(val){
        this.head = new Node(val)

        this.tail = this.head
        this.length = 1
    }

    toString(){
        const elements = []
        let current_node = this.head

        while(current_node){
            elements.push(current_node.value)
            current_node = current_node.next
        }
        return `<LinkedList elements='${elements}' />`
    }

    _traverse_list_to_index(index){
        // validate index
        // iterate through the list
        // stop at index
        // return node at index
        // need two working vars, counter + current_node
        let counter = 0
        let current_node = this.head

        while(counter != index){
            current_node = current_node.next
            counter++
        }

        return current_node
    }

    append(val){
        let node = new Node(val)
        this.tail.next = node
        this.tail = node
        this.length++
        return this
    }

    prepend(val){
        let newNode = new Node(val)
        newNode.next = this.head;
        this.head = newNode
        this.length++
    }

    insert(val, index){
        // check the parameters
            // - can val be null???
            // - can index be null??
            // what about out of bounds index
            // negative index??
            // index is int

        // find the node before,

        // 1        3 - 4 - 5
        //    \  /
        //      2

        if(index >= this.length){
            return this.append(val)
        }

        if(index == 0){
            return this.prepend(val)
        }

        let preceding_index = index - 1
        const leader = this._traverse_list_to_index(preceding_index)
        
        const node = new Node(val)
        // point 2 -> 3
        node.next = leader.next;
        // point 1 -> 2
        leader.next = node;
        this.length++

    }
}


let mylist = new LinkedList(10)
mylist.append(12)
mylist.prepend('first')
mylist.append(100);
mylist.prepend("firster");

console.log(mylist.toString())

mylist.insert('ZERO', 0)
console.log(mylist.toString())