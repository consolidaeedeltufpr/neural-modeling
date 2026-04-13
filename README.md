# 📡 PA Modeling

Modelagem de Amplificador de Potência (PA) com redes neurais para predição de sinais complexos (`I/Q`), incluindo análise **AM/AM** e **AM/PM**.

---

## 📑 Sumário

- [Objetivo](#-objetivo)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Arquitetura do modelo](#-arquitetura-do-modelo)
- [Formato esperado do CSV](#-formato-esperado-do-csv)
- [Requisitos](#️-requisitos)
- [Setup rápido](#-setup-rápido-windows)
- [Execução](#️-execução)
- [Testes](#-testes)
- [Métricas](#-métricas)
- [Solução de problemas](#️-solução-de-problemas)
- [Limpeza de artefatos](#-limpeza-de-artefatos)
- [Workflow de branches](#-workflow-de-branches)

---

## ✅ Objetivo

Este projeto implementa um pipeline completo para:

- carregar e preparar dados de PA (normalização, divisão treino/teste);
- treinar modelo de rede neural para predição de saída complexa (`I/Q`);
- avaliar desempenho com métricas de regressão (MSE, NMSE, R²);
- gerar relatório HTML com gráficos AM/AM e AM/PM.

---

## 📁 Estrutura do projeto

```text
neural-modeling/
├─ data/
│  ├─ raw/                           # dados brutos originais
│  └─ processed/
│     └─ dados_in_out_PA_banda_simples.csv
├─ reports/
│  └─ validation.html                # gerado automaticamente
├─ scripts/
│  └─ generate_report.py             # pipeline completo: treino → avaliação → relatório
├─ src/
│  ├─ __init__.py
│  ├─ data_processing.py             # normalização e divisão de dados
│  ├─ evaluate.py                    # cálculo de métricas e resultados AM/AM–AM/PM
│  ├─ model.py                       # definição da arquitetura MLP
│  ├─ plots.py                       # geração dos gráficos
│  └─ train.py                       # loop de treinamento
├─ tests/
│  ├─ conftest.py
│  ├─ test_data.py
│  ├─ test_model.py
│  └─ test_training.py
├─ requirements.txt
└─ README.md
```

---

## 🧠 Arquitetura do modelo

O modelo padrão é um **MLP (Multilayer Perceptron)** com a seguinte topologia:

| Camada  | Neurônios | Ativação |
|---------|-----------|----------|
| Entrada | 2         | —        |
| Oculta 1| 32        | ReLU     |
| Oculta 2| 32        | ReLU     |
| Saída   | 2         | Linear   |

- **Entradas:** `real_in`, `imag_in`
- **Saídas:** `real_out`, `imag_out`
- **Otimizador:** Adam
- **Função de perda:** MSE

---

## 📌 Formato esperado do CSV

O pipeline aceita os seguintes esquemas de colunas:

| Esquema         | Colunas                                     |
|-----------------|---------------------------------------------|
| **Preferencial**| `real_in, imag_in, real_out, imag_out`      |

Exemplo de cabeçalho (preferencial):

```csv
real_in,imag_in,real_out,imag_out
```

---

## ⚙️ Requisitos

- Python 3.10+
- `pip`
- ambiente virtual (`venv`)

Principais dependências (ver `requirements.txt`):
- `tensorflow` / `keras`
- `scikit-learn`
- `numpy`, `pandas`

---

## 🚀 Setup rápido (Windows)

**1. Criar e ativar o ambiente virtual:**

```bat
python -m venv .venv
.\.venv\Scripts\activate
```

**2. Instalar dependências:**

```bat
pip install -r requirements.txt
```

---

## ▶️ Execução

### Gerar relatório completo (treino + avaliação + gráficos)

Execute sempre a partir da raiz do projeto (`neural-modeling/`):

```bat
python scripts\generate_report.py
```

Saída esperada no terminal:

```
data: OK
train: OK
model: OK
evaluate: OK
plots: OK
report: OK
```

Relatório gerado em:

```
reports/validation.html
```

---

## 🧪 Testes

Para executar a suíte de testes unitários:

```bat
pytest tests/
```

Os testes cobrem:
- pré-processamento de dados (`test_data.py`)
- estrutura e saída do modelo (`test_model.py`)
- consistência do treinamento (`test_training.py`)

---

## 📊 Métricas

| Métrica   | Descrição |
|-----------|-----------|
| **MSE**   | Mean Squared Error — erro quadrático médio entre saída real e predita |
| **NMSE**  | Normalized MSE em dB — $10\log_{10}\!\left(\frac{\text{MSE}}{\text{Var}(y)}\right)$ |
| **R²**    | Coeficiente de determinação — fração da variância explicada pelo modelo |

---

## 🛠️ Solução de problemas

### `ModuleNotFoundError: No module named 'src'`

O script injeta automaticamente a raiz do projeto no `sys.path`. Certifique-se de executá-lo a partir de `neural-modeling/`:

```bat
python scripts\generate_report.py
```

### `FileNotFoundError` ao carregar o CSV

Confirme que o arquivo existe em `data/processed/` com o nome exato:

```
dados_in_out_PA_banda_simples.csv
```

---

## 🧹 Limpeza de artefatos

Os seguintes itens podem ser removidos sem risco:

```
__pycache__/
*.pyc
.pytest_cache/
reports/validation.html   ← gerado automaticamente
```

---

## 🔀 Workflow de branches

| Branch         | Propósito                              |
|----------------|----------------------------------------|
| `main`         | versão estável e revisada              |
| `develop`      | integração contínua de funcionalidades |
| `feature/*`    | novas funcionalidades                  |
| `experiment/*` | experimentos de modelagem              |

Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para o fluxo detalhado de contribuição.

---