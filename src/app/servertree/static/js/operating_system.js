/*
* Add and edit for operating system type module
*/
$(document).ready(function(){
    $(document).on('click', '#addOperatingSystemButton, #editOperatingSystemButton', function(){
      $('#operatingSystemForm')[0].reset();
      var operating_system_id = $(this).attr('data-id');
      if(operating_system_id){
        $('#operatingSystemModalLabel').html('Editar sistema operativo');
        $('#operatingSystemForm').attr('action', '/operating_system/edit/' + operating_system_id);
        $.ajax({
          url: '/operating_system/get/' + operating_system_id,
          method: 'post',
          data: {operating_system_id: operating_system_id},
          dataType: 'json',
          success:function(data){
            if(data){
              $('#operating_system_name').val( data.name ).prev().addClass('active');
              $('#operating_system_version').val( data.version ).prev().addClass('active');
              $('#operating_system_architect').val( data.architect ).prev().addClass('active');
              $('#operating_system_is_active').prop('checked', data.is_active);
            } else {
               $('#operatingSystemModal').hide();
               location.reload();
            }
          }
        });
      } else {
        $('#operatingSystemModalLabel').html('Nuevo sistema operativo');
        $('#operatingSystemModal').modal('show');
        $('#operatingSystemForm').attr('action', '/operating_system/add');
      }
    });
  });
    
  /*
  * Delete for operating system module
  */
  $(document).ready(function(){
    $(document).on('click', '#deleteOperatingSystemButton', function(){
      var operating_system_id = $(this).attr('data-id');
      $('#deleteOperatingSystemForm').attr('action', '/operating_system/delete/' + operating_system_id)
    });
  });