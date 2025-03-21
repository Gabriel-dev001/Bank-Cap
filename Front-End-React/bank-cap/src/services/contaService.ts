import { apiFetch } from "./api";

export const criarContaApi = async (
    usuario_id: string,
    nome: string,
    banco: string,
    tipo: string
  ) => {
    const accountData = {
      usuario_id,
      nome,
      banco,
      tipo,
      saldo: null,
    };
  
    const response = await apiFetch("/contas/create", "POST", accountData);
  
    if (!response) {
      throw new Error("Erro ao conectar com a API.");
    }
  
    return response;
  };