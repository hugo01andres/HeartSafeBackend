import { cn } from "@/utilities/cn";

interface FormProps extends React.HTMLProps<HTMLFormElement> {
  title?: string;
  children?: React.ReactNode;
}

export default function Form({
  title,
  className,
  children,
  ...props
}: FormProps) {
  return (
    <form
      {...props}
      className={cn(
        "flex flex-col gap-2 max-w-sm border rounded-md mx-auto p-4",
        className
      )}
    >
      {title && <h1 className="text-lg font-semibold">{title}</h1>}
      {children}
    </form>
  );
}
