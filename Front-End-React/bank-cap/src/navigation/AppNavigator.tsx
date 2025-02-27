import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import { NavigationContainer } from '@react-navigation/native';
import Login from '../screens/Login/Login';
import Main from '../screens/Main/Main';
import Register from '../screens/Register/Register';
import Start from '../screens/Start';

import { RootStackParamList } from './types'; // Importa os tipos corretamente

const Stack = createStackNavigator<RootStackParamList>(); // Define os tipos aqui!

export default function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Main" component={Main} options={{ headerShown: false }} />

        <Stack.Screen name="Register" component={Register} options={{ headerShown: false }} />

        <Stack.Screen name="Login" component={Login} options={{ headerShown: false }} />

        <Stack.Screen name="Start" component={Start} options={{ headerShown: false }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
