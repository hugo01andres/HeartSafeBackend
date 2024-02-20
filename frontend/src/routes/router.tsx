import {
  Route,
  createBrowserRouter,
  createRoutesFromElements,
} from "react-router-dom";
import PatientAnalysisPage from "@/modules/patient_analysis/pages/PatientAnalysisPage";
import RootLayout from "@/layouts/RootLayout";
export const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<RootLayout />}>
      <Route index element={<PatientAnalysisPage />} />
    </Route>
  )
);
