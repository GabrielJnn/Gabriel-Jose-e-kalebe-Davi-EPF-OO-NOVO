% rebase('base.tpl')

<h2>Minhas Plantas</h2>

% if plants:
    <ul>
    % for p in plants:
        <li>
            <strong>{{ p['name'] }}</strong><br>
            Espécie: {{ p['species'] }}<br>
            Última rega: {{ p.get('last_watering', 'Nunca') }}<br>
            <a href="/plants/{{p['id']}}/edit">Editar</a>
        </li>
    % end
    </ul>
% else:
    <p>Nenhuma planta cadastrada.</p>
% end

<a href="/plants/new" class="btn">Cadastrar nova planta</a>
