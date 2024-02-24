def main():
    tasks=[]
    while True:
        print("\n ******To-Do-List******")
        print("1.Add Task")
        print("2.Show Tasks")
        print("3.Mark Task as Done")
        print("4.Delete Task")
        print("4.Exit")
        choice=input("enter your chice:")

        if choice =='1':
            print()
            n_tasks=int(input("How many tasks you need to add:"))

            for i in range(n_tasks):
                task=input("enter tasks:")
                tasks.append({"task":task,"done":False})
                print("Task added!")

        elif choice=='2':
            print("\n Tasks")
            for index,task in enumerate(tasks):
                status="Done" if task["done"] else "Not Done"
                print(f"{index+1}.{task['task']}-{status}")

        elif choice =='3':
            task_index=int(input("Enter the task number to mark as done:"))-1
            if 0<=task_index<len(tasks):
                tasks[task_index]["done"]=True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice =='4':
            if len(tasks) == 0:
                print("There is no task to delete.")
            else:
                print("Tasks")
                for i,task in enumerate(tasks):
                     print(f'{i+1}.{task}')
                choice = int(input("Enter the task number to delete:"))
            if 0 < choice <=len(tasks):
                del tasks[choice-1]
                print("Tasks deleted successfully.")
            else:
                print("Invalid task number.")

        elif choice =='5':
            print("Exiting the To-Do list.")
            break
        else:
            print("Invalid choice.Please try again.")


if __name__ =="__main__":
    main()
        
