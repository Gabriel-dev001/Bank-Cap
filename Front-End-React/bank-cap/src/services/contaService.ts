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
      saldo: 0.0,
    };
  
    const response = await apiFetch("/contas/", "POST", accountData);
  
    if (!response) {
      throw new Error("Erro ao conectar com a API.");
    }
  
    return response;
};