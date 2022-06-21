class HashTable{
    constructor(size){
        this.data = new Array(size)
    }

    _hash(key){
        // O(1)

        let hash = 0;
        // returns a int between 0-65k
        // this use utf-16 encoding
        for(let i=0; i<key.length; i++){
            hash = (hash + key.charCodeAt(i) * i) % this.data.length
        }
        return hash
    }

    set(key, value){
        // o(1)
        const address = this._hash(key)
        if(!this.data[address]){
            this.data[address] = []
            this.data[address].push([key, value])
        }else{
            this.data[address].push([key,value])
        }
        return this.data
    }

    get(key){
        // O(1)
        let address = this._hash(key)
        const currentBucket = this.data[address]
        if(currentBucket.length){
            for(let i = 0; i < currentBucket.length; i++){
                if(currentBucket[i][0] == key){
                    // currentBucket = [[key, value], [key, value]]
                    return currentBucket[i][1]
                }
            }
        }

        return undefined

    }

    keys(){
        if(!this.data.length){
            return undefined
        }
        let _keys = []
        for(let i= 0; i < this.data.length; i++){
            if(this.data[i]){
                for(let k=0; k < this.data[i].length; k++){
                    _keys.push(this.data[i][k][0])
                }
            }
        }

        return _keys
    }
}


