import Button from "@components/Button";
import { useAnalysisFormContext } from "@/hooks/useAnalysisFormContext";

export default function AnalysisFormStepper() {
  const { setStep, ...state } = useAnalysisFormContext();
  const { step, maxStep } = state;

  function nextStep() {
    setStep(step + 1);
  }

  function prevStep() {
    setStep(step - 1);
  }

  const restrictions = {
    canPrevStep: step > 0,
    canNextStep: step < maxStep,
  };

  return (
    <nav className="flex items-center justify-between">
      <Button
        type="button"
        className={"border border-blue-500 bg-transparent text-blue-500"}
        onClick={prevStep}
        disabled={!restrictions.canPrevStep}
      >
        {" "}
        &larr; Back
      </Button>

      <Button
        type="button"
        className="border border-blue-500 bg-transparent text-blue-500"
        onClick={nextStep}
        disabled={!restrictions.canNextStep}
      >
        {" "}
        Next &rarr;
      </Button>
    </nav>
  );
}
