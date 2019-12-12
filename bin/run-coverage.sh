#!/bin/sh

# Reports de cobertura
pytest --cov-report=html --cov=app tests/

# Sobe o diretório html num endereço local
http-server htmlcov