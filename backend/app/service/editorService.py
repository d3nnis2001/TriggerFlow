import pandas as pd
import numpy as np
from io import StringIO
import contextlib
import traceback

from pandas.errors import DtypeWarning
from ..other.dangerous_functions import DANGEROUS_FUNCTIONS

class EditorService:
    def __init__(self, table_name):
        self.table_name = table_name

    def run_code(self, code, curr_col):
        try:
            data = pd.read_csv(f'../app/data/{self.table_name}.csv')
            column_data = data[curr_col].values
        except Exception as e:
            return {'error': f"Fehler beim Einlesen der Daten: {str(e)}"}

        results = []
        for index, val in enumerate(column_data):
            output = StringIO()
            with contextlib.redirect_stdout(output):
                try:
                    exec_globals = {
                        'pd': pd,
                        'np': np,
                        'index': index,
                        'val': val,
                        'result': None
                    }

                    exec(code, exec_globals)

                    if exec_globals['result'] is not None:
                        results.append(exec_globals['result'])
                    else:
                        captured_output = output.getvalue().strip()
                        results.append(captured_output if captured_output else None)

                except Exception as e:
                    error_message = f"Fehler bei Index {index}:\n{traceback.format_exc()}"
                    return {'error': error_message}

        return {'results': results}

    def is_code_safe(self, code):
        return all(func not in code for func in DANGEROUS_FUNCTIONS)
