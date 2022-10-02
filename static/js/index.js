document.getElementById("active").addEventListener("click",()=>{
    decir(document.getElementById("decir").value);
});

function decir(texto){
    speechSynthesis.speak(new SpeechSynthesisUtterance(texto));
}