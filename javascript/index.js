
function find_smallest(arr) {
    if(!Array.isArray(arr) || (!arr) || (arr.length == 0)) {
        return null;
    }

    let smallest = arr[0];
    let smallest_index = 0;

    for(let i = 1; i < arr.length; i++) {
        if(smallest > arr[i]) {
            smallest = arr[i];
            smallest_index = i;
        }
    }

    return smallest_index;
}

function selection_sort(arr) {
    if(!Array.isArray(arr) || (!arr) || (arr.length == 0)) {
        return arr;
    }

    let old_arr = Array.from(arr);
    let new_arr = [];
    const size = old_arr.length;

    for(let i = 0; i < size; i++) {
        const min_index = find_smallest(old_arr);
        
        if(Number.isInteger(min_index)) {
            new_arr.push(old_arr[min_index]);
            old_arr.splice(min_index, 1);
        }
    }

    return new_arr;
}


let arr = [-10, 2, 3, -200, 50, 123, 4];
let new_arr = selection_sort(arr);

console.log(new_arr);