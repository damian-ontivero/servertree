/*
* Add and edit for server module
*/
$(document).ready(function(){
  $(document).on('click', '#addButton, #editButton', function(){
    $('#serverForm')[0].reset();
    var server_id = $(this).attr('data-id');
    if(server_id){
      $('#serverModalLabel').html('Editar servidor');
      $('#serverForm').attr('action', '/server/edit_server/' + server_id);
      $.ajax({
        url: '/server/get_server',
        method: 'post',
        data: {server_id: server_id},
        dataType: 'json',
        success:function(data){
          console.log(data)
          if(data){
            $('#name').val( data.name ).prev().addClass('active');
            $('#environment_id').val( data.environment_id );
            $('#operating_system_id').val( data.operating_system_id );
            $('#cpu').val( data.cpu ).prev().addClass('active');
            $('#ram').val( data.ram ).prev().addClass('active');
            $('#hdd').val( data.hdd ).prev().addClass('active');
            $('#is_active').prop('checked', data.is_active);
          } else {
             $('#serverModal').hide();
             location.reload();
          }
        }
      });
    } else {
      $('#serverModalLabel').html('Nuevo servidor');
      $('#serverModal').modal('show');
      $('#serverForm').attr('action', '/server/add_server');
    }
  });
});
  
/*
* Delete for server module
*/
$(document).ready(function(){
  $(document).on('click', '#deleteButton', function(){
    var server_id = $(this).attr('data-id');
    $('#deleteServerForm').attr('action', '/server/delete_server/' + server_id)
  });
});