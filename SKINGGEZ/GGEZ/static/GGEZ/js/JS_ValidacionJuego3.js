var juego = document.getElementById("nombreJuego3");
var form = document.getElementById("form");
var men = document.getElementById("mensaje");



form.addEventListener("submit", e=>{

    

    let men = "";
    let entrar = false;
  


    if ( juego.value.length < 1 ) {


        men += "Debe ingresar un nombre de juego valido";
        entrar = true;

    } 

   


    if(entrar){
        e.preventDefault();
        mensaje.innerHTML = men
        e.preventDefault();
        
    }else{


        
        mensaje.innerHTML = 'Validaciones cumplidas correctamente'
        
    }
    

} )

//Aqui terminan las del enzo  ↥ ↥ ↥ ↥ ↥ ↥ ↥ ↥

