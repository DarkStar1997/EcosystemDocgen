import sys
import sqlite3
import argparse
import pandas as pd
import helper.generate_plots as plot_generator

def get_table(db_path: str, table_name: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + table_name)
    rows = cursor.fetchall()
    cols = list(map(lambda x: x[0], cursor.description))
    df = pd.DataFrame(rows, columns=cols).dropna()
    return df

def generate_report(db_path: str, full_species_name: str):
    kind = full_species_name[full_species_name.find('/') + 1 :]
    kingdom = full_species_name[0: full_species_name.find('/')]
    table_name = 'STATS_' + kind.upper()

    df = get_table(db_path, table_name)

    if kingdom == 'animal':
        plot_generator.Animal.generate_graphs(df, savepath='outputs/img/')
    elif kingdom == 'plant':
        plot_generator.Plant.generate_graphs(df, savepath='outputs/img/')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Report generator for Ecosystem Simulator')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-n', '--full_species_name', type=str, required=True, help='Full species name for report. Eg.- animal/deer')
    required.add_argument('-p', '--db_path', type=str, required=True, help='Path to sqlite database')
    args = parser.parse_args()

    db_path = args.db_path
    full_species_name = args.full_species_name

    generate_report(db_path, full_species_name)
