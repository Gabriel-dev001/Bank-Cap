import React, { useState, useEffect } from "react";
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
} from "react-native";
import Modal from "react-native-modal";

import ButtonTextCenter from "../../../components/Commom/ButtonTextCenter";
import ModalConta from "../Modals/ModalConta";
import ModalContaEdicao from "../Modals/ModalContaEdicao";
import { buscarContasDoUsuario, deletarConta } from "../../../services/contaService";

interface Conta {
  id: string;
  nome: string;
  banco: string;
  tipo: "PESSOAL" | "EMPRESARIAL";
}

interface ModalListaContasProps {
  isVisible: boolean;
  onClose: () => void;
  contas: Conta[];
  usuario_id: string;
  onSelecionarConta: (contaId: string) => void;
}

const ModalListaContas: React.FC<ModalListaContasProps> = ({
  isVisible,
  onClose,
  contas,
  usuario_id,
  onSelecionarConta,
}) => {
  const [modalCriarVisible, setModalCriarVisible] = useState(false);
  const [modalEditarVisible, setModalEditarVisible] = useState(false);
  const [contasState, setContasState] = useState<Conta[]>(contas);
  const [contaParaEditar, setContaParaEditar] = useState<Conta | undefined>(undefined);

  const carregarContas = async () => {
    const novasContas = await buscarContasDoUsuario(usuario_id);
    setContasState(novasContas);
  };

  useEffect(() => {
    setContasState(contas);
  }, [contas]);

  const handleEditar = (conta: Conta) => {
    setContaParaEditar(conta);
    setModalEditarVisible(true);
  };

  const handleExcluir = async (contaId: string) => {
    await deletarConta(contaId);
    carregarContas();
  };

  const renderContas = () => {
    return contasState.map((conta) => (
      <View key={conta.id} style={styles.contaContainer}>
        <TouchableOpacity
          style={styles.contaButton}
          onPress={() => onSelecionarConta(conta.id)}
        >
          <Text style={styles.contaTexto}>{conta.nome}</Text>
          <Text style={styles.contaTexto}>{conta.banco}</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.acaoBotao}
          onPress={() => handleEditar(conta)}
        >
          <Text style={styles.acaoTexto}>✏️</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.acaoBotao}
          onPress={() => handleExcluir(conta.id)}
        >
          <Text style={styles.acaoTexto}>🗑️</Text>
        </TouchableOpacity>
      </View>
    ));
  };

  return (
    <Modal isVisible={isVisible} onBackdropPress={onClose}>
      <View style={styles.modalContainer}>
        <Text style={styles.title}>Minhas Contas</Text>

        <ScrollView style={styles.scrollContainer}>
          {renderContas()}
          <ButtonTextCenter
            title="Criar Conta"
            onPress={() => setModalCriarVisible(true)}
          />
        </ScrollView>

        {/* Modal para criar nova conta */}
        <ModalConta
          isVisible={modalCriarVisible}
          onClose={() => setModalCriarVisible(false)}
          usuario_id={usuario_id}
          onContaCriada={carregarContas}
        />

        {/* Modal para editar conta */}
        {contaParaEditar && (
          <ModalContaEdicao
            isVisible={modalEditarVisible}
            onClose={() => {
              setModalEditarVisible(false);
              setContaParaEditar(undefined);
            }}
            conta={contaParaEditar}
            onContaEditada={carregarContas}
            usuarioId={usuario_id}
          />
        )}
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
  scrollContainer: {
    width: "100%",
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

