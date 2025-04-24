import React, { useRef, useState } from "react";
import {
  View,
  TouchableOpacity,
  Animated,
  StyleSheet,
  Image,
} from "react-native";
import { AntDesign } from "@expo/vector-icons";
import ModalReceitaCadastro from "../Start/Modals/ModalReceitaCadastro";

type Props = {
  idConta: string; 
};

const FloatingButton = ({ idConta }: Props) => {
  const [expanded, setExpanded] = useState(false);
  const [modalReceitaVisible, setModalReceitaVisible] = useState(false);
  const animation = useRef(new Animated.Value(0)).current;

  const toggleMenu = () => {
    setExpanded(!expanded);
    Animated.timing(animation, {
      toValue: expanded ? 0 : 1,
      duration: 300,
      useNativeDriver: false,
    }).start();
  };

  const button1Style = {
    transform: [
      {
        translateY: animation.interpolate({
          inputRange: [0, 1],
          outputRange: [0, -60],
        }),
      },
      {
        translateX: animation.interpolate({
          inputRange: [0, 1],
          outputRange: [0, -80],
        }),
      },
    ],
  };

  const button2Style = {
    transform: [
      {
        translateY: animation.interpolate({
          inputRange: [0, 1],
          outputRange: [0, -100],
        }),
      },
    ],
  };

  const button3Style = {
    transform: [
      {
        translateY: animation.interpolate({
          inputRange: [0, 1],
          outputRange: [0, -60],
        }),
      },
      {
        translateX: animation.interpolate({
          inputRange: [0, 1],
          outputRange: [0, 80],
        }),
      },
    ],
  };

  return (
    <View style={styles.container}>
      {/* Botão 1 - Receita */}
      <Animated.View style={[styles.subButton, button1Style]}>
        <TouchableOpacity
          style={styles.secondaryButton}
          onPress={() => setModalReceitaVisible(true)}
        >
          <Image
            source={require("../../assets/receita.png")}
            style={styles.icon}
          />
        </TouchableOpacity>
      </Animated.View>

      <ModalReceitaCadastro
        isVisible={modalReceitaVisible}
        onClose={() => setModalReceitaVisible(false)}
        conta_id={idConta}
        onReceitaCriada={() => {
          setModalReceitaVisible(false);
        }}
      />

      {/* Botão 2 - Cripto */}
      <Animated.View style={[styles.subButton, button2Style]}>
        <TouchableOpacity style={styles.secondaryButton}>
          <Image
            source={require("../../assets/cripto.png")}
            style={styles.icon}
          />
        </TouchableOpacity>
      </Animated.View>

      {/* Botão 3 - Despesa */}
      <Animated.View style={[styles.subButton, button3Style]}>
        <TouchableOpacity style={styles.secondaryButton}>
          <Image
            source={require("../../assets/despesa.png")}
            style={styles.icon}
          />
        </TouchableOpacity>
      </Animated.View>

      {/* Botão Principal */}
      <TouchableOpacity style={styles.mainButton} onPress={toggleMenu}>
        <AntDesign name={expanded ? "close" : "plus"} size={30} color="#fff" />
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    position: "absolute",
    top: "85%", // Centraliza verticalmente
    left: "50%",
    transform: [{ translateX: -35 }, { translateY: -35 }],
    alignItems: "center",
  },
  mainButton: {
    width: 80,
    height: 80,
    backgroundColor: "rgb(0, 71, 187)",
    justifyContent: "center",
    alignItems: "center",
    borderRadius: 50,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
  },
  secondaryButton: {
    width: 70,
    height: 70,
    backgroundColor: "rgb(0, 71, 187)",
    justifyContent: "center",
    alignItems: "center",
    borderRadius: 50,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
  },
  subButton: {
    position: "absolute",
  },
  icon: {
    width: 150, // Ajuste conforme necessário
    height: 130,
    resizeMode: "contain",
  },
  buttonText: {
    color: "#fff",
    fontSize: 25,
    fontWeight: "bold",
  },
});

export default FloatingButton;
