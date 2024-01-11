import React from "react";

const EmailInput = ({ name, label, hooks }) => {
  return (
    <div className="EmailInput">
      <label className="block text-gray-600 text-lg ml-2 mb-1" htmlFor={name}>
        {label}
      </label>

      <div className="sm:block flex flex-col w-full sm:border-2 border-gray-400 p-1 rounded text-lg focus:border-amber-400 mb-3">
        <input
          className="sm:border-none border-2 focus:border-amber-400 border-gray-400 p-1"
          name={name}
          type="text"
          value={hooks.email}
          onChange={(e) => hooks.setEmail(e.target.value)}
        />
        <select
          className="mt-2 text-right bg-white"
          name="domain"
          onChange={(e) => {
            hooks.setDomain(e.target.value);
          }}
        >
          <option className="" value="@student.sfit.ac.in">
            @student.sfit.ac.in
          </option>
          <option value="@sfit.ac.in">@sfit.ac.in</option>
        </select>
      </div>
    </div>
  );
};

export default EmailInput;
