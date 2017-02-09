/* AQUI VAN LOS JAVASCRIPT PROPIOS */
$( function() {
 	$("#fecha_inicio").datepicker({ dateFormat: "dd-mm-yy" });
} );

$( function() {
  $("#fecha_fin").datepicker({ dateFormat: "dd-mm-yy" });
} );

$("#guardar").on("click",guardar_anuncio_nuevo);
function guardar_anuncio_nuevo(){
	 		var titulo = $("#titulo").val();
	 		console.log(titulo);
	 		var fecha_inicio = $("#fecha_inicio").val();
	 		var fecha_fin = $("#fecha_fin").val();
	 		console.log(fecha_inicio);
	 		console.log(fecha_fin);
	 		if (titulo == "") {
	 			alert("Error ... No se puede Crear un Anuncio sin Titulo");
	 			return false;
	 		} else if (fecha_inicio == "" || fecha_fin == ""){
	 			alert("Error ... Debe ingresar Fecha de Inicio y Fin del Anuncio");
	 			return false;
	 		} else if (fecha_inicio > fecha_fin){
	 			alert("Error ... La Fecha de Inicio es posterior a la de Fin");
	 			return false;
	 		} else {
	 			return true;
	 		}
	 		
 		}
/*

$(document).on("ready", function(){
		$("#guardar").on("click",guardar_anuncio_nuevo);
 		function guardar_anuncio_nuevo(){
	 		var titulo = $("#titulo").val();
	 		console.log(titulo);
	 		return false;
 		}
 });
*/
