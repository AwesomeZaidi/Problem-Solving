function vowelsAndConsonants(s) {
    let consonants = "";

    // For each letter in string s:
    for (let letter of s.split('')) {
        if (letter == 'a' ||
            letter == 'e' ||
            letter == 'i' ||
            letter == 'o' ||
            letter == 'u'
           ) {
            console.log("vowels: ", letter);
        } 
        else {
            consonants += letter;
        }
    }
    
    for (let letter of consonants) {
        console.log("consonants: ", letter);
    }
}

const useCase1 = vowelsAndConsonants("hello")