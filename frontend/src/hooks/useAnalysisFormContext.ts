import { useContext } from "react";
import { AnalysisFormContext } from "@/contexts/AnalysisFormContext";

export function useAnalysisFormContext() {
  const context = useContext(AnalysisFormContext);

  if (!context) {
    throw new Error(
      "useAnalysisFormContext must be used within a AnalysisFormProvider"
    );
  }

  return context;
}
