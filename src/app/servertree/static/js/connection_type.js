/*
* Add and edit for connection type module
*/
$(document).ready(function(){
    $(document).on('click', '#addConnectionTypeButton, #editConnectionTypeButton', function(){
      $('#connectionTypeForm')[0].reset();
      var connection_type_id = $(this).attr('data-id');
      if(connection_type_id){
        $('#connectionTypeModalLabel').html('Editar tipo de conexión');
        $('#connectionTypeForm').attr('action', '/connection_type/edit_connection_type/' + connection_type_id);
        $.ajax({
          url: '/connection_type/get_connection_type_by_id',
          method: 'post',
          data: {connection_type_id: connection_type_id},
          dataType: 'json',
          success:function(data){
            if(data){
              $('#connection_type_name').val( data.name ).prev().addClass('active');
              $('#connection_type_is_active').prop('checked', data.is_active);
            } else {
               $('#connectionTypeModal').hide();
               location.reload();
            }
          }
        });
      } else {
        $('#connectionTypeModalLabel').html('Nuevo tipo de conexión');
        $('#connectionTypeModal').modal('show');
        $('#connectionTypeForm').attr('action', '/connection_type/add_connection_type');
      }
    });
  });
    
  /*
  * Delete for connection type module
  */
  $(document).ready(function(){
    $(document).on('click', '#deleteConnectionTypeButton', function(){
      var connection_type_id = $(this).attr('data-id');
      $('#deleteConnectionTypeForm').attr('action', '/connection_type/delete_connection_type/' + connection_type_id)
    });
  });