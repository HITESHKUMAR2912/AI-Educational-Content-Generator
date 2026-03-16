function typeWriter(text, element, speed=20){

element.innerHTML=""
let i=0

function typing(){

if(i<text.length){
element.innerHTML+=text.charAt(i)
i++
setTimeout(typing,speed)
}

}

typing()

}

document.addEventListener("DOMContentLoaded",function(){

let form=document.querySelector("form")
let loader=document.getElementById("loader")

if(form){

form.addEventListener("submit",function(){

loader.classList.remove("hidden")

})

}

})