
function binary_search(list, target) {
    if(!Array.isArray(list)) {
        return null;
    } else if(list.length == 0) {
        return null;
    }

    if(typeof target !== typeof list[0]) {
        return null;
    }

    let low = 0;
    let high = (list.length - 1);

    while(low <= high) {
        const middle = Math.floor((low + high) / 2);
        const guess = list[middle];

        if(guess == target) {
            return middle;
        } else if(guess < target) {
            low = (middle + 1);
        } else {
            high = (middle - 1);
        }
    }

    return null;
}

const arr = [1, 2, 3, 4, 5, 8, 10, 14, 17, 20];

const index = binary_search(arr, 12);
if(index !== null && index !== undefined) {
    console.log(index);
    console.log(arr[index]);
} else {
    console.log("Not found");
}
