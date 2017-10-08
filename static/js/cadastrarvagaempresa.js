$(".form-control").on({
  focusin: function () {
    $(this).parent().addClass('has-danger');
  },
  focusout: function () {
    $(this).parent().removeClass('has-danger');
  }
});
$("#successModal").modal();
