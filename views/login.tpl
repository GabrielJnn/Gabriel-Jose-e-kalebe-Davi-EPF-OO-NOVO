% rebase('base.tpl')

<div class="row justify-content-center">
    <div class="col-lg-6 col-xl-4">
        <div class="card">
            <div class="card-header text-center">
                <h3 class="mb-0">Entrar no PlantsVsTime</h3>
            </div>
            <div class="card-body">
                % if error:
                    <div class="alert alert-danger">
                        ⚠️ {{ error }}
                    </div>
                % end

                <form action="/login" method="post">
                    <div class="mb-4">
                        <label for="email" class="form-label">
                            <span style="font-size: 1.1em;">📧</span> Email
                        </label>
                        <input type="email" class="form-control" id="email" name="email"
                               required placeholder="seu@email.com">
                    </div>

                    <div class="mb-4">
                        <label for="password" class="form-label">
                            <span style="font-size: 1.1em;">🔒</span> Senha
                        </label>
                        <input type="password" class="form-control" id="password" name="password"
                               required placeholder="Sua senha">
                    </div>

                    <div class="d-grid">
                        <button type="submit" class="btn btn-success">
                            <span style="font-size: 1.1em;">🚀</span> Entrar no PlantsVsTime
                        </button>
                    </div>
                </form>

                <div class="text-center mt-4">
                    <p class="mb-3" style="color: #7f8c8d;">Ainda não tem conta?</p>
                    <a href="/signup" class="btn btn-outline-primary">
                        <span style="font-size: 1.1em;">✨</span> Criar Minha Conta
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>
