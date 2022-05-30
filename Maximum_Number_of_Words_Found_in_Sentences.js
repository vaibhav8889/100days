/**
 * @param {string[]} sentences
 * @return {number}
 */
 var mostWordsFound = function(sentences) {
    b =0;
    for (let i =0; i< sentences.length; i++){
        let a = sentences[i].split(" ");
        if (b < a.length){
            b = a.length;
        }
    }
    return b;
    
};