import { StackNavigationProp } from '@react-navigation/stack';
import { RouteProp } from '@react-navigation/native';

// Define as telas do Stack Navigator
export type RootStackParamList = {
  Login: undefined;
  Main: undefined;
  Register: undefined;
  Start: { userId: string };
};

// Tipos para navegação
export type NavigationProps<T extends keyof RootStackParamList> = {
  navigation: StackNavigationProp<RootStackParamList, T>;
  route: RouteProp<RootStackParamList, T>;
};
