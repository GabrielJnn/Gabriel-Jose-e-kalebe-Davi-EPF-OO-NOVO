% rebase('layout.tpl', user_id=user_id)
% block include
% if plant:
  <h3>Editar Planta</h3>
% else:
  <h3>Nova Planta</h3>
% end
% if error:
  <div class="alert alert-danger">{{error}}</div>
% end
<form method="post" action="{{action}}">
  <div class="mb-3">
    <label>Nome</label>
    <input name="name" class="form-control" value="% if plant: {{plant['name']}} % end">
  </div>
  <div class="mb-3">
    <label>Espécie</label>
    <input name="species" class="form-control" value="% if plant: {{plant['species']}} % end">
  </div>
  <div class="mb-3">
    <label>Intervalo de rega (dias)</label>
    <input name="interval" type="number" class="form-control" value="% if plant: {{plant['watering_interval_days']}} else: 3 % end">
  </div>
  <button class="btn btn-success" type="submit">Salvar</button>
</form>
% end