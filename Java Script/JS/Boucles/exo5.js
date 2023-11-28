let friends = [];
let firstName=prompt("Entrer le prénom d'une amie :");

do {    
    firstName=prompt("Entrer le prénom d'une amie :");
    if (firstName.length) {
        friends.push(firstName);
    }
} while(firstName.length)

console.log(friends.join(', '));