"""Program to manage guitars from a file and user input."""

from guitar import Guitar


def load_guitars(filename):
    """Load guitars from a file and return a list of Guitar objects."""
    guitars = []
    try:
        with open( filename, 'r' ) as file:
            for line in file:
                name, year, cost = line.strip().split( ',' )
                guitars.append( Guitar( name, int( year ), float( cost ) ) )
    except FileNotFoundError:
        print( f"File {filename} not found." )
    return guitars


def save_guitars(filename, guitars):
    """Save guitars to a file."""
    with open( filename, 'w' ) as file:
        for guitar in guitars:
            file.write( f"{guitar.name},{guitar.year},{guitar.cost}\n" )


def get_new_guitar():
    """Get guitar details from user input."""
    name = input( "Name: " )
    while name != "":
        try:
            year = int( input( "Year: " ) )
            cost = float( input( "Cost: $" ) )
            return Guitar( name, year, cost )
        except ValueError:
            print( "Invalid input" )
        name = input( "Name: " )
    return None


def main():
    """Main program for guitar management."""
    FILENAME = "guitars.csv"
    guitars = load_guitars( FILENAME )

    print( "These are my guitars:" )
    for i, guitar in enumerate( guitars, 1 ):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print( f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}" )

    print( "\nSorted by year:" )
    guitars.sort()  # This will use the __lt__ method we defined
    for guitar in guitars:
        print( guitar )

    print( "\nAdd new guitars:" )
    new_guitar = get_new_guitar()
    while new_guitar:
        guitars.append( new_guitar )
        new_guitar = get_new_guitar()

    save_guitars( FILENAME, guitars )
    print( "\nGuitars have been saved to", FILENAME )


if __name__ == '__main__':
    main()