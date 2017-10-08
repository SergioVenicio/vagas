$("#btn-editar").on({
  click: function() {
    var FormEmpresa = $("#form_editar_empresa");
    var email = FormEmpresa[0][1].value;
    var razao_social = FormEmpresa[0][2].value;
    var endereco = FormEmpresa[0][3].value;
    var ramo = FormEmpresa[0][4].value;
    var numero = FormEmpresa[0][5].value;
    var senha = FormEmpresa[0][6].value;
    var Confirm_senha = FormEmpresa[0][7].value;
    var id = FormEmpresa[0][8].value;
    console.log(FormEmpresa);
    if(senha)
    {
      if(senha.length >= 6)
      {
        if(senha === Confirm_senha)
        {
          $.ajax({
            url: '.',
            method: 'POST',
            dataType: 'json',
            data: {
              id: id, email: email, razao_social: razao_social,
              endereco: endereco, ramo: ramo, numero: numero, senha:senha
            },
            success: function(data)
            {
              $(".modal-title").text('Alteração de perfil');
              $(".modal-text").text('Perfil atualizado com sucesso.');
              $("#errorModal").modal();
            }
          });
        } else {
          $(".modal-title").text('As senhas não conferem');
          $(".modal-text").text('As senhas não são iguais.');
          $("#id_senha").parent().addClass('has-error');
          $("#id_Confirm_senha").parent().addClass('has-error');
          $("#errorModal").modal();
        }
      } else {
        $(".modal-title").text('Tamanho da senha');
        $(".modal-text").text('O tamanho da senha dever ser maior ou igual a 6, você digitou uma senha de ' + senha.length + ' caracteres.');
        $("#id_senha").parent().addClass('has-error');
        $("#errorModal").modal();
      }
    } else {
      $.ajax({
        url: '.',
        method: 'POST',
        dataType: 'json',
        data: {
          id: id, email: email, razao_social: razao_social,
          endereco: endereco, ramo: ramo, numero: numero
        },
        success: function(data)
        {
          $(".modal-title").text('Alteração de perfil');
          $(".modal-text").text('Perfil atualizado com sucesso.');
          $("#errorModal").modal();
        }
      });
    }
  }
});
