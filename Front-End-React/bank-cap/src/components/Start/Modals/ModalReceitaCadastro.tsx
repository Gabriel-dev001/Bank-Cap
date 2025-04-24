import React, { useState } from "react";
import { View, Text, StyleSheet, TouchableOpacity } from "react-native";
import Modal from "react-native-modal";
import InputText from "../../Commom/InputText";
import ButtonTextCenter from "../../Commom/ButtonTextCenter";
import ErrorMessage from "../../Commom/ErrorMessage";
import DateTimePickerModal from "react-native-modal-datetime-picker";
import moment from "moment"; 
import { cadastrarReceitaApi } from "../../../services/receitaService";

interface ModalReceitaCadastroProps {
  isVisible: boolean;
  onClose: () => void;
  conta_id: string;
  onReceitaCriada: () => void;
}

const ModalReceitaCadastro: React.FC<ModalReceitaCadastroProps> = ({
  isVisible,
  onClose,
  conta_id,
  onReceitaCriada,
}) => {
  const [valor, setValor] = useState("");
  const [data, setData] = useState("");
  const [categoria, setCategoria] = useState("");
  const [descricao, setDescricao] = useState("");
  const [apiError, setApiError] = useState("");
  const [isDatePickerVisible, setDatePickerVisibility] = useState(false);

  const showDatePicker = () => {
    setDatePickerVisibility(true); // Exibe o modal do DateTimePicker
  };

  const hideDatePicker = () => {
    setDatePickerVisibility(false); // Oculta o modal do DateTimePicker
  };

  const handleConfirm = (date: Date) => {
    setData(moment(date).format("DD-MM-YYYY")); // Formata a data no formato DD-MM-YYYY
    hideDatePicker();
  };

  const handleCadastro = async () => {
    if (!valor || !data || !categoria || !descricao) {
      setApiError("Preencha todos os campos");
      return;
    }

    try {
      // Faça a chamada para a API aqui
      // const response = await cadastrarReceitaApi({
      //   conta_id,
      //   valor: parseFloat(valor),
      //   data,
      //   categoria,
      //   descricao,
      // });

      // if (response) {
      //   setApiError("");
      //   setValor("");
      //   setData("");
      //   setCategoria("");
      //   setDescricao("");
      //   onClose();
      //   onReceitaCriada();
      // } else {
      //   Alert.alert("Erro", "Não foi possível cadastrar a receita.");
      // }
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
        <Text style={styles.title}>Cadastrar Receita</Text>

        <InputLabel label="Valor (R$):" />
        <InputText
          keyboardType="numeric"
          value={valor}
          onChangeText={setValor}
        />

        <InputLabel label="Data (DD-MM-YYYY):" />
        <TouchableOpacity onPress={showDatePicker}>
          <InputText
            value={data}
            editable={false} // Desativa a edição manual
          />
        </TouchableOpacity>

        <InputLabel label="Categoria:" />
        <InputText value={categoria} onChangeText={setCategoria} />

        <InputLabel label="Descrição:" />
        <InputText value={descricao} onChangeText={setDescricao} />

        <ErrorMessage message={apiError || ""} />
        <ButtonTextCenter title="Cadastrar" onPress={handleCadastro} />
      </View>

      {/* Modal de seleção de data */}
      <DateTimePickerModal
        isVisible={isDatePickerVisible}
        mode="date"
        onConfirm={handleConfirm}
        onCancel={hideDatePicker}
      />
    </Modal>
  );
};

const InputLabel = ({ label }: { label: string }) => (
  <View style={{ alignSelf: "flex-start", width: "85%" }}>
    <Text style={styles.textSmall}>{label}</Text>
  </View>
);

const styles = StyleSheet.create({
  title: {
    fontSize: 20,
    fontWeight: "bold",
    color: "#FFF",
    marginBottom: 15,
  },
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
    marginTop: 8,
  },
});

export default ModalReceitaCadastro;
