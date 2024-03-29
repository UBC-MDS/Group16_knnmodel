import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np
from pkg_pyknnclassifier.scaling import scaling

def test_invalid_impute_strategy():
    """Test scaling with invalid impute strategy."""
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    invalid_strategy = "invalid_strategy"
    try:
        scaling(df, invalid_strategy, 'StandardScaler')
    except ValueError as e:
        expected_message = "impute_strategy must be 'mean', 'median', 'most_frequent', or 'constant'."
        assert str(e) == expected_message, f"Expected message: '{expected_message}' but got '{str(e)}'"
    else:
        assert False, "Expected ValueError not raised for invalid impute strategy"


def test_invalid_scale_method():
    """Test scaling with invalid scale method."""
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    invalid_scale_method = "invalid_scale"
    try:
        scaling(df, 'mean', invalid_scale_method)
    except ValueError as e:
        assert str(e) == "scale_method must be 'StandardScaler' or 'MinMaxScaler'."


def test_non_dataframe_input():
    """Test scaling with non-DataFrame input. """
    non_dataframe_input = [1, 2, 3]
    try:
        scaling(non_dataframe_input, 'mean', 'StandardScaler')
    except ValueError as e:
        expected_message = "train_X must be a pandas DataFrame."
        assert str(e) == expected_message, f"Expected message: '{expected_message}' but got '{str(e)}'"
    else:
        assert False, "Expected ValueError not raised for non-DataFrame input"
