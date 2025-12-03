% rebase('base.tpl')

<div class="welcome-section">
    <h1 class="welcome-title">🌱 PlantsVsTime</h1>
    <p class="welcome-subtitle">Gerencie suas plantas e acompanhe suas regas de forma inteligente e organizada. Mantenha suas plantas sempre saudáveis e nunca esqueça uma rega.</p>

    <div class="d-flex justify-content-center gap-3 flex-wrap">
        % if defined('user_id') and user_id:
            <a href="/plants" class="btn btn-success">
                <span style="font-size: 1.1em;">🌿</span> Ver Minhas Plantas
            </a>
            <a href="/logout" class="btn btn-outline-primary">
                <span style="font-size: 1.1em;">🚪</span> Sair
            </a>
        % else:
            <a href="/login" class="btn btn-success">
                <span style="font-size: 1.1em;">🔑</span> Entrar
            </a>
            <a href="/signup" class="btn btn-outline-primary">
                <span style="font-size: 1.1em;">✨</span> Criar Conta
            </a>
        % end
    </div>
</div>

<div class="feature-cards">
    <div class="feature-card">
        <div class="feature-icon">🌿</div>
        <h4>Gerencie Plantas</h4>
        <p>Adicione e organize todas as suas plantas em um só lugar. Mantenha um catálogo completo da sua coleção botânica.</p>
    </div>
    <div class="feature-card">
        <div class="feature-icon">💧</div>
        <h4>Acompanhe Regas</h4>
        <p>Receba lembretes automáticos e mantenha o histórico detalhado de todas as regas realizadas.</p>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h4>Relatórios</h4>
        <p>Visualize estatísticas e relatórios sobre o cuidado das suas plantas. Mantenha todas elas sempre saudáveis.</p>
    </div>
</div>
