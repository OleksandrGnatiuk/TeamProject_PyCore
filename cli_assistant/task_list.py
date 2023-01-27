from datetime import datetime


class ResponsiblePerson:
    """Клас для створення відповідальної особи"""

    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name


class Task:
    """Клас для створення завдання"""

    cnt = 0

    def __init__(self, text: str, person: ResponsiblePerson, deadline):
        self.text = text
        self.person = person

        y, m, d = deadline.split("-")
        self.deadline = datetime(year=int(y), month=int(m), day=int(d))

        self.status = "in process"

        Task.cnt += 1
        self.id = self.cnt


    def well_done(self):  # зміна статусу виконання завдання
        self.status = "done"


    def is_in_time(self):
        """функція перевіряє статус виконання на момент визову"""

        today = datetime.now()
        if today > self.deadline:
            self.status = "FAIL :("
        else:
            self.status = "in process"


    def __str__(self):
        self.is_in_time()
        return f"\nID: {self.id}     DEADLINE: {self.deadline.date()}\nTASK: {self.text}\nResponsible person: {self.person.name}\nSTATUS:   {self.status}\n"

   

class TaskList:
    """Клас для створення списку завдань"""
    
    def __init__(self):
        self.task_lst = {}


    def add_task(self, task: Task):  # додаємо нове завдання
        self.task_lst[task.id] = task


    def remove_task(self, ID):  # видаляємо завдання по ID
        if int(ID) in self.task_lst:
            self.task_lst.pop(int(ID))


    def show_all_tasks(self):  # виводимо перелік всіх завдань
        for k, v in self.task_lst.items():
            print(str(v))


    def change_deadline(self, ID, new_deadline):  
        '''змінюємо термін виконання завдання по ID'''

        y, m, d = new_deadline.split("-")
        new_deadline = datetime(year=int(y), month=int(m), day=int(d))

        if int(ID) in self.task_lst:
            self.task_lst[int(ID)].deadline = new_deadline


    def search_task(self, text_to_search):  # шукаємо завдання по тексту
        for task in self.task_lst.values():
            if text_to_search.lower() in task.text.lower():
                print(str(task))


    def search_respons_person(self, responsible_person: str):  
        '''шукаємо всі завдання, за які відповідає/відповідала особа'''

        result = "\n"
        for id, task in self.task_lst.items():
            if responsible_person.title() == task.person.name:
                result += str(task)
        return result




if __name__ == "__main__":

    sasha = ResponsiblePerson("Sasha")
    oleg = ResponsiblePerson("Oleg")
    artem = ResponsiblePerson("Artem")
    anastasiya = ResponsiblePerson("Anastasiya")

    task_1 = Task("Написати функцію", sasha, "2023-1-27")
    task_2 = Task("Написати класи та методи", oleg, "2023-1-28")
    task_3 = Task("Створити хендлер", oleg, "2023-1-29")
    task_4 = Task("Підготувати презениацію", anastasiya, "2023-1-30")

    # print(task_1)
    # task_1.well_done()
    # task_1.in_time()
    # print(task_1)

    to_do = TaskList()

    to_do.add_task(task_1)
    to_do.add_task(task_2)
    to_do.add_task(task_3)
    to_do.add_task(task_4)

    # to_do.show_all_tasks()

    # to_do.change_deadline(1, '2023-3-1')

    # to_do.show_all_tasks()

    to_do.search_task("підготувати")
    print(to_do.search_respons_person("oleg"))
