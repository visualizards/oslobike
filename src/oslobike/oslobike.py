"""Functionality to get bike sharing data from Oslo Bysykkel.
"""

import pandas as pd


def get_historical(month, year):
    """Fetch the historical bike data for the given month.

    Parameters
    ----------
    month : int
        Month to download bike sharing data from
    year : int
        Year to download bike sharing data from

    Returns
    -------
    pd.DataFrame
        Data frame containing the bike sharing data.
    """
    endpoint = f"https://data.urbansharing.com/oslobysykkel.no/trips/v1/{year:04d}/{month:02d}.csv"
    bike_data = pd.read_csv(endpoint)
    bike_data["started_at"] = pd.to_datetime(bike_data["started_at"])
    bike_data["ended_at"] = pd.to_datetime(bike_data["ended_at"])
    return bike_data
