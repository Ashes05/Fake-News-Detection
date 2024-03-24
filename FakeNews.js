// Selects the textarea from the page
const textarea = document.querySelector("textarea");

// Adds an event listener to the textare
textarea.addEventListener("keyup", e =>{
    // Sets the initial height of the textarea to 400px
    textarea.style.height = "400px";
    // Get the height of the content in the textarea
    let scHeight = e.target.scrollHeight;
    // Set the textarea to the scroll height, allowing it to grow as the user inputs content
    textarea.style.height = `${scHeight}px`;
});

// Selects the checkbox from the page
let checkbox = document.getElementById("check");
// Defines the dark gradient background
var darkgradient = 'linear-gradient(#272727, #181818)'; 
// Defines the light gradient background
var lightgradient = 'linear-gradient(#e3e3e3, #dcdbdb)';

// Function to toggle between the light and dark mode
function isChecked(){
    //check if the check box it checked
    if(checkbox.checked == 1){
        // Set the bodys background to the light gradient
       document.body.style.background = lightgradient;
        // Update the text content to light mode
       document.getElementById("lightmodetext").textContent = " Light Mode ";
        // Update the text colour to black
       document.getElementById("lightmodetext").style.color = "black";
    }else{
        // Set the bodys background to the dark gradient
        document.body.style.background = darkgradient;
        // Update the text content to dark mode
        document.getElementById("lightmodetext").textContent = "Dark Mode";
        // Update the text colour to white
        document.getElementById("lightmodetext").style.color = "white";
    }
}
