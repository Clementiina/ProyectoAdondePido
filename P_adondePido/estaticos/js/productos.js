/* AQUI VAN LOS JAVASCRIPT NECESARIOS PARA EL MODELOS PRODUCTOS */
$(document).ready(function(){
   
   $('#categorias').on("change",get_subcategoria);
    function get_subcategoria(){
        var categoria_dist = $("#categorias").val();
        console.log(categoria_dist);
        $("#subCategorias").html("");
        $.ajax({
            url:"/distribuidoras/select_SubCategoria_Ajax/",
            type:"get",
            data:{"categoria_dist":categoria_dist},
            success: function(data){
                $("#subCategorias").append("<option></option");
                for(var i = 0; i<data.length ; i++){    
                    $("#subCategorias").append("<option value='"+data[i].id+"'>" +data[i].nombre+"</option>")
                }
            }
        })
    };

    $('#subCategorias').on("change",get_marca_subcategoria);
    function get_marca_subcategoria(){
        var subCategorias_dist = $("#subCategorias").val();
        console.log(subCategorias_dist)
        $("#m_x_sc_d").html("");
        $.ajax({
            url:"/distribuidoras/select_Marca_SubCategoria_Ajax/",
            type:"get",
            data:{"subCategorias_dist":subCategorias_dist},
            success: function(data){
                $("#m_x_sc_d").append("<option></option");
                for(var i = 0; i<data.length ; i++){    
                    $("#m_x_sc_d").append("<option value='"+data[i].id+"'>" +data[i].nombre+"</option>")
                }
            }
        })
    };

    $('#m_x_sc_d').on("change",get_marca_subcategoria_distribuidora);
    function get_marca_subcategoria_distribuidora(){
        var m_x_sc_d = $("#m_x_sc_d").val();
        console.log(m_x_sc_d);
        $.ajax({
            url:"/distribuidoras/select_Marca_SubCategoria_Dist_Ajax/",
            type:"get",
            data:{"m_x_sc_d":m_x_sc_d},
            success: function(data){
                var html = "<div  style='margin-top: 1%; overflow:scroll;height:400px;'> <div class='list-group'>"
                for(var i = 0; i<data.length ; i++){    
                    html += "<a class='list-group-item' href=/distribuidoras/lista_productos/?lalo="+data[i].id+">"+data[i].nombre+"</a>"
                }
                html += "</div></div>"
                $("#tabla").html(html);                   
            }
        })
    };

    $("#id_categoria").on("change", f);
    function f(){
        var categoria = $("#id_categoria").val()
            $("#id_subCategoria").html("");
        $.ajax({
            url:"/productos/selecCategriaAjax/",
            type:"get",
            data:{"categoria":categoria},
            success: function(data){ 
                $("#id_subCategoria").append("<option></option");
                for(var i = 0; i<data.length; i++){
                    $("#id_subCategoria").append("<option value='"+data[i].pk+"-"+data[i].fields.tipo_presentacion+"'>" +data[i].fields.nombre+"</option>")        
                }
            }
        })

    }

    $("#id_subCategoria").on("change", k);
    function k(){
        var subCategoria = $("#id_subCategoria").val()
        $("#id_tipo_presentacion").html("");
        $("#id_presentacion").html("");
        $.ajax({
            url:"/productos/selecSubCategriaAjax/",
            type:"get",
            data:{"subCategoria":subCategoria},
            success: function(data){     
                for (var i = 0 ; i<data.tipo_presentacion.length ; i++){
                            if (data.tipo_presentacion[i].id == data.t_p_id){
                                $("#id_tipo_presentacion").append("<option value='"+data.tipo_presentacion[i].id+"'selected>"+data.tipo_presentacion[i].nombre+"</option>");
                            } else {
                                $("#id_tipo_presentacion").append("<option value='"+data.tipo_presentacion[i].id+"'  >"+data.tipo_presentacion[i].nombre+"</option>");
                            }

                }
                var nro = 1;
                if(data.presentacion.length>nro){
                    
                    $("#id_presentacion").append("<option value='"+data.presentacion[0].id+"'selected>"+data.presentacion[0].capacidad+"</option>");
                    for (var i = 1; i<data.presentacion.length; i++) {

                        $("#id_presentacion").append("<option value='"+data.presentacion[i].id+"'>"+data.presentacion[i].capacidad+"</option>");
                    }    
                }else{
                    $("#id_presentacion").append("<option value='"+data.presentacion[0].id+"'selected>"+data.presentacion[0].capacidad+"</option>");
                    alert("lecopppp");
                }
            }
                
        })
    };

    $("#id_tipo_presentacion").on("change", c);
    function c(){
        var tipo = $("#id_tipo_presentacion").val();
        $("#id_presentacion").html("");
        $.ajax({
            url:"/productos/selecTipo_PresentacionAjax/",
            type:"get",
            data:{"tipo":tipo},
            success: function(data){
                $("#id_presentacion").append("<option></option");
                for(var i = 0; i<data.length; i++){
                    $("#id_presentacion").append("<option value='"+data[i].pk+"'>" +data[i].fields.capacidad+"</option>")        
                }
            }
        })

    }
    
});
 
