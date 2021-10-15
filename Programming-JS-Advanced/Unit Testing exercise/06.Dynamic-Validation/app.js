function validate() {
    const inputField = document.getElementById("email")
    const validMailPattern = /(^[a-z]+@[a-z]+\.[a-z]+$)/;
    inputField.addEventListener("change", ()=>{
        if (!validMailPattern.test(inputField.value)){
            inputField.classList.add("error")
        }else {
            inputField.classList.remove("error")
        }
    })
}