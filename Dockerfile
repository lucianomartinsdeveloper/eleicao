FROM python:3.13

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala o binário do uv a partir da imagem oficial
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Instala dependências do sistema
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia as configurações do projeto
COPY pyproject.toml uv.lock* ./

# Instala as dependências no ambiente virtual do uv (.venv)
RUN uv sync --frozen --no-cache

# Adiciona o ambiente virtual do uv ao PATH do sistema
ENV PATH="/app/.venv/bin:$PATH"

# Instala as dependências do projeto no ambiente do sistema
RUN uv pip install --system -r pyproject.toml

COPY . .

RUN chmod +x /app/entrypoint.prod.sh

CMD ["/app/entrypoint.prod.sh"]