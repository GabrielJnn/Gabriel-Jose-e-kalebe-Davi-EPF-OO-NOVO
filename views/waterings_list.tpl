% rebase('base.tpl')

<div class="d-flex justify-content-between align-items-center mb-4">
    <h2 class="mb-0">Histórico de Rega - {{ plant['name'] if plant else 'Planta' }}</h2>
    <a href="/plants/{{plant['id']}}/watering/new" class="btn btn-success">Registrar Rega</a>
</div>

% if waterings:
    <div class="card">
        <div class="card-body">
            <div class="list-group list-group-flush">
            % for w in waterings:
                <div class="list-group-item d-flex justify-content-between align-items-center">
                    <div>
                        <strong>Rega realizada</strong>
                        <small class="text-muted ms-2">{{ w['date'] }}</small>
                    </div>
                    <span class="badge bg-success">Concluída</span>
                </div>
            % end
            </div>
        </div>
    </div>

    <div class="mt-3 text-muted">
        <small>Total de regas: {{ len(waterings) }}</small>
    </div>
% else:
    <div class="text-center py-5">
        <div style="font-size: 4rem; color: #e9ecef; margin-bottom: 1rem;">💧</div>
        <h4 class="text-muted">Nenhuma rega registrada ainda</h4>
        <p class="text-muted mb-4">Comece registrando a primeira rega desta planta!</p>
        <a href="/plants/{{plant['id']}}/watering/new" class="btn btn-success">Registrar Primeira Rega</a>
    </div>
% end

<div class="mt-4">
    <a href="/plants" class="btn btn-outline-secondary">Voltar às Plantas</a>
</div>
