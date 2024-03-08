import reflex as rx
from src.components.Menu.price_tag import PriceTag
from src.components.Menu.stock_tag import StockTag
# state
from src.state import MenuItemState


def MenuItem(item) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.box(
            PriceTag(item["item_price"]), class_name="absolute top-[-8px] left-[-8px]"
        ),
        rx.chakra.box(
            StockTag(item["item_quantity"]), class_name="absolute top-[-5px] right-[-8px]"
        ),
        rx.chakra.box(
            rx.chakra.image(
                src=item["item_icon"],
                class_name="object-cente object-cover aspect-video",
            ),
            class_name="rounded-t-lg overflow-hidden",
        ),
        rx.chakra.text(item["item_name"], class_name="text-gray-600 font-semibold text-center"),
        class_name=rx.cond(
            MenuItemState.selected,
            "FoodItem h-fit m-2 relative rounded-lg bg-white shadow border-[3px] border-amber-500 shadow-md",
            "FoodItem h-fit m-2 relative rounded-lg bg-white shadow border-[3px] hover:border-primary-400 border-white",
        ),
        max_width="10rem",
    )
