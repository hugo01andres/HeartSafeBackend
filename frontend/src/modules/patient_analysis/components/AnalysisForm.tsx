import Form from "@/shared/components/Form";
import {
  AnalysisFormBiochemical,
  AnalysisFormGeneral,
  AnalysisFormStepper,
} from "@modules/patient_analysis/components";
import Button from "@shared/components/Button";
import { useAnalysisFormContext } from "@/modules/patient_analysis/hooks/useAnalysisFormContext";

export default function AnalysisForm() {
  const { handleSubmit: submit } = useAnalysisFormContext();

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    submit();
  }

  return (
    <div>
      <Form onSubmit={handleSubmit} className="max-w-lg gap-4">
        <h1 className="text-lg font-semibold">Formulario de análisis</h1>

        <AnalysisFormGeneral />
        <AnalysisFormBiochemical />

        <AnalysisFormStepper />
        <Button type="submit">Submit</Button>
      </Form>
    </div>
  );
}
