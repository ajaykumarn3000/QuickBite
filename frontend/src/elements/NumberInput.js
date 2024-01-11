import React from "react";

const NumberInput = ({ name, label, hooks }) => {
  return (
    <div className="NumberInput">
      <label htmlFor={name} className="block text-gray-600 text-lg ml-2 mb-1">
        {label}
      </label>
      <input
        className="block border-2 border-gray-400 p-1 rounded text-lg focus:border-amber-400 w-full mb-3"
        type="number"
        name={name}
        onChange={(e) => hooks.setPid(e.target.value)}
        value={hooks.pid}
      />
    </div>
  );
};

export default NumberInput;
