import { Outlet } from "react-router-dom";

export default function RootLayout() {
  return (
    <div className="flex flex-col min-h-[100svh]">
      <h1>Header component</h1>

      <main className="flex-1 my-8 px-4">
        <Outlet />
      </main>

      <h1>Footer component</h1>
    </div>
  );
}
