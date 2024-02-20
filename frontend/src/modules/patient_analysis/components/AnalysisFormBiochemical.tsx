import Input from "@/shared/components/Input";
import NumberInput from "@/shared/components/InputNumber";
import { useAnalysisFormContext } from "@/modules/patient_analysis/hooks/useAnalysisFormContext";

export default function AnalysisFormBiochemical() {
  const { setValue, ...state } = useAnalysisFormContext();

  const { form } = state;

  return (
    state.step === 1 && (
      <>
        <Input label="Creatinina fosfoquinasa">
          <NumberInput
            placeholder="Su nivel de creatinina fosfoquinasa"
            value={form.creatininePhosphokinase}
            onChange={(value) => setValue("creatininePhosphokinase", value)}
          />
        </Input>

        <Input label="Fracción de eyección">
          <NumberInput
            placeholder="Su fracción de eyección"
            value={form.ejectionFraction}
            onChange={(value) => setValue("ejectionFraction", value)}
          />
        </Input>

        <Input label="Nivel de plaquetas">
          <NumberInput
            placeholder="Su nivel de plaquetas"
            value={form.platelets}
            onChange={(value) => setValue("platelets", value)}
          />
        </Input>

        <Input label="Nivel de creatinina sérica">
          <NumberInput
            placeholder="Su nivel de creatinina sérica"
            value={form.serumCreatinine}
            onChange={(value) => setValue("serumCreatinine", value)}
          />
        </Input>

        <Input label="Nivel de sodio">
          <NumberInput
            placeholder="Su nivel de sodio"
            value={form.serumSodium}
            onChange={(value) => setValue("serumSodium", value)}
          />
        </Input>

        <Input label="Nivel de sodio">
          <NumberInput
            placeholder="Su nivel de sodio"
            value={form.serumSodium}
            onChange={(value) => setValue("serumSodium", value)}
          />
        </Input>
      </>
    )
  );
}
