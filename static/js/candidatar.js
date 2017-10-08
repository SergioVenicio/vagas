$("#realizar_candidatura").on({
  click: function () {
    var id = $("#id").val();
    $.ajax({
      url: '.',
      method: 'POST',
      dataType: 'json',
      data: {
        id: id
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
