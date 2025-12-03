% rebase('layout.tpl', user_id=user_id)
% block include
<h3>Minhas Plantas</h3>
<p><a class="btn btn-success" href="/plants/new">Adicionar Planta</a></p>
% if not plants:
  <p>Você não tem plantas cadastradas.</p>
% else:
  <table class="table">
    <thead><tr><th>Nome</th><th>Espécie</th><th>Intervalo (dias)</th><th>Ações</th></tr></thead>
    <tbody>
      % for p in plants:
        <tr>
          <td>{{p["name"]}}</td>
          <td>{{p["species"]}}</td>
          <td>{{p["watering_interval_days"]}}</td>
          <td>
            <a class="btn btn-sm btn-primary" href="/plants/{{p['id']}}">Detalhes</a>
            <a class="btn btn-sm btn-warning" href="/plants/edit/{{p['id']}}">Editar</a>
            <form style="display:inline" method="post" action="/plants/delete/{{p['id']}}">
              <button class="btn btn-sm btn-danger" type="submit">Remover</button>
            </form>
          </td>
        </tr>
      % end
    </tbody>
  </table>
% end
% end