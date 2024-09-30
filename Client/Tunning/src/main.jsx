import * as React from "react";
import * as ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";
import { HomePage } from "./Components/Pages/Home/HomePage";
import { LoginPage } from "./Components/Pages/Login/Login";
import { CreateAccountPage } from "./Components/Pages/CriarConta/CriarConta";
import { ProtectedRoute } from "./Components/ProtectedRoute";

const router = createBrowserRouter([
  {
    path: "/",
    element: ( <ProtectedRoute /> ),
    children: [
      {
        path: "/home",
        element: (
            <HomePage />
        ),
      },
      
    ]
  },  
  {
    path: "/login",
    element: <LoginPage />,
  },
  {
    path: "/criar_Conta",
    element: <CreateAccountPage />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);