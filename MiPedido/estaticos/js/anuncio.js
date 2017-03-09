/* AQUI VAN LOS JAVASCRIPT NECESARIOS PARA EL MODELOS ANUNCIOS */
$(document).ready(function(){
    var fecha = new Date();
    $("#errorTitulo").hide();
    $("#errorInicio").hide();
    $("#errorFin").hide();
    $("#errorFecha").hide();
/* funciones de fecha y calendario */
    $( function(){
        $("#id_fecha_inicio").datepicker({ dateFormat: "dd/mm/yy" });
    });
    $( function(){
        $("#id_fecha_fin").datepicker({ dateFormat: "dd/mm/yy" });
    });
/* Validaciones antes de enviar en metodo post */
    $("#btn_guardar_anuncio").on("click",guardar_anuncio_nuevo);
    function guardar_anuncio_nuevo(){
        var titulo = $("#id_titulo").val();
        var fecha_inicio = $("#id_fecha_inicio").val();
        console.log(fecha_inicio);
        var fecha_fin = $("#id_fecha_fin").val();
        console.log(fecha_fin);
        if (titulo == "") {
                $("#errorTitulo").show();
                return false;
        } else if (fecha_inicio == "") {
            $("#errorInicio").show();
            return false;
        }  else if (fecha_fin == ""){
                $("#errorFin").show();
                return false;
        } else if (fecha_inicio > fecha_fin){
                $("#errorFecha").show();
                return false;
        } else {
            return true;
        }
        alerte('ya paso');
    }
/* Activacion del metodo para guardar un cambio */
    $("#btn_activa_guardar").on("click", activa_editar);
    function activa_editar(){
        $("#id_titulo").removeAttr('disabled');
        $("#id_fecha_inicio").removeAttr('disabled');
        $("#id_fecha_fin").removeAttr('disabled');
        $("#id_descripcion").removeAttr('disabled');
        $("#id_imagen").removeAttr('disabled');
        $("#id_estado").removeAttr('disabled');
        $("#btn_guardar_anuncio").removeAttr('disabled');
    }
});
