from typing import Any, Dict
import pandas as pd
import numpy as np


class PandasExp:
    """
    Apply the exponential function to a pandas DataFrame and converting non-numeric values to NaN.
    
    category: Math
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame) -> tuple:
        """
        Converts non-numeric values to NaN and applies the exponential function to the DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing the processed DataFrame.
        """
        dataframe = dataframe.apply(pd.to_numeric, errors='coerce')
        dataframe = np.exp(dataframe)
        return (dataframe,)
