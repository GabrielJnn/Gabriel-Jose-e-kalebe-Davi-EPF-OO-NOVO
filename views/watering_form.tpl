% rebase('base.tpl')

<div class="row justify-content-center">
    <div class="col-lg-8 col-xl-6">
        <div class="card">
            <div class="card-header">
                <h3 class="mb-0">
                    <span style="font-size: 1.1em;">💧</span>
                    Registrar Rega - {{ plant['name'] }}
                </h3>
            </div>
            <div class="card-body">
                <div class="text-center mb-4">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🌱</div>
                    <h5>Registrar nova rega para {{ plant['name'] }}</h5>
                    <p class="text-muted">Confirme que regou sua planta hoje</p>
                </div>

                <form action="{{ action }}" method="post">
                    <div class="mb-4 text-center">
                        <div class="alert alert-info">
                            <strong>Planta:</strong> {{ plant['name'] }}<br>
                            <strong>Espécie:</strong> {{ plant['species'] }}<br>
                            <strong>Data:</strong> <span id="current-date"></span>
                        </div>
                    </div>

                    <div class="d-grid gap-2 d-md-flex justify-content-md-center">
                        <a href="/plants/{{ plant['id'] }}" class="btn btn-outline-secondary me-md-2">
                            <span style="font-size: 1.1em;">⬅️</span> Cancelar
                        </a>
                        <button type="submit" class="btn btn-success">
                            <span style="font-size: 1.1em;">💧</span> Confirmar Rega
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<script>
    // Mostrar data atual
    document.getElementById('current-date').textContent = new Date().toLocaleDateString('pt-BR');
</script>

