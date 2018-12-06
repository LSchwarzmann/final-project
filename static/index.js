// Implementation of Speech-to-Text API from https://medium.freecodecamp.org/how-to-build-a-simple-speech-recognition-app-a65860da6108
// and modified with added functions to fit specific purpose
window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;
const recognition = new SpeechRecognition();

const icon = document.querySelector('i.fa.fa-microphone')

// Create containers to hold text
let paragraph = document.createElement('p');
let container = document.querySelector('.text-box');
container.appendChild(paragraph);

// Listen to the pressing of the button
icon.addEventListener('click', () => {
    dictate();
});

// Deal with the start of speech and displaying it
const dictate = () => {
    recognition.start();
    recognition.onresult = (event) => {
        const speechToText = event.results[0][0].transcript;

        paragraph.textContent = speechToText;

        // Transmit results to server
        console.log(speechToText);
        call_server(speechToText);
    }
}

// Transmits text to the server for sentiment analysis
function call_server(txt) {
    let xhttp = new XMLHttpRequest();
    xhttp.open('POST', '/analyze', true);

    xhttp.onload = function() {
        let resp = xhttp.responseText;
        let obj = JSON.parse(resp);
        let sent = obj["sentiment"]["score"];
        if (sent > 0.65) {
            paragraph.style.color = "#28560a"
        } else if (sent > 0.25) {
            paragraph.style.color = "#5ae510"
        } else if (sent > -0.25) {
            paragraph.style.color = "black"
        } else if (sent > -0.65) {
            paragraph.style.color = "#f41313"
        } else {
            paragraph.style.color = "#890202"
        }

        // Generate sentiment table
        create_sentiment_table(obj);

        // Generate classify table if such analysis was possible
        let ls = obj["classify"];
        if (ls.length != 0) {
            create_classify_table(obj);
        }

        // Generate entity table if such analysis was possible
        if (obj["entities"].length != 0) {
            create_entity_table(obj);
        }

        // Generate syntax table
        create_syntax_table(obj);
    };

    xhttp.send(txt);
}
