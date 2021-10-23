class SummerCamp{
    constructor(organizer, location){
        this.organizer = organizer
        this.location = location
        this.priceForTheCamp = {
            "child":150,
            "student":300,
            "collegian":500
        }
        this.listOfParticipants = []
    }


    registerParticipant(name, condition, money){
        money = Number(money)
        const money_needed = this.priceForTheCamp[condition]
        if (!this.priceForTheCamp[condition]){
            throw new Error("Unsuccessful registration at camp.")
        }
        if (this.priceForTheCamp[name]){
            return `The ${name} is already registered at the camp.`
        }
        if (money< money_needed){
            return `The money is not enough to pay the stay at camp.`
        }
        this.listOfParticipants.push({name, condition, power:100, wins:0})
        return `The ${name} was successfully registered.`
    }

    unregisterParticipant(name){
        const participant = this.listOfParticipants.find((participant) => participant.name == name);
        if (!this.listOfParticipants.includes(name)){
            throw new Error(`The ${name} is not registered in the camp.`)
        }
        const index = this.listOfParticipants.indexOf(name)
        this.listOfParticipants.splice(index, 1)
        return `The ${name} removed successfully.`
    }
    timeToPlay (typeOfGame, participant1Name, participant2Name){
        const participant1 = this.listOfParticipants.find((participant) => participant.name == participant1Name)
        const participant2 = this.listOfParticipants.find((participant) => participant.name == participant2Name)
        if (participant1.name == undefined && participant2.name == undefined){
            throw new Error(`Invalid entered name/s.`)
        }

        if (typeOfGame == "Battleship"){

            participant1.power += 20
            return `The ${participant1.name} successfully completed the game ${typeOfGame}`
        }else {
            if (participant1.condition != participant2.condition){
                throw new Error(`Choose players with equal condition`)
            }
            if (participant1.power > participant2.power){
                participant1.wins += 1
                return `The ${participant1.name} is the winner in the game ${typeOfGame}.`
            }else if(participant1.power< participant2.power){
                participant2.wins += 1
                return `The ${participant2.name} is the winner in the game ${typeOfGame}.`
            }else if(participant1.power == participant2.power){
                return "There is no winner."
            }
        }
    }
    toString(){
        let result = [];
        result.push(`${this.organizer} will take ${this.listOfParticipants.length} participants on camping to ${this.location}`)

        this.listOfParticipants.sort((a, b) => b.wins - a.wins)

        for (const participant of this.listOfParticipants) {
            result.push(`${participant.name} - ${participant.condition} - ${participant.power} - ${participant.wins}`);
        }

        return result.join('\n');
    }

}

