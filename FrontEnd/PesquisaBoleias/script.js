$(document).ready(function() {
    $('#tabela').DataTable({
        language: {
            searchPanes: {
                clearMessage: 'Obliterate Selections',
                collapse: {0: 'Search Options', _: 'Search Options (%d)'}

            }
        },
        buttons: [
            'searchPanes'
        ],
        dom: 'Bfrtip'
    });
});

//$.fn.dataTable.SearchPanes.defaults.collapse = false;
$.fn.dataTable.SearchPane.defaults.collapse = false;

/*

$(document).ready(function (){
    let table = new DataTable('#tabela', {
        responsive:{
            details: {
                display:  $.fn.dataTable.Responsive.display.modal({
                    Headers: function (row){
                        var data = row.data();
                        return 'Detalhes de '+ data[0] + '' + data[1];
                    }
                }),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll()
            }
        }  
    });
    
})
*/