function cooking(num ,op1 ,op2, op3, op4, op5){
    num = Number(num)
    let chop = function (n) {
        return n / 2
    }
    let dice = function (n){
        return Math.sqrt(n)
    }
    let spice = function (n){
        return n +1
    }
    let bake = function (n) {
        return n * 3
    }
    let fillet = function (n){
        return n * 0.8
    }

    const arr = [op1, op2, op3, op4, op5]
    let result = num

    for (let i = 0; i <arr.length; i ++){
        switch (arr[i]){
            case "chop":
                result = chop(result)
                console.log(result)
                break
            case "dice":
                result = dice(result)
                console.log(result)
                break
            case "spice":
                result = spice(result)
                console.log(result)
                break
            case "bake":
                result = bake(result)
                console.log(result)
                break
            case "fillet":
                result = fillet(result)
                console.log(result)
                break

        }
    }
}
cooking('9', 'dice', 'spice', 'chop', 'bake', 'fillet')