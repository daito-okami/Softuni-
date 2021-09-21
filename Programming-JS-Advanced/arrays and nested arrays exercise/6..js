function solve(arr){
    const result = arr.sort((a,b) => a.localeCompare(b))
    let orderNumber = 1

    arr.forEach((el) => {
        console.log(`${orderNumber}.${el}`)
        orderNumber++
    })
}