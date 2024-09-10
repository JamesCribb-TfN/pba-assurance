from .pba_assure import compare


def main() -> None:
    workbook1 = rf"T:\4JH\SCM Assurance runs for JC\pre-scm\working_book_amenity_indicators_K1P_2042_v3.2.xlsx"
    workbook2 = rf"T:\4JH\SCM Assurance runs for JC\pre-scm\working_book_amenity_indicators_JPI_2042_v3.2.xlsx"

    compare(workbook1, workbook2)


if __name__ == "__main__":
    main()
