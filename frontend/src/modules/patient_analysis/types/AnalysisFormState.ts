import { ActionWithPayload } from "../../../shared/types/utility";
import { GenderType } from "../../../shared/types/genderType";

export type AnalysisFormPayload = {
  age: number;
  serumCreatinine: number;
  serumSodium: number;
  platelets: number;
  ejectionFraction: number;
  creatininePhosphokinase: number;
  anaemia: boolean | undefined;
  diabetes: boolean | undefined;
  highBloodPressure: boolean | undefined;
  smoking: boolean | undefined;
  sex: GenderType | undefined;
};

export type AnalysisFormState = {
  form: AnalysisFormPayload;
  step: number;
  maxStep: number;
  setValue: (
    key: keyof AnalysisFormPayload,
    value: AnalysisFormPayload[keyof AnalysisFormPayload]
  ) => void;
  setStep: (step: number) => void;
  handleSubmit: () => void;
};

type AnalysisFormPayloadKeys = keyof AnalysisFormPayload;

export type SetValueAction = ActionWithPayload<
  "SET_VALUE",
  {
    key: AnalysisFormPayloadKeys;
    value: AnalysisFormPayload[AnalysisFormPayloadKeys];
  }
>;
export type SetStepAction = ActionWithPayload<"SET_STEP", number>;

export type AnalysisFormActionTypes = SetValueAction | SetStepAction;
