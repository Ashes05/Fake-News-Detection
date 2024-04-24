
document.getElementById('checkButton').addEventListener('click', function() {   

    // Replace this part with actual backend call to check news authenticity
    // This is just a placeholder
    var isRealNews = Math.random() < 0.5; // Randomly generate if news is real or fake
        
    if (isRealNews) {
        document.getElementById('resultMessage').innerText = "The news on this website appears to be real.";
        document.getElementById('resultMessage').className = "result real";
        document.getElementById('resultScore').innerText = "50% Real";
        document.getElementById('resultScore').className = "result real";
    } else {
        document.getElementById('resultMessage').innerText = "The news on this website appears to be fake.";
        document.getElementById('resultMessage').className = "result fake";
        document.getElementById('resultScore').innerText = "50% Fake";
        document.getElementById('resultScore').className = "result fake";
    }
});
