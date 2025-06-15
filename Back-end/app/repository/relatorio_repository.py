from app.models.despesa_model import Despesa
from app.models.receita_model import Receita
from app.models.conta_model import Conta
from sqlalchemy import and_
from app import db
from datetime import datetime

def formatar_dinheiro(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatar_data(data):
    if isinstance(data, str):
        data = datetime.strptime(data, "%Y-%m-%d").date()
    return data.strftime("%d/%m/%Y") if data else None

class RelatorioRepository:
    @staticmethod
    def extrato_conta(data_inicial, data_final, conta_id):
        # Converte datas se necessário
        if isinstance(data_inicial, str):
            data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d").date()
        if isinstance(data_final, str):
            data_final = datetime.strptime(data_final, "%Y-%m-%d").date()

        receitas = Receita.query.filter(
            Receita.conta_id == conta_id,
            Receita.data >= data_inicial,
            Receita.data <= data_final
        ).all()

        despesas = Despesa.query.filter(
            Despesa.conta_id == conta_id,
            Despesa.data >= data_inicial,
            Despesa.data <= data_final
        ).all()

        extrato = []

        for receita in receitas:
            extrato.append({
                "data": formatar_data(receita.data),
                "tipo": "ENTRADA",
                "valor": formatar_dinheiro(float(receita.valor)),
                "categoria": receita.categoria,
                "descricao": receita.descricao
            })

        for despesa in despesas:
            extrato.append({
                "data": formatar_data(despesa.data),
                "tipo": "SAIDA",
                "valor": formatar_dinheiro(float(despesa.valor)),
                "categoria": despesa.categoria,
                "descricao": despesa.descricao
            })

        extrato.sort(key=lambda x: datetime.strptime(x["data"], "%d/%m/%Y") if x["data"] else datetime.min)

        return {"relatorio": extrato}

    @staticmethod
    def relatorio_gastos(data_inicial, data_final, conta_id):
        if isinstance(data_inicial, str):
            data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d").date()
        if isinstance(data_final, str):
            data_final = datetime.strptime(data_final, "%Y-%m-%d").date()

        resultados = (
            db.session.query(
                Despesa.categoria,
                db.func.sum(Despesa.valor).label("total")
            )
            .filter(
                Despesa.conta_id == conta_id,
                Despesa.data >= data_inicial,
                Despesa.data <= data_final
            )
            .group_by(Despesa.categoria)
            .all()
        )

        total_geral = sum([float(r.total) for r in resultados])

        relatorio = [
            {"categoria": r.categoria, "total": formatar_dinheiro(float(r.total))}
            for r in resultados
        ]

        relatorio.append({"categoria": "TOTAL GERAL", "total": formatar_dinheiro(total_geral)})

        return {"relatorio": relatorio}

    @staticmethod
    def relatorio_ganhos(data_inicial, data_final, conta_id):
        if isinstance(data_inicial, str):
            data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d").date()
        if isinstance(data_final, str):
            data_final = datetime.strptime(data_final, "%Y-%m-%d").date()

        resultados = (
            db.session.query(
                Receita.categoria,
                db.func.sum(Receita.valor).label("total")
            )
            .filter(
                Receita.conta_id == conta_id,
                Receita.data >= data_inicial,
                Receita.data <= data_final
            )
            .group_by(Receita.categoria)
            .all()
        )

        total_geral = sum([float(r.total) for r in resultados])

        relatorio = [
            {"categoria": r.categoria, "total": formatar_dinheiro(float(r.total))}
            for r in resultados
        ]

        relatorio.append({"categoria": "TOTAL GERAL", "total": formatar_dinheiro(total_geral)})

        return {"relatorio": relatorio}
    
    @staticmethod
    def extrato_geral(data_inicial, data_final, conta_id):
        if isinstance(data_inicial, str):
            data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d").date()
        if isinstance(data_final, str):
            data_final = datetime.strptime(data_final, "%Y-%m-%d").date()

        conta = Conta.query.filter_by(id=conta_id).first()
        if not conta:
            return {"erro": "Conta não encontrada"}

        usuario_id = conta.usuario_id

        contas_usuario = Conta.query.filter_by(usuario_id=usuario_id).all()
        contas_ids = [c.id for c in contas_usuario]

        receitas = (
            db.session.query(
                Receita.categoria,
                db.func.sum(Receita.valor).label("total")
            )
            .filter(
                Receita.conta_id.in_(contas_ids),
                Receita.data >= data_inicial,
                Receita.data <= data_final
            )
            .group_by(Receita.categoria)
            .all()
        )

        despesas = (
            db.session.query(
                Despesa.categoria,
                db.func.sum(Despesa.valor).label("total")
            )
            .filter(
                Despesa.conta_id.in_(contas_ids),
                Despesa.data >= data_inicial,
                Despesa.data <= data_final
            )
            .group_by(Despesa.categoria)
            .all()
        )

        resumo = []

        for r in receitas:
            resumo.append({
                "tipo": "ENTRADA",
                "categoria": r.categoria,
                "total": formatar_dinheiro(float(r.total))
            })

        for d in despesas:
            resumo.append({
                "tipo": "SAIDA",
                "categoria": d.categoria,
                "total": formatar_dinheiro(float(d.total))
            })

        total_entradas = sum([float(r.total) for r in receitas])
        total_saidas = sum([float(d.total) for d in despesas])

        resumo.append({"categoria": "TOTAL ENTRADAS", "tipo": formatar_dinheiro(total_entradas)})
        resumo.append({"categoria": "TOTAL SAIDAS", "tipo": formatar_dinheiro(total_saidas)})
        resumo.append({"categoria": "SALDO FINAL", "tipo": formatar_dinheiro(total_entradas - total_saidas)})

        return {"relatorio": resumo}

    @staticmethod
    def relatorio_transacoes_cripto(data_inicial, data_final, conta_id):
        from app.models.cripto_model import Cripto

        if isinstance(data_inicial, str):
            data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d").date()
        if isinstance(data_final, str):
            data_final = datetime.strptime(data_final, "%Y-%m-%d").date()

        transacoes = Cripto.query.filter(
            Cripto.conta_id == conta_id,
            Cripto.criado_em >= data_inicial,
            Cripto.criado_em <= data_final
        ).all()

        relatorio = []
        for t in transacoes:
            relatorio.append({
                "nome": t.nome,
                "valor reais": formatar_dinheiro(float(t.valor_reais)),
                "valor cripto": f"{float(t.valor_cripto):,.8f}".replace(",", "X").replace(".", ",").replace("X", "."),
                "data": formatar_data(t.criado_em)
            })

        total_reais = sum([float(t.valor_reais) for t in transacoes])
        total_cripto = sum([float(t.valor_cripto) for t in transacoes])

        relatorio.append({
            "tipo": "TOTAL",
            "valor reais": formatar_dinheiro(total_reais),
            "valor cripto": f"{total_cripto:,.8f}".replace(",", "X").replace(".", ",").replace("X", ".")
        })

        return {"relatorio": relatorio}