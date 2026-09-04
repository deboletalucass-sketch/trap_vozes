"""
==========================================================
TRAP VOZES
TCC - Técnico em Informática

Tema:
Do Silenciamento ao Protagonismo:
O Espaço da Mulher Negra no Trap Brasileiro

Desenvolvido por:
Lucas Gabriel Rocha Deboleta
Helena Monteiro Coracini

Framework:
Flask

==========================================================
"""

# ==========================================================
# IMPORTAÇÕES
# ==========================================================

from flask import Flask, render_template

# ==========================================================
# CONFIGURAÇÃO DA APLICAÇÃO
# ==========================================================

app = Flask(__name__)

app.config["SECRET_KEY"] = "trapvozes2026"

# ==========================================================
# DADOS DO PROJETO
# (utilizaremos depois em todas as páginas)
# ==========================================================

SITE = {
    "titulo": "Trap Vozes",
    "subtitulo": "Do Silenciamento ao Protagonismo",
    "instituicao": "Instituto Federal do Paraná",
    "curso": "Técnico em Informática",
    "ano": 2026
}

# ==========================================================
# ROTAS
# ==========================================================

@app.route("/")
def index():
    return render_template(
        "index.html",
        site=SITE,
        titulo="Página Inicial"
    )


@app.route("/sobre")
def sobre():
    return render_template(
        "sobre.html",
        site=SITE,
        titulo="Sobre o Projeto"
    )


@app.route("/artistas")
def artistas():
    return render_template(
        "artistas.html",
        site=SITE,
        titulo="Artistas"
    )


@app.route("/analises")
def analises():
    return render_template(
        "analises.html",
        site=SITE,
        titulo="Análises"
    )


@app.route("/referencias")
def referencias():
    return render_template(
        "referencias.html",
        site=SITE,
        titulo="Referências"
    )


@app.route("/equipe")
def equipe():
    return render_template(
        "equipe.html",
        site=SITE,
        titulo="Equipe"
    )


# ==========================================================
# ERRO 404
# ==========================================================

@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template(
        "404.html",
        site=SITE,
        titulo="Página não encontrada"
    ), 404


# ==========================================================
# EXECUÇÃO
# ==========================================================

if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )