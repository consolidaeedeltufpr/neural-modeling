import plotly.graph_objects as go


def plot_amplitude(results):

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=results["amp_in"],
        y=results["amp_out_true"],
        mode="markers",
        name="Amplitude Real"
    ))

    fig.add_trace(go.Scatter(
        x=results["amp_in"],
        y=results["amp_out_pred"],
        mode="markers",
        name="Amplitude Prevista"
    ))

    fig.update_layout(
        title="Amplitude x Amplitude",
        xaxis_title="|Input|",
        yaxis_title="|Output|",
        template="plotly_white"
    )

    return fig


def plot_phase(results):

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=results["amp_in"],
        y=results["phase_diff_true"],
        mode="markers",
        name="Diferença de fase real"
    ))

    fig.add_trace(go.Scatter(
        x=results["amp_in"],
        y=results["phase_diff_pred"],
        mode="markers",
        name="Diferença de fase prevista"
    ))

    fig.update_layout(
        title="Amplitude x Diferença de Fase",
        xaxis_title="|Input|",
        yaxis_title="ΔPhase [rad]",
        template="plotly_white"
    )

    return fig