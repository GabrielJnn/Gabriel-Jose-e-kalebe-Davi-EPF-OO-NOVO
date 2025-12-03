% rebase('base.tpl')

<div class="d-flex justify-content-between align-items-center mb-4">
    <h2 class="mb-0">Usuários Cadastrados</h2>
    <a href="/users/new" class="btn btn-success">Adicionar Usuário</a>
</div>

% if users:
    <div class="row">
    % for u in users:
        <div class="col-lg-6 col-xl-4 mb-4">
            <div class="plant-card">
                <div class="plant-name">{{ u['name'] }}</div>
                <div class="plant-info">
                    <i class="fas fa-envelope me-1"></i>{{ u['email'] }}
                </div>

                <div class="plant-actions">
                    <a href="/users/{{u['id']}}/edit" class="btn btn-outline-primary btn-sm">Editar</a>
                    <a href="/users/{{u['id']}}/delete" class="btn btn-danger btn-sm"
                       onclick="return confirm('Tem certeza que deseja excluir este usuário?')">Excluir</a>
                </div>
            </div>
        </div>
    % end
    </div>
% else:
    <div class="text-center py-5">
        <div style="font-size: 4rem; color: #e9ecef; margin-bottom: 1rem;">👥</div>
        <h4 class="text-muted">Nenhum usuário cadastrado</h4>
        <p class="text-muted mb-4">Comece adicionando o primeiro usuário ao sistema!</p>
        <a href="/users/new" class="btn btn-success">Adicionar Primeiro Usuário</a>
    </div>
% end

<div class="mt-4">
    <a href="/" class="btn btn-outline-secondary">Voltar ao Início</a>
</div>
