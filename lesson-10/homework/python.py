# Create a Task class with attributes such as task title, description, due date, and status

from datetime import date

class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date  # тип date
        self.status = status

    def __str__(self):
        return f"Task: {self.title}\nDescription: {self.description}\nDue: {self.due_date}\nStatus: {self.status}"
    

task1 = Task(
    title="Finish Report",
    description="Complete the financial report for Q1",
    due_date=date(2025, 5, 10),
    status="In Progress"
)

print(task1)

# 2.1. Define ToDoList Class
 
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        
        self.tasks.append(task)

    def remove_task(self, title):
        
        self.tasks = [t for t in self.tasks if t.title != title]

    def list_tasks(self):
        
        for task in self.tasks:
            print(task)
            print("-" * 40)

    def get_overdue_tasks(self, today):
        
        return [t for t in self.tasks if t.due_date < today and t.status != "Completed"]

    def mark_task_completed(self, title):
        
        for task in self.tasks:
            if task.title == title:
                task.status = "Completed"

from datetime import date

task1 = Task("Study SQL", "Finish the JOINs section", date(2025, 5, 3))
task2 = Task("Submit Project", "Banking DB schema", date(2025, 5, 1))


todo = ToDoList()
todo.add_task(task1)
todo.add_task(task2)


todo.list_tasks()


todo.mark_task_completed("Study SQL")


todo.remove_task("Submit Project")

# 2.2. 

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        
        self.tasks.append(task)

    def mark_task_completed(self, title):
        
        for task in self.tasks:
            if task.title == title:
                task.status = "Completed"
                return True
        return False  

    def list_all_tasks(self):
        
        if not self.tasks:
            print("Нет задач в списке.")
            return
        print("Все задачи:")
        for task in self.tasks:
            print(task)
            print("-" * 40)

    def display_incomplete_tasks(self):
        
        incomplete = [t for t in self.tasks if t.status != "Completed"]
        if not incomplete:
            print("Все задачи выполнены!")
            return
        print("Невыполненные задачи:")
        for task in incomplete:
            print(task)
            print("-" * 40)

            from datetime import date

class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return (f"Task: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due: {self.due_date}\n"
                f"Status: {self.status}")
    todo = ToDoList()

todo.add_task(Task("Learn SQL", "Study joins and subqueries", date(2025, 5, 1)))
todo.add_task(Task("Finish report", "Complete banking system doc", date(2025, 5, 3)))

todo.list_all_tasks()

todo.mark_task_completed("Learn SQL")

todo.display_incomplete_tasks()

# 3. 

from datetime import datetime, date

class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return (f"Task: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due: {self.due_date}\n"
                f"Status: {self.status}")

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.status = "Completed"
                return True
        return False

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks.")
            return
        print("All Tasks:")
        for task in self.tasks:
            print(task)
            print("-" * 40)

    def display_incomplete_tasks(self):
        incomplete = [t for t in self.tasks if t.status != "Completed"]
        if not incomplete:
            print("No incomplete tasks.")
            return
        print("Incomplete Tasks:")
        for task in incomplete:
            print(task)
            print("-" * 40)

# ---------------- CLI -------------------

def main():
    todo = ToDoList()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. List All Tasks")
        print("4. Show Incomplete Tasks")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_str = input("Due date (YYYY-MM-DD): ")
            try:
                due_date = datetime.strptime(due_str, "%Y-%m-%d").date()
                task = Task(title, description, due_date)
                todo.add_task(task)
                print("Task added!")
            except ValueError:
                print("Invalid date format.")
        elif choice == "2":
            title = input("Enter title of the task to mark as completed: ")
            if todo.mark_task_completed(title):
                print("Task marked as completed.")
            else:
                print("Task not found.")
        elif choice == "3":
            todo.list_all_tasks()
        elif choice == "4":
            todo.display_incomplete_tasks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()


from datetime import date

class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return (f"Task: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due: {self.due_date}\n"
                f"Status: {self.status}")

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.status = "Completed"
                return True
        return False

    def list_all_tasks(self):
        print("\nAll Tasks:")
        for task in self.tasks:
            print(task)
            print("-" * 40)

    def display_incomplete_tasks(self):
        print("\nIncomplete Tasks:")
        for task in self.tasks:
            if task.status != "Completed":
                print(task)
                print("-" * 40)


