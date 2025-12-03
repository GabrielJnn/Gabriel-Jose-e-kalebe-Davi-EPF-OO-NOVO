% rebase('base.tpl')

<h2>{{ 'Editar Planta' if plant else 'Nova Planta' }}</h2>

<form action="{{ action }}" method="post">
    <label>Nome:</label><br>
    <input type="text" name="name" value="{{ plant['name'] if plant else '' }}" required><br><br>

    <label>Espécie:</label><br>
    <input type="text" name="species" value="{{ plant['species'] if plant else '' }}" required><br><br>

    <label>Frequência de rega (dias):</label><br>
    <input type="number" name="frequency" value="{{ plant['frequency'] if plant else '' }}" required><br><br>

    <button type="submit">Salvar</button>
</form>

<p><a href="/plants">Voltar</a></p>
