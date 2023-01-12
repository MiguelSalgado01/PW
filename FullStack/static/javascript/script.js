$(document).ready(function() {
    var events = $('#events');
   var table = $('#tabela').DataTable({
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
        dom: 'Bfrtip',
        
        select: true,
        
    });
     
        $(".reservar").click(function(e){
            e.preventDefault();

            let formData={
                id: $(this).attr("id")
            }
            $.ajax({
                url: '/reserva',
                type: 'POST',
                data: formData,
                async: false,
                success: function(data){
                    alert(data);
                    //validar status code 201 e 404 ajax
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