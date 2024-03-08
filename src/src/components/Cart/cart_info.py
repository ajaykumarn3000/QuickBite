import reflex as rx

def CartInfo(item) -> rx.Component:
  return rx.fragment(
    rx.divider(),
    rx.chakra.box(
      rx.text(f'{item["quantity"]} x {item["name"]} ₹ {item["price"]}'),
      rx.text(f'₹ {item["total"]}'),
      class_name="flex justify-between font-medium text-lg my-2"
    )
  )