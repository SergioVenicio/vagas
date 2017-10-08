$("#btn-editar").on({
  click: function () {
    var Formcandidato = $("#form_editar_candidato");
    var escolaridade = Formcandidato[0][1].value;
    var experiencia = Formcandidato[0][2].value;
    var distancia = Formcandidato[0][3].value;
    var faixa_salarial = Formcandidato[0][4].value;
    $.ajax({
      url: '.',
      method: 'POST',
      dataType: 'json',
      data: {
        escolaridade: escolaridade, experiencia: experiencia,
        distancia: distancia, faixa_salarial: faixa_salarial
      },
      success: function (data) {
        $("#successModal").modal();
      }
    });
  }
});
