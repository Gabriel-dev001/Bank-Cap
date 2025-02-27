import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
  background: {
    flex: 1,
    width: "100%",
    height: "100%",
  },
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
  },
  text: {
    fontSize: 15,
    color: "#FFF",
    fontWeight: "bold",
    textAlign: "center",
    opacity: 0.8,
  },
  button: {
    width: "85%",
    height: 50,
    backgroundColor: "rgb(0, 71, 187)",
    flexDirection: "row",
    alignItems: "center",
    borderRadius: 12,
    marginTop: 10,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
    paddingVertical: 12,
    paddingHorizontal: 20,
  },
  icon: {
    width: 35,
    height: 35,
    marginRight: 15,
  },
});

export default styles;
