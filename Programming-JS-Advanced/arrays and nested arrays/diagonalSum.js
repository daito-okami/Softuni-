function solve(matrix){
    let sum1 = 0
    let sum2 = 0
    for (let i = 0; i <matrix.length; i++){
        sum1 += matrix[i][i]
        sum2 += matrix[i][matrix.length - i - 1]
    }

    console.log(`${sum1} ${sum2}`)
}