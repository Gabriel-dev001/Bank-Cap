import { apiFetch } from "./api";
import { apiPut } from "./api";

export const cadastrarReceitaApi = async (
    conta_id: string,
    valor: number,
    data: string,
    categoria: string,
    descricao: string
  ) => {
    const receitaData = {
      conta_id,
      valor,
      data,
      categoria,
      descricao,
    };
  
    const response = await apiFetch("/receitas/", "POST", receitaData);
  
    if (!response) {
      throw new Error("Erro ao conectar com a API.");
    }
  
    return response;
  };
