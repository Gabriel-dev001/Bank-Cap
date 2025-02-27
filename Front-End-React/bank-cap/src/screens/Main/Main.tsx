import React from 'react';
import { 
  View, Text, TouchableOpacity, 
} from 'react-native';

import { StackNavigationProp } from '@react-navigation/stack';
import { RouteProp } from '@react-navigation/native';
import { NavigationProps } from '../../navigation/types';
import { ImageBackground } from 'react-native';
import { Image } from 'react-native';

import Title from "../../components/Title";
import SubTitleText from "../../components/SubTitleText";
import styles from "./StyleMain";

// Importa os tipos da navegação para manter o código limpo
type RootStackParamList = {
  Main: undefined;
};

type MainScreenNavigationProp = StackNavigationProp<RootStackParamList, 'Main'>;
type MainScreenRouteProp = RouteProp<RootStackParamList, 'Main'>;

type Props = {
  navigation: MainScreenNavigationProp;
  route: MainScreenRouteProp;
};

const Main: React.FC<NavigationProps<'Main'>> = ({ navigation }) => {
  return (
    <ImageBackground 
        source={require('../../assets/background.jpg')} style={styles.background}
    >
      <View style={styles.container}>
        <Title>Bank Cap</Title>
        <SubTitleText>Seja bem-vindo</SubTitleText>

        <TouchableOpacity style={styles.button} onPress={() => navigation.navigate("Login")}>
          <Image source={require("../../assets/envelope.png")} style={styles.icon} />
          <Text style={styles.text}>Continuar com Email</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.button}>
          <Image source={require("../../assets/google.png")} style={styles.icon} />
          <Text style={styles.text}>Continuar com Google</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.button} onPress={() => navigation.navigate("Register")}>
          <Image source={require("../../assets/lapis.png")} style={styles.icon} />
            <Text style={styles.text}>       Registra-se</Text>
        </TouchableOpacity>
      </View>
    </ImageBackground>
  );
};

export default Main;