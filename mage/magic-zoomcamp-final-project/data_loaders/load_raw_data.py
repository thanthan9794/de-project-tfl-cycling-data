import io
import pandas as pd
# import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    urls = ['https://cycling.data.tfl.gov.uk/ActiveTravelCountsProgramme/2022%20Q1%20(Jan-Mar)-Central.csv',
            'https://cycling.data.tfl.gov.uk/ActiveTravelCountsProgramme/2022%20W1%20spring-Central.csv',
            'https://cycling.data.tfl.gov.uk/ActiveTravelCountsProgramme/2022%20W1%20spring-Cycleways.csv',
            'https://cycling.data.tfl.gov.uk/ActiveTravelCountsProgramme/2022%20W1%20spring-Inner-Part1.csv',
            'https://cycling.data.tfl.gov.uk/ActiveTravelCountsProgramme/2022%20W1%20spring-Inner-Part2.csv',
            'https://cycling.data.tfl.gov.uk/ActiveTravelCountsProgramme/2022%20W1%20spring-Outer.csv',
            'https://cycling.data.tfl.gov.uk/ActiveTravelCountsProgramme/2022%20W2%20autumn-Cycleways.csv',
            'https://cycling.data.tfl.gov.uk/ActiveTravelCountsProgramme/2023%20W1%20spring-Central.csv',
            'https://cycling.data.tfl.gov.uk/ActiveTravelCountsProgramme/2023%20W1%20spring-Cycleways.csv',
            'https://cycling.data.tfl.gov.uk/ActiveTravelCountsProgramme/2023%20W1%20spring-Inner-Part1.csv',
            'https://cycling.data.tfl.gov.uk/ActiveTravelCountsProgramme/2023%20W1%20spring-Inner-Part2.csv',
            'https://cycling.data.tfl.gov.uk/ActiveTravelCountsProgramme/2023%20W1%20spring-Outer.csv',
            'https://cycling.data.tfl.gov.uk/ActiveTravelCountsProgramme/2023%20W2%20autumn-Cycleways.csv']
    
    # urls = urls[-6:]

    storage_options = {'User-Agent': 'Mozilla/5.0'}

    data =[]
    for url in urls:
        df = pd.read_csv(url, sep=',', storage_options=storage_options)
        data.append(df)

    df = pd.concat(data, ignore_index=True)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
