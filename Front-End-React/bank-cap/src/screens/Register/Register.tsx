import React, { useState } from 'react';
import { 
  View, Text, TextInput, TouchableOpacity, StyleSheet, ImageBackground, Keyboard, TouchableWithoutFeedback 
} from 'react-native';
import { StackNavigationProp } from '@react-navigation/stack';
import { RouteProp } from '@react-navigation/native';
import { API_BASE_URL } from '@env';
import Title from '../../components/Title';
import SubTitleText from '../../components/SubTitleText';
import InputText from '../../components/InputText';
import ErrorMessage from '../../components/ErrorMessage';
import ButtonTextCenter from '../../components/ButtonTextCenter';
import StyleRegister from './StyleRegister';

// Definição dos tipos de navegação
type RootStackParamList = {
  Register: undefined;
  Main: undefined;
  Start: { userId: string };
};

type RegisterScreenNavigationProp = StackNavigationProp<RootStackParamList, 'Register'>;
type RegisterScreenRouteProp = RouteProp<RootStackParamList, 'Register'>;

type Props = {
  navigation: RegisterScreenNavigationProp;
  route: RegisterScreenRouteProp;
};

const Register: React.FC<Props> = ({ navigation }) => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [emailError, setEmailError] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [passwordError, setPasswordError] = useState('');

  const [generalError, setGeneralError] = useState('');

  async function handleRegister() {
    if (password !== confirmPassword) {
      setPasswordError('As senhas não coincidem');
      return;
    }
  
    if (emailError) {
      return;
    }
  
    const userData = {
      nome: name,
      email,
      senha: password,
    };
  
    try {
      const response = await fetch(`${API_BASE_URL}/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userData),
      });
  
      if (!response.ok) {
        const errorData = await response.json();
        setGeneralError(errorData.error || 'Erro ao registrar');
        return;
      }
  
      const data = await response.json();
      console.log('Registro bem-sucedido:', data);
  
      if (data.usuario && data.usuario.id) {
        navigation.navigate('Start', { userId: data.usuario.id.toString() });
      } else {
        console.error('Erro: ID do usuário não encontrado na resposta da API', data);
        setGeneralError('Erro ao processar registro.');
      }
  
    } catch (error) {
      console.error('Erro na requisição:', error);
      setGeneralError('Erro de conexão. Verifique sua internet.');
    }
  }
  
  function validatePasswordMatch(text: string) {
    setConfirmPassword(text);
    if (password && text !== password) {
      setPasswordError('As senhas não coincidem');
    } else {
      setPasswordError('');
    }
  }
  
  function validateEmail(text: string) {
    setEmail(text);
    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(text)) {
      setEmailError('E-mail inválido');
    } else {
      setEmailError('');
    }
  }
  

  return (
    <ImageBackground source={require('../../assets/background.jpg')} style={StyleRegister.background}>
      <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
        <View style={StyleRegister.container}>
          <Title>Bank Cap</Title>
          <SubTitleText>Registra-se</SubTitleText>

          <View style={{ alignSelf: 'flex-start', width: '85%'}}>
            <Text style={StyleRegister.textSmall}>Nome Completo:</Text>
          </View>
          <InputText 
              value={name}
              onChangeText={setName}
            />

          <View style={{ alignSelf: 'flex-start', width: '85%'}}>
          <Text style={StyleRegister.textSmall}>Email:</Text>
          </View>
          <InputText 
              onChangeText={validateEmail}
              keyboardType="email-address"
              autoCapitalize="none"
            />

          <View style={{ alignSelf: 'flex-start', width: '85%'}}>
            <Text style={StyleRegister.textSmall}>Senha:</Text>
          </View>
          <InputText 
              secureTextEntry={true}
              value={password}
              onChangeText={setPassword}
            />

          <View style={{ alignSelf: 'flex-start', width: '85%'}}>
            <Text style={StyleRegister.textSmall}>Confirme Sua Senha:</Text>
          </View>
          <InputText 
              secureTextEntry={true}
              value={confirmPassword}
              onChangeText={validatePasswordMatch}
              placeholderTextColor="#FFF"
            />

          <ErrorMessage message={passwordError} />
          <ErrorMessage message={emailError} />
          <ErrorMessage message={generalError} />

          <ButtonTextCenter title="Criar Conta" onPress={handleRegister} />
        </View>
      </TouchableWithoutFeedback> 
    </ImageBackground>
  );
};

export default Register;