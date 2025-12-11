import flet as ft

def main(page: ft.Page):
    page.title = "Convertisseur Tout Terrain"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 600
    page.window_height = 400

    # Input fields
    value_input = ft.TextField(label="Value to convert", hint_text="Enter the value here", keyboard_type=ft.KeyboardType.NUMBER)
    unit_input = ft.TextField(label="Unit to convert (e.g., km, miles, cm, inch, kg, pds, C, F)", hint_text="Enter the unit here", keyboard_type=ft.KeyboardType.TEXT)
    money_input = ft.TextField(label="Amount of money to convert")
    
    # 
    page.add(
        ft.Column([
            ft.Text(
                "Convertisseur Tout Terrain",
                size=24,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                color=ft.Colors.WHITE70
            ),
            ft.Divider(height=10),
            value_input,
            ft.Divider(height=10),
            unit_input,
            ft.Divider(height=10),
            money_input,
            ft.Divider(height=20),

            ft.ElevatedButton(
                "Clear All",
                icon=ft.Icons.CLEAR,
            ),

        ])
    )

ft.app(main)
