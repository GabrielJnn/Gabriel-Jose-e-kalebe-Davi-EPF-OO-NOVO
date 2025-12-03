% rebase('base.tpl')

<div class="text-center mb-5">
    <h2 class="mb-3">Minhas Plantas</h2>
    <p class="text-muted mb-4">Gerencie sua coleção de plantas e mantenha todas elas saudáveis</p>
    <a href="/plants/new" class="btn btn-success">
        <span style="font-size: 1.1em;">➕</span> Adicionar Nova Planta
    </a>
</div>

% if plants:
    <div class="row">
    % for p in plants:
        <div class="col-lg-6 col-xl-4 mb-4">
            <div class="plant-card" data-status="{{ p.get('watering_status', 'unknown') }}">
                <div class="plant-name">{{ p['name'] }}</div>
                <div class="plant-info"><strong>Espécie:</strong> {{ p['species'] }}</div>
                <div class="plant-info"><strong>Intervalo:</strong> {{ p.get('watering_interval_days', 'N/A') }} dias</div>
                <div class="plant-info"><strong>Próxima rega:</strong> {{ p.get('watering_message', '❓ Nunca regada') }}</div>
                <div class="plant-info">
                    <strong>Status:</strong>
                    % if p.get('watering_status') == 'overdue':
                        <span style="color: #d32f2f; font-weight: bold;">⚠️ Atrasada</span>
                    % elif p.get('watering_status') == 'urgent':
                        <span style="color: #f57c00; font-weight: bold;">💧 Regar hoje!</span>
                    % elif p.get('watering_status') == 'warning':
                        <span style="color: #f57c00; font-weight: bold;">⏰ Amanhã</span>
                    % elif p.get('watering_status') == 'ok':
                        <span style="color: #388e3c;">✅ Em {{ p.get('days_until_next_watering', '?') }} dias</span>
                    % elif p.get('watering_status') == 'never_watered':
                        <span style="color: #757575;">❓ Nunca regada</span>
                    % else:
                        <span style="color: #757575;">Status desconhecido</span>
                    % end
                </div>
                <div class="plant-info">
                    <strong>Próxima rega:</strong>
                    % if p.get('watering_status') == 'never_watered':
                        <span style="color: #f44336;">Nunca regada</span>
                    % elif p.get('watering_status') == 'overdue':
                        <span style="color: #f44336; font-weight: bold;">{{ abs(p.get('days_until_next_watering', 0)) }} dias atrasada ⚠️</span>
                    % elif p.get('watering_status') == 'urgent':
                        <span style="color: #ff9800; font-weight: bold;">Hoje! 🚨</span>
                    % elif p.get('watering_status') == 'warning':
                        <span style="color: #ff9800;">Amanhã ⚡</span>
                    % elif p.get('watering_status') == 'ok':
                        <span style="color: #4CAF50;">Em {{ p.get('days_until_next_watering', 0) }} dias ✅</span>
                    % else:
                        <span style="color: #666;">Calcular...</span>
                    % end
                </div>

                <div class="plant-actions">
                    <a href="/plants/{{p['id']}}" class="btn btn-outline-primary btn-sm">Ver Detalhes</a>
                    <a href="/plants/{{p['id']}}/edit" class="btn btn-outline-primary btn-sm">Editar</a>
                    <form action="/plants/{{p['id']}}/delete" method="post" style="display:inline;" onsubmit="return confirm('Tem certeza que deseja excluir esta planta?')">
                        <button type="submit" class="btn btn-danger btn-sm">Excluir</button>
                    </form>
                </div>
            </div>
        </div>
    % end
    </div>
% else:
    <div class="text-center py-5">
        <div style="font-size: 5rem; margin-bottom: 1.5rem;">🌱</div>
        <h4 style="color: #5a6c7d; margin-bottom: 1rem;">Nenhuma planta cadastrada ainda</h4>
        <p style="color: #7f8c8d; margin-bottom: 2rem; max-width: 500px; margin-left: auto; margin-right: auto;">
            Comece sua jornada botânica adicionando sua primeira planta ao PlantsVsTime!
        </p>
        <a href="/plants/new" class="btn btn-success">
            <span style="font-size: 1.2em;">🌱</span> Adicionar Minha Primeira Planta
        </a>
    </div>
% end
