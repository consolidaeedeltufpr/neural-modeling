# 📡 PA Modeling

Modelagem de Amplificadores de Potência (Power Amplifiers – PA) utilizando Redes Neurais Artificiais para representação de comportamento não linear em banda simples.

Este repositório contém código, experimentos e ferramentas para treinamento, avaliação e comparação de modelos aplicados à modelagem de PA.

## 📑 Sumário

- [📌 Overview](#-overview)
- [🎯 Objetivo](#-objetivo)
- [📂 Estrutura do Repositório](#-estrutura-do-repositório)
- [🧠 Modelos Implementados](#-modelos-implementados)
- [📊 Métricas Avaliadas](#-métricas-avaliadas)
- [📁 Dataset](#-dataset)
- [🚀 Como Executar](#-como-executar)
- [🌳 Workflow de Branches](#-workflow-de-branches)
- [🔬 Reprodutibilidade](#-reprodutibilidade)
- [🤝 Contribuição](#-contribuição)
- [📜 Licença](#-licença)

---

## 📌 Overview


---

## 🎯 Objetivo

Desenvolver uma estrutura modular para:

- Modelagem não linear de amplificadores de potência
- Predição de sinais complexos (real e imaginário)
- Análise AM/AM e AM/PM
- Avaliação via métricas como MSE, NMSE e R²
- Comparação entre diferentes arquiteturas de redes neurais

---


## 📂 Estrutura do Repositório

A organização do projeto foi pensada para garantir modularidade, reprodutibilidade e escalabilidade dos experimentos.


---

### 📊 `data/`
Contém os datasets utilizados no projeto.

- `raw/` → Dados brutos (ex: `dados_in_out_PA_banda_simples.csv`)
- `processed/` → Dados normalizados e preparados para treinamento

---

### 📓 `notebooks/`
Notebooks exploratórios utilizados para:

- Análise inicial dos dados
- Testes rápidos de modelos
- Visualização de resultados
- Protótipos experimentais

---

### 🧠 `src/`
Código principal do projeto, modularizado.

- `data_processing.py` → Funções de normalização, divisão treino/teste e preparação dos dados  
- `model.py` → Definição das arquiteturas de redes neurais  
- `train.py` → Script de treinamento  
- `evaluate.py` → Cálculo de métricas (MSE, NMSE, R²)  
- `utils.py` → Funções auxiliares  

---

### 📈 `results/`
Armazena:

- Métricas salvas
- Logs de treinamento
- Modelos exportados (.h5)
- Resultados de experimentos

---

### 📊 `figures/`
Gráficos gerados:

- Curvas de treinamento
- AM/AM
- AM/PM
- Comparações modelo vs medição

---

### 🧪 `tests/`
Scripts para validação de:

- Funções de pré-processamento
- Estrutura do modelo
- Consistência de métricas

---

## 📄 Arquivos Principais

### `requirements.txt`
Lista de dependências do projeto.

---

### `README.md`
Documentação principal do repositório.

---

### `CONTRIBUTING.md`
Guia para contribuições e workflow de branches.

---

### `.gitignore`
Define arquivos que não devem ser versionados (ex: `.venv/`, `__pycache__/`, modelos treinados grandes, etc).

---

## 🌳 Workflow de Desenvolvimento

- `main` → versão estável  
- `develop` → integração contínua  
- `feature/*` → novas funcionalidades  
- `experiment/*` → testes de novos modelos  

---

## 🎯 Organização Científica

Esta estrutura permite:

- Reprodutibilidade dos experimentos  
- Comparação estruturada de modelos  
- Escalabilidade para novos datasets  
- Integração futura com artigos científicos  



---

## 🧠 Modelos Implementados

- MLP (Multi-Layer Perceptron)
- Modelos com regularização
- Estruturas experimentais para modelos com memória (em desenvolvimento)

---

## 📊 Métricas Avaliadas

- MSE
- NMSE (dB)
- R²
- AM/AM
- AM/PM

---

## 🚀 Como Executar

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 3️⃣ Executar o treinamento
```bash
pip src/train.py
```

### 4️⃣ Avaliar o modelo
```bash
python src/evaluate.py
```