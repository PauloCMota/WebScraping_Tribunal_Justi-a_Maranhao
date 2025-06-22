from tribunais import pje
import datetime

def main():
    data_consulta = input("Digite a data para consulta (YYYY-MM-DD) [hoje]: ") or datetime.date.today().strftime("%Y-%m-%d")
    prazos = []
    # Exemplo apenas para TJMA
    prazos += pje.acessar_expediente("PJE_TJMA", data_consulta)
    # Repita para outros tribunais/sistemas (TRF1, TJPA, etc.)
    for p in prazos:
        print(f"Processo: {p['processo']}, Prazo: {p['prazo']}, Descrição: {p['descricao']}")

if __name__ == "__main__":
    main()