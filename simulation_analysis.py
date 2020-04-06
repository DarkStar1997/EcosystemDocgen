import sys
import sqlite3
import pandas as pd

db_path = None

def get_table(table_name):
    global db_path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + table_name)
    rows = cursor.fetchall()
    cols = list(map(lambda x: x[0], cursor.description))
    df = pd.DataFrame(rows, columns=cols).dropna()
    return df

def generate_report(full_species_name: str):
    kind = full_species_name[full_species_name.find('/') + 1 :]
    kingdom = full_species_name[0: full_species_name.find('/')]
    table_name = 'STATS_' + kind.upper()

    df = get_table(table_name)

    if kingdom == 'animal':
        import helper.report_animal as rep
        rep.generate_pdf(df, kind, savepath="outputs/")
    elif kingdom == 'plant':
        import helper.report_plant as rep
        rep.generate_pdf(df, kind, savepath="outputs/")


if __name__ == '__main__':
    db_path = sys.argv[2]
    generate_report(sys.argv[1])
