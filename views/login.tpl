% rebase('base.tpl')

<div class="login-container">
    <h2>Login</h2>

    % if error:
        <p style="color:red;">{{error}}</p>
    % end

    <form action="/login" method="post">
        <label>Email:</label>
        <input type="email" name="email" required>

        <label>Senha:</label>
        <input type="password" name="password" required>

        <button type="submit">Entrar</button>
    </form>

    <p>Ainda não tem conta? <a href="/register">Criar conta</a></p>
</div>
