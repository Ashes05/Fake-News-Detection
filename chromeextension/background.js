chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    fetch('http://localhost:5000/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'url': request.url })
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Network response was not ok.');
            }
        })
        .then(data => {
            console.log("This is the data" + data);
            sendResponse(data); // Sends the data back to be displayed
        })
        .catch(error => {
            console.error('Error with request:', error.message);
            sendResponse({ result: 'Error' }); // Send an error response
        });
    return true; // Crucial for async sendResponse
});