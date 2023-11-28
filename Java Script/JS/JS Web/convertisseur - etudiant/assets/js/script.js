/**
 * Prend en paramètre une température en celsius et renvoie son équivalent en fahrenheit
 * @param {*} tmp 
 */
function getFahrenheitTemp(tmp) {
    // TODO 
    return (parseInt(tmp) * 9/5) + 32
}
/**
 * Prend en paramètre une température en celsius et renvoie son équivalent en kelvin
 * @param {*} tmp 
 */
function getKelvinTemp(tmp) {
    // TODO
    return 273.15+ parseInt(tmp);
}

// Déclarez ici les 3 variables (celsuis, kelvin, fahrenheit)
celsius = document.querySelector(".celsius p");

fahrenheit = document.querySelector(".fahrenheit p");

kelvin = document.querySelector(".kelvin p")

/**
 * Fonction qui gère l'affichage par défaut
 * @param {*} temp 
 */
function reset(temp) {
    kelvin.textContent = getKelvinTemp(temp);
    fahrenheit.textContent = getFahrenheitTemp(temp);
}
// on récupère une référence du input range
let temp = document.querySelector('#temp');
window.addEventListener('DOMContentLoaded', function(){
    reset(temp.value);
});

temp.addEventListener('input', function() {
    // On récupère la valeur du input range
    let tmp = this.value;
    // On ajoute la valeur tmp au paragraphe du bloc celsius
    celsius.textContent = tmp;
    // On ajoute la valeur en °K au paragraphe du bloc kelvin
    kelvin.textContent = getKelvinTemp(tmp);
    // On ajoute la valeur en °F au paragraphe du bloc fahrenheit
    fahrenheit.textContent = getFahrenheitTemp(tmp);
})



