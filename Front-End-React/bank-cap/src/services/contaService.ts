import { apiFetch } from "./api";

// Buscar todas as contas de um usuário
export const buscarContasDoUsuario = async (usuario_id: string) => {
  try {
    const response = await apiFetch(`/contas/usuario/${usuario_id}`, "GET");

    if (!response || !Array.isArray(response)) {
      throw new Error("Erro ao buscar contas do usuário.");
    }

    return response;
  } catch (error) {
    console.error("Erro em buscarContasDoUsuario:", error);
    return [];
  }
};

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