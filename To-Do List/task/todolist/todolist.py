# Write your code here
from datastore import *

session = create_datastore()


def print_tasks():
    print("Today:")
    rows = session.query(Table).all()
    if rows:
        for num, row in enumerate(rows, start=1):
            print(str(num) + ". " + row.task)
    else:
        print("Nothing to do!")
        print()


def add_task():
    print("Enter task")
    input_task = input()
    new_row = Table(task=input_task)
    session.add(new_row)
    session.commit()
    print("The task has been added!")
    print()


if __name__ == "__main__":
    while True:
        print("1) Today's tasks")
        print("2) Add task")
        print("0) Exit")
        command = int(input())
        print()
        if command == 0:
            break
        if command == 1:
            print_tasks()
        elif command == 2:
            add_task()
    print("Bye!")
