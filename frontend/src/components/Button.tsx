import { ButtonType } from "@/types/buttonTypes";
import { cn } from "@/utilities/cn";

interface ButtonProps extends React.HTMLProps<HTMLButtonElement> {
  type?: ButtonType;
  children?: React.ReactNode;
}

export default function Button({ children, className, ...props }: ButtonProps) {
  return (
    <button
      {...props}
      className={cn("bg-blue-500 text-white px-4 py-2 rounded-md", className)}
    >
      {children}
    </button>
  );
}
