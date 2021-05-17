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


/*
* Table access module
*/
$(document).ready(function(){
  $(document).on('click', '#accessButton', function(){
    $("#accessTable tbody tr").empty();
    var server_id = $(this).attr('data-id');
    if(server_id){
      $.ajax({
        url: '/server/get_server_access',
        method: 'post',
        data: {server_id: server_id},
        dataType: 'json',
        success:function(access){
          $.each(access, function(key, val) {
            $('<tr>').append(
              $('<td>').text(val.server_name),
              $('<td>').text(val.connection_type_name),
              $('<td>').text(val.ip_local),
              $('<td>').text(val.port_local),
              $('<td>').text(val.ip_public),
              $('<td>').text(val.port_public),
              $('<td>').text(val.username),
              $('<td>').text(val.password),
              $('<td>').text(val.is_active)
          ).appendTo('#accessTable');
          });
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
* Add and edit for access module
*/
$(document).ready(function(){
  $(document).on('click', '#addAccessButton, #editAccessButton', function(){
    $('#accessForm')[0].reset();
    var access_id = $(this).parent().attr('access-id');
    var server_id = $('#accessButton').attr('data-id');
    console.log(server_id);
    if(access_id){
      $('#addEditAccessModalLabel').html('Editar acceso');
      $('#accessForm').attr('action', '/server/edit_server_access/' + access_id);
      $.ajax({
        url: '/server/get_server_access',
        method: 'post',
        data: {access_id: access_id},
        dataType: 'json',
        success:function(data){
          if(data){
            $('#name').val( data.name ).prev().addClass('active');
            $('#environment_id').val( data.environment_id );
            $('#operating_system_id').val( data.operating_system_id );
            $('#cpu').val( data.cpu ).prev().addClass('active');
            $('#ram').val( data.ram ).prev().addClass('active');
            $('#hdd').val( data.hdd ).prev().addClass('active');
            $('#is_active').prop('checked', data.is_active);
          } else {
             $('#addEditAccessModal').hide();
             location.reload();
          }
        }
      });
    } else {
      $('#addEditAccessModalLabel').html('Nuevo acceso');
      $('#addEditAccessModal').modal('show');
      $('#accessForm').attr('action', '/server/add_server_access');
      $('#server_id').val(server_id)
    }
  });
});