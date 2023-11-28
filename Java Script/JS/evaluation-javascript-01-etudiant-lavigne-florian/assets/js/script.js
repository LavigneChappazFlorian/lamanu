let hours = parseInt(prompt("L'heure actuelle : "));
let minutes = parseInt(prompt("La minute actuelle : "));
let duration = parseInt(prompt("La durée du rdv : "));
let duration_end = minutes + duration


console.log(`Il est ${hours}h${minutes} \nLe rdv durera ${duration} minutes`)