import os
import sys
from pathlib import Path
import pandas as pd

# Garante import de "src" ao executar o script diretamente
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.data_processing import load_data
from src.train import train_model
from src.evaluate import evaluate_model
from src.plots import plot_amplitude, plot_phase

# Aceita os 2 schemas
REQUIRED_SETS = [
    {"real_in", "imag_in", "real_out", "imag_out"},
]


def has_required_columns(csv_file: Path) -> bool:
    try:
        cols = pd.read_csv(csv_file, nrows=0).columns
        normalized = {str(c).strip().lower() for c in cols}
        return any(req.issubset(normalized) for req in REQUIRED_SETS)
    except Exception:
        return False


def find_file_anywhere(possible_names: list[str]) -> Path:
    preferred_dirs = [
        PROJECT_ROOT / "data" / "processed",
        PROJECT_ROOT.parent / "data" / "processed",
        Path.cwd(),
        PROJECT_ROOT,
        PROJECT_ROOT.parent,
        Path.home(),
    ]

    # 1) Busca rápida em diretórios preferenciais
    for d in preferred_dirs:
        for name in possible_names:
            p = d / name
            if p.exists() and has_required_columns(p):
                return p

    # 2) Busca recursiva
    roots = [PROJECT_ROOT.parent, PROJECT_ROOT, Path.cwd(), Path.home()]

    # 3) Windows fallback: todas as unidades existentes
    if os.name == "nt":
        for letter in "CDEFGHIJKLMNOPQRSTUVWXYZ":
            drive = Path(f"{letter}:\\")
            if drive.exists():
                roots.append(drive)

    seen = set()
    for root in roots:
        try:
            root_resolved = root.resolve()
        except Exception:
            root_resolved = root

        key = str(root_resolved).lower()
        if key in seen:
            continue
        seen.add(key)

        try:
            for current_root, _, files in os.walk(root_resolved):
                file_set = set(files)
                for name in possible_names:
                    if name in file_set:
                        candidate = Path(current_root) / name
                        if has_required_columns(candidate):
                            return candidate
        except (PermissionError, OSError):
            continue

    raise FileNotFoundError(f"Nenhum CSV válido encontrado para: {possible_names}")


def main() -> None:
    print("init: OK", flush=True)

    csv_names = [
        "dados_in_out_PA_banda_simples.csv",
    ]
    csv_path = find_file_anywhere(csv_names)
    print(f"csv: OK ({csv_path})", flush=True)

    (
        X_train,
        X_test,
        y_train,
        y_test,
        X_train_scaled,
        X_test_scaled,
        y_train_scaled,
        y_test_scaled,
        scaler_y,
    ) = load_data(str(csv_path))
    print("data: OK", flush=True)

    model, history = train_model(X_train_scaled, y_train_scaled)
    print("train: OK", flush=True)
    print("model: OK", flush=True)

    metrics, results = evaluate_model(
        model,
        X_test,
        X_test_scaled,
        y_test,
        scaler_y,
    )
    print("evaluate: OK", flush=True)

    fig_amp = plot_amplitude(results)
    fig_phase = plot_phase(results)
    print("plots: OK", flush=True)

    reports_dir = PROJECT_ROOT / "reports"
    os.makedirs(reports_dir, exist_ok=True)

    html_amp = fig_amp.to_html(full_html=False, include_plotlyjs="cdn")
    html_phase = fig_phase.to_html(full_html=False, include_plotlyjs=False)

    html = f"""
<html>
<body style="font-family:Arial; margin:40px">
<h1>Neural Model Validation</h1>

<h2>Métricas</h2>
<ul>
<li>MSE: {metrics["MSE"]:.6e}</li>
<li>NMSE (dB): {metrics["NMSE_DB"]:.4f}</li>
<li>R²: {metrics["R2"]:.6f}</li>
</ul>

<h2>Amplitude x Amplitude</h2>
{html_amp}

<h2>Amplitude x Diferença de Fase</h2>
{html_phase}
</body>
</html>
"""

    output_file = reports_dir / "validation.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print("report: OK", flush=True)
    print(f"CSV usado: {csv_path}", flush=True)
    print(f"Relatório gerado em {output_file}", flush=True)


if __name__ == "__main__":
    main()