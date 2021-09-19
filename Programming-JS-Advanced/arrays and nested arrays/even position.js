function  evenPosition(strings){
    let result = ''

    for (let i = 0; i < strings.length; i++){
        result += strings[i]
        result += " "
        i += 1
    }
    console.log(result)

}
arr = [1, 2, 3, 4, 5]
evenPosition(arr)