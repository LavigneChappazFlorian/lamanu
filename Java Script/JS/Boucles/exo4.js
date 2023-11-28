let primes = []
for (let i = 0; i<101; i++) {
    primes [i] = true;
}

primes[0] = false;
primes[1] = false;

for (let i=2; i<101; i++) {
    if (primes[i]== false) {
        //primes [i] is already know not to be prime
        continue;
    }
    else {
        let coeff=2;
        while (i*coeff<101) {
            primes[i*coeff++] = false;
        }
    }
    //Check if primes(i) is true
    // if no -> continue
    // if yes -> on boucle pour éliminer les multiples 
}

for (let i=0; i<100; i++) {
    console.log(`Le nombre ${i} est ${i%2==0?`pair`:`impair`}`);
    if (primes=[i]) {
        console.log(`Ce nombre est premier`)
    }
}
