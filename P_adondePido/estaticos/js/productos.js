/* AQUI VAN LOS JAVASCRIPT NECESARIOS PARA EL MODELOS ANUNCIOS */
$(document).ready(function(){
   

   $('#m_s_c_d').on("change",get_marca_subcategoria);
    function get_productos(){
        var m_s_c_d_id = $("#m_s_c_d").val();
        $.ajax({
            
            url:"/distribuidoras/selectMarca_SubCategoria_Ajax/",
            type:"get",
            data:{"m_s_c_d_id":m_s_c_d_id},
            success: function(data){
                $("#m_s").append("<option></option");
                for(var i = 0; i<data.length ; i++){    
                    $("#id_marca").append("<option value='"+data[i].id+"'>" +data[i].marca+"</option>")
                }
            }
        })
    }

    

});