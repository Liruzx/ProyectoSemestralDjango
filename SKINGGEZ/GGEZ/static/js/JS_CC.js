// De aqui en adelante agregaré las del cambio de contrasenia deseenme suerte //

var form2 = document.getElementById("form2");
var cambiodecontra = document.getElementById("nuevacontrasenia");
var cambiodecontra2 = document.getElementById("nuevacontrasenia2");
var men2 = document.getElementById("mensaje2");


form2.addEventListener("submit", e=>{

    e.preventDefault();

    let men2 = "";
    let espacios = false;
    let cont = 0;
    
    let entrar = false;






if(cambiodecontra.value.length==0){

    men2 += "Debe ingresar una contraseña válida.<br>";
    entrar = true;
}

while (!espacios && (cont < cambiodecontra.value.length)) {
    if (cambiodecontra.value.charAt(cont) == " ")
      espacios = true;
    cont++;
  }
     
  if (espacios) {
    men2 += "La contraseña no puede tener espacios en blanco.<br>";
    entrar = true;
    

    return false;
  }



if (cambiodecontra.value.length < 7 ){

    men2 += "Esta debe ser mayor a 7 caracteres.<br>";
    entrar = true;


} 
if(cambiodecontra.value.match(/[a-z]/g)){


}else{

    men2 += "Debe tener al menos 1 letra.<br>";
    entrar = true;

}

if (cambiodecontra.value.match(/[$@$!%*?&#.]/g)){


}else{
    men2 += "Debe tener al menos 1 caracter especial.<br>";
    entrar = true;


}




if (cambiodecontra.value != cambiodecontra2.value ){

    men2 += "Sus contraseñas deben coincidir."
    entrar = true

}




if(entrar){
    mensaje2.innerHTML = men2
    
}else{
    
    mensaje2.innerHTML = '<p>Cambio exitoso</p> <a  href="mensajeCambioContrasenia.html">Presione aqui</a>'
    
}





} )