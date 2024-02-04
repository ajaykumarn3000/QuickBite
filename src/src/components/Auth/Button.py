import reflex as rx


class Button:
    def __init__(self, label, type_=""):
        self.label = label
        self.type_ = type_

    def render(self, class_name=""):
        return rx.button(
            self.label,
                class_name=class_name,
                type_=self.type_,
                name=self.label,
                background="auto",
                _hover={"background": "auto"}
            )
