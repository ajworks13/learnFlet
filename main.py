import flet as ft


class TaskApp(ft.UserControl):

    def build(self):
        self.textField = ft.TextField(width=350)
        self.addBtn = ft.FloatingActionButton(
            icon=ft.icon.ADD, on_click=self.addClick)

        self.task = ft.Column()
        taskRow = ft.Column(controls=[
            ft.Row(controls=[self.textField, self.addBtn])
        ])

        return taskRow

    def addClick(self, e):
        pass

    def taskDelete(self, task):
        pass


class Task(ft.UserControl):
    def __init__(self, taskName, taskDelete):
        super().__init__()
        self.taskName = taskName
        self.taskDelete = taskDelete

    def build(self):
        self.displayTask = ft.Checkbox(label=self.taskName, value=False)
        self.editName = ft.TextField()


def main(page: ft.page):
    page.title = "Tasking app by aj"
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = "BLACK"

    taskingApp = TaskApp()
    page.add(taskingApp)


ft.app(tartget=main)


# def main(page: ft.page):

#     # functions need to be inside def main

#     def addTask(p):
#         checkBox = ft.Checkbox(value=False)
#         checkBoxText = ft.Text(value=textField.value,
#                                width=350, bgcolor="WHITE", size=20)

#         taskRow = ft.Row(controls=[
#             checkBox,
#             checkBoxText
#         ],
#             alignment=ft.MainAxisAlignment.START
#         )

#         page.add(taskRow)

#     page.window_width = 500
#     page.window_height = 700
#     page.bgcolor = "WHITE"

#     textField = ft.TextField(width=350)
#     addBtn = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=addTask)

#     entiresRow = ft.Row(controls=[
#         textField,
#         addBtn
#     ],
#         alignment=ft.MainAxisAlignment.SPACE_BETWEEN
#     )

#     page.add(entiresRow)


# ft.app(target=main)


# def main(page: Page) -> None:
#     page.title = "My Store"

#     def route_change(e: RouteChangeEvent) -> None:
#         page.views.clear()

#         # Home
#         page.views.append(
#             View(
#                 route='/',
#                 controls=[
#                     AppBar(title=Text("Home"), bgcolor='blue'),
#                     Text(value='Home', size=30),
#                     ElevatedButton(text='Go to store',
#                                    on_click=lambda _: page.go('/store'))
#                 ],
#                 vertical_alignment=MainAxisAlignment.CENTER,
#                 horizontal_alignment=CrossAxisAlignment.CENTER,
#                 spacing=26
#             )
#         )

#         # Store
#         if page.route == '/store':
#             page.views.append(
#                 View(
#                     route='/store',
#                     controls=[
#                         AppBar(title=Text('Store'), bgcolor='blue'),
#                         Text(value='Store', size=30),
#                         ElevatedButton(
#                             text='Go back', on_click=lambda _: page.go('/'))
#                     ],
#                     vertical_alignment=MainAxisAlignment.CENTER,
#                     horizontal_alignment=CrossAxisAlignment.CENTER,
#                     spacing=26
#                 )
#             )
#         page.update()

#     def view_pop(e: ViewPopEvent) -> None:
#         page.views.pop()
#         top_view: View = page.views[-1]
#         page.go(top_view.route)

#     page.on_route_change = route_change
#     page.on_view_pop = view_pop
#     page.go(page.route)


# if __name__ == "__main__":
#     ft.app(target=main)
