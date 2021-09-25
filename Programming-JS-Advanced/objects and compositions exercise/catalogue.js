function ex(arr){
    const productCatalogue = {}

    arr.forEach((el) => {
        let [productName, price] = el.split(" : ")
        price = Number(price)
        const index = productName[0]
        if (!productCatalogue[index]) {
            productCatalogue[index] = {}
        }
        productCatalogue[index][productName] = price;
    })
    let initialSort = Object.keys(productCatalogue).sort((a,b) => a.localeCompare(b))

    for (const key of initialSort){
        let products = Object.entries(productCatalogue[key])
            .sort((a, b) => a[0].localeCompare(b[0]))
        console.log(key)
        products.forEach((el) => {
            console.log(`  ${el[0]}: ${el[1]}`)
        })
    }
}