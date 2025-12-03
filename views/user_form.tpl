% rebase('base.tpl')

<div class="container">
    <h2>{{title}}</h2>

<form action="{{action}}" method="POST">

    <label>Nome</label>
    <input type="text" name="name" value="{{user.get('name','')}}" required>

    <label>Email</label>
    <input type="email" name="email" value="{{user.get('email','')}}" required>

    <label>Senha</label>
    <input type="password" name="password" required>

    <button class="btn">Salvar</button>
</form>

</div>