todo = ToDoList()

task1 = Task("Study SQL", "Learn joins and indexes", date(2025, 5, 1))
task2 = Task("Build App", "Finish to-do list CLI", date(2025, 5, 2))
task3 = Task("Backup Files", "Backup project data", date(2025, 5, 5))


todo.add_task(task1)
todo.add_task(task2)
todo.add_task(task3)

todo.mark_task_completed("Build App")


todo.list_all_tasks()

todo.display_incomplete_tasks()

# Homework 2. Create a Post class with attributes like title, content, and author.

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Content:\n{self.content}") 

post1 = Post(
    title="My First Blog Post",
    content="Today I learned about classes in Python. It's powerful and fun!",
    author="Alice"
)

print(post1)

# 2. 

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        
        self.posts.append(post)

    def list_all_posts(self):
        
        if not self.posts:
            print("Блог пуст.")
            return
        print("Все посты:")
        for post in self.posts:
            print(post)
            print("-" * 40)

    def display_posts_by_author(self, author_name):

        found = [p for p in self.posts if p.author == author_name]
        if not found:
            print(f"Нет постов от автора {author_name}.")
            return
        print(f"Посты автора {author_name}:")
        for post in found:
            print(post)
            print("-" * 40)

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent:\n{self.content}"
if __name__ == "__main__":
    blog = Blog()

    post1 = Post("Python OOP", "Classes and objects in Python.", "Alice")
    post2 = Post("Databases", "SQL basics explained.", "Bob")
    post3 = Post("Decorators", "Advanced Python functions.", "Alice")

    blog.add_post(post1)
    blog.add_post(post2)
    blog.add_post(post3)

    blog.list_all_posts()

    blog.display_posts_by_author("Alice")

    # 3. Create Main Program:

    
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Content:\n{self.content}")


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("No posts in the blog.")
            return
        print("\nAll Posts:")
        for post in self.posts:
            print(post)
            print("-" * 40)

    def display_posts_by_author(self, author_name):
        found = [p for p in self.posts if p.author.lower() == author_name.lower()]
        if not found:
            print(f"No posts found for author '{author_name}'.")
            return
        print(f"\nPosts by {author_name}:")
        for post in found:
            print(post)
            print("-" * 40)


def main():
    blog = Blog()

    while True:
        print("\n📚 Blog CLI Menu")
        print("1. Add a Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            blog.add_post(Post(title, content, author))
            print("✅ Post added!")

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name to search: ")
            blog.display_posts_by_author(author)

        elif choice == "0":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

# 4. 

from datetime import datetime


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Date: {self.created_at.strftime('%Y-%m-%d %H:%M')}\n"
                f"Content:\n{self.content}")

# --------- Blog class ---------
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("No posts found.")
            return
        print("\nAll Posts:")
        for post in self.posts:
            print(post)
            print("-" * 40)

    def display_posts_by_author(self, author_name):
        found = [p for p in self.posts if p.author.lower() == author_name.lower()]
        if not found:
            print(f"No posts found for author '{author_name}'.")
            return
        print(f"\nPosts by {author_name}:")
        for post in found:
            print(post)
            print("-" * 40)

    def delete_post(self, title):
        for i, post in enumerate(self.posts):
            if post.title == title:
                del self.posts[i]
                print(f"✅ Post '{title}' deleted.")
                return
        print("❌ Post not found.")

    def edit_post(self, title, new_title=None, new_content=None):
        for post in self.posts:
            if post.title == title:
                if new_title:
                    post.title = new_title
                if new_content:
                    post.content = new_content
                print("✅ Post updated.")
                return
        print("❌ Post not found.")

    def display_latest_posts(self, count=3):
        if not self.posts:
            print("No posts found.")
            return
        print(f"\n📌 Latest {count} Post(s):")
        for post in sorted(self.posts, key=lambda p: p.created_at, reverse=True)[:count]:
            print(post)
            print("-" * 40)

