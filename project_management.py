# project_management.py

import os
import sys
from project import Project


def load_projects(filename):
    projects = []
    with open( filename, 'r' ) as file:
        next( file )  # Skip the header line
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split( '\t' )
            projects.append( Project( name, start_date, priority, cost_estimate, int( completion_percentage ) ) )
    return projects


def save_projects(filename, projects):
    with open( filename, 'w' ) as file:
        file.write( "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n" )
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime( '%d/%m/%Y' )}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n" )


def display_projects(projects):
    incomplete = [p for p in projects if not p.is_completed()]
    completed = [p for p in projects if p.is_completed()]

    incomplete.sort()
    completed.sort()

    print( "Incomplete projects:" )
    for project in incomplete:
        print( f"  {project}" )

    print( "Completed projects:" )
    for project in completed:
        print( f"  {project}" )


def filter_projects_by_date(projects, date):
    filtered = [p for p in projects if p.start_date > date]
    filtered.sort()
    return filtered


def add_new_project(projects):
    name = input( "Name: " )
    start_date = input( "Start date (dd/mm/yyyy): " )
    priority = int( input( "Priority: " ) )
    cost_estimate = input( "Cost estimate: " )
    completion_percentage = int( input( "Percent complete: " ) )

    projects.append( Project( name, start_date, priority, cost_estimate, completion_percentage ) )


def update_project(projects):
    for index, project in enumerate( projects ):
        print( f"{index} {project}" )

    project_choice = int( input( "Project choice: " ) )
    project = projects[project_choice]

    new_percentage = input( "New Percentage: " )
    if new_percentage:
        project.completion_percentage = int( new_percentage )

    new_priority = input( "New Priority: " )
    if new_priority:
        project.priority = int( new_priority )


def main():
    projects = []
    default_file = "projects.txt"

    if os.path.exists( default_file ):
        projects = load_projects( default_file )
        print( f"Loaded {len( projects )} projects from {default_file}" )

    while True:
        print( "- (L)oad projects" )
        print( "- (S)ave projects" )
        print( "- (D)isplay projects" )
        print( "- (F)ilter projects by date" )
        print( "- (A)dd new project" )
        print( "- (U)pdate project" )
        print( "- (Q)uit" )

        choice = input( ">>> " ).lower()

        if choice == 'l':
            filename = input( "Enter filename to load projects from: " )
            projects = load_projects( filename )
        elif choice == 's':
            filename = input( "Enter filename to save projects to: " )
            save_projects( filename, projects )
        elif choice == 'd':
            display_projects( projects )
        elif choice == 'f':
            date_string = input( "Show projects that start after date (dd/mm/yyyy): " )
            date = datetime.strptime( date_string, "%d/%m/%Y" ).date()
            filtered_projects = filter_projects_by_date( projects, date )
            for project in filtered_projects:
                print( project )
        elif choice == 'a':
            add_new_project( projects )
        elif choice == 'u':
            update_project( projects )
        elif choice == ' q':
            save_choice = input( "Would you like to save to projects.txt? (yes/no): " )
            if save_choice.lower() == 'yes':
                save_projects( default_file, projects )
            print( "Thank you for using custom-built project management software." )
            break
        else:
            print( "Invalid choice. Please try again." )


if __name__ == "__main__":
    main()
