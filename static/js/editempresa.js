$(".form-control").on({
  focusin: function () {
    $(this).parent().addClass('has-warning');
  },
  focusout: function () {
    $(this).parent().removeClass('has-warning');
  }
});
$("#id_Confirm_senha").on({
  focusin: function () {
    $(this).parent().removeClass('has-warning');
  }
});
$("#id_senha").on({
  focusin: function () {
    $(this).parent().removeClass('has-warning');
  }
});

$("#btn-editar").on({
  click: function () {
    var id = $("#id").val();
    var Formcandidato = $("#formEditarVaga");
    var descricao = Formcandidato[0][1].value;
    var faixa_salarial_min = Formcandidato[0][2].value;
    var faixa_salarial_max = Formcandidato[0][3].value;
    var experiencia = Formcandidato[0][4].value;
    var escolaridade = Formcandidato[0][5].value;
    var distancia = Formcandidato[0][6].value;

    $.ajax({
      url: '.',
      method: 'POST',
      dataType: 'json',
      data: {
        id: id, descricao: descricao, faixa_salarial_min: faixa_salarial_min,
        faixa_salarial_max: faixa_salarial_max, experiencia: experiencia,
        escolaridade: escolaridade, distancia: distancia
      },
      success: function (data) {
        $("#successModal").modal();
        $("#successModal").on({
          'hide.bs.modal': function () {
            window.location = 'http://localhost:8000/home/';
          }
        });
      }
    });
  }
});
