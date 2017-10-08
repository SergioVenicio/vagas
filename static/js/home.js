$(".excluir").on({
  click: function () {
    var id = $(this).val();
    $("#excluirModal").modal();
    $("#confirmar").on({
      click: function () {
        $.ajax({
          url: '../empresa/vaga/excluir/',
          method: 'POST',
          dataType: 'json',
          data: {id: id},
          success: function (data)
          {
            location.reload();
          },
          error: function () {
            alert('Lamentamos, não foi possivel excluir essa vaga, tente novamente mais tarde!');
          }
        });
      }
    });
  }
});
