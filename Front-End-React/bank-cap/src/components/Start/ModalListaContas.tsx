import React, { useState } from "react";
import { View, Text, StyleSheet, TouchableOpacity, ScrollView } from "react-native";
import Modal from "react-native-modal"; 
import ButtonTextCenter from "../../components/Commom/ButtonTextCenter"; 
import ModalConta from "../../components/Start/ModalConta"; 

interface Conta {
  id: number;
  nome: string;
  banco: string;
}

interface ModalListaContasProps {
  isVisible: boolean;
  onClose: () => void;
  contas: Conta[];
  usuario_id: string; // Passando o ID do usuário
}

const ModalListaContas: React.FC<ModalListaContasProps> = ({
  isVisible,
  onClose,
  contas,
  usuario_id,  // Recebendo o ID do usuário
}) => {
  const [modalVisible, setModalVisible] = useState(false);  // Estado do modal

  return (
    <Modal isVisible={isVisible} onBackdropPress={onClose}>
      <View style={styles.modalContainer}>
        <Text style={styles.title}>Minhas Contas</Text>

        <ScrollView style={{ width: "100%" }}>
          {contas.map((conta) => (
            <View key={conta.id} style={styles.contaContainer}>
              <TouchableOpacity style={styles.contaButton}>
                <Text style={styles.contaTexto}>{conta.nome} | {conta.banco}</Text>
              </TouchableOpacity>

              <TouchableOpacity style={styles.acaoBotao}>
                <Text style={styles.acaoTexto}>✏️</Text>
              </TouchableOpacity>

              <TouchableOpacity style={styles.acaoBotao}>
                <Text style={styles.acaoTexto}>🗑️</Text>
              </TouchableOpacity>
            </View>
          ))}

          {/* Botão para abrir o ModalConta */}
          <ButtonTextCenter title="Suas Contas" onPress={() => setModalVisible(true)} />

          {/* ModalConta passando o usuario_id */}
          <ModalConta
            isVisible={modalVisible}
            onClose={() => setModalVisible(false)}
            usuario_id={usuario_id}
          />
        </ScrollView>
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  modalContainer: {
    backgroundColor: "rgb(17, 13, 13)",
    padding: 20,
    borderRadius: 10,
    alignItems: "center",
    maxHeight: "80%",
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
    color: "#FFF",
    marginBottom: 15,
  },
  contaContainer: {
    flexDirection: "row",
    alignItems: "center",
    marginBottom: 10,
    width: "100%",
  },
  contaButton: {
    flex: 1,
    backgroundColor: "rgb(0, 71, 187)",
    padding: 10,
    borderRadius: 10,
    justifyContent: "center",
    marginRight: 10,
  },
  contaTexto: {
    color: "#FFF",
    fontSize: 16,
    fontWeight: "bold",
  },
  acaoBotao: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: "#333",
    justifyContent: "center",
    alignItems: "center",
    marginLeft: 5,
  },
  acaoTexto: {
    color: "#FFF",
    fontSize: 16,
  },
});

export default ModalListaContas;


