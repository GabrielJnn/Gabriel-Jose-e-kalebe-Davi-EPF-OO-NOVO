% rebase('base.tpl')

<h2>Histórico de Rega</h2>

% if waterings:
    <ul>
    % for w in waterings:
        <li>
            Planta: <strong>{{w['plant_name']}}</strong><br>
            Data: {{w['date']}}
        </li>
    % end
    </ul>
% else:
    <p>Nenhuma rega registrada.</p>
% end

<p><a href="/plants">Voltar</a></p>
