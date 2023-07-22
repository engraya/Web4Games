const wordText = document.querySelector(".word"),
hintText = document.querySelector(".hint span"),
timeText = document.querySelector(".time b"),
inputField = document.querySelector("input"),
refreshBtn = document.querySelector(".refresh-word"),
checkBtn = document.querySelector(".check-word"),
messageSection = document.getElementById("message")

let correctWord, timer;

const initTimer = maxTime => {
    clearInterval(timer);
    timer = setInterval(() => {
        if(maxTime > 0) {
            maxTime--;   /// dECREMENT MAX TIME BY -1
            return timeText.innerText = maxTime;
        }
        clearInterval(timer);
        let message = `Time off! ${correctWord.toUpperCase()} was the Correct Word`
        messageSection.innerHTML = message;
        alert(message);
        initGame();  /// calling init function so that the game starts

    }, 1000);
}


const initGame = () => {
    initTimer(30);
    let randomObj = words[Math.floor(Math.random() * words.length)]   // getting random object from words
    let wordArray = randomObj.word.split("");   // spliiting each letter of random word

    for (let i = wordArray.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));   //getting random number

        [wordArray[i], wordArray[j]] = [wordArray[j], wordArray[i]]; // shuffling and swapping array letters randomly
    }
    wordText.innerText = wordArray.join("");    // passing shuffle word as word text
    hintText.innerText = randomObj.hint;  // passing random object as hint text
    correctWord = randomObj.word.toLowerCase();  /// Passing random word to correct word
    inputField.value = "";
    inputField.setAttribute("maxlength", correctWord.length);
}

initGame();

const checkWord = () => {
    let message;
    let userWord = inputField.value.toLocaleLowerCase();   /// getting User value
    if(!userWord) return alert("Please Enter a word Check"); // if the user didn't enter any value or word

    // if user input doesnt match the correct word
    if(userWord !== correctWord) return alert(`OOpps! ${userWord} is not a Correct word`);

    // if the input matches the words and the above two conditions are false
    message = `Congratulations! ${userWord.toUpperCase()} is a Correct word`
    messageSection.innerHTML = message;
    alert(message);
    initGame();
}



refreshBtn.addEventListener("click", initGame);
checkBtn.addEventListener("click", checkWord);

