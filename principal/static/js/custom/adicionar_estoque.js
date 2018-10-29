function adicionar_estoque(produto, usuario, quantidade) {
  quantidade = $(`#quantidade-produto-${produto}`).val();
  swal({
      title: "Deseja incluir produto ao estoque ?",
      text: "",
      type: "warning",
      showCancelButton: true,
      confirmButtonClass: 'btn-danger',
      confirmButtonText: 'Sim',
      cancelButtonText: 'não',
      closeOnConfirm: false,
    },
    function () {
      window.location.replace(`/estoque/inserir/${produto}/${usuario}/${quantidade}`);
    });
}