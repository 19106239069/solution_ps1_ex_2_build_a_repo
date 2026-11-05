
import polars as pl
import seaborn as sns
import matplotlib.axes


def plot_gdp(df: pl.DataFrame) -> matplotlib.axes.Axes:
    """
    This function takes in a Polars DataFrame
    and plots the GDP of the countries in the dataframe.
    """

    return sns.lineplot(
        data=df,
        x="Year",
        y="GDP",
        hue="Country Name"
    )
