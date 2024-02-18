import React from "react";
import { cn } from "@/utilities/cn";

type InputProps = {
  label?: string;
  error?: string;
  children?: React.ReactNode;
  inputClass?: string;
  labelClass?: string;
};

export default function Input({
  label,
  error,
  children,
  inputClass,
  labelClass,
}: InputProps) {
  return (
    <div className="flex flex-col gap-2">
      <label className={cn("inline-flex flex-col gap-2", labelClass)}>
        {label}
        {React.cloneElement(children as React.ReactElement, {
          className: cn("border p-2 py-1 rounded-md", inputClass),
        })}
      </label>

      {error && <p>{error}</p>}
    </div>
  );
}
