import { ButtonType } from "@/types/buttonType";
import { cn } from "@/utilities/cn";

interface ButtonProps extends React.HTMLProps<HTMLButtonElement> {
  type?: ButtonType;
  children?: React.ReactNode;
}

export default function Button({
  children,
  disabled,
  className,
  ...props
}: ButtonProps) {
  return (
    <button
      {...props}
      className={cn("bg-blue-500 text-white px-4 py-2 rounded-md", className, {
        "cursor-not-allowed": disabled,
        "opacity-50": disabled,
      })}
    >
      {children}
    </button>
  );
}
