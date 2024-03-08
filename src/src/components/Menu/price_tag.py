import reflex as rx


def PriceTag(price) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.image(src="images/pricetag.png", class_name="w-9 h-9"),
        rx.chakra.text(f"₹{price}", class_name="absolute text-white font-semibold text-sm"),
        class_name="PriceTag flex justify-center items-center relative w-9 h-9",
    )
