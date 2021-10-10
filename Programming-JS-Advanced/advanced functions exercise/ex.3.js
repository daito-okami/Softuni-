function robot(){
    const recipes = {
        apples: {carbohydrate : 1 , flavour : 2},
        lemonade: {carbohydrate : 10 , flavour : 20},
        burger : {carbohydrate: 5, fat: 7, flavour: 3},
        eggs : {protein : 5, fat: 1, flavour: 1},
        turkey: {carbohydrate: 10, protein: 10, fat: 10 , flavour: 10}
    }
    const storage = {
        carbohydrate: 0,
        flavour: 0 ,
        fat: 0,
        protein:0,
    }
    function restock(element, quantity){
        storage[element] += Number(quantity)
        return `Success`
    }

    function prepare(recipe, quantity){
        const remainingStorage = {}
        for (const element in recipes[recipe]){
            const remaining = storage[element] - recipes[recipe][element] * quantity
            if (remaining <0) {
                return `Error: not enough ${element} in stock`
            }else {
                remainingStorage[element] = remaining
            }
        }
        Object.assign(storage, remainingStorage)
        return `Success`
    }
    function report(){
        return `protein=${storage.protein} carbohydrate=${storage.carbohydrate} fat=${storage.fat} flavour=${storage.flavour}`
    }

    function control(str){
        const [command, item, quantity] = str.split(" ")

        switch (command){
            case "restock":
                return restock(item, quantity)
            case "prepare":
                return  prepare(item, quantity)
            case "report" :
                return report()

        }
    }
    return control
}