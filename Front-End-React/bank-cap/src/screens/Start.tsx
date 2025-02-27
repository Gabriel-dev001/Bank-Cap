import React from 'react';
import { View, Text, ImageBackground, StyleSheet } from 'react-native';
import { StackNavigationProp } from '@react-navigation/stack';
import { RouteProp } from '@react-navigation/native';

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
    <ImageBackground source={require('../assets/background.jpg')} style={styles.background}>
      <View style={styles.container}>
        <Text style={{ color: '#fff', fontSize: 20 }}>Bem-vindo, {userId}, oi</Text>
      </View>
    </ImageBackground>
  );
};

const styles = StyleSheet.create({
  background: {
    flex: 1,
    resizeMode: 'cover',
    justifyContent: 'center',
  },
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default Start;
