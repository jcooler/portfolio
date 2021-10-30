let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

function generateTarget(){
return Math.floor(Math.random() * 9);

}

function compareGuesses(currentHumanGuess, computerGuess, target){
if (Math.abs(currentHumanGuess, target) <= Math.abs(computerGuess, target)) {
return true 
} else {
        return false;
    }

}

function updateScore(winner){

    if (winner ==='human') {
        humanScore += 1;
    } else if (winner ==='computer'){
        computerScore += 1;
    } else {
        humanScore += 1;
    }
  
}

  
function advanceRound(){
    currentRoundNumber++;
}
