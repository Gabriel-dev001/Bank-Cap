import React from "react";
import { View, Text, TouchableOpacity, StyleSheet, Dimensions, Image } from "react-native";

const TopBar = ({ title }: { title: string }) => {
    return (
      <View style={styles.container}>
          <Text style={styles.text}>{title}</Text>
          
          <TouchableOpacity style={styles.button} onPress={() => console.log("Botão clicado!")}>
            <Image source={require("../assets/user.png")} style={styles.icon} />
          </TouchableOpacity>
      </View>
    );
  };
  
  const styles = StyleSheet.create({
    container: {
      position: "absolute",
      top: 50,
      left: 0, 
      right: 0,
      width: Dimensions.get("window").width,    
      height: 60,
      flexDirection: "row",
      alignItems: "center",
      justifyContent: "space-between",
      paddingHorizontal: 20,
      zIndex: 1000, 
    },
    text: {
      left: 25,
      flex: 1,
      fontSize: 22,
      fontWeight: "bold",
      color: "#fff",
      textAlign: "center",
    },
    button: {
      width: 50, 
      height: 50,
      alignItems: "center",
      justifyContent: "center",
    },
    icon: {
      width: 200,
      height: 40,
      resizeMode: "contain",
    },
  });
  
  export default TopBar;