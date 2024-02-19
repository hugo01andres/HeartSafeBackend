export const genderTypes = {
  MALE: "male",
  FEMALE: "female",
  OTHER: "other",
} as const;

export type GenderType = (typeof genderTypes)[keyof typeof genderTypes];
