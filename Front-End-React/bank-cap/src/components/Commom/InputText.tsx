import React from "react";
import { TextInput, StyleSheet, TextInputProps } from "react-native";

interface InputTextProps extends TextInputProps {}

const InputText: React.FC<InputTextProps> = ({ style, onChangeText, ...rest }) => {
  return <TextInput style={[styles.input, style]} onChangeText={onChangeText} {...rest} />;
};

const styles = StyleSheet.create({
  input: {
    width: '85%',
    height: 50,
    backgroundColor: 'rgb(0, 71, 187)', // Tom mais claro para diferenciar
    borderRadius: 12,
    marginTop: 2,
    marginBottom: 10,
    paddingHorizontal: 20,
    fontSize: 15, 
    color: '#FFF', 
    fontWeight: 'bold',
    textAlign: 'left',
    borderWidth: 0.9, 
    borderColor: '#FFF', // Borda branca para destacar
    opacity: 0.9,
  },
});

export default InputText;
