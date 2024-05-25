import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
            ft.dropdown.Option("123"),
            ft.dropdown.Option("fefew"),
            ft.dropdown.Option("Greeeeeeeeeeeeeeen"),
            ft.dropdown.Option("rrè"),
            ft.dropdown.Option("vć"),
            ft.dropdown.Option("Blue"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)


ft.app(target=main)
