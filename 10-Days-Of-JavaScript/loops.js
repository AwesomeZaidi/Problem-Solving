function vowelsAndConsonants(s) {
    let consonants = "";

    // For each letter in string s:
    // or instead of splitting the string, i could use JS String Method charAt()
    // to return a character at the specified index in the string.
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