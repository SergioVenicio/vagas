$("#btn-editar").on({
  click: function() {
    var Formcandidato = $("#form_editar_candidato");
    var email = Formcandidato[0][1].value;
    var escolaridade = Formcandidato[0][2].value;
    var experiencia = Formcandidato[0][3].value;
    var distancia = Formcandidato[0][4].value;
    var faixa_salarial = Formcandidato[0][5].value;
    var senha = Formcandidato[0][6].value;
    var Confirm_senha = Formcandidato[0][7].value;
    var id = Formcandidato[0][8].value;
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
              id: id, email: email, escolaridade: escolaridade,
              experiencia: experiencia, distancia: distancia,
              faixa_salarial: faixa_salarial, senha: senha
            },
            success: function(data)
            {
              $(".modal-title").text('Alteração de perfil');
              $(".modal-text").text('Perfil atualizado com sucesso.');
              $("#errorModal").modal();
            },
            error: function ()
            {
              $(".modal-title").text('Alteração de perfil');
              $(".modal-text").text('Lamentamos, não conseguimos alterar o perfil, tente novamente mais tarde.');
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
          id: id, email: email, escolaridade: escolaridade,
          experiencia: experiencia, distancia: distancia,
          faixa_salarial: faixa_salarial
        },
        success: function(data)
        {
          $(".modal-title").text('Alteração de perfil');
          $(".modal-text").text('Perfil atualizado com sucesso.');
          $("#errorModal").modal();
        },
        error: function ()
        {
          $(".modal-title").text('Alteração de perfil');
          $(".modal-text").text('Lamentamos, não conseguimos alterar o perfil, tente novamente mais tarde.');
          $("#errorModal").modal();
        },
      });
    }
  }
});
