const vowels = ['a', 'e', 'i', 'o', 'u', 'y'];

function countVowel(myStr){
    let nbVowel=0;
    for (char of myStr) {
        if (vowels.includes(char.toLowerCase())) {
            nbVowel++
        }
    }
    return nbVowel;
}
console.log(countVowel('mA jolie phrase'))