let btnGenerar = document.getElementById("btnReporte");
let contenedor = document.getElementById("conenedor");



btnGenerar.addEventListener('click', (evento) =>{
    evento.preventDefault()
    contenedor.classList.remove("d-none");
})