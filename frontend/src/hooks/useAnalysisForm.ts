import {
  AnalysisFormActionTypes,
  AnalysisFormPayload,
  AnalysisFormState,
} from "@/types/AnalysisFormState";
import { useReducer } from "react";

const initialState: AnalysisFormState = {
  form: {
    age: 0,
    creatininePhosphokinase: 0,
    ejectionFraction: 0,
    serumCreatinine: 0,
    serumSodium: 0,
    platelets: 0,
    anaemia: undefined,
    diabetes: undefined,
    highBloodPressure: undefined,
    smoking: undefined,
    sex: undefined,
  },
  step: 0,
  maxStep: 1,
  setValue: () => {},
  setStep: () => {},
  handleSubmit: () => {},
};

const reducer = (state: AnalysisFormState, action: AnalysisFormActionTypes) => {
  switch (action.type) {
    case "SET_VALUE":
      return {
        ...state,
        form: { ...state.form, [action.payload.key]: action.payload.value },
      };
    case "SET_STEP":
      if (action.payload < 0 || action.payload > state.maxStep) return state;

      return {
        ...state,
        step: action.payload,
      };
    case "HANDLE_SUBMIT":
      console.log("Submitting form");
      return state;
    default:
      return state;
  }
};

export const useAnalysisForm = () => {
  const [state, dispatch] = useReducer(reducer, initialState);

  const setValue = (
    key: keyof AnalysisFormPayload,
    value: AnalysisFormPayload[keyof AnalysisFormPayload]
  ) => {
    dispatch({ type: "SET_VALUE", payload: { key, value } });
  };

  const setStep = (step: number) => {
    dispatch({ type: "SET_STEP", payload: step });
  };

  const handleSubmit = () => {
    dispatch({ type: "HANDLE_SUBMIT", payload: undefined });
  };

  return { ...state, setValue, setStep, handleSubmit };
};
