class Movie{
    constructor(name, price) {
        this.movieName = name
        this.ticketPrice = Number(price)
        this.screening = []
        this._revenue = 0
        this._ticketsSold = 0

    }

    newScreening(date, hall, description){
        if (this.screening.some(s => s.date == date && s.hall == hall)){
            throw new Error(`Sorry, ${hall} hall is not available one ${date}`)
        }
        this.screening.push({
            date,
            hall,
            description
        })

        return `New screening of ${this.movieName} is added.`

    }

    endScreening(date, hall, tickets){
        const screening = this.screening.find(s => s.date == date && s.hall == hall)
        if (screening == undefined){
            throw new Error(`Sorry, there is no such screening for ${this.movieName} movie.`)
        }

        const index = this.screening.indexOf(screening)
        this.screening.splice(index, 1)

        const profit = this.ticketPrice * tickets

        this._revenue += profit
        this._ticketsSold += tickets

        return `${this.movieName} movie screening on ${date} in ${hall} hall has ended. Screening profit: ${profit}`
    }



    toString(){
        const result = [
            `${this.movieName} full information:`,
            `Total profit: ${this._revenue.toFixed(0)}$`,
            `Sold Tickets: ${this._ticketsSold}`,
        ]

        if (this.screening.length == 0) {
            result.push("No more screenings!")
        }else {
            result.push("Remaining film screenings:")
            this.screening.sort((a,b)=> a.hall.localeCompare(b.hall)).forEach(s => result.push(`${s.hall} - ${s.date} - ${s.description}`))
        }
        return result.join('\n')
    }
}


let m = new Movie('Wonder Woman 1984', '10.00');
console.log(m.newScreening('October 2, 2020', 'IMAX 3D', `3D`));
console.log(m.newScreening('October 3, 2020', 'Main', `regular`));
console.log(m.newScreening('October 4, 2020', 'IMAX 3D', `3D`));
console.log(m.endScreening('October 2, 2020', 'IMAX 3D', 150));
console.log(m.endScreening('October 3, 2020', 'Main', 78));
console.log(m.toString());

m.newScreening('October 4, 2020', '235', `regular`);
m.newScreening('October 5, 2020', 'Main', `regular`);
m.newScreening('October 3, 2020', '235', `regular`);
m.newScreening('October 4, 2020', 'Main', `regular`);
console.log(m.toString());
