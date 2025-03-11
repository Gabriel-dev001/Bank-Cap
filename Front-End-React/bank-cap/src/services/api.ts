import { API_BASE_URL } from "@env";

export const apiFetch = async (endpoint: string, method = "GET", body?: any) => {
    try {
      const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        method,
        headers: { "Content-Type": "application/json" },
        body: body ? JSON.stringify(body) : undefined,
      });
  
      const data = await response.json();
  
      if (!response.ok) {
        console.warn("Erro na API:", data);
        return null;
      }
  
      return data;
    } catch (error: any) {
      console.error("Erro na requisição:", error.message);
      return null;
    }
  };
  
  
  
