% rebase('base.tpl')

<div>
  <h2>Registros de Rega — {{plant['name']}}</h2>

  % if waterings:
    % for w in waterings:
      <div class="card">
        <p><strong>Data:</strong> {{w['date']}}</p>
      </div>
    % end
  % else:
    <div class="card">
      <p>Sem registros ainda.</p>
    </div>
  % end

  <div style="margin-top:10px;">
    <a class="btn" href="/plants/{{plant['id']}}/water">Regar Agora</a>
    <a class="btn ghost" href="/plants">Voltar</a>
  </div>
</div>
