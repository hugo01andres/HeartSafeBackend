import React from "react";
import { cn } from "@/utilities/cn";

type InputProps = {
  label?: string;
  error?: string;
  children?: React.ReactNode;
  inputClass?: string;
};

export default function Input({
  label,
  error,
  children,
  inputClass = "",
}: InputProps) {
  console.log(cn("border rounded-md"));

  return (
    <div className="flex flex-col gap-2">
      {label && <label>{label}</label>}
      {React.cloneElement(children as React.ReactElement, {
        className: cn("border rounded-md", inputClass),
      })}
      {error && <p>{error}</p>}
    </div>
  );
}
