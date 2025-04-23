import React, { useState, useEffect } from "react";
import { View, Text, Alert, StyleSheet, TouchableOpacity } from "react-native";
import Modal from "react-native-modal";
import Title from "../Commom/Title";
import InputText from "../Commom/InputText";
import ButtonTextCenter from "../Commom/ButtonTextCenter";
import ErrorMessage from "../Commom/ErrorMessage";
import { atualizarConta } from "../../services/contaService";

interface Conta {
  id: string;
  nome: string;
  banco: string;
  tipo: "PESSOAL" | "EMPRESARIAL";
}

interface ModalContaEdicaoProps {
  isVisible: boolean;
  onClose: () => void;
  conta: Conta;
  onContaEditada: () => Promise<void>;
  usuarioId: string;
}

const ModalContaEdicao: React.FC<ModalContaEdicaoProps> = ({
  isVisible,
  onClose,
  conta,
  onContaEditada,
  usuarioId,
}) => {
  const [nome, setNome] = useState(conta.nome);
  const [banco, setBanco] = useState(conta.banco);
  const [tipo, setTipo] = useState(conta.tipo);
  const [apiError, setApiError] = useState("");

  useEffect(() => {
    setNome(conta.nome);
    setBanco(conta.banco);
    setTipo(conta.tipo);
  }, [conta]);

  const handleEditar = async () => {
    if (!nome || !banco || !tipo) {
      setApiError("Preencha todos os campos.");
      return;
    }

    try {
        const response = await atualizarConta(conta.id, { nome, banco, tipo, usuario_id: usuarioId,});
        console.log(response);
        console.log(conta.id);

        if (response) {
        setApiError("");
        await onContaEditada();
        onClose();
        } else {
        setApiError("Não foi possível atualizar a conta.");
        }
    } catch (error) {
        const errorMessage =
        typeof error === "string"
            ? error
            : error instanceof Error
            ? error.message
            : "Erro ao conectar com a API.";
        setApiError(errorMessage);
    }
  };

  return (
    <Modal isVisible={isVisible} onBackdropPress={onClose}>
      <View style={styles.modalContainer}>
        <Title>Editar Conta</Title>

        <View style={{ alignSelf: "flex-start", width: "85%" }}>
          <Text style={styles.textSmall}>Nome da Conta:</Text>
        </View>
        <InputText autoCapitalize="none" value={nome} onChangeText={setNome} />

        <View style={{ alignSelf: "flex-start", width: "85%" }}>
          <Text style={styles.textSmall}>Nome do Banco:</Text>
        </View>
        <InputText
          autoCapitalize="none"
          value={banco}
          onChangeText={setBanco}
        />

        <View style={{ alignSelf: "flex-start", width: "85%" }}>
          <Text style={styles.textSmall}>Tipo da Conta:</Text>
        </View>
        <View style={styles.tipoContainer}>
          <TouchableOpacity
            style={[
              styles.button,
              tipo === "PESSOAL" ? styles.buttonActive : {},
            ]}
            onPress={() => setTipo("PESSOAL")}
          >
            <Text style={styles.textButton}>Pessoal</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[
              styles.button,
              tipo === "EMPRESARIAL" ? styles.buttonActive : {},
            ]}
            onPress={() => setTipo("EMPRESARIAL")}
          >
            <Text style={styles.textButton}>Empresarial</Text>
          </TouchableOpacity>
        </View>

        <ErrorMessage message={apiError || ""} />

        <ButtonTextCenter title="Salvar" onPress={handleEditar} />
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
  },
  textSmall: {
    fontSize: 15,
    color: "#FFF",
    fontWeight: "bold",
    textAlign: "left",
    paddingLeft: 28,
    opacity: 0.8,
  },
  tipoContainer: {
    flexDirection: "row",
    justifyContent: "space-around",
    width: "100%",
    marginBottom: 10,
    marginTop: 3,
  },
  button: {
    flex: 1,
    height: 45,
    backgroundColor: "rgb(0, 71, 187)",
    justifyContent: "center",
    alignItems: "center",
    borderRadius: 12,
    marginHorizontal: 23,
    borderWidth: 1,
    borderColor: "#FFF",
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
  },
  buttonActive: {
    backgroundColor: "rgb(0, 51, 150)",
  },
  textButton: {
    fontSize: 16,
    color: "#FFF",
    fontWeight: "bold",
    textAlign: "center",
    opacity: 0.9,
  },
});

export default ModalContaEdicao;
