document.addEventListener("DOMContentLoaded", function () {

const button = document.querySelector("button");

if(button){

button.addEventListener("mouseover", function(){
button.style.transform = "scale(1.1)";
button.style.transition = "0.3s";
});

button.addEventListener("mouseout", function(){
button.style.transform = "scale(1)";
});

}

const score = document.querySelector(".score");

if(score){

let value = 0;
let finalScore = parseInt(score.innerText);

let counter = setInterval(function(){

if(value >= finalScore){
clearInterval(counter);
}

score.innerText = value;
value++;

},20);

}

});