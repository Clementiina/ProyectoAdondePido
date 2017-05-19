/* AQUI VAN LOS JAVASCRIPT NECESARIOS PARA EL MODELOS ANUNCIOS */
$(document).ready(function(){
   

   $('#id_categoria').on("change",get_productos);
    function get_productos(){
        $("#id_marca").html("");
        var id_categoria = $("#id_categoria").val();
        var dist =$("#dist").val();
        $.ajax({
            
            url:"/distribuidoras/selectProducto/",
            type:"get",
            data:{"id_categoria":id_categoria, "dist":dist},
            success: function(data){
                $("#id_marca").append("<option></option");
                for(var i = 0; i<data.length ; i++){    
                    $("#id_marca").append("<option value='"+data[i].id+"'>" +data[i].marca+"</option>")
                }
            }
        })
    }

    $('#id_marca').on("change",get_marca);
    function get_marca(){
        $("#id_descripcion").html("");
        var id_marca = $("#id_marca").val();
        //var dist =$("#dist").val();
        $.ajax({
            
            url:"/distribuidoras/selectMarca/",
            type:"get",
            data:{"id_marca":id_marca},
            success: function(data){
                $("#id_descripcion").append("<option> </option");
                for(var i = 0; i<data.length ; i++){    
                    $("#id_descripcion").append("<option value='"+data[i].id_marca_subCategoria+"'>" +data[i].subCategoria+"</option>")
                }
            }
        })
    }


    $('#id_descripcion').on("change",get_descripcion);
    function get_descripcion(){
        $("#id_categoria2").html("");
        var id_marca_subCategoria = $("#id_descripcion").val();
        $.ajax({
            
            url:"/distribuidoras/selectDescripcion/",
            type:"get",
            data:{"id_marca_subCategoria":id_marca_subCategoria},
            success: function(data){
                $("#id_categoria2").append("<option> </option");
                for(var i = 0; i<data.length ; i++){    
                    $("#id_categoria2").append("<option value='"+data[i].nombre+"'>" +data[i].nombre+"</option>")
                }
            }
        })
    }
    //$('#id_descripcion').on("change",get_descripcion);
    $("#id_categoria2").on("change", get_presentacion);
    function get_presentacion(){
        console.log('leo');
        $("#id_presentacion").html("");
        var producto = $("#id_categoria2").val();
        console.log(producto);
        $.ajax({
            
            url:"/distribuidoras/selectPresentacion/",
            type:"get",
            data:{"producto":producto},
            success: function(data){
                for(var i = 0; i<data.length ; i++){    
                    $("#id_presentacion").append("<option value='"+data[i].id+"'>" +data[i].presentacion+"</option>")
                }    
            }
            
        })
    }
    

});