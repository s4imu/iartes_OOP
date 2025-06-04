#!/bin/bash

# Criar e ativar a virtual environment
echo "Criando virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Instalar as dependências
echo "Instalando dependências..."
pip install -r requirements.txt
echo
echo

# Rodar o app.py
echo "Iniciando o aplicativo..."
python ./app.py &
echo
echo

# Executar os testes
echo "Executando testes automatizados..."
python -m unittest discover ./tests -v
echo
echo

# Exibir os relatórios gerados
echo "Exibindo relatórios..."
cat relatorio_testes.csv
echo "----------------------------------------------------------------------
"
cat relatorio_produtos.csv