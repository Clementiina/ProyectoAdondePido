/* AQUI VAN LOS JAVASCRIPT NECESARIOS PARA EL MODELOS PRODUCTOS */
$(document).ready(function(){
   
   $('#categorias').on("change",get_subcategoria);
    function get_subcategoria(){
        var categoria_dist = $("#categorias").val();
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
        $.ajax({
            url:"/distribuidoras/select_Marca_SubCategoria_Dist_Ajax/",
            type:"get",
            data:{"m_x_sc_d":m_x_sc_d},
            success: function(data){
                var html = "<div class='container'><div class='list-group col-md-9'>"
                for(var i = 0; i<data.length ; i++){    
                    html += "<a class='list-group-item' href=/distribuidoras/lista_productos/?lalo="+data[i].id+">"+data[i].nombre+"</a>"
                }
                html += "</div></div>"
                $("#tabla").html(html);                   
            }
        })
    };
});
 
