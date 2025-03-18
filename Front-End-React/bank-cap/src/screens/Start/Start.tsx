import React from "react";
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
  const { userId } = route.params; // Pegando o userId passado via navigation

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

        <ButtonTextCenter title="Suas Contas" onPress={() => {}} />

        {/* Botões redondos*/}
        <FloatingButton/>

      </View>
    </ImageBackground>
  );
};

export default Start;
