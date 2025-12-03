% rebase('layout.tpl', user_id=None)
% block include
<h3>Login</h3>
% if error:
  <div class="alert alert-danger">{{error}}</div>
% end
<form method="post" action="/login">
  <div class="mb-3">
    <label>Email</label>
    <input name="email" class="form-control" />
  </div>
  <div class="mb-3">
    <label>Senha</label>
    <input name="password" type="password" class="form-control" />
  </div>
  <button class="btn btn-primary" type="submit">Entrar</button>
</form>
% end