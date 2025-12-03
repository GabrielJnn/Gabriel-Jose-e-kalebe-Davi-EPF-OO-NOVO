<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>PlantsVsTime</title>
  <!-- opcional: google font (funciona sem web.run) -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
  <div class="app-wrap">
    <div class="container">
      <header class="header">
        <div class="brand">
          <div class="logo">PV</div>
          <div>
            <div class="site-title">PlantsVsTime</div>
            <div style="font-size:12px;color:#6b8b8a">Cuide das suas plantinhas</div>
          </div>
        </div>

        <nav class="nav-links">
          % if request.get_cookie('user_id'):
            <a href="/plants" class="btn-ghost">Minhas Plantas</a>
            <a href="/logout" class="btn-ghost">Sair</a>
          % else:
            <a href="/login" class="btn-ghost">Login</a>
            <a href="/register" class="btn-ghost">Registrar</a>
          % end
        </nav>
      </header>

      <!-- conteúdo específico da página -->
      % include
    </div>
  </div>
</body>
</html>
