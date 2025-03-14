import React from 'react';
import { View, Text, ImageBackground, StyleSheet } from 'react-native';
import { StackNavigationProp } from '@react-navigation/stack';
import { RouteProp } from '@react-navigation/native';
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

        <Text style={{ color: '#fff', fontSize: 20 }}>Bem-vindo, {userId}, yedy</Text>
      </View>
    </ImageBackground>
  );
};



export default Start;
