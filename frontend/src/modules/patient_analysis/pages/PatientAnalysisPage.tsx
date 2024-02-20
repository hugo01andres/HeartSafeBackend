import { AnalysisForm } from "@modules/patient_analysis/components";
import { AnalysisFormProvider } from "@modules/patient_analysis/contexts";

export default function PatientAnalysisPage() {
  return (
    <div>
      <AnalysisFormProvider>
        <AnalysisForm />
      </AnalysisFormProvider>
    </div>
  );
}
