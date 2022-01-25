/**
 * This is a data structures refresher course.
 * There shall be no real magic here.
 * Or shall there?
 * */ 

// task 1
// given 2 arrays create a function 
// that lets the user know whether these two arrays 
// contain any common elements

/***
 * Checks whether the two arrays contain any 
 * similar elements
 * 
 */
const contains_similar = (ar_1, ar_2)=>{
    // how large are the elements going to be?
    // does space and time matter?

    // start with the brute force approach
    // this looks like a nested loop

    // O(n^2) ~ nested loops; this may not be the case if dif size
    // dif size loops with O(a*b)

    // brute force solution
    // for(element of ar_1){
    //     for(element_2 of ar_2){
    //         if(element === element_2){
    //             return true
    //         }
    //     }
    // }
    // return false


    // revision of solution

    // steps
    // loop through first array and create object
    // where properties are items of the array
    //  loop through second and check if item in second
    // exists in second

    let _map = {}
    for(element of ar_1){
        _map[element] = true
    }

    for(element of ar_2){
        if(_map[element]){
            console.log('found common element ', element )
            return true
        }
    }

    return false

    // Time complexity O(a + b)
    // space complexity O(a) ~ that is space complexity is equal to size 
    // of a
}

const array_1 = ["a", "b", "c", "d"];
const array_2 = ["z", "g", "r", "e"];

console.log(contains_similar(array_1, array_2))

const contains_similar_2 = (array_1, array_2) =>{
    // another option
    // better readability
    return array_1.some(item=> array_2.includes(item))
}