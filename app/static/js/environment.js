/*
* Add and edit for environment module
*/
$(document).ready(function(){
    $(document).on('click', '#addEnvironmentButton, #editEnvironmentButton', function(){
      $('#environmentForm')[0].reset();
      var environment_id = $(this).attr('data-id');
      if(environment_id){
        $('#environmentModalLabel').html('Editar entorno');
        $('#environmentForm').attr('action', '/environment/edit/' + environment_id);
        $.ajax({
          url: '/environment/get_by_id',
          method: 'post',
          data: {environment_id: environment_id},
          dataType: 'json',
          success:function(data){
            if(data){
              $('#environment_name').val( data.name ).prev().addClass('active');
              $('#environment_is_active').prop('checked', data.is_active);
            } else {
               $('#environmentModal').hide();
               location.reload();
            }
          }
        });
      } else {
        $('#environmentModalLabel').html('Nuevo entorno');
        $('#environmentModal').modal('show');
        $('#environmentForm').attr('action', '/environment/add');
      }
    });
  });
    
  /*
  * Delete for environment module
  */
  $(document).ready(function(){
    $(document).on('click', '#deleteEnvironmentButton', function(){
      var environment_id = $(this).attr('data-id');
      $('#deleteEnvironmentForm').attr('action', '/environment/delete/' + environment_id)
    });
  });