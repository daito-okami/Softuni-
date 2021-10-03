function focused() {
     const fields = Array.from(document.getElementsByTagName('input'))

    function onFocus(ev) {
         ev.target.parentNode.className = "focused"

    }

    function onBlur(ev) {
        ev.target.parentNode.className = ""
    }

    for (let field of fields){
        field.addEventListener('focus', onFocus)
        field.addEventListener('blur', onBlur)
    }
}