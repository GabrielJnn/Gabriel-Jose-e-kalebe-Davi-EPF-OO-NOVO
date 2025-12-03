% rebase('base.tpl')

<div class="row justify-content-center">
    <div class="col-lg-8 col-xl-6">
        <div class="card">
            <div class="card-header">
                <h3 class="mb-0">{{ 'Editar Planta' if plant else 'Nova Planta' }}</h3>
            </div>
            <div class="card-body">
                % if error:
                    <div class="alert alert-danger">
                        <i class="fas fa-exclamation-triangle me-2"></i>{{ error }}
                    </div>
                % end

                <form action="{{ action }}" method="post">
                    <div class="mb-4">
                        <label for="name" class="form-label">
                            <span style="font-size: 1.1em;">🌱</span> Nome da Planta
                        </label>
                        <input type="text" class="form-control" id="name" name="name"
                               value="{{ plant['name'] if plant else '' }}" required
                               placeholder="Ex: Orquídea, Cacto, Suculenta...">
                    </div>

                    <div class="mb-4">
                        <label for="species" class="form-label">
                            <span style="font-size: 1.1em;">🌿</span> Espécie
                        </label>
                        <input type="text" class="form-control" id="species" name="species"
                               value="{{ plant['species'] if plant else '' }}" required
                               placeholder="Ex: Flor, Frutífera, Medicinal...">
                    </div>

                    <div class="mb-4">
                        <label for="interval" class="form-label">
                            <span style="font-size: 1.1em;">💧</span> Frequência de Rega (dias)
                        </label>
                        <input type="number" class="form-control" id="interval" name="interval"
                               value="{{ plant.get('watering_interval_days', '') if plant else '' }}"
                               required min="1" max="365"
                               placeholder="Ex: 3, 7, 14...">
                        <div class="form-text">Quantos dias entre cada rega?</div>
                    </div>

                    <div class="d-grid gap-2 d-md-flex justify-content-md-end mt-4">
                        <a href="/plants" class="btn btn-outline-secondary me-md-2">
                            <span style="font-size: 1.1em;">⬅️</span> Voltar
                        </a>
                        <button type="submit" class="btn btn-success">
                            <span style="font-size: 1.1em;">💾</span> {{ 'Salvar' if plant else 'Adicionar Planta' }}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
