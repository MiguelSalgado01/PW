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
        dom: 'Bfrtip'
    });
});


//https://datatables.net/examples/ajax/null_data_source.html
//https://datatables.net/examples/api/select_single_row.html