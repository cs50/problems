from tasks import add_task, remove_task, txt_length, update_txt
import sys

def main():

    argument = sys.argv[1]
    tasks = ['Attend Lecture', 'Rip a Phonebook']
    description = sys.argv[3]
    filepath = sys.argv[1]

    if argument == "add":
        tasks.add_task(tasks, description, filepath)
        print(tasks.txt_length(filepath))

if __name__ == "__main__":
    main()
