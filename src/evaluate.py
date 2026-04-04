import numpy as np
from sklearn.metrics import mean_squared_error, r2_score


def evaluate_model(model, X_test, X_test_scaled, y_test, scaler_y):

    y_pred_scaled = model.predict(X_test_scaled)

    y_pred = scaler_y.inverse_transform(y_pred_scaled)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    nmse_linear = mse / np.var(y_test)
    nmse_db = 10 * np.log10(nmse_linear)

    amp_in = np.sqrt(X_test[:,0]**2 + X_test[:,1]**2)

    vout_true = y_test[:,0] + 1j*y_test[:,1]
    vout_pred = y_pred[:,0] + 1j*y_pred[:,1]

    amp_out_true = np.abs(vout_true)
    amp_out_pred = np.abs(vout_pred)

    phase_diff_true = np.angle(vout_true) - np.angle(X_test[:,0] + 1j*X_test[:,1])
    phase_diff_pred = np.angle(vout_pred) - np.angle(X_test[:,0] + 1j*X_test[:,1])

    metrics = {
        "MSE": mse,
        "NMSE_DB": nmse_db,
        "R2": r2
    }

    results = {
        "amp_in": amp_in,
        "amp_out_true": amp_out_true,
        "amp_out_pred": amp_out_pred,
        "phase_diff_true": phase_diff_true,
        "phase_diff_pred": phase_diff_pred
    }

    return metrics, results
