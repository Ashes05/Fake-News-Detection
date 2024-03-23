document.getElementById('checkButton').addEventListener('click', function() {
    /*chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        var currentTab = tabs[0];
        var tabUrl = currentTab.url;*/
        
        // Replace this part with actual backend call to check news authenticity
        // This is just a placeholder
        var isRealNews = Math.random() < 0.5; // Randomly generate if news is real or fake
        console.log(isRealNews);
        if (isRealNews) {
            document.getElementById('resultMessage').innerText = "The news on this website appears to be real.";
            document.getElementById('resultMessage').className = "result real";
        } else {
            document.getElementById('resultMessage').innerText = "The news on this website appears to be fake.";
            document.getElementById('resultMessage').className = "result fake";
        }
    });
//});
