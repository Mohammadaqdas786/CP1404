def extract_name(email):
    """
    Extracts a name from an email address.

    Args:
    email (str): The email address.

    Returns:
    str: The extracted name.
    """
    # Split the email at the '@' symbol
    local_part = email.split( '@' )[0]

    # Split the local part at the '.' symbol
    names = local_part.split( '.' )

    # Join the names with a space and title case them
    name = ' '.join( names ).title()

    return name


def main():
    email_dict = {}

    email = input( "Email: " )  # Prompt for the first email
    while email:  # Continue as long as the email is not blank
        # Extract the name from the email
        name = extract_name( email )

        # Ask the user to confirm their name
        response = input( f"Is your name {name}? (Y/n) " )

        # If the user doesn't press Enter or type 'Y', ask for their name
        if response.lower() != '' and response.lower() != 'y':
            name = input( "Name: " )

        # Add the email and name to the dictionary
        email_dict[email] = name

        # Prompt for the next email
        email = input( "Email: " )

    # Print out the email and name dictionary
    for email, name in email_dict.items():
        print( f"{name} ({email})" )


if __name__ == "__main__":
    main()
