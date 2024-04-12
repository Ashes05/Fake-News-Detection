function myFunction() {
chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var tab = tabs[0];
    var url = tab.url;
    console.log("Retrieved URL:", url);

    // Create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();
      
    // Configure it: POST-request for the URL
    xhr.open('POST', 'http://localhost:5000/data');
      
    // Set the appropriate header
    xhr.setRequestHeader('Content-Type', 'application/json');
      
    // The data to send
    var data = JSON.stringify({'url': url});
    console.log("Sent data:", data);
      
    // Send the request
    xhr.send(data);
});
}

document.addEventListener("DOMContentLoaded", function() {
    var checkButton = document.getElementById("checkButton");
    checkButton.addEventListener("click", myFunction());
    console.log("pressed");
});
