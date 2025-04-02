import ItemDetails from "./ItemDetails";
import QuantityControl from "./QuantityControl";
import { useMenuContext } from "../../context/menuContext";

const Editor = () => {
  console.log("EDITOR");
  const { currentItem } = useMenuContext();
  return (
    <div className="py-4 px-4 max-w-72 min-w-72 bg-white">
      {currentItem ? (
        <>
          <ItemDetails />
          <QuantityControl quantity={5} />
        </>) : (
          <div className="h-full w-full flex items-center justify-center rounded-lg shadow">
            <h1 className="text-lg text-center text-slate-400">Select an item to edit</h1>
          </div>
        )
      }
    </div>
  );
};

export default Editor;
