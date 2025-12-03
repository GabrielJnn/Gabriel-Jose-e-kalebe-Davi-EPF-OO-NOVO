% rebase('base.tpl')

<div>
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
    <h2>Minhas Plantas</h2>
    <a href="/plants/new" class="btn">+ Nova Planta</a>
  </div>

  % if plants:
    % for p in plants:
      <div class="card">
        <h3>{{p['name']}}</h3>
        <p><strong>Espécie:</strong> {{p['species']}}</p>
        <p><strong>Última rega:</strong> {{ p.get('last_watering','Nunca') }}</p>

        <div style="margin-top:8px;display:flex;gap:8px;">
          <a class="btn-ghost action-link" href="/plants/{{p['id']}}">Ver</a>
          <a class="btn-ghost action-link" href="/plants/edit/{{p['id']}}">Editar</a>
          <form method="post" action="/plants/delete/{{p['id']}}" style="display:inline;">
            <button class="btn ghost" type="submit">Remover</button>
          </form>
        </div>
      </div>
    % end
  % else:
    <div class="card">
      <p>Nenhuma planta cadastrada. Comece agora!</p>
      <a class="btn" href="/plants/new">Cadastrar</a>
    </div>
  % end
</div>
