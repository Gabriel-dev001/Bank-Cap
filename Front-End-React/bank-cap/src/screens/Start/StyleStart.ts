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
      marginTop: -275
    },
    saldoContainer: {
      marginTop: 0, 
      alignItems: "center", 
    },
    row: {
      flexDirection: "row", 
      alignItems: "center", 
      justifyContent: "space-between", 
      width: "90%", 
      marginBottom: -50,
    },
    textTitlle: {
      color: '#fff', 
      fontSize: 25,
      fontWeight: 'bold',
      textAlign: 'center',
      marginTop: 5,
    },
    text: {
      color: '#fff', 
      fontSize: 20,
      fontWeight: 'bold',
      textAlign: 'center',
      marginTop: 10,
    },
    squareGreen: {
      width: 170,
      height: 100,
      backgroundColor: "rgba(22, 215, 22, 0.65)",
      borderRadius: 10, 
      borderWidth: 1, 
      borderColor: "#FFFFFF", 
      alignSelf: "center",
      justifyContent: "center",
      alignItems: "center",
    },
    squareRed: {
      width: 170,
      height: 100,
      backgroundColor:"rgba(199, 0, 0, 0.9)",
      borderRadius: 10,
      borderWidth: 1, 
      borderColor: "#FFFFFF",
      alignSelf: "center",
      justifyContent: "center",
      alignItems: "center",
    },
    buttonContainer: {
      marginTop: 50, // Espaçamento do botão em relação ao conteúdo acima
    },
  });

  export default StyleStart;