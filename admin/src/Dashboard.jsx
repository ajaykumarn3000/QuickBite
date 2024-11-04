import React from "react";
import clsx from "clsx";
import LunchDiningIcon from "@mui/icons-material/LunchDining";
import ListAltRoundedIcon from "@mui/icons-material/ListAltRounded";
import SettingsRoundedIcon from "@mui/icons-material/SettingsRounded";
import { useNavigate } from "react-router-dom";

const Dashboard = ({ children }) => {
  console.log("DASHBOARD");
  const [open, setOpen] = React.useState("Menu");
  const navigate = useNavigate();

  return (
    <div className="h-full flex bg-slate-100">
      <div className="Dashboard w-60 flex flex-col shrink-0">
        <div className="flex gap-1 items-baseline text-gray-900 justify-center p-4">
          <span className="font-bold text-xl">QUICKBITE</span>
          <span className="text-xs font-semibold">admin</span>
        </div>
        <hr className="border-t-[1.5px]" />
        <div className="flex flex-col gap-1 mt-1">
          {[
            ["Menu", LunchDiningIcon, "/"],
            ["Orders", ListAltRoundedIcon, "/orders"],
          ].map(([item, Icon, path], index) => (
            <div
              key={index}
              className={clsx(
                "text-sm font-semibold py-2 px-4 mx-4 rounded transition-all cursor-pointer flex items-center gap-2",
                open === item
                  ? "bg-slate-200/70 hover:bg-slate-200 text-slate-800"
                  : "hover:bg-slate-200/40  text-slate-500"
              )}
              onClick={() => {
                setOpen(item);
                navigate(path);
              }}
            >
              <Icon />
              {item}
            </div>
          ))}
        </div>
      </div>
      {React.cloneElement(children, { open })}
    </div>
  );
};

export default Dashboard;
