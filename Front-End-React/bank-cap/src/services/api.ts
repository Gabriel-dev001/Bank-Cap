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

    // Verificando o status da resposta
    console.log("Status da resposta PUT:", response.status);

    // Se o status da resposta não for 2xx (OK), vamos capturar a mensagem de erro
    if (!response.ok) {
      const errorData = await response.text();
      console.warn("Erro na API PUT:", errorData);
      throw new Error(`Erro ao atualizar conta: ${errorData}`);
    }

    // Verificando o tipo de resposta para garantir que é JSON
    const contentType = response.headers.get("content-type");

    if (contentType && contentType.includes("application/json")) {
      const data = await response.json();
      console.log("Dados retornados da API PUT:", data);
      return data;
    }

    // Se a resposta não for JSON, retornar um objeto vazio
    console.warn("A resposta não é do tipo JSON. Retornando um objeto vazio.");
    return {};
  } catch (error: any) {
    // Log de erro e propagação
    console.error("Erro na requisição PUT:", error.message);
    throw error; // Lançamos o erro para que a função 'atualizarConta' possa tratá-lo adequadamente
  }
};
