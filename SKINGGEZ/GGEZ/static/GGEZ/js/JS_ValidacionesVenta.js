
var usser = document.getElementById("usser");
var correo = document.getElementById("correo");
var precio = document.getElementById("precio");
var skinname = document.getElementById("skinname");
var men = document.getElementById("mensajeVALO");
var form = document.getElementById("form");



form.addEventListener("submit", e=>{

    

    let men = "";
    
    let entrar = false;

    
    


    //if (usserv.value.length < 1){

      //  mensajeVALO += "Debe ingresar una contraseña.<br>";
       // entrar = true;
    
    
    //}


    

    if (precio.value < 1){
        men+="Debe ingresar un precio válido.<br>"
        entrar=true


    }

    if (skinname.value.length < 1){

        men+="Debe ingresar un nombre de skin válido.<br>"
        entrar=true

    }






    if(entrar){
        e.preventDefault();
        mensaje.innerHTML = men
        e.preventDefault();
        
        
    }else{
        mensaje.innerHTML = 'Registrado'
        
    }
    







} )