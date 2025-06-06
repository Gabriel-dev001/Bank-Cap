import { apiFetch } from "./api";
import { apiPut } from "./api";


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

export const atualizarConta = async (
  id: string,
  dados: { nome: string; banco: string; tipo: string; usuario_id: string }
) => {
  try {
    // Fazendo a requisição PUT para atualizar a conta
    const response = await apiPut(`/contas/${id}`, dados);

    // Verificando se a resposta é válida
    if (!response) {
      throw new Error("Erro ao atualizar conta: sem resposta da API.");
    }

    // Adicionando log para verificar o conteúdo da resposta
    console.log("Resposta da API:", response);

    // Retorna a resposta da API, que deverá ser o objeto atualizado
    return response;
  } catch (error) {
    // Captura e loga o erro
    console.error("Erro ao atualizar conta:", error);
    return null;
  }
};

export const deletarConta = async (id: string) => {
  try {
    const response = await apiFetch(`/contas/${id}`, "DELETE");
    return response;
  } catch (error) {
    console.error("Erro ao deletar conta:", error);
    return null;
  }
};