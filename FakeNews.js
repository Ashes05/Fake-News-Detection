
// Selects the textarea from the page
const textarea = document.querySelector("textarea");
// Adds an event listener to the textarea
textarea.addEventListener("keyup", e => {
    textheight(e)
});

function textheight(e)
{
    // Sets the initial height of the textarea to 400px
    textarea.style.height = "400px";
    // Get the height of the content in the textarea
    let scHeight = e.target.scrollHeight;
    // Set the textarea to the scroll height, allowing it to grow as the user inputs content
    textarea.style.height = `${scHeight}px`;
}

// Selects the checkbox from the page
let checkbox = document.getElementById("check");
// Defines the dark gradient background
var darkgradient = 'linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url(WebsiteBg.jpg)'; 
// Defines the light gradient background
var lightgradient = 'linear-gradient(rgba(227,227,227,0.5), rgba(227,227,227,0.5)), url(WebsiteBg.jpg)';


// Function to toggle between the light and dark mode
function isChecked(){
    //check if the check box is checked
    if(checkbox.checked == 1){
        // Set the bodys background to the light gradient
       document.body.style.backgroundImage  = lightgradient;
        // Update the text content to light mode
       document.getElementById("lightmodetext").textContent = " Light Mode ";
        // Update the text colour to black
       document.getElementById("lightmodetext").style.color = "black";
       
       document.getElementById("themetext1").style.color = "black";
       document.getElementById("finalresult").style.color = "black";

       document.getElementById("button").style.backgroundImage = "linear-gradient(rgb(255, 0, 0),rgb(200, 0, 0))";
       document.getElementById("button2").style.backgroundImage = "linear-gradient(rgb(255, 0, 0),rgb(200, 0, 0))";

       let currentClass = document.querySelector('.container');
        if (currentClass) {
        currentClass.style.backgroundColor = 'rgba(147, 147, 147, 0.9)';
        }
    }else{
        // Set the bodys background to the dark gradient
        document.body.style.backgroundImage  = darkgradient;
        // Update the text content to dark mode
        document.getElementById("lightmodetext").textContent = "Dark Mode";
        // Update the text colour to white
        document.getElementById("lightmodetext").style.color = "white";
        document.getElementById("themetext1").style.color = "white";
        document.getElementById("finalresult").style.color = "white";

        document.getElementById("button").style.backgroundImage = "linear-gradient(rgb(177, 0, 0),rgb(255, 0, 0))";
        document.getElementById("button2").style.backgroundImage = "linear-gradient(rgb(177, 0, 0),rgb(255, 0, 0))";

        let currentClass = document.querySelector('.container');
        if (currentClass) {
            currentClass.style.backgroundColor = 'rgba(47, 47, 47, 0.9)';
        }
    }
}

function resetPage()
{
    document.getElementById("fakeness").value = 0;
    document.getElementById("finalresult").textContent = " ";
    document.getElementById("text").value = "";
    textheight();
}
