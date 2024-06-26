function  city(name, population, treasury){
    return {
        name: name,
        population: population,
        treasury: treasury,
        taxRate: 10,
        collectTaxes() {
            this.treasury += Math.floor(this.population * this.taxRate)
        },
        applyGrowth(percent) {
            this.population += Math.floor(this.population * (percent / 100))
        },
        applyRecession(percent) {
            this.treasury -= Math.ceil(this.treasury * (percent / 100))
        }
    }
}