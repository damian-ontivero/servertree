/*
* Add and edit for user module
*/
$(document).ready(function(){
    $(document).on('click', '#addButton, #editButton', function(){
      $('#userForm')[0].reset();
      var change_password_label = document.getElementById('change_password_label');
      var change_password = document.getElementById('change_password');
      var password_label = document.getElementById('password_label');
      var password = document.getElementById('password');
      var show_password = document.getElementById('show_password');
      var show_password_label = document.getElementById('show_password_label');
      var user_id = $(this).attr('data-id');
      if(user_id){
        $('#userModalLabel').html('Editar usuario');
        $('#userForm').attr('action', '/auth/edit_user/' + user_id);
        $.ajax({
          url: '/auth/get_user',
          method: 'post',
          data: {user_id: user_id},
          dataType: 'json',
          success:function(data){
            if(data){
              $('#firstname').val( data.firstname ).prev().addClass('active');
              $('#lastname').val( data.lastname ).prev().addClass('active');
              $('#email').val( data.email ).prev().addClass('active');
              $('#password').val( data.password ).prev().addClass('active');
              $('#role_id').val( data.role_id );
              $('#is_active').prop('checked', data.is_active);
            } else {
               $('#userModal').hide();
               location.reload();
            }
          }
        });
        change_password_label.style.display = "block";
        change_password.style.display = "block";
        password_label.style.display = "none";
        password.style.display = "none";
        show_password.style.display = "none";
        show_password_label.style.display = "none";
        change_password.addEventListener('change', function() {
          if(change_password.checked) {
            password.style.display = "block";
            $(password).val('');
            password_label.style.display = "block";
            show_password.style.display = "block";
            show_password_label.style.display = "block";
            show_password.addEventListener('change', function() {
              if(show_password.checked) {
                password.type = 'text';
              } else {
                password.type = 'password';
              }
            })
          } else {
            password.style.display = "none";
            password_label.style.display = "none";
            show_password.style.display = "none";
            show_password_label.style.display = "none";
          }
        });
      } else {
        $('#userModalLabel').html('Nuevo usuario');
        $('#userModal').modal('show');
        $('#userForm').attr('action', '/auth/add_user');
        change_password_label.style.display = "none";
        change_password.style.display = "none";
        password_label.style.display = "block";
        password.style.display = "block";
        show_password.style.display = "block";
        show_password_label.style.display = "block";
        show_password.addEventListener('change', function() {
          if(show_password.checked) {
            password.type = 'text';
          } else {
            password.type = 'password';
          }
        });
      }
    });
});

/*
* Delete for user module
*/
$(document).ready(function(){
    $(document).on('click', '#deleteButton', function(){
      var user_id = $(this).attr('data-id');
      $('#deleteUserForm').attr('action', '/auth/delete_user/' + user_id)
    });
});