import React, { useState } from "react";
import {
  View,
  Text,
  StyleSheet,
  Pressable,
  TouchableWithoutFeedback,
  Keyboard,
  TouchableOpacity,
  Alert,
} from "react-native";
import Modal from "react-native-modal";
import { MaskedTextInput } from "react-native-mask-text";
import InputText from "../../Commom/InputText";
import ButtonTextCenter from "../../Commom/ButtonTextCenter";
import ErrorMessage from "../../Commom/ErrorMessage";
import DateTimePickerModal from "react-native-modal-datetime-picker";
import DropDownPicker from "react-native-dropdown-picker";
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
  const [valorRaw, setValorRaw] = useState("");
  const [data, setData] = useState("");
  const [descricao, setDescricao] = useState("");
  const [apiError, setApiError] = useState("");
  const [isDatePickerVisible, setDatePickerVisibility] = useState(false);

  // Select
  const [open, setOpen] = useState(false);
  const [categoria, setCategoria] = useState<string>("");
  const [items, setItems] = useState([
    { label: "Salário", value: "SALARIO" },
    { label: "Renda Extra", value: "RENDA EXTRA" },
    { label: "Vendas exporádicas", value: "VENDAS" },
    { label: "Presente", value: "PRESENTE" },
  ]);

  const formatCurrency = (text: string) => {
    const cleaned = text.replace(/\D/g, ""); // remove tudo que não for número
    const floatValue = (parseInt(cleaned || "0", 10) / 100).toFixed(2);
    return `R$ ${floatValue.replace(".", ",")}`;
  };

  const handleChange = (text: string, rawText: string) => {
    const cleaned = rawText.replace(/\D/g, ""); 
    const floatValue = parseFloat(cleaned) / 100; 
    const formatted = formatCurrency(rawText);
  
    setValor(formatted); 
    setValorRaw(rawText); 
  };

  const showDatePicker = () => {
    setDatePickerVisibility(true);
  };

  const hideDatePicker = () => {
    setDatePickerVisibility(false);
  };

  const handleConfirm = (date: Date) => {
    setData(moment(date).format("YYYY-MM-DD"));
    hideDatePicker();
  };

  const handleCadastro = async () => {
    if (!descricao || !valorRaw || !data || !categoria) {
      setApiError("Preencha todos os campos");
      return;
    }

    if (isNaN(parseFloat(valorRaw)) || !valorRaw) {
      setApiError("Valor inválido.");
      return;
    }

    try {
      const response = await cadastrarReceitaApi(
        conta_id,
        parseFloat((parseInt(valorRaw || "0", 10) / 100).toFixed(2)),
        data,
        categoria,
        descricao
      );
      if (response) {
        setApiError("");
        setValor("");
        setData("");
        setCategoria("");
        setDescricao("");
        onClose();
        onReceitaCriada();
      } else {
        Alert.alert("Erro", "Não foi possível cadastrar a receita.");
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
      <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
        <View style={styles.modalContainer}>
          <Text style={styles.title}>Cadastrar Receita</Text>

          {/* Estou com bug aqui */}
          <InputLabel label="Valor (R$):" />

          <MaskedTextInput
            type="currency"
            options={{
              prefix: "R$ ",
              decimalSeparator: ",",
              groupSeparator: ".",
              precision: 2,
            }}
            keyboardType="numeric"
            value={valor}
            onChangeText={handleChange}
            placeholder="0,00"
            style={styles.inputValor}
          />

          <InputLabel label="Data:" />
          <TouchableOpacity onPress={showDatePicker} style={{ width: "100%" }}>
            <InputText
              value={data}
              editable={false}
              style={{ marginLeft: 20 }}
            />
          </TouchableOpacity>

          <InputLabel label="Categoria:" />
          <DropDownPicker
            open={open}
            value={categoria}
            items={items}
            setOpen={setOpen}
            setValue={setCategoria}
            setItems={setItems}
            placeholder="Selecione uma categoria"
            style={styles.input}
            placeholderStyle={styles.placeholder}
            dropDownContainerStyle={styles.dropDownContainerStyle}
            textStyle={styles.placeholder}
          />

          <InputLabel label="Descrição:" />
          <InputText value={descricao} onChangeText={setDescricao} />

          <ErrorMessage message={apiError || ""} />
          <ButtonTextCenter title="Cadastrar" onPress={handleCadastro} />
        </View>
      </TouchableWithoutFeedback>

      {/* Modal de seleção de data */}
      <DateTimePickerModal
        isVisible={isDatePickerVisible}
        mode="date"
        onConfirm={handleConfirm}
        onCancel={hideDatePicker}
        themeVariant="light"
        cancelTextIOS="Cancelar"
        confirmTextIOS="Confirmar"
        date={new Date()}
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
  input: {
    marginLeft: 20,
    width: "85%",
    height: 50,
    backgroundColor: "rgb(0, 71, 187)", // Azul claro
    borderRadius: 12,
    marginTop: 2,
    marginBottom: 10,
    paddingHorizontal: 20,
    fontSize: 15,
    color: "#FFF",
    fontWeight: "bold",
    textAlign: "left",
    borderWidth: 0.9,
    borderColor: "#FFF",
    opacity: 0.9,
  },
  inputValor: {
    width: "85%",
    height: 50,
    backgroundColor: "rgb(0, 71, 187)", // Azul claro
    borderRadius: 12,
    marginTop: 2,
    marginBottom: 10,
    paddingHorizontal: 20,
    fontSize: 15,
    color: "#FFF",
    fontWeight: "bold",
    textAlign: "left",
    borderWidth: 0.9,
    borderColor: "#FFF",
    opacity: 0.9,
  },
  dropDownContainerStyle: {
    backgroundColor: "rgb(0, 71, 187)",
    borderColor: "#FFF",
  },
  placeholder: {
    fontSize: 12,
    color: "#FFF",
    fontWeight: "bold",
    textAlign: "left",
    opacity: 0.8,
  },
  contaContainer: {
    flexDirection: "row",
    alignItems: "center",
    marginBottom: 10,
    width: "100%",
  },
});

export default ModalReceitaCadastro;
