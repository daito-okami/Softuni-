const { expect } = require('chai')
const sum = require("./ex 2")
const {isOddOrEven} = require("./ex 2");



describe("Test oddOrEven", ()=>{
    it("Test invalid input", ()=>{
        expect(isOddOrEven(1)).to.be.undefined
        expect(isOddOrEven({})).to.be.undefined
        expect(isOddOrEven([])).to.be.undefined
    } )

    it("Test if odd is returned", ()=>{
        expect(isOddOrEven("abc")).to.be.string("odd")
    })

    it("Test if even is returned", ()=>{
        expect(isOddOrEven("ad")).to.be.string("even")
    })
})