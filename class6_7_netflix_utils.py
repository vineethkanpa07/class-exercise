import logging
import re
import pandas as pd

logger = logging.getLogger(__name__)

def clean_text(value):
    """Normalize one text value."""
    if not isinstance(value, str):
        return value  # leave NaN/None/non-strings untouched
    value = value.strip().lower()
    return re.sub(r"\s+", " ", value)


def remove_iqr_outliers(df, column, threshold):
    """Remove IQR outliers from one column."""
    if column not in df.columns:
        logger.error(f"Column '{column}' not found in DataFrame")
        raise ValueError(f"Column '{column}' not found in DataFrame")

    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1

    lower = q1 - threshold * iqr
    upper = q3 + threshold * iqr

    newdf = df[(df[column] >= lower) & (df[column] <= upper)]
    logger.debug(
        f"Bounds for '{column}': lower={lower}, upper={upper}, "
        f"rows removed: {len(df) - len(newdf)}"
    )
    return newdf

def show_overview(df):
    """Display basic information about a DataFrame."""
    # TODO 1:
    # Log a DEBUG message containing the shape.
    # Print the shape, first five rows, column names, and data types.
    logger.debug(f"Shape: {df.shape}")
    print(f"Shape: {df.shape}, {df.head()}, {list(df.columns)}, {df.dtypes}")


def remove_duplicates(df):
    """Remove exact duplicate rows."""
    # TODO 2:
    # Remove exact duplicate rows.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    newdf = df.drop_duplicates()
    logger.debug(f"Row count before: {len(df)}, Row count after: {len(newdf)}")
    return newdf


def drop_missing_rows(df):
    """Remove rows containing missing values."""
    # TODO 3:
    # Log a DEBUG message containing the before and after row counts.
    # Drop rows containing one or more missing values.
    # Return the resulting DataFrame.
    newdf = df.dropna()
    logger.debug(f"Row count before: {len(df)}, Row count after: {len(newdf)}")
    return newdf
