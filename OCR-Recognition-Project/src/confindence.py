import pandas as pd


def calculate_confidence(data):

    if "conf" not in data.columns:
        return 0

    conf_series = pd.to_numeric(
        data["conf"],
        errors="coerce"
    )

    conf_series = conf_series.dropna()

    conf_series = conf_series[
        conf_series >= 0
    ]

    if len(conf_series) == 0:
        return 0

    return round(conf_series.mean(), 2)

def get_status(confidence):

    if confidence >= 80:
        return "PASS"

    return "FAIL"