function solve(input){

    const carBrands = new Map()


    input.forEach((el) =>{
        let [brand, model, count] = el.split(" | ")
        count = Number(count)

        if (carBrands.has(brand)){
            let carBrand = carBrands.get(brand)
            if (carBrand.has(model)){
                let carModel = carBrand.get(model)
                carModel += count
                carBrand.set(model, carModel)

            }else {
                carBrand.set(model, count)
            }
        }else {
            const modelMap = new Map()
            modelMap.set(model, count)
            carBrands.set(brand, modelMap)
        }
    })

    for (const key of carBrands.keys()){
        console.log(key)
        const brand = carBrands.get(key)
        for (const [model, count] of brand){
            console.log(`###${model} -> ${count}`)
        }
    }
}