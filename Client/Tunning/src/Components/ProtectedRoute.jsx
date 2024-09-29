import React from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios"; // Import axios

export function ProtectedRoute({ children }) {
  const navigate = useNavigate();

  React.useEffect(() => {
    const checkAuth = async () => {
      try {
        await axios.get('http://localhost:8000/auth/checkToken', {
          withCredentials: true,  // Para incluir cookies
        });
        console.log('ok')
      } catch (error) {
        // If there's an error, redirect to login
        console.error("Access denied:", error.response ? error.response.data : error.message);
        navigate("/login");
      }
    };

    checkAuth(); // Call the async function
  }, [navigate]);

  // If authenticated, render the children
  return children; 
}
