import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment


def main(page: Page) -> None:
    page.title = "My Store"

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text("Home"), bgcolor='blue'),
                    Text(value='Home', size=30),
                    ElevatedButton(text='Go to store',
                                   on_click=lambda _: page.go('/store'))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )
