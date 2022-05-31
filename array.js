// building an array from scratch

class CustomArray {
    constructor() {
        this.length = 0;
        this.data = {};
    }

    get(index) {
        return this.data[index];
    }

    push(item){
        // push normally returns length of array
        this.data[this.length] = item
        this.shiftItems()
        this.length++
        return this.length
    }

    pop(){
        if(this.length == 0){ throw RangeError }
        delete this.data[this.length-1]
        this.length--
        return 
    }

    delete(index){
        const item = this.data[index]
        this.shiftItems(index)
    }

    shiftItems(index){
        // this will move the

        for(let i=indx; i < this.length -1; i++ ){
            // start at the index that we want to move from
            // then add the contents from the next index
            // ultimately we shifting the items to the left
            this.data[i] = this.data[i+1]
        }
        delete this.data[this.length-1]
        this.length--

    }
}

let list = new CustomArray()

console.log(list)
list.pop()
console.log(list);


const merge_and_sort = (array1, array2)=>{
    // check input
    // will this be strings or ints?
    // using spread and built-in sort
    return [...array1, ...array2].sort()
}