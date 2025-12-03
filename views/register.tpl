% rebase('layout.tpl', user_id=None)
% block include
<h3>Registrar</h3>
% if error:
  <div class="alert alert-danger">{{error}}</div>
% end
<form method="post" action="/register">
  <div class="mb-3">
    <label>Nome</label>
    <input name="name" class="form-control" />
  </div>
  <div class="mb-3">
    <label>Email</label>
    <input name="email" class="form-control" />
  </div>
  <div class="mb-3">
    <label>Senha</label>
    <input name="password" type="password" class="form-control" />
  </div>
  <button class="btn btn-success" type="submit">Registrar</button>
</form>
% end