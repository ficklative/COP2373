# This program will display a database for ten cities
# in Florida, and will give a user a graph of the next
# 20 years for the population growth/decline

import matplotlib.pyplot as plt
import sqlite3
import random

# Create a database named population_RA
def main():
    # Variables
    city_name = 0

    # Connect to database population_RA
    sqlconn = sqlite3.connect('population_RA.db')

    # Create cursor to run SQL commands
    cursor = sqlconn.cursor()

    # Drop the table for future reruns
    sqlconn.execute("DROP TABLE IF EXISTS population")

    # Create the table named population with fields city, year, and population
    cursor.execute("""
        CREATE TABLE population(City VARCHAR(25), 
        Year INT(4), 
        Population INT(7))
    """)

    # insert data into database, use:
    # cursor.execute("INSERT INTO population(City, Year, Population) VALUES ('?', 0, 0)")
    cursor.execute("INSERT INTO population(City, Year, Population) VALUES ('Jacksonville', 2023, 985843)")
    cursor.execute("INSERT INTO population(City, Year, Population) VALUES ('Miami', 2023, 455924)")
    cursor.execute("INSERT INTO population(City, Year, Population) VALUES ('Tampa', 2023, 403364)")
    cursor.execute("INSERT INTO population(City, Year, Population) VALUES ('Orlando', 2023, 320742)")
    cursor.execute("INSERT INTO population(City, Year, Population) VALUES ('St. Petersburg', 2023, 263553)")
    cursor.execute("INSERT INTO population(City, Year, Population) VALUES ('Port St. Lucie', 2023, 245021)")
    cursor.execute("INSERT INTO population(City, Year, Population) VALUES ('Cape Coral', 2023, 224455)")
    cursor.execute("INSERT INTO population(City, Year, Population) VALUES ('Hialeah', 2023, 221300)")
    cursor.execute("INSERT INTO population(City, Year, Population) VALUES ('Tallahassee', 2023, 202221)")
    cursor.execute("INSERT INTO population(City, Year, Population) VALUES ('Fort Lauderdale', 2023, 184255)")

    # Display the data
    print('*' * 40,
          '\n(City, Year, Population)')
    for row in cursor.execute("SELECT * FROM population"):
        print(row)
    print('*' * 40)

    # Call function to simulate population
    simulate_pop(sqlconn)

    # Commit new population data to database population_RA
    sqlconn.commit()

    # Call a function for data visualization
    visualize_pop(sqlconn, city_name)

    # Close the database population_RA
    sqlconn.close()

# Simulate the population growth and decline from 2023 + 20 years
def simulate_pop(sqlconn):
    cursor = sqlconn.cursor()

    # Select the latest record per year
    cursor.execute("""SELECT City, MAX(Year), Population from population GROUP BY City""")
    all_cities = cursor.fetchall()

    # Simulate the population growth and decline and insert into database
    for city, latest_year, population in all_cities:
        # Start with current population
        current_population = population

        # Use a range to get a simulation for each record in database
        for year in range(latest_year + 1, latest_year + 21):
            # Create a rate
            growth_rate = random.uniform(-0.01, 0.04)

            # Multiply current_pop by growth_rate to get new value
            current_population = int(current_population * (1 + growth_rate))

            # Insert new data into population_RA database
            cursor.execute("""INSERT INTO population (City, Year, Population) VALUES (?, ?, ?)""", (city, year, current_population))

    # Commit the changes to database
    sqlconn.commit()

    # Return the database
    return sqlconn

# Create a function for data visualization
def visualize_pop(sqlconn, city_name):
    # Variable
    city_name = 0

    cursor = sqlconn.cursor()

    # List of cities for user to choose from
    cities_list = ['Jacksonville', 'Miami', 'Tampa', 'Orlando', 'St. Petersburg',
                   'Port St. Lucie', 'Cape Coral', 'Hialeah', 'Tallahassee',
                   'Fort Lauderdale']

    # Get which city from user
    # Ensure user picks between 1-10
    while city_name < 1 or city_name > len(cities_list):
        print('\nFlorida Cities:')
        for c, place in enumerate(cities_list, start=1):
            print(f"{c}. {place}")

        print(' ')

        # Instruct user to choose a city, get city input
        try:
            city_name = int(input("To see a simulated population growth from 2023-2043,"
                                  "\nChoose a city from the list above (1-10): "))
        except ValueError: # Ensure correct input
            print('\nINVALID INPUT, please enter a number between 1 and 10.'
                  '\n',
                  '*' * 50,
                  '\n')
            # Calls visualize_pop() if input is invalid
            visualize_pop(sqlconn, city_name)

    # Convert chosen int to city string
    chosen_city = cities_list[city_name - 1]

    # Select chosen city from the database
    cursor.execute("""
        SELECT year, population FROM population 
        WHERE city = ? 
        ORDER BY year
    """, (chosen_city,))

    # Connect to database for chosen city only
    city_pop_data = cursor.fetchall()

    # Plot the data
    years = [row[0] for row in city_pop_data] # x-axis
    populations = [row[1] for row in city_pop_data] # y-axis

    plt.figure(figsize=(15, 5)) # Graph size
    plt.plot(years, populations, marker='o', color='blue', linewidth=1)

    # Label the graph
    plt.xticks(years)
    plt.title(f"Population Growth for {chosen_city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)

    # Display the graph
    plt.show()

    # Repeat the main function to choose another city
    main()

# Call the main function
if __name__ == '__main__':
    main()