import dataclasses

import pandas as pd


@dataclasses.dataclass
class Workbooks:
    workbook1_file_path: str
    workbook2_file_path: str
    df1: pd.DataFrame = None
    df2: pd.DataFrame = None

    def _load_accessibility(self, str_file_path: str) -> None:
        self.df1 = pd.read_excel(str_file_path, sheet_name='Accessibility', header=1)
        self.df2 = pd.read_excel(str_file_path, sheet_name='Accessibility', header=1)

    def compare_accessibility(self) -> None:
        print(self.df1['Total score'])


def compare(workbook1_file_path: str, workbook2_file_path: str) -> None:
    wbs = Workbooks(workbook1_file_path, workbook2_file_path)
    wbs.compare_accessibility()



