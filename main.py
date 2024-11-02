# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from db_handler import create_table, add_task, get_tasks, delete_task

class ToDoApp(App):
    def build(self):
        self.title = "To-Do List"
        create_table()  # Crear la base de datos si no existe

        layout = BoxLayout(orientation='vertical')
        self.task_list = BoxLayout(orientation='vertical')

        # Mostrar las tareas guardadas
        self.load_tasks()

        # Entrada para agregar nuevas tareas
        self.input_task = BoxLayout(size_hint_y=None, height=50)
        self.task_input = Label(text="Nueva Tarea:")
        self.add_button = Button(text="Agregar", on_press=self.add_task)

        self.input_task.add_widget(self.task_input)
        self.input_task.add_widget(self.add_button)

        layout.add_widget(self.task_list)
        layout.add_widget(self.input_task)

        return layout

    def load_tasks(self):
        tasks = get_tasks()
        self.task_list.clear_widgets()
        for task in tasks:
            task_label = Label(text=task[1])
            delete_btn = Button(text="Eliminar", on_press=lambda x, t=task[0]: self.remove_task(t))
            task_item = BoxLayout()
            task_item.add_widget(task_label)
            task_item.add_widget(delete_btn)
            self.task_list.add_widget(task_item)

    def add_task(self, instance):
        task_text = self.task_input.text
        add_task(task_text)
        self.load_tasks()

    def remove_task(self, task_id):
        delete_task(task_id)
        self.load_tasks()

if __name__ == "__main__":
    ToDoApp().run()
