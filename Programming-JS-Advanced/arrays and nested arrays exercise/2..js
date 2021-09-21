function solve(arr, step){
    const array_result = []
    for (let i = 0; i < arr.length; i + step){
        array_result.push(arr[i])
    }
    return array_result
}