import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios"; // Import axios

export function ProtectedRoute({ children }) {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true); // Estado de carregamento
  const [isAuthenticated, setIsAuthenticated] = useState(false); // Estado de autenticação

  useEffect(() => {
    const checkAuth = async () => {
      try {
        // Faz a verificação do token de autenticação
        await axios.get('http://localhost:8000/auth/checkToken', {
          withCredentials: true,  // Para incluir cookies
        });
        setIsAuthenticated(true); // Usuário autenticado
      } catch (error) {
        // Se houver erro, redireciona para a página de login
        console.error("Access denied:", error.response ? error.response.data : error.message);
        navigate("/login");
      } finally {
        setLoading(false); // Verificação concluída
      }
    };

    checkAuth(); // Chama a função de verificação
  }, [navigate]);

  if (isAuthenticated) {
    return children;
  }
}
