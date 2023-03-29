"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import os
import sqlite3
from create_relationships import db_path
import pandas as pd

def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)

def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("""
    SELECT person1.name, person2.name, start_date, type FROM relationships
    JOIN people person1 ON person1_id = person1.id
    JOIN people person2 ON person2_id = person2.id;
    """)
    married_couples = cur.fetchall()
    con.commit()
    con.close()
    # TODO: Function 
    return married_couples

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    # TODO: Function body
    df = pd.DataFrame(married_couples, columns=["person1", "person2", "start_date", "type"])
    df.to_csv(csv_path, index=False)

    for person1, person2, start_date, type in married_couples:
        print(f'{person1} has been a {type} of {person2} since {start_date}.')



if __name__ == '__main__':
   main()