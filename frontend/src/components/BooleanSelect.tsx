import React from "react";

interface BooleanSelectProps
  extends Omit<React.HTMLProps<HTMLSelectElement>, "value" | "onChange"> {
  value: boolean | undefined;
  optionLabels?: [string, string];
  disabledOptionLabel?: string;
  onChange: (value: boolean) => void;
}

export default function BooleanSelect({
  value,
  optionLabels = ["Sí", "No"],
  disabledOptionLabel,
  className,
  onChange,
}: BooleanSelectProps) {
  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedValue = event.target.value === "true";
    onChange(selectedValue);
  };

  const selectValue = value?.toString() ?? "undefined";

  return (
    <select className={className} value={selectValue} onChange={handleChange}>
      <option value={"undefined"} disabled>
        {disabledOptionLabel ?? "Seleccione una opción"}
      </option>
      <option value="true">{optionLabels[0]}</option>
      <option value="false">{optionLabels[1]}</option>
    </select>
  );
}
