function extractNumber(intNum){
    const strNum = intNum.toString()
    let result = parseInt(strNum[0])
    let is_same = false

    for (let i = 1; i < strNum.length; i ++){
        result +=parseInt(strNum[i])

        if (strNum[i] != strNum[i-1]) {
            is_same = true
        }
    }
    console.log(is_same)
    console.log(result)
}
extractNumber(77777)