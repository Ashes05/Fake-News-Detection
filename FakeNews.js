const textarea = document.querySelector("textarea");

textarea.addEventListener("keyup", e =>{
    textarea.style.height = "400px";
    let scHeight = e.target.scrollHeight;
    textarea.style.height = `${scHeight}px`;
});


let checkbox = document.getElementById("check");
var darkgradient = 'linear-gradient(#272727, #181818)'; 
var lightgradient = 'linear-gradient(#e3e3e3, #dcdbdb)';

function isChecked(){
    if(checkbox.checked == 1){
       document.body.style.background = lightgradient;
       document.getElementById("lightmodetext").textContent = " Light Mode ";
       document.getElementById("lightmodetext").style.color = "black";
    }else{
        document.body.style.background = darkgradient;
        document.getElementById("lightmodetext").textContent = "Dark Mode";
        document.getElementById("lightmodetext").style.color = "white";
    }
}
