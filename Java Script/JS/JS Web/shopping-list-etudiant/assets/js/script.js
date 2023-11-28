let ul = document.querySelector('ul');
let input = document.querySelector('#item');


function addToList() {
    let newItem = input.value;
    let li = document.createElement("li");
    let span = document.createElement("span");
    let button = document.createElement("button");
    li.innerHTML = input.value;

    input.appendChild(span);
    li.appendChild(span);
    li.appendChild(button);
    ul.appendChild(li)

    button.addEventListener('click', removeToList);
    button.innerHTML = "Suprimer"
}

function removeToList() {
    console.log("Bouton cliqué")
    this.parentElement.remove()
}

