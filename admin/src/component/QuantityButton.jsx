import clsx from 'clsx'
import React from 'react'

const QuantityButton = ({quantity, add, onClick}) => {
  return (
    <button onClick={onClick} className={clsx('transition-transform rounded-full w-10 text-center hover:scale-110 scale-100 active:scale-90 text-sm border-[1.5px]', add ? "border-green-600 text-green-600 bg-green-50" : "border-red-600 text-red-600 bg-red-50")}>
      {add ? "+" : "-"}{quantity}
    </button>
  )
}

export default QuantityButton