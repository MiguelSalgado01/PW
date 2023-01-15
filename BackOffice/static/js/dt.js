 //  Chamar botao em JS
 $(document).ready( function () {
    $('#tabela').DataTable();
 } );

//  funcao butao
$(".apagar").click(function(e){
   e.preventDefault();

   let DadosReserva={
       id: $(this).attr("id"),
       action: "apagar"
   }
   console.log(DadosReserva);
   $.ajax({
       url: '/reserva',
       type: 'POST',
       data: DadosReserva,
       async: false,
       success: function(data){
           alert(data.message);
           console.log(data.message)
           window.location.reload()
       },
       error: function(data){
           alert(data);
       }
   })
})