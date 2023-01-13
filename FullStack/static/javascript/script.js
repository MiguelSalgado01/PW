$(document).ready(function() {
   
$('#tabela').DataTable({
        language: {
            searchPanes: {
                clearMessage: 'Delete',
                collapse: {0: 'Search Options', _: 'Search Options (%d)'}

            }
        },
        responsive:{
            details: {
                display:  $.fn.dataTable.Responsive.display.modal({
                    Headers: function (row){
                        var data = row.data();
                        return 'Detalhes de '+ data[0] ;//+ '' + data[1];
                    }
                }),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll()
            }
        } , 
        buttons: [      
            'searchPanes'
        ],
        columnDefs: [
            {
                target: 0,
                visible: false,
            }],
        dom: 'Bfrtip',
        
        select: true,
        
        
    });
     
        $(".reservar").click(function(e){
            e.preventDefault();

            let DadosReserva={
                id: $(this).attr("id")
            }
            console.log(DadosReserva);
            $.ajax({
                url: '/reserva',
                type: 'POST',
                data: DadosReserva,
                async: false,
                success: function(data){
                    alert(data);
                    //validar status code 201 e 404 ajax amanha e ver modal tirar botao resevar tentar pesquisar depois
                    // if(data[1]===201){
                    //     alert("Parabens sabes Registar")
                    // }
                    // else
                    // {
                    //     alert("Erro es um merdas")
                    // }
                    console.log(data)
                    
                },
                error: function(data){
                    alert(data);
                }
            })
        })
      
});

//https://datatables.net/examples/ajax/null_data_source.html
//https://datatables.net/examples/api/select_single_row.html
//https://datatables.net/extensions/select/examples/api/events.html