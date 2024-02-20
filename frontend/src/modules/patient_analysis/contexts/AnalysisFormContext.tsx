import { useAnalysisForm } from "@/modules/patient_analysis/hooks/useAnalysisForm";
import { AnalysisFormState } from "@modules/patient_analysis/types/AnalysisFormState";
import { createContext } from "react";

export type AnalysisProviderProps = {
  children: React.ReactNode;
};

export const AnalysisFormContext = createContext<AnalysisFormState | null>(
  null
);

export function AnalysisFormProvider({ children }: AnalysisProviderProps) {
  const state = useAnalysisForm();

  return (
    <AnalysisFormContext.Provider value={{ ...state }}>
      {children}
    </AnalysisFormContext.Provider>
  );
}
