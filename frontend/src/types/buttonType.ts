const ButtonTypes = {
  Button: "button",
  Submit: "submit",
  React: "reset",
} as const;

export type ButtonType = (typeof ButtonTypes)[keyof typeof ButtonTypes];
