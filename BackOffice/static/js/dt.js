 //  Chamar botao em JS
 $(document).ready( function () {
    $('#tabela').DataTable();
 } );

//  funcao butao
$(".Apagar").click(function(e){
   e.preventDefault();
   let DadosReserva={
       id: $(this).attr("id")
       
   }
   console.log(DadosReserva);
   $.ajax({
       url: '/usersPage',
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

