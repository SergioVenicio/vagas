$(".btn-excluir").on({
  click: function () {
    var id = $(this).val();
    $("#exluirModal").modal();
    $("#excluir").on({
      click: function () {
        $.ajax({
          url: '/empresa/deletar/vaga_candidato/',
          method: 'POST',
          dataType: 'json',
          data: {id: id},
          success: function (data)
          {
            location.reload();
          },
          error: function ()
          {
            $("#excluirModal").modal();
            $(".modal-text").text('Lamentamos, não foi possivel excluir o candidato, tente novamnete mais tarde.');
            $("#excluir").delete;
          }
        });
      }
    });
  }
});
