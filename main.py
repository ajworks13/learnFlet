import flet as ft


def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=500)

    btn = ft.ElevatedButton("Click me!")

    page.add(
        ft.Row([new_task, btn, ft.ElevatedButton("Add", on_click=add_clicked)]))


ft.app(target=main)
