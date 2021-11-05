import oslobike


def test_get_historical():
    month = 1
    year = 2021

    dataset = oslobike.get_historical(month, year)
    assert all(dataset["started_at"].dt.month == month)
    assert all(dataset["started_at"].dt.year == year)
