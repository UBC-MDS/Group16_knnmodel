import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def scaling(train_X, impute_strategy, scale_method):
    """ Apply imputation and scaling to the given data.

    Parameters
    ----------
    train_X: pd.DataFrame 
        The features DataFrame to be preprocessed.
        
    impute_strategy: str
        The strategy for imputation, 'mean', 'median', 'most_frequent', or 'constant'.
        
    scale_method: str
        The scaling method, either 'StandardScaler' or 'MinMaxScaler'.
        
    Returns
    ----------
    pd.DataFrame
        The scaled features DataFrame.
    """
    
    # Impute missing values in the features
    imputer = SimpleImputer(strategy=impute_strategy)
    train_X_imputed = pd.DataFrame(imputer.fit_transform(train_X), columns=train_X.columns)

    # Scale features data
    if scale_method == 'StandardScaler':
        scaler = StandardScaler()
    elif scale_method == 'MinMaxScaler':
        scaler = MinMaxScaler()
    else:
        raise ValueError("scale_method must be 'StandardScaler' or 'MinMaxScaler'.")

    # Apply scaling to the features
    train_X_scaled = pd.DataFrame(scaler.fit_transform(train_X_imputed), columns=train_X.columns)

    return train_X_scaled