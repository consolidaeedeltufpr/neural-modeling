# 📡 PA Modeling

Modelagem de Amplificador de Potência (PA) com redes neurais para predição de sinais complexos (`I/Q`), incluindo análise **AM/AM** e **AM/PM**.

---

## ✅ Objetivo

Este projeto implementa um pipeline para:

- carregar e preparar dados de PA;
- treinar modelo neural para predição de saída complexa;
- avaliar desempenho com métricas de regressão;
- gerar relatório HTML com gráficos AM/AM e AM/PM.

---

## 📁 Estrutura do projeto

```text
neural-modeling/
├─ data/
│  ├─ raw/
│  └─ processed/
│     └─ data_in_out_PA_banda_simples.csv
├─ reports/
│  └─ validation.html                # gerado automaticamente
├─ scripts/
│  └─ generate_report.py
├─ src/
│  ├─ __init__.py
│  ├─ data_processing.py
│  ├─ evaluate.py
│  ├─ model.py
│  ├─ plots.py
│  └─ train.py
├─ tests/
│  ├─ test_data.py
│  ├─ test_model.py
│  └─ test_training.py
├─ requirements.txt
└─ README.md
```

---

## 📌 Formato esperado do CSV

O pipeline aceita os esquemas de colunas:

- `real_in, imag_in, real_out, imag_out` **(preferencial)**
- `in_real, in_imag, out_real, out_imag` **(compatibilidade)**

Exemplo de cabeçalho:

```csv
real_in,imag_in,real_out,imag_out
```

---

## ⚙️ Requisitos

- Python 3.10+ (recomendado)
- `pip`
- ambiente virtual (`venv`)

---

## 🚀 Setup rápido (Windows)

1. Criar e ativar ambiente virtual:

```bat
python -m venv .venv
.\.venv\Scripts\activate
```

2. Instalar dependências:

```bat
pip install -r requirements.txt
```

---

## ▶️ Execução

### Gerar relatório completo (treino + avaliação + gráficos)

Na raiz do projeto (`neural-modeling`):

```bat
python scripts\generate_report.py
```

Saída esperada no terminal (status):
- `data: OK`
- `train: OK`
- `model: OK`
- `evaluate: OK`
- `plots: OK`
- `report: OK`

Relatório gerado em:

```text
reports/validation.html
```

---

## 🧪 Métricas usadas

- **MSE**
- **NMSE (dB)**
- **R²**

---

## 🧰 Solução de problemas

### 1) `ModuleNotFoundError: No module named 'src'`
O script já injeta automaticamente a raiz do projeto no `sys.path`.  
Execute sempre a partir da pasta `neural-modeling`:

```bat
python scripts\generate_report.py
```

### 2) `FileNotFoundError` do CSV
Confirme se o arquivo usA o nome esperado:
- `dados_in_out_PA_banda_simples.csv`

---

## 🧹 Limpeza de artefatos

Pode remover sem risco:
- `__pycache__/`
- `*.pyc`
- `.pytest_cache/`
- `reports/validation.html` (gerado automaticamente)

---

## 🔀 Workflow sugerido de branches

- `main`: estável
- `develop`: integração
- `feature/*`: novas funcionalidades
- `experiment/*`: experimentos de modelagem

---

## 📄 Licença

Definir conforme política do projeto (ex.: MIT, Apache-2.0, uso acadêmico interno).