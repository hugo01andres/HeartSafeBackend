import Form from "@components/Form";
import {
  AnalysisFormBiochemical,
  AnalysisFormGeneral,
  AnalysisFormStepper,
} from "@/components/PatientAnalysis";
import Button from "../Button";
import { useAnalysisFormContext } from "@/hooks/useAnalysisFormContext";

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
