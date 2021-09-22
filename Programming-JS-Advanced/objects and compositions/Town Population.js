function population(townsAsStrings){
    const towns = {}

    for (let data of townsAsStrings){
        const tokens = data.split(' <-> ')
        const name = tokens[0]
        let pop = Number(tokens[1])

        if (towns[name]){
            pop += towns[name]
        }
        towns[name] = pop
    }
    for (const [name, pop ] of Object.entries(towns)) {
        console.log(`${name} : ${pop}`)
    }
}

