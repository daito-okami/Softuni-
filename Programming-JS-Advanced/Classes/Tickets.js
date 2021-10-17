function solve(tickets, criteria){
    class Ticket {
        constructor(destination, price, status) {
            this.destination = destination
            this.price = price
            this.status = status
        }

    }
    const ticketsObjs = []


    tickets.forEach((entry) =>{
        const [dest, price, status] = entry.split("|")
        ticketsObjs.push(new Ticket(dest, Number(price), status))
    })
    if (criteria == "destination"){
        ticketsObjs.sort((a,b) =>{
            return a.destination.localeCompare(b.destination)
        })
    }else if (criteria == "status") {
        ticketsObjs.sort((a, b) => {
            return a.status.localeCompare(b.status)
        })
    }else {
        ticketsObjs.sort((a,b) => {
            return a.price - b.price
        })
    }

    return ticketsObjs
}
