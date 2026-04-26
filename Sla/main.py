import flet as ft

def main(page: ft.Page):
    page.padding = 0
    page.title = 'Janelinha'
    page.window.maximized = True
    page.theme.color
    page.update()

    container1 = ft.Container(
        content = ft.Button('butão')
    )

    page.add(container1)
ft.app(target=main)