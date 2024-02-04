import reflex as rx


class FormInput:
    def __init__(self, label, type_="text"):
        self.label = label
        self.type_ = type_

    def render(self, class_name=""):
        return rx.input(
                class_name=class_name,
                placeholder=self.label,
                type_=self.type_,
                name=self.label,
                _hover={"border_color": "auto", "border_width": "auto"},
                _focus_visible={"border_color": "auto", "border_width": "auto"},
                _active={"border_color": "auto", "border_width": "auto"}
            )
