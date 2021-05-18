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
    server_id = $(this).attr('data-id');
    if(server_id){
      $.ajax({
        url: '/server/get_server_access_by_server_id',
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
              $('<td>').text(val.is_active),
              $('<td><button type="button" class="btn btn-info btn-sm" id="editAccessButton" data-id='+val.access_id+' data-bs-dismiss="modal" data-bs-toggle="modal" data-bs-target="#addEditAccessModal"><i class="fas fa-edit"></i></button></td>'),
              $('<td><button type="button" class="btn btn-danger btn-sm" id="deleteAccessButton" data-id='+val.access_id+' data-bs-dismiss="modal" data-bs-toggle="modal" data-bs-target="#deleteAccessModal"><i class="fas fa-trash-alt"></i></button></td>')
          ).appendTo('#accessTable');
          });
        }
      });
    }
  });


  /*
  * Add and edit for access module
  */
  $(document).on('click', '#addAccessButton, #editAccessButton', function(){
    $('#accessForm')[0].reset();
    access_id = $(this).attr('data-id');
    if(access_id){
      $('#addEditAccessModalLabel').html('Editar acceso');
      $('#accessForm').attr('action', '/server/edit_server_access/' + access_id);
      $.ajax({
        url: '/server/get_server_access_by_access_id',
        method: 'post',
        data: {access_id: access_id},
        dataType: 'json',
        success:function(data){
          if(data){
            $('#server_id').val( data.server_id );
            $('#connection_type_id').val( data.connection_type_id );
            $('#ip_local').val( data.ip_local ).prev().addClass('active');
            $('#port_local').val( data.port_local ).prev().addClass('active');
            $('#ip_public').val( data.ip_public ).prev().addClass('active');
            $('#port_public').val( data.port_public ).prev().addClass('active');
            $('#username').val( data.username ).prev().addClass('active');
            $('#password').val( data.password ).prev().addClass('active');
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

/*
* Delete for acesss module
*/
$(document).ready(function(){
  $(document).on('click', '#deleteAccessButton', function(){
    var access_id = $(this).attr('data-id');
    $('#deleteAccessForm').attr('action', '/server/delete_server_access/' + access_id)
  });
});