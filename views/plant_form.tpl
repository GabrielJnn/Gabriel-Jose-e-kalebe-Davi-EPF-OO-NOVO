% rebase('base.tpl')

<div class="grid">
  <div>
    <div class="card">
      <h3>{{ 'Editar Planta' if plant else 'Nova Planta' }}</h3>

      <form class="form" action="{{action}}" method="post">
        <label>Nome</label>
        <input type="text" name="name" value="{{ plant.get('name','') if plant else '' }}" required>

        <label>Espécie</label>
        <input type="text" name="species" value="{{ plant.get('species','') if plant else '' }}" required>

        <div class="actions" style="margin-top:6px;">
          <button class="btn" type="submit">Salvar</button>
          <a href="/plants" class="btn ghost">Cancelar</a>
        </div>
      </form>
    </div>
  </div>

  <div>
    <div class="card">
      <h3>Info</h3>
      <p>Informe nome e espécie. Depois registre as regas na página da planta.</p>
    </div>
  </div>
</div>