def main():
    blog = Blog()

    while True:
        print("\n📚 Blog CLI Menu")
        print("1. Add a Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete a Post")
        print("5. Edit a Post")
        print("6. Show Latest Posts")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
            print("✅ Post added.")

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Author to search: ")
            blog.display_posts_by_author(author)

        elif choice == "4":
            title = input("Title of post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Title of post to edit: ")
            new_title = input("New title (leave empty to keep current): ")
            new_content = input("New content (leave empty to keep current): ")
            blog.edit_post(title, new_title or None, new_content or None)

        elif choice == "6":
            try:
                n = int(input("How many recent posts to show? "))
            except ValueError:
                n = 3
            blog.display_latest_posts(n)

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
if __name__ == "__main__":
    main()

# 5. 

from time import sleep  

blog = Blog()

post1 = Post("Intro to Python", "Python is a versatile language.", "Alice")
sleep(1)  
post2 = Post("SQL Basics", "Let's learn about SELECT and JOIN.", "Bob")
sleep(1)
post3 = Post("Advanced Python", "Decorators and generators explained.", "Alice")

blog.add_post(post1)
blog.add_post(post2)
blog.add_post(post3)


print("\n▶ All Posts:")
blog.list_all_posts()


print("\n▶ Posts by 'Alice':")
blog.display_posts_by_author("Alice")


print("\n▶ Editing 'SQL Basics'...")
blog.edit_post("SQL Basics", new_content="UPDATED: Learn SELECT, JOIN, and GROUP BY.")


print("\n▶ Deleting 'Advanced Python'...")
blog.delete_post("Advanced Python")

print("\n▶ Latest 2 Posts:")
blog.display_latest_posts(2)

# Homework 3. Define Account Class

class Account:
    def __init__(self, number, holder, balance=0.0):
        self.number = number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    def __str__(self):
        return f"Account Number: {self.number}\nHolder: {self.holder}\nBalance: ${self.balance:.2f}"

# 2. 

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.number in self.accounts:
            return False
        self.accounts[account.number] = account
        return True

    def get_account(self, number):
        return self.accounts.get(number)

    def check_balance(self, number):
        account = self.get_account(number)
        return account.balance if account else None

    def deposit(self, number, amount):
        account = self.get_account(number)
        return account.deposit(amount) if account else False

    def withdraw(self, number, amount):
        account = self.get_account(number)
        return account.withdraw(amount) if account else False

    def transfer(self, from_number, to_number, amount):
        from_acc = self.get_account(from_number)
        to_acc = self.get_account(to_number)
        if not from_acc or not to_acc:
            return False
        if from_acc.withdraw(amount):
            to_acc.deposit(amount)
            return True
        return False

    def show_details(self, number):
        account = self.get_account(number)
        return str(account) if account else "Account not found."
def main():
    bank = Bank()

    while True:
        print("\n🏦 Bank System Menu")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer Money")
        print("6. Show Account Details")
        print("0. Exit")

        choice = input("Select option: ")

        if choice == "1":
            number = input("Account Number: ")
            holder = input("Holder Name: ")
            try:
                balance = float(input("Initial Balance: "))
            except ValueError:
                balance = 0.0
            acc = Account(number, holder, balance)
            if bank.add_account(acc):
                print("✅ Account added.")
            else:
                print("❌ Account already exists.")

        elif choice == "2":
            number = input("Enter account number: ")
            balance = bank.check_balance(number)
            print(f"Balance: ${balance:.2f}" if balance is not None else "❌ Account not found.")

        elif choice == "3":
            number = input("Account number: ")
            amount = float(input("Amount to deposit: "))
            print("✅ Success." if bank.deposit(number, amount) else "❌ Failed to deposit.")

        elif choice == "4":
            number = input("Account number: ")
            amount = float(input("Amount to withdraw: "))
            print("✅ Success." if bank.withdraw(number, amount) else "❌ Insufficient funds or error.")

        elif choice == "5":
            from_acc = input("From account: ")
            to_acc = input("To account: ")
            amount = float(input("Amount to transfer: "))
            print("✅ Transfer successful." if bank.transfer(from_acc, to_acc, amount) else "❌ Transfer failed.")

        elif choice == "6":
            number = input("Account number: ")
            print(bank.show_details(number))

        elif choice == "0":
            print("👋 Exiting system.")
            break

        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()







 

