% rebase('layout.tpl', user_id=user_id)
% block include
<div class="d-flex justify-content-between">
  <h3>Planta: {{plant['name']}}</h3>
  <form method="post" action="/plants/{{plant['id']}}/water">
    <button class="btn btn-primary" type="submit">Regar Agora</button>
  </form>
</div>
<p>Espécie: {{plant['species']}} • Intervalo: {{plant['watering_interval_days']}} dias</p>

<h5>Registros de Rega</h5>
% if not waterings:
  <p>Ainda não há registros.</p>
% else:
  <ul>
  % for w in waterings:
    <li>{{w['date']}} (usuário #{{w['user_id']}})</li>
  % end
  </ul>
% end

<p><a href="/plants" class="btn btn-secondary">Voltar</a></p>
% end