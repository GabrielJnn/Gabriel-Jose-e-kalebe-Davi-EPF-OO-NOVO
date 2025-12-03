% rebase('base.tpl')

<div class="register-container">
    <h2>Criar Conta</h2>

    % if error:
        <p style="color:red;">{{error}}</p>
    % end

    <form action="/register" method="post">
        <label>Nome:</label>
        <input type="text" name="name" required>

        <label>Email:</label>
        <input type="email" name="email" required>

        <label>Senha:</label>
        <input type="password" name="password" required>

        <button type="submit">Registrar</button>
    </form>

    <p>Já tem conta? <a href="/login">Entrar</a></p>
</div>
