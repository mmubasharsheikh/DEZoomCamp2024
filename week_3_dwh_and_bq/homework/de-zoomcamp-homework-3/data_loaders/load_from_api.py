import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    li = []
    total_count = 0
    for x in range(1, 13):
        url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{x:02d}.parquet"
        # print(f'appending URL {url}')
        df = pd.read_parquet(url)
        # print(df.head(0))
        # print(f"DF count of {url} is {len(df)}")
        li.append(df)
        total_count += len(df)

    frame = pd.concat(li, axis=0, ignore_index=True)
    # print(frame.head(62495))
    # print(f"Frame count is {len(frame)} and calculated count is {total_count}")
    # response = requests.get(url)

    # return pd.read_csv(io.StringIO(response.text), sep=',')
    return frame


# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
