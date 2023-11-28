pAll = document.querySelectorAll("#site-content p");
myP = pAll[pAll.length-1];
myImg = document.querySelector("#site-content img");

myP.addEventListener("click" , () => {
    myP.innerHTML = "<i>Nouveau texte en italique</i>";
})

myImg.addEventListener("mouseover",  () => {
    myImg.src = "assets/images/2.jpg";
})

myImg.addEventListener("mouseout",  () => {
    myImg.src = "assets/images/1.jpg";
})