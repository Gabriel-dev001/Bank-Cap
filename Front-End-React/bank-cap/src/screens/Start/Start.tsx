import React from 'react';
import { View, Text, ImageBackground, StyleSheet, Dimensions } from 'react-native';
import { StackNavigationProp } from '@react-navigation/stack';
import { RouteProp } from '@react-navigation/native';
import { ProgressChart } from "react-native-chart-kit";
import StyleStart from './StyleStart';
import TopBar from '../../components/TopBar';


// Definição dos tipos de navegação
type RootStackParamList = {
  Start: { userId: string }; // Start recebe userId via navigation
  Login: undefined;
  Register: undefined;
  Main: undefined;
};

type StartScreenNavigationProp = StackNavigationProp<RootStackParamList, 'Start'>;
type StartScreenRouteProp = RouteProp<RootStackParamList, 'Start'>;

type Props = {
  navigation: StartScreenNavigationProp;
  route: StartScreenRouteProp;
};



const Start: React.FC<Props> = ({ route }) => {
  const { userId } = route.params; // Pegando o userId passado via navigation

  return (
    <ImageBackground source={require('../../assets/background.jpg')} style={StyleStart.background}>
      <View style={StyleStart.container}>
        <TopBar title={`Usuário: ${userId}`} />

        <View style={StyleStart.saldoContainer}>
          <Text style={StyleStart.text}>RS: {/* Valor do Saldo Aqui */}</Text>
          <Text style={StyleStart.text}>Saldo</Text>
        </View>

      

        <View style={StyleStart.row}>
          <Text style={StyleStart.text}>Texto 1</Text>
          <Text style={StyleStart.text}>Texto 2</Text>
        </View>

      </View>
    </ImageBackground>
  );
};



export default Start;
