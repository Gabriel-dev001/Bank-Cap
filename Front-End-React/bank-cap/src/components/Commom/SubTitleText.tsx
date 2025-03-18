import React from "react";
import { Text, StyleSheet, TextProps } from "react-native";

interface CustomTextProps extends TextProps {
  children: React.ReactNode;
}

const SubTitleText: React.FC<CustomTextProps> = ({ children, style, ...rest }) => {
  return <Text style={[styles.text, style]} {...rest}>{children}</Text>;
};

const styles = StyleSheet.create({
  text: {
    fontSize: 15,
    color: "#FFF",
    fontWeight: "bold",
    textAlign: "center",
    opacity: 0.8,
  },
});

export default SubTitleText;
