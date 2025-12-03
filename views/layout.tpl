<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>PlantsVsTime</title>
  <link rel="stylesheet" href="/static/css/style.css" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <nav class="navbar navbar-expand-lg navbar-dark bg-success">
    <div class="container">
      <a class="navbar-brand" href="/">PlantsVsTime</a>
      <div class="collapse navbar-collapse">
        % if defined('user_id') and user_id:
          <ul class="navbar-nav me-auto">
            <li class="nav-item"><a class="nav-link" href="/plants">Minhas Plantas</a></li>
          </ul>
          <ul class="navbar-nav">
            <li class="nav-item"><a class="nav-link" href="/logout">Sair</a></li>
          </ul>
        % else:
          <ul class="navbar-nav ms-auto">
            <li class="nav-item"><a class="nav-link" href="/login">Login</a></li>
            <li class="nav-item"><a class="nav-link" href="/signup">Registrar</a></li>
          </ul>
        % end
      </div>
    </div>
  </nav>

  <div class="container mt-4">
    <div class="card p-3 shadow-sm">
      % include
    </div>
  </div>

  <footer class="text-center mt-4 mb-4 small text-muted">
    PlantsVsTime - Projeto POO
  </footer>
</body>
</html>
