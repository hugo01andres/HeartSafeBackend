import { FormEvent } from "react";
import Input from "@components/Input";
import NumberInput from "@components/InputNumber";
import BooleanSelect from "@components/BooleanSelect";
import { useAnalysisFormContext } from "@/hooks/useAnalysisFormContext";
import { genderTypes, GenderType } from "@/types/genderType";

export default function AnalysisFormGeneral() {
  const { setValue, ...state } = useAnalysisFormContext();

  const { form } = state;

  return (
    state.step === 0 && (
      <>
        <Input label="Edad">
          <NumberInput
            placeholder="Su edad"
            value={form.age}
            onChange={(value) => setValue("age", value)}
          />
        </Input>

        <Input label="Sexo">
          <select
            value={form.sex ?? "undefined"}
            onChange={(e: FormEvent<HTMLSelectElement>) => {
              setValue("sex", e.currentTarget.value as GenderType);
            }}
          >
            <option value={"undefined"} disabled>
              Seleccione una opción
            </option>
            <option value={genderTypes.MALE}>Masculino</option>
            <option value={genderTypes.FEMALE}>Femenino</option>
            <option value={genderTypes.OTHER}>Prefiero no decirlo</option>
          </select>
        </Input>

        <Input label="¿Es fumador?">
          <BooleanSelect
            value={form.smoking}
            onChange={(value) => setValue("smoking", value)}
          />
        </Input>

        <Input label="¿Padece de anemia?">
          <BooleanSelect
            value={form.anaemia}
            onChange={(value) => setValue("anaemia", value)}
          />
        </Input>

        <Input label="¿Padece de diabetes?">
          <BooleanSelect
            value={form.diabetes}
            onChange={(value) => setValue("diabetes", value)}
          />
        </Input>

        <Input label="¿Padece de hipertensión arterial?">
          <BooleanSelect
            value={form.highBloodPressure}
            onChange={(value) => setValue("highBloodPressure", value)}
          />
        </Input>
      </>
    )
  );
}
