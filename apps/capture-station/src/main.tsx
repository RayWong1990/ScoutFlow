import React from "react";
import ReactDOM from "react-dom/client";

import "./styles/tokens/tokens.css";
import "./styles/tokens/density-compact.css";
import "./styles/tokens/type-weight-heavy.css";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
