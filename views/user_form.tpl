% rebase('base.tpl')

<div class="row justify-content-center">
    <div class="col-lg-8 col-xl-6">
        <div class="card">
            <div class="card-header">
                <h3 class="mb-0">{{ 'Editar Usuário' if user else 'Novo Usuário' }}</h3>
            </div>
            <div class="card-body">
                % if error:
                    <div class="alert alert-danger">
                        <i class="fas fa-exclamation-triangle me-2"></i>{{ error }}
                    </div>
                % end

                <form action="{{ '/users/' + str(user['id']) + '/update' if user else '/users/new' }}" method="post">
                    <div class="mb-3">
                        <label for="name" class="form-label">Nome Completo</label>
                        <input type="text" class="form-control" id="name" name="name"
                               value="{{ user['name'] if user else '' }}" required
                               placeholder="Nome completo do usuário">
                    </div>

                    <div class="mb-3">
                        <label for="email" class="form-label">Email</label>
                        <input type="email" class="form-control" id="email" name="email"
                               value="{{ user['email'] if user else '' }}" required
                               placeholder="usuario@email.com">
                    </div>

                    <div class="mb-4">
                        <label for="birthdate" class="form-label">Data de Nascimento</label>
                        <input type="date" class="form-control" id="birthdate" name="birthdate"
                               value="{{ user['birthdate'] if user else '' }}">
                        <div class="form-text">Opcional - para calcular idade</div>
                    </div>

                    % if not user:
                        <div class="mb-4">
                            <label for="password" class="form-label">Senha</label>
                            <input type="password" class="form-control" id="password" name="password"
                                   required placeholder="Crie uma senha segura" minlength="6">
                            <div class="form-text">Mínimo de 6 caracteres</div>
                        </div>
                    % end

                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <a href="/users" class="btn btn-outline-secondary me-md-2">Voltar</a>
                        <button type="submit" class="btn btn-success">{{ 'Salvar Alterações' if user else 'Criar Usuário' }}</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
