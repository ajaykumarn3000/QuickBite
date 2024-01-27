import React from "react";

const TextInput = ({ label, name, type, hooks }) => {
  return (
    <div className="TextInput">
      <label htmlFor={name} className="block text-gray-600 text-lg ml-2 mb-1">
        {label}
      </label>
      <input
        type={type}
        name={name}
        value={hooks.password}
        onChange={(e) => hooks.setPassword(e.target.value)}
        className="block border-2 border-gray-400 p-1 rounded text-lg focus:border-amber-400 w-full mb-3"
      />
    </div>
  );
};

export default TextInput;
