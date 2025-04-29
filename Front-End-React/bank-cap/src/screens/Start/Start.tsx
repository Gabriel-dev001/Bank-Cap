import React, { useState, useEffect } from "react";
import {
  View,
  Text,
  ImageBackground,
  TouchableOpacity,
} from "react-native";
import { StackNavigationProp } from "@react-navigation/stack";
import { RouteProp } from "@react-navigation/native";
import StyleStart from "./StyleStart";
import TopBar from "../../components/Start/TopBar";
import DonutChart from "../../components/Start/DonutChart";
import LineSeparator from "../../components/Start/LineSeparator";
import ButtonTextCenter from "../../components/Commom/ButtonTextCenter";
import FloatingButton from "../../components/Start/FloatingButton";
import ModalListaContas from "../../components/Start/Modals/ModalListaContas"; 
import { apiFetch } from "../../services/api";
import { buscarContasDoUsuario } from "../../services/contaService";

// Definição dos tipos de navegação
type RootStackParamList = {
  Start: { userId: string }; 
  Login: undefined;
  Register: undefined;
  Main: undefined;
};

type StartScreenNavigationProp = StackNavigationProp<
  RootStackParamList,
  "Start"
>;
type StartScreenRouteProp = RouteProp<RootStackParamList, "Start">;

type Props = {
  navigation: StartScreenNavigationProp;
  route: StartScreenRouteProp;
};

interface Conta {
  id: string;
  usuario_id: string;
  nome: string;
  banco: string;
  tipo: "PESSOAL" | "EMPRESARIAL";
  saldo: number;
  criado_em: string;
}

const Start: React.FC<Props> = ({ route }) => {
  const [modalVisible, setModalVisible] = useState(false); 
  const [listaContas, setListaContas] = useState<Conta[]>([]);  
  const [dadosConta, setDadosConta] = useState<any>(null);
  const [contaSelecionadaId, setContaSelecionadaId] = useState<string | null>(null);
  const { userId } = route.params;

  const buscarDadosConta = async (id: string) => {
    const dados = await apiFetch(`/contas/${contaSelecionadaId}`);
    if (dados) {
      setDadosConta(dados);
    }
  };

  useEffect(() => {
    if (contaSelecionadaId) {
      buscarDadosConta(contaSelecionadaId.toString());
    }
  }, [contaSelecionadaId]);

  useEffect(() => {
    const carregarContas = async () => {
      const contas = await buscarContasDoUsuario(userId); 
      if (contas) {
        setListaContas(contas);
      }
    };
    carregarContas();
  }, [userId]);

  const handleSelecionarConta = (contaId: string) => {
    setContaSelecionadaId(contaId); 
    setModalVisible(false);
  };

  return (
    <ImageBackground
      source={require("../../assets/background.jpg")}
      style={StyleStart.background}
    >
      <View style={{ flex: 0, justifyContent: "flex-start", alignItems: "center", paddingTop: 120,}}>
      <TopBar title={`${dadosConta ? dadosConta.nome : "--"}`} />
        {/* <DonutChart saldo={dadosConta?.saldo || 0}/>Aqui eu vou ter que passar o tanto de receita e de despesa que eu tenho */}
        <DonutChart saldoReal={dadosConta?.saldo ?? 0} despesas={1} />


      </View>

      <View style={StyleStart.container}>
        <LineSeparator />

        <View style={StyleStart.row}>
          {/* Coluna Receita */}
          <View>
            <TouchableOpacity style={StyleStart.squareGreen} onPress={() => console.log("Botão de Receita pressionado")}>
              <Text style={StyleStart.textTitlle}>Receitas</Text>
              <Text style={StyleStart.text}>/*R$: */</Text>
            </TouchableOpacity>
          </View>

          {/* Coluna Despesa */}
          <View >
            <TouchableOpacity style={StyleStart.squareRed} onPress={() => console.log("Botão de Despesa pressionado")}>
              <Text style={StyleStart.textTitlle}>Despesa</Text>
              <Text style={StyleStart.text}>/*R$: */</Text>
            </TouchableOpacity>
          </View>
        </View>

        
        <ButtonTextCenter title="Suas Contas" onPress={() => setModalVisible(true)} /> 
          
        <ModalListaContas
          isVisible={modalVisible}
          onClose={() => setModalVisible(false)} 
          contas={listaContas}
          usuario_id={userId}
          onSelecionarConta={handleSelecionarConta} 
        />

        {/* Debug */}
        <Text style={{ color: "white" }}>Conta Selecionada: {contaSelecionadaId}</Text>
      
        {/* Botões redondos*/}
        <FloatingButton idConta={contaSelecionadaId ?? ""}/>

      </View>
    </ImageBackground>
  );
};

export default Start;