from app.models.despesa_model import Despesa
from app.models.receita_model import Receita
from app.models.conta_model import Conta

from sqlalchemy import and_
from app import db

class RelatorioRepository:
    @staticmethod
    def extrato_conta(data_inicial, data_final, conta_id):
        # Buscar receitas (entradas)
        receitas = Receita.query.filter(
            Receita.conta_id == conta_id,
            Receita.data >= data_inicial,
            Receita.data <= data_final
        ).all()

        # Buscar despesas (saídas)
        despesas = Despesa.query.filter(
            Despesa.conta_id == conta_id,
            Despesa.data >= data_inicial,
            Despesa.data <= data_final
        ).all()

        extrato = []

        for receita in receitas:
            extrato.append({
                "data": receita.data.strftime("%Y-%m-%d"),
                "tipo": "ENTRADA",
                "valor": float(receita.valor),
                "categoria": receita.categoria,
                "descricao": receita.descricao
            })

        for despesa in despesas:
            extrato.append({
                "data": despesa.data.strftime("%Y-%m-%d"),
                "tipo": "SAIDA",
                "valor": float(despesa.valor),
                "categoria": despesa.categoria,
                "descricao": despesa.descricao
            })

        # Ordenar por data
        extrato.sort(key=lambda x: x["data"])

        return {"relatorio": extrato}

    @staticmethod
    def relatorio_gastos(data_inicial, data_final, conta_id):
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
            {"categoria": r.categoria, "total": float(r.total)}
            for r in resultados
        ]

        relatorio.append({"categoria": "TOTAL_GERAL", "total": total_geral})

        return {"relatorio": relatorio}

    @staticmethod
    def relatorio_ganhos(data_inicial, data_final, conta_id):
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
            {"categoria": r.categoria, "total": float(r.total)}
            for r in resultados
        ]

        relatorio.append({"categoria": "TOTAL_GERAL", "total": total_geral})

        return {"relatorio": relatorio}
    
    @staticmethod
    def extrato_geral(data_inicial, data_final, conta_id):
        # Descobre o usuario_id da conta informada
        conta = Conta.query.filter_by(id=conta_id).first()
        if not conta:
            return {"erro": "Conta não encontrada"}

        usuario_id = conta.usuario_id

        # Busca todas as contas do usuário
        contas_usuario = Conta.query.filter_by(usuario_id=usuario_id).all()
        contas_ids = [c.id for c in contas_usuario]

        # Total de receitas (entradas) por categoria para todas as contas do usuário
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

        # Total de despesas (saídas) por categoria para todas as contas do usuário
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
                "total": float(r.total)
            })

        for d in despesas:
            resumo.append({
                "tipo": "SAIDA",
                "categoria": d.categoria,
                "total": float(d.total)
            })

        # Soma total de entradas e saídas
        total_entradas = sum([float(r.total) for r in receitas])
        total_saidas = sum([float(d.total) for d in despesas])

        resumo.append({"tipo": "TOTAL_ENTRADAS", "total": total_entradas})
        resumo.append({"tipo": "TOTAL_SAIDAS", "total": total_saidas})
        resumo.append({"tipo": "SALDO_FINAL", "total": total_entradas - total_saidas})

        return {"relatorio": resumo}

    @staticmethod
    def relatorio_transacoes_cripto(data_inicial, data_final, conta_id):
        from app.models.cripto_model import Cripto

        transacoes = Cripto.query.filter(
            Cripto.conta_id == conta_id,
            Cripto.criado_em >= data_inicial,
            Cripto.criado_em <= data_final
        ).all()

        relatorio = []
        for t in transacoes:
            relatorio.append({
                "id": t.id,
                "conta_id": t.conta_id,
                "nome": t.nome,
                "valor_reais": float(t.valor_reais),
                "valor_cripto": float(t.valor_cripto),
                "criado_em": t.criado_em.strftime("%Y-%m-%d") if t.criado_em else None
            })

        total_reais = sum([float(t.valor_reais) for t in transacoes])
        total_cripto = sum([float(t.valor_cripto) for t in transacoes])

        relatorio.append({
            "tipo": "TOTAL",
            "valor_reais": total_reais,
            "valor_cripto": total_cripto
        })

        return {"relatorio": relatorio} 