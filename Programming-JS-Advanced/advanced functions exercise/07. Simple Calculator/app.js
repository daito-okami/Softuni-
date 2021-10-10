function calculator() {
    let firstInput
    let secondInput
    let resultbox
    function init(selector1, selector2, selector3){
        firstInput = document.querySelector(selector1)
        secondInput = document.querySelector(selector2)
        resultbox = document.querySelector(selector3)
    }

    function add(){
        resultbox.value = Number(firstInput.value) + Number(secondInput.value)
    }

    function subtract(){
        resultbox.value = Number(firstInput.value) - Number(secondInput.value)
    }

    return {
        init,
        add,
        subtract
    }
}




