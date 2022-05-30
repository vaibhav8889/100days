/**
 * @param {number[][]} accounts
 * @return {number}
 */
 var maximumWealth = function(accounts) {
    let max = 0;
    for(let i =0; i< accounts.length; i++){
        let sum = 0;
        while(accounts[i].length){
            sum = sum + accounts[i].shift();
        }
        if(max<= sum){
            max = sum;
        }
    }
    return max;
    
};