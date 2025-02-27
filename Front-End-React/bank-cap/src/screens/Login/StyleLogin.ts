import { StyleSheet } from 'react-native';

const StyleLogin = StyleSheet.create({
  background: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  container: {
    width: '90%',
    alignItems: 'center',
  },
  textSmall: {
    fontSize: 15,
    color: '#FFF',
    fontWeight: 'bold',
    textAlign: 'left',
    paddingLeft: 28,
    opacity: 0.8,
  },
  linkText: {
    fontSize: 13,
    color: '#FFF',
    fontWeight: 'bold',
    marginTop: 15,
    textDecorationLine: 'underline',
    opacity: 0.8,
  },
  errorText: {
    color: 'red',
    fontSize: 14,
    marginTop: 5,
  },
});

export default StyleLogin;
