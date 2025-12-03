% rebase('base.tpl')

<div class="row justify-content-center">
    <div class="col-lg-6 col-xl-4">
        <div class="card">
            <div class="card-header text-center">
                <h3 class="mb-0">Criar Conta no PlantsVsTime</h3>
            </div>
            <div class="card-body">
                % if error:
                    <div class="alert alert-danger">
                        ⚠️ {{ error }}
                    </div>
                % end

                <form action="/signup" method="post">
                    <div class="mb-4">
                        <label for="name" class="form-label">
                            <span style="font-size: 1.1em;">👤</span> Nome Completo
                        </label>
                        <input type="text" class="form-control" id="name" name="name"
                               required placeholder="Seu nome completo">
                    </div>

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
                               required placeholder="Crie uma senha segura" minlength="6">
                        <div class="form-text">Mínimo de 6 caracteres</div>
                    </div>

                    <div class="d-grid">
                        <button type="submit" class="btn btn-success">
                            <span style="font-size: 1.1em;">🌱</span> Criar Minha Conta
                        </button>
                    </div>
                </form>

                <div class="text-center mt-4">
                    <p class="mb-3" style="color: #7f8c8d;">Já tem conta?</p>
                    <a href="/login" class="btn btn-outline-primary">
                        <span style="font-size: 1.1em;">🚀</span> Entrar
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>
