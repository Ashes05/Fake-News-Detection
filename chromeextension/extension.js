function onButtonPress() {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        var tab = tabs[0]; //Get the current tab the user is in
        var url = tab.url; //Get the url from the current tab
        //console.log("Retrieved URL:", url);
        chrome.runtime.sendMessage({ url: url }, function (response) { //Sends a message to background.js
            if (chrome.runtime.lastError) {
                console.error(chrome.runtime.lastError.message);
                updateResult('Error'); // handle the error in the UI
            } else {
                //console.log("Response received:", response);
                updateResult(response); // update UI with response
            }
        });
    });
}
document.addEventListener("DOMContentLoaded", function () {
    console.log("DOMContentLoaded Loaded");
    var checkButton = document.getElementById("checkButton");
    checkButton.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent default form submission, before it was resetting the html to its default, ie. without the result there.
        onButtonPress();
    });
});
function updateResult(data) {
    //console.log(data);
    //console.log(data.result);
    //console.log(data.prob);
    const resultDiv = document.getElementById('resultMessage'); // element to display the result
    const scoreDiv = document.getElementById('resultScore'); // element to display the probability/confidence
    //If error, show that in UI, else show answer
    if (typeof data === 'object' && data.result === 'Error') {
        let errorMessage = 'An error occurred while processing your request.';
        if (data.message) { // Assuming you might also send a more specific error message
            errorMessage += ` Error: ${data.message}`;
        } else {
            errorMessage += ' Unknown error.'; // Generic error message if no specifics provided
        }

        console.error('An error occurred:', errorMessage);
        resultDiv.textContent = errorMessage;
        resultDiv.className = 'result fake';
        scoreDiv.textContent = ''; // Clear any text that might have been added
        scoreDiv.className = ''; // Clear any class that might have been added
        //What this error looks like in the UI: https://prnt.sc/EN0XHOWJ3nrp
    }
    else {
        if (data.result === 'FAKE') {
            resultDiv.textContent = 'This news is likely FAKE.';
            resultDiv.className = 'result fake'; //red text
        } else {
            resultDiv.textContent = 'This news is likely REAL.';
            resultDiv.className = 'result real'; //green text
        }
        if (data.prob < 50) {
            scoreDiv.textContent = `Confidence: ${(data.prob).toFixed(2)}%`; //make sure it's fixed to 2 decimal places
            scoreDiv.className = 'result fake'; //red text
        }
        else {
            scoreDiv.textContent = `Confidence: ${(data.prob).toFixed(2)}%`; //make sure it's fixed to 2 decimal places
            scoreDiv.className = 'result real'; //green text
        }
    }
}
