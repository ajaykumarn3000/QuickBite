import reflex as rx

def StockTag(stock) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.text(f"{stock} left", class_name="text-white font-semibold text-sm"),
        class_name="PriceTag flex justify-center items-center bg-green-500 px-1 rounded"
    )