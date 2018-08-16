(function ($) {
  "use strict";

  $('.dropdown-toggle').dropdown()

  var logout_btn = $('#logout');

  logout_btn.click(() => {
    swal({
        title: "Deseja realmente sair do sistema ?",
        text: "",
        type: "warning",
        showCancelButton: true,
        confirmButtonClass: 'btn-danger',
        confirmButtonText: 'Sim',
        cancelButtonText: 'não',
        closeOnConfirm: false,
      },
      function () {
        window.location.replace("/logout");
      });
  });


})(jQuery);