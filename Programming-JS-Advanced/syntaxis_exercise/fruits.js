function calcFruits(fruit, weight, price) {
    const weightInKg = (weight / 1000)
    const moneyNeeded = weightInKg * price
    
    console.log(`I need $${moneyNeeded.toFixed(2)} to buy ${weightInKg.toFixed(2)} kilograms ${fruit}.`)
}


calcFruits('orange', 2500, 1.80)