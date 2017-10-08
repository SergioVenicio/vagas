$(".form-control").on({
  focusin: function () {
    $(this).parent().addClass('has-info');
  },
  focusout: function () {
    $(this).parent().removeClass('has-info');
  }
});
$("#id_Confirm_senha").on({
  focusin: function () {
    $(this).parent().removeClass('has-error');
  }
});
$("#id_senha").on({
  focusin: function () {
    $(this).parent().removeClass('has-error');
  }
});
