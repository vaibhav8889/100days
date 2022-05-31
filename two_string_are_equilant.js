/**
 * @param {string[]} word1
 * @param {string[]} word2
 * @return {boolean}
 */
 var arrayStringsAreEqual = function(word1, word2) {
    let a = "";
    let b = "";
    for (let i =0; i<= word1.length; i++){
        a = a + String(word1[i]);
    }
    for(let i=0; i<= word2.length; i++){
        b = b + String(word2[i]);
    }
    
        if(a === b){
            return true;
        }
        else{
            return false;
        }

    
};