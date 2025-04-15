import React, { useState } from "react";
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
import ModalConta from "../../components/Start/ModalConta"; 
import { apiFetch } from "../../services/api";

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

const Start: React.FC<Props> = ({ route }) => {
  const [modalVisible, setModalVisible] = useState(false);
  const [totalReceitas, setTotalReceitas] = useState<number>(0); // Estado para o total das receitas
  const [totalDespesas, setTotalDespesas] = useState<number>(0);
  const { userId } = route.params;

  const fetchTotalReceitas = async () => {
    try {
      const response = await apiFetch(`/receitas/${userId}`, "GET");

      if (response && Array.isArray(response)) {
        const total = response.reduce((acc: number, receita: any) => acc + receita.valor, 0);
        setTotalReceitas(total);
      }
    } catch (error) {
      console.error("Erro ao buscar receitas:", error);
    }
  };
  

  return (
    <ImageBackground
      source={require("../../assets/background.jpg")}
      style={StyleStart.background}
    >
      <View style={{ flex: 0, justifyContent: "flex-start", alignItems: "center", paddingTop: 120,}}>
        <TopBar title={`Usuário: ${userId}`} />
        <DonutChart />{/*Aqui eu vou ter que passar o tanto de receita e de despesa que eu tenho*/}
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
      
        <ModalConta
          isVisible={modalVisible}
          onClose={() => setModalVisible(false)}
          usuario_id={userId} 
        />

        {/* Botões redondos*/}
        <FloatingButton/>

      </View>
    </ImageBackground>
  );
};

export default Start;
