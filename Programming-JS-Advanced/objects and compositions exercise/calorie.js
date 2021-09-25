function ex1(arr){
    let result  = {}

    for (let i = 0; i < result.length; i += 2){
        result[arr[i]] = Number(arr[i+1])
    }
}