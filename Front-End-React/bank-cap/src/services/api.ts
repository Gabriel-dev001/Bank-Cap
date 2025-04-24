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
}

export const apiPut = async (endpoint: string, body: any) => {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      const errorData = await response.text();
      console.warn("Erro na API PUT:", errorData);
      throw new Error(`Erro ao atualizar conta: ${errorData}`);
    }

    const contentType = response.headers.get("content-type");

    if (contentType && contentType.includes("application/json")) {
      const data = await response.json();
      console.log("Dados retornados da API PUT:", data);
      return data;
    }

    return {};
  } catch (error: any) {
    throw error; 
  }
};
