window.addEventListener('load', solve);

function solve() {
    const addBtn = document.getElementById("add-btn")
    addBtn.addEventListener("click", addSong)


    function addSong(e){
        const divElement = document.getElementsByClassName("all-hits-container")[0]
        const genreField = document.getElementById("genre").value
        const nameField = document.getElementById("name").value
        const authorField = document.getElementById("author").value
        const dateField = document.getElementById('date').value
        e.preventDefault()


        if (genreField != "" && nameField != "" && authorField != "" && dateField != ""){
            const song = document.createElement('div');
            song.classList.add('hits-info')

            song.innerHTML = `      <img src="./static/img/img.png">
                                    <h2>Genre: ${genreField}</h2>
                                    <h2>Name: ${nameField}</h2>
                                    <h2>Author: ${authorField}</h2>
                                    <h3>Date: ${dateField}</h3>
                                    <button class="save-btn">Save song</button><button class="like-btn">Like song</button><button class="delete-btn">Delete</button> 
                                    </div>`


            divElement.appendChild(song)

            const [buttonSave, buttonLike, buttonDelete] = song.querySelectorAll('button');
            buttonLike.addEventListener("click", likeSong)
            buttonSave.addEventListener("click", saveSong)
            buttonDelete.addEventListener("click", deleteSong)





        }
        genreField.value = ""
        nameField.value = ""
        authorField.value = ""
        dateField.value = ""
    }


    function saveSong(e){
        const saved = document.getElementsByClassName('saved-container')[0];
        const song = e.target.parentElement;
        const [buttonSave, buttonLike, buttonDelete] = song.querySelectorAll('button');
        buttonSave.remove();
        buttonLike.remove();
        saved.appendChild(song);


    }

    function deleteSong(ev){
        ev.target.parentElement.remove();

    }

    function likeSong(ev){
        const likes = document.querySelector("#total-likes > div > p");
        let count = Number(likes.textContent.split(':')[1].trim());
        count++;
        likes.textContent = `Total Likes: ${count}`

        ev.target.disabled = true;

    }
}
