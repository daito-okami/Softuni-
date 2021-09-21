function solve(arr){
    let biggest = Number.MIN_SAFE_INTEGER
    const result = arr.filter((el) => {
        if (el > biggest){
            biggest = el
            return true
        }
        return false
    })

    return result

}