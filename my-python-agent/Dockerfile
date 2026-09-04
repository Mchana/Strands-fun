# Use uv's Python base image
FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

# Copy uv files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-cache --no-install-project

# Copy agent file
COPY . .

# Expose port
EXPOSE 8080

# Run application
CMD ["uv", "run", "python", "agent.py"]