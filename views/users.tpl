% rebase('base.tpl')

<h2>Usuários Cadastrados</h2>

% if users:
    <ul>
    % for u in users:
        <li>
            <strong>{{u['name']}}</strong> – {{u['email']}}
            <br>
            <a href="/users/{{u['id']}}/edit">Editar</a> |
            <a href="/users/{{u['id']}}/delete">Excluir</a>
        </li>
    % end
    </ul>
% else:
    <p>Nenhum usuário encontrado.</p>
% end

<p><a href="/">Voltar</a></p>
