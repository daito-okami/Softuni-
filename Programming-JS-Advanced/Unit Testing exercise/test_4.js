const { expect } = require('chai')
const {mathEnforcer} = require("./ex 4")


describe("Test mathEnforcer addFive functionality", ()=>{
    it("Expect undefined on wrong input typo", ()=>{
        expect(mathEnforcer.addFive("5")).to.be.undefined
        expect(mathEnforcer.addFive([])).to.be.undefined
        expect(mathEnforcer.addFive({})).to.be.undefined
        expect(mathEnforcer.addFive(undefined)).to.be.undefined
    })
    it("Expect proper number outcome", ()=>{
        expect(mathEnforcer.addFive(5)).to.be.equals(10)
        expect(mathEnforcer.addFive(-10)).to.be.equals(-5)
        expect(mathEnforcer.addFive(5.05)).to.be.closeTo(10.05, 0.01)
    })

    it("Expect undefined on wrong input typo using sum", ()=>{
        expect(mathEnforcer.sum("5", 10)).to.be.undefined
        expect(mathEnforcer.sum([], "")).to.be.undefined
        expect(mathEnforcer.sum({}, {})).to.be.undefined
        expect(mathEnforcer.sum(undefined, NaN)).to.be.undefined
    })

    it("Expect proper number outcome using sum", ()=> {
        expect(mathEnforcer.sum(5, 10)).to.be.equals(15)
        expect(mathEnforcer.sum(20, -20)).to.be.equals(0)
        expect(mathEnforcer.sum(20, -30)).to.be.equals(-10)
        expect(mathEnforcer.sum(5.05, 5)).to.be.closeTo(10.05, 0.01)
    })

    it("Expect undefined on wrong input typo using subtract", ()=>{
        expect(mathEnforcer.subtractTen("5")).to.be.undefined
        expect(mathEnforcer.subtractTen([])).to.be.undefined
        expect(mathEnforcer.subtractTen({})).to.be.undefined
        expect(mathEnforcer.subtractTen(undefined)).to.be.undefined
    })

    it("Expect proper number outcome using subtract", ()=>{
        expect(mathEnforcer.subtractTen(5)).to.be.equals(-5)
        expect(mathEnforcer.subtractTen(20)).to.be.equals(10)
        expect(mathEnforcer.subtractTen(-10)).to.be.equals(-20)
        expect(mathEnforcer.subtractTen(5.05)).to.be.closeTo(-4.95, 0.01)
    })

})

