import { StyleSheet } from 'react-native';

const StyleStart = StyleSheet.create({
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
    saldoContainer: {
      marginTop: 0, // Ajuste para ficar logo abaixo do título
      alignItems: "center", // Centraliza os textos horizontalmente
    },
  
    row: {
      flexDirection: "row", // Deixa os textos lado a lado
      alignItems: "center", // Centraliza no eixo vertical
      justifyContent: "space-between", // Aumenta o espaço entre os textos
      width: "80%", // Define uma largura para espaçamento melhor
    },
    text: {
      color: '#fff', 
      fontSize: 20,
      fontWeight: 'bold',
      textAlign: 'left',
      marginTop: 5,
    },
  });

  export default StyleStart;