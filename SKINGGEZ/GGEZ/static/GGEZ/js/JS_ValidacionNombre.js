var usuario = document.getElementById("nombreUsuario");

var form = document.getElementById("form");
var men = document.getElementById("mensaje");



form.addEventListener("submit", e=>{

    

    let men = "";
    let entrar = false;
   


    if ( usuario.value.length < 5 ) {


        men += "Debe ingresar un usuario valido, y debe tener mas de 5 caracteres.<br>";
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

