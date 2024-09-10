import dataclasses

import pandas as pd


@dataclasses.dataclass
class Workbooks:
    workbook1: pd.DataFrame
    workbook2: pd.DataFrame


def _load_accessibility(str_file_path: str) -> pd.DataFrame:
    return pd.read_excel(str_file_path, sheet_name='Accessibility', header=1)


def compare(workbook1_file_path: str, workbook2_file_path: str) -> None:
    wb1 = _load_accessibility(workbook1_file_path)
    wb2 = _load_accessibility(workbook2_file_path)
    wbs = Workbooks(workbook1=wb1, workbook2=wb2)

