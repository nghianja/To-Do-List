# Write your code here
from datastore import *
from datetime import datetime, timedelta

session = create_datastore()


def print_rows(deadline_day):
    rows = session.query(Table).filter(Table.deadline == deadline_day.date()).all()
    if rows:
        for num, row in enumerate(rows, start=1):
            print(str(num) + ". " + row.task)
    else:
        print("Nothing to do!")
    print()


def print_today():
    today = datetime.today()
    print(today.strftime("Today %-d %b:"))
    print_rows(today)


def print_week():
    today = datetime.today()
    for i in range(7):
        week_day = today + timedelta(days=i)
        print(week_day.strftime("%A %-d %b"))
        print_rows(week_day)


def print_all():
    print("All tasks:")
    rows = session.query(Table).order_by(Table.deadline).all()
    if rows:
        for num, row in enumerate(rows, start=1):
            print(str(num) + ". " + row.task + ". " + row.deadline.strftime("%-d %b"))
    else:
        print("Nothing to do!")
    print()


def print_tasks(choice):
    if choice == 1:
        print_today()
    elif choice == 2:
        print_week()
    elif choice == 3:
        print_all()


def add_task():
    print("Enter task")
    input_task = input()
    print("Enter deadline")
    input_deadline = datetime.strptime(input(), "%Y-%m-%d").date()
    new_row = Table(task=input_task, deadline=input_deadline)
    session.add(new_row)
    session.commit()
    print("The task has been added!")
    print()


if __name__ == "__main__":
    while True:
        print("1) Today's tasks")
        print("2) Week's tasks")
        print("3) All tasks")
        print("4) Add task")
        print("0) Exit")
        command = int(input())
        print()
        if command == 0:
            break
        if command == 4:
            add_task()
        else:
            print_tasks(command)
    print("Bye!")
