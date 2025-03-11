import { apiFetch } from "./api";

export const loginApi = async (email: string, senha: string) => {
  return apiFetch("/auth/login", "POST", { email, senha });
};

export const registerApi = async (name: string, email: string, password: string) => {
    const userData = { nome: name, email, senha: password };
  
    const response = await apiFetch("/auth/register", "POST", userData);
  
    if (!response) {
      throw new Error("Erro ao conectar com a API.");
    }
  
    return response;
  };