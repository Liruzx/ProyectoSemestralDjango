
var usser = document.getElementById("nombreUsuario");
var precio = document.getElementById("precio");
var skinname = document.getElementById("nombreSkin");
var men = document.getElementById("mensaje");
var form = document.getElementById("form");



form.addEventListener("submit", e=>{

    

    let men = "";
    
    let entrar = false;

    
    


    if (usser.value.length < 1){

        men += "Debe ingresar una contraseña.<br>";
        entrar = true;
    
    
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
        e.preventDefault();
        
        
    }else{
        mensaje.innerHTML = 'Registrado'
        
    }
    







} )