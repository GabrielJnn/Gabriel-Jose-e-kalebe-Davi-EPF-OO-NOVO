% rebase('base.tpl')

<h2>Editar Usuário</h2>

<form action="/users/{{ user['id'] }}/update" method="post">

    <label>Nome:</label><br>
    <input type="text" name="name" value="{{ user['name'] }}" required><br><br>

    <label>Email:</label><br>
    <input type="email" name="email" value="{{ user['email'] }}" required><br><br>

    <label>Data de nascimento:</label><br>
    <input type="date" name="birthdate" value="{{ user['birthdate'] }}"><br><br>

    <button type="submit">Salvar</button>
</form>

<p><a href="/users">Voltar</a></p>
