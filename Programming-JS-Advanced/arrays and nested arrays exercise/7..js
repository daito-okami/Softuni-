function solve(arr){
    arr = arr.sort((a,b) => {
        return a - b
    })
    const result = []
    const count = Math.floor(arr.length/2)
    // for (let i = 0; i <count; i++){
    //     result.push(arr[i])
    //     result.push(arr[arr.length-i])
    // }
    while (arr.length != 0){
        result.push(arr.shift(), arr.pop())

    }
    return result
}