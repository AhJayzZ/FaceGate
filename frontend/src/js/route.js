import { Routes, Route } from "react-router-dom";

import NavigateBar from "./navigateBar"
import Info from "./info";

export default function Router() {
  return (
    <div>
      <NavigateBar />
      <Routes>
        <Route index element={<Info />} />
      </Routes>
    </div>
  );
}
