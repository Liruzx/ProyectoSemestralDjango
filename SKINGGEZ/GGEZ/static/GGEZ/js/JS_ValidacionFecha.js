
var fecha_nac = document.getElementById("fechaNac");

var form = document.getElementById("form");
var men = document.getElementById("mensaje");



form.addEventListener("submit", e=>{

    

    let men = "";
    let entrar = false;
    let date_regex = /^(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01])\/(0[1-9]|1[1-9]|2[1-9])$/;
   


   

    if (date_regex.test(fecha_nac.value)){

        
    }else{

        men+= "Debe ingresar una fecha valida<br>"
        entrar = true

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

