import {
  Route,
  createBrowserRouter,
  createRoutesFromElements,
} from "react-router-dom";
import PatientAnalysisPage from "@/pages/PatientAnalysisPage";
import RootLayout from "@/layout/RootLayout";
import { AnalysisFormProvider } from "@/contexts/AnalysisFormContext";

export const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<RootLayout />}>
      <Route
        index
        element={
          <AnalysisFormProvider>
            <PatientAnalysisPage />
          </AnalysisFormProvider>
        }
      />
    </Route>
  )
);
