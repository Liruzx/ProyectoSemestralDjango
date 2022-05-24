
var usser = document.getElementById("usser");
var correo = document.getElementById("correo");
var precio = document.getElementById("precio");
var skinname = document.getElementById("skinname");
var men = document.getElementById("mensajeVALO");
var form = document.getElementById("form");



form.addEventListener("submit", e=>{

    e.preventDefault();

    let men = "";
    
    let entrar = false;

    let validar = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;


    if (usser.value.length < 5){

        men += 'Debe ingresar un usuario válido. Esta debe ser mayor a 7 caracteres.<br>';
        entrar = true;
    
    
    }


    //if (usserv.value.length < 1){

      //  mensajeVALO += "Debe ingresar una contraseña.<br>";
       // entrar = true;
    
    
    //}


    if (validar.test(correo.value)){


    }else{

        men+="Debe ingresar un correo válido.<br>"
        entrar=true

    }

    if (precio.value < 1){
        men+="Debe ingresar un precio válido.<br>"
        entrar=true


    }

    if (skinname.value.length < 1){

        men+="Debe ingresar un nombre de skin válido.<br>"
        entrar=true

    }






    if(entrar){
        mensaje.innerHTML = men
        
    }else{
        mensaje.innerHTML = 'Registrado'
        
    }
    







} )