// npm init
// npm install mocha
// npm install chai
// set up in package json file

const cinema = {
    showMovies: function(movieArr) {

        if (movieArr.length == 0) {
            return 'There are currently no movies to show.';
        } else{
            let result = movieArr.join(', ');
            return result;
        }

    },
    ticketPrice: function(projectionType) {

        const schedule = {
            "Premiere": 12.00,
            "Normal": 7.50,
            "Discount": 5.50
        }
        if (schedule.hasOwnProperty(projectionType)) {
            let price = schedule[projectionType];
            return price;
        } else {
            throw new Error('Invalid projection type.')
        }

    },
    swapSeatsInHall: function(firstPlace, secondPlace) {

        if (!Number.isInteger(firstPlace) || firstPlace <= 0 || firstPlace > 20 ||
            !Number.isInteger(secondPlace) || secondPlace <= 0 || secondPlace > 20 || firstPlace === secondPlace) {
            return "Unsuccessful change of seats in the hall.";
        } else {
            return "Successful change of seats in the hall.";
        }

    }
};


const {expect} = require('chai')

describe("Tests …", function() {
    describe("showMovies", function() {
        it("empty arr", function() {
            expect(cinema.showMovies([])).to.be.equal('There are currently no movies to show.')
        });
        it("array of movie", function (){
            expect(cinema.showMovies(["one movie", "second movie", "third movie"])).to.be.equal("one movie, second movie, third movie")
        })
        it("array of 1 movie", function (){
            expect(cinema.showMovies(["one movie"])).to.be.equal("one movie")
        })
    });
    describe('ticketPrice', function() {
        it('test Premiere ', function () {
            expect(cinema.ticketPrice("Premiere")).to.be.equal(12.00)
        });
        it('test Normal ', function () {
            expect(cinema.ticketPrice("Normal")).to.be.equal(7.50)
        });
        it('test Discount ', function () {
            expect(cinema.ticketPrice("Discount")).to.be.equal(5.50)
        });
        it('test Invalid ', function () {
            expect(() => cinema.ticketPrice("Invalid")).to.throw('Invalid projection type.')
        });
    })
    describe('swapSeatsInHall', function() {
        it('only 1 param given ', function () {
            expect(cinema.swapSeatsInHall(1)).to.be.equal("Unsuccessful change of seats in the hall.")
        });
        it("string given", function (){
            expect(cinema.swapSeatsInHall("1", 4)).to.be.equal("Unsuccessful change of seats in the hall.")
        })
        it("higher 1st number given", function (){
            expect(cinema.swapSeatsInHall(25, 5)).to.be.equal("Unsuccessful change of seats in the hall.")
        })
        it("float number given", function (){
            expect(cinema.swapSeatsInHall(1.25, 5)).to.be.equal("Unsuccessful change of seats in the hall.")
        })
        it("negative number given", function (){
            expect(cinema.swapSeatsInHall(-5, 1)).to.be.equal("Unsuccessful change of seats in the hall.")
        })
        it('normal output', function () {
            expect(cinema.swapSeatsInHall(5, 10)).to.be.equal("Successful change of seats in the hall.")
        });
    })
});
