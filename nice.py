from nicegui import ui

ui.label('CALCULATOR').classes("bold item-center")


with ui.grid(columns = 4):
    ui.button("1")
    ui.button("2")
    ui.button("3")
    ui.button("/")

    ui.button("4")
    ui.button("5")
    ui.button("6")
    ui.button("*")

    ui.button("7")
    ui.button("8")
    ui.button("9")
    ui.button("-")

    ui.button("")
    ui.button("0")
    ui.button("")
    ui.button("+")

ui.button("calculate")

ui.run()
