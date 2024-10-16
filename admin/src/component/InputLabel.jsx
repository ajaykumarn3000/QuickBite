import clsx from "clsx";
import React from "react";

const InputLabel = ({ title, htmlFor, children, disabled }) => {
  return (
    <div
      className={clsx(
        "transition-all relative border-2 rounded",
        !disabled ? "border-slate-600" : "border-slate-300"
      )}
    >
      <label
        htmlFor={htmlFor}
        className={clsx(
          "transition-all absolute -top-3 left-2 bg-white px-1 text-sm",
          !disabled ? "text-slate-600" : "text-slate-400"
        )}
      >
        {String(title)[0].toUpperCase() + String(title).slice(1).toLowerCase()}
      </label>
      {children}
    </div>
  );
};

const inputStyle = (disabled) =>
  clsx(
    "transition-all font-medium border-none pl-2 pr-2 pb-1.5 pt-2.5 bg-transparent w-full outline-none",
    !disabled ? "text-black" : "text-slate-500"
  );

  export default InputLabel;
  export { inputStyle };
