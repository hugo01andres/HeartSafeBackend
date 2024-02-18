import { useState, ChangeEvent, useEffect } from "react";

interface NumberInputProps
  extends Omit<React.HTMLProps<HTMLInputElement>, "onChange"> {
  value: number | undefined;
  showPlaceholderOnZero?: boolean;
  onChange: (value: number | undefined) => void;
}

export default function NumberInput({
  value,
  showPlaceholderOnZero = true,
  onChange,
  ...props
}: NumberInputProps) {
  const [inputValue, setInputValue] = useState(value?.toString() || "");

  useEffect(() => {
    if (showPlaceholderOnZero && value === 0) {
      setInputValue("");
    }
  }, [value, showPlaceholderOnZero]);

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const newValue = e.target.value;
    if (!isNaN(Number(newValue))) {
      onChange(newValue === "" ? undefined : Number(newValue));
      setInputValue(newValue);
    }
  };

  return (
    <input
      {...props}
      type="number"
      value={inputValue}
      onChange={handleChange}
    />
  );
}
