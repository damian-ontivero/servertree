/*
* Add and edit for server module
*/
$(document).ready(function(){
  $(document).on('click', '#addServerButton, #editServerButton', function(){
    $('#serverForm')[0].reset();
    var server_id = $(this).attr('data-id');
    if(server_id){
      $('#serverModalLabel').html('Editar servidor');
      $('#serverForm').attr('action', '/server/edit_server/' + server_id);
      $.ajax({
        url: '/server/get_server_by_id',
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
  $(document).on('click', '#deleteServerButton', function(){
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
        url: '/server/get_access_by_server_id',
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
      $('#accessForm').attr('action', '/server/edit_access/' + access_id);
      $.ajax({
        url: '/server/get_access_by_id',
        method: 'post',
        data: {access_id: access_id},
        dataType: 'json',
        success:function(data){
          if(data){
            $('#access_server_id').val( data.server_id );
            $('#access_connection_type_id').val( data.connection_type_id );
            $('#access_ip_local').val( data.ip_local ).prev().addClass('active');
            $('#access_port_local').val( data.port_local ).prev().addClass('active');
            $('#access_ip_public').val( data.ip_public ).prev().addClass('active');
            $('#access_port_public').val( data.port_public ).prev().addClass('active');
            $('#access_username').val( data.username ).prev().addClass('active');
            $('#access_password').val( data.password ).prev().addClass('active');
            $('#access_is_active').prop('checked', data.is_active);
          } else {
             $('#addEditAccessModal').hide();
             location.reload();
          }
        }
      });
    } else {
      $('#addEditAccessModalLabel').html('Nuevo acceso');
      $('#addEditAccessModal').modal('show');
      $('#accessForm').attr('action', '/server/add_access');
      $('#access_server_id').val(server_id)
    }
  });
});

/*
* Delete for acesss module
*/
$(document).ready(function(){
  $(document).on('click', '#deleteAccessButton', function(){
    var access_id = $(this).attr('data-id');
    $('#deleteAccessForm').attr('action', '/server/delete_access/' + access_id)
  });
});

/*
* Table service module
*/
$(document).ready(function(){
  $(document).on('click', '#serviceButton', function(){
    $("#serviceTable tbody tr").empty();
    server_id = $(this).attr('data-id');
    if(server_id){
      $.ajax({
        url: '/server/get_service_by_server_id',
        method: 'post',
        data: {server_id: server_id},
        dataType: 'json',
        success:function(access){
          $.each(access, function(key, val) {
            $('<tr>').append(
              $('<td>').text(val.server_name),
              $('<td>').text(val.service),
              $('<td>').text(val.version),
              $('<td>').text(val.architect),
              $('<td>').text(val.ip_local),
              $('<td>').text(val.port_local),
              $('<td>').text(val.ip_public),
              $('<td>').text(val.port_public),
              $('<td>').text(val.install_dir),
              $('<td>').text(val.log_dir),
              $('<td>').text(val.is_active),
              $('<td><button type="button" class="btn btn-info btn-sm" id="editServiceButton" data-id='+val.service_id+' data-bs-dismiss="modal" data-bs-toggle="modal" data-bs-target="#addEditServiceModal"><i class="fas fa-edit"></i></button></td>'),
              $('<td><button type="button" class="btn btn-danger btn-sm" id="deleteServiceButton" data-id='+val.service_id+' data-bs-dismiss="modal" data-bs-toggle="modal" data-bs-target="#deleteServiceModal"><i class="fas fa-trash-alt"></i></button></td>')
          ).appendTo('#serviceTable');
          });
        }
      });
    }
  });


  /*
  * Add and edit for service module
  */
  $(document).on('click', '#addServiceButton, #editServiceButton', function(){
    $('#serviceForm')[0].reset();
    service_id = $(this).attr('data-id');
    if(service_id){
      $('#addEditServiceModalLabel').html('Editar servicio');
      $('#serviceForm').attr('action', '/server/edit_service/' + service_id);
      $.ajax({
        url: '/server/get_service_by_id',
        method: 'post',
        data: {service_id: service_id},
        dataType: 'json',
        success:function(data){
          if(data){
            $('#service_server_id').val( data.server_id );
            $('#service').val( data.service ).prev().addClass('active');
            $('#service_version').val( data.version ).prev().addClass('active');
            $('#service_architect').val( data.architect ).prev().addClass('active');
            $('#service_ip_local').val( data.ip_local ).prev().addClass('active');
            $('#service_port_local').val( data.port_local ).prev().addClass('active');
            $('#service_ip_public').val( data.ip_public ).prev().addClass('active');
            $('#service_port_public').val( data.port_public ).prev().addClass('active');
            $('#service_install_dir').val( data.install_dir ).prev().addClass('active');
            $('#service_log_dir').val( data.log_dir ).prev().addClass('active');
            $('#service_is_active').prop('checked', data.is_active);
          } else {
             $('#addEditServiceModal').hide();
             location.reload();
          }
        }
      });
    } else {
      $('#addEditServiceModalLabel').html('Nuevo servicio');
      $('#addEditServiceModal').modal('show');
      $('#serviceForm').attr('action', '/server/add_service');
      $('#service_server_id').val(server_id)
    }
  });
});

/*
* Delete for service module
*/
$(document).ready(function(){
  $(document).on('click', '#deleteServiceButton', function(){
    var service_id = $(this).attr('data-id');
    $('#deleteServiceForm').attr('action', '/server/delete_service/' + service_id)
  });
});