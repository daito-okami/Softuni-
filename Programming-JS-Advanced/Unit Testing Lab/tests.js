const {expect} = require('chai')
const isSymmetric = require('./symmetry')

describe('Symmetry Checker', () => {
    it('return true for symmetry array',() =>{
      expect(isSymmetric([1,2,2,1])).to.be.true
    })

    it ('returns false for non symmetric array', () => {
        expect(isSymmetric([1,2,3])).to.be.false
    })
    it ('returns false for non array', ()=> {
        expect(isSymmetric(5)).to.be.false
    })
    it ("returns false for symmetric array with odd numbers", ()=> {
        expect(isSymmetric(1,2,1)).to.be.false
    })
    it ('returns false for symmetric array with letter', ()=> {
        expect(isSymmetric('a','b','b','a')).to.be.false
    })
})