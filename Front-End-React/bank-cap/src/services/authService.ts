import { GOOGLE_CLIENT_ID } from "@env";
import * as Google from "expo-auth-session/providers/google";
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

  export const googleApi = () => {
    const [request, response, promptAsync] = Google.useAuthRequest({
      clientId: GOOGLE_CLIENT_ID
    });
  
    async function handleGoogleLogin() {
      if (!response || response.type !== "success") {
        console.error("Erro na resposta do Google:", response);
        return;
      }
    
      const id_token = response?.params?.id_token;
      if (!id_token) {
        console.error("ID Token não encontrado na resposta:", response);
        return;
      }
    
      try {
        const userInfoResponse = await fetch(
          "https://www.googleapis.com/oauth2/v3/userinfo",
          { headers: { Authorization: `Bearer ${id_token}` } }
        );
        const userInfo = await userInfoResponse.json();
    
        const userData = {
          google_id: userInfo.sub,
          email: userInfo.email,
        };
    
        let apiResponse = await apiFetch("/auth/google/login", "POST", userData);
    
        if (!apiResponse) {
          console.log("Usuário não encontrado, realizando cadastro...");
          
          const registerData = {
            ...userData,
            nome: userInfo.name,
          };
          await apiFetch("/auth/google/register", "POST", registerData);
    
          apiResponse = await apiFetch("/auth/google/login", "POST", userData);
        }
    
        if (!apiResponse) {
          console.error("Erro ao autenticar usuário.");
          return;
        }
    
        console.log("Usuário autenticado com sucesso:", apiResponse);
        return apiResponse;
      } catch (error) {
        console.error("Erro na autenticação com Google:", error);
      }
    }
  
    return { request, promptAsync, handleGoogleLogin };
  };