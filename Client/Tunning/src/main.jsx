import * as React from "react";
import * as ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";
import { HomePage } from "./Components/Pages/Home/HomePage";
import { LoginPage } from "./Components/Pages/Login/Login";

const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />,
  }, 
  {
    path: "/login",
    element: <LoginPage />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);