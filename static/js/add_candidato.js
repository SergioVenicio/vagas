$(".form-control").on({
  focusin: function () {
    $(this).parent().addClass('has-warning');
  },
  focusout: function () {
    $(this).parent().removeClass('has-warning');
  }
});
