
var correo = document.getElementById("correo");

var form = document.getElementById("form");
var men = document.getElementById("mensaje");



form.addEventListener("submit", e=>{

    

    let men = "";
    let entrar = false;
    let validar = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;



    if (validar.test(correo.value)){


    }else{

        men+="Debe ingresar un correo válido.<br>"
        entrar=true

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

