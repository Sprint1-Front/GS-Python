import time

# ===================================================
# 1. ESTRUTURA DE DADOS
# ===================================================
MAPA_DIAGNOSTICO = {
    "SUPORTE TECNICO": {
        "risco": 0.65,
        "foco": ["Inteligência Artificial Aplicada", "Comunicação Empática", "Gestão de Bots"],
        "soft_skills": ["Pensamento Crítico", "Adaptabilidade"]
    },
    "ANALISTA DE DADOS": {
        "risco": 0.20,
        "foco": ["Machine Learning Avançado", "Visualização em Tempo Real"],
        "soft_skills": ["Colaboração Global", "Visão Estratégica"]
    },
    "ASSISTENTE ADMINISTRATIVO": {
        "risco": 0.55,
        "foco": ["Automação de Processos (RPA)", "Análise de Dados Financeiros"],
        "soft_skills": ["Resolução de Problemas", "Liderança"]
    },
    "DESIGNER DE UX/UI": {
        "risco": 0.15,
        "foco": ["Realidade Aumentada (AR/VR)", "Design de Experiências Imersivas"],
        "soft_skills": ["Criatividade", "Pensamento Crítico"]
    },
    "ARQUITETO DE NUVEM": {
        "risco": 0.10,
        "foco": ["Segurança Cibernética", "Computação Quântica"],
        "soft_skills": ["Visão Estratégica", "Gestão de Complexidade"]
    },
    "ESPECIALISTA EM SUSTENTABILIDADE": {
        "risco": 0.05,
        "foco": ["Modelagem Preditiva Climática", "Economia Verde"],
        "soft_skills": ["Negociação", "Liderança e Propósito"]
    }
}

# Listas globais para armazenar estado do usuário
progresso_modulos = []      
modulos_carregados = []     

# ===================================================
# 2. FUNÇÕES
# ===================================================
def classificar_risco(percentual):
    """Classifica o risco de automação com base no percentual."""
    if percentual >= 0.50:
        return "ALTO"
    elif percentual >= 0.25:
        return "MÉDIO"
    else:
        return "BAIXO"


def realizar_diagnostico(prof_usuario):
    """Consulta o dicionário e carrega os módulos recomendados na lista global."""
    global modulos_carregados
    prof_upper = prof_usuario.strip().upper()

    if prof_upper in MAPA_DIAGNOSTICO:
        dados = MAPA_DIAGNOSTICO[prof_upper]
        risco_percentual = dados["risco"]
        nivel_risco = classificar_risco(risco_percentual)

        print("\n" + "="*50)
        print(" RELATÓRIO PREDITIVO DE CARREIRA")
        print(f"Profissão Analisada: {prof_usuario.title()}")
        print(f"Risco de Automação: {nivel_risco} ({risco_percentual*100:.0f}%)")
        print("="*50)

        print("\nTrilhas de RESKILLING Recomendadas (Foco em IA):")
        for i, skill in enumerate(dados["foco"]):
            print(f"  [{i+1}] {skill}")

        print("\nSoft Skills Essenciais:")
        for skill in dados["soft_skills"]:
            print(f"  - {skill}")

        print("\nRetorne ao menu para iniciar o treinamento.")
        
        # Armazena os módulos recomendados na lista global
        modulos_carregados = dados["foco"][:]
        return dados["foco"]
    else:
        print("\nProfissão não encontrada no banco de dados.")
        modulos_carregados = []
        return []


def iniciar_treinamento(modulos_foco):
    """Percorre a lista de módulos e permite marcar como concluído."""
    global progresso_modulos

    if not modulos_foco:
        print("\nSelecione uma profissão primeiro (Opção 1).")
        return

    total_modulos = len(modulos_foco)
    print("\n" + "─"*50)
    print(">>> INICIANDO TREINAMENTO ADAPTATIVO <<<")
    print("─"*50)

    for i, modulo in enumerate(modulos_foco):
        if modulo in progresso_modulos:
            continue 

        print(f"\n[MÓDULO {i+1}/{total_modulos}] Treinando: {modulo}")
        
        while True:
            feedback = input("Marcar como Concluído? (S/N): ").strip().upper()
            if feedback == 'S':
                progresso_modulos.append(modulo)
                print(f"Módulo '{modulo}' registrado como concluído!")
                time.sleep(1)
                break
            elif feedback == 'N':
                print("Módulo adiado. Você pode retornar depois.")
                time.sleep(1)
                return  # Sai do treinamento sem concluir tudo
            else:
                print("Entrada inválida. Digite apenas S ou N.")


def exibir_progresso():
    """Mostra progresso com base nas duas listas: modulos_carregados e progresso_modulos."""
    global progresso_modulos, modulos_carregados

    if not modulos_carregados:
        print("\nPor favor, realize o Diagnóstico de Risco (Opção 1) primeiro.")
        return

    concluidos = len(progresso_modulos)
    alvo = len(modulos_carregados)
    taxa = (concluidos / alvo) * 100 if alvo > 0 else 0

    print("\n" + "═"*50)
    print("          SEU PROGRESSO ATUAL")
    print("═"*50)
    print(f"Módulos Concluídos: {concluidos} de {alvo}")
    print(f"Taxa de Conclusão: {taxa:.0f}%")

    print("\nMódulos Dominados:")
    for modulo in progresso_modulos:
        print(f"  {modulo}")

    if concluidos < alvo:
        faltam = [m for m in modulos_carregados if m not in progresso_modulos]
        print(f"\nFaltam {len(faltam)} módulo(s):")
        for m in faltam:
            print(f"  {m}")
    else:
        print("\nVocê está 100% preparado para o futuro da profissão!")


# ===================================================
# 3. EXECUÇÃO PRINCIPAL
# ===================================================
def main():
    print("="*60)
    print("          TALENTFORGE: SIMULADOR DE RESKILLING          ")
    print("     Prepare-se para o futuro do trabalho com IA       ")
    print("="*60)

    profissoes_disponiveis = list(MAPA_DIAGNOSTICO.keys())

    while True:
        try:
            print("\n--- MENU PRINCIPAL ---")
            print("1. Realizar Diagnóstico de Risco")
            print("2. Iniciar Treinamento Adaptativo")
            print("3. Exibir Progresso")
            print("4. Sair do Programa")

            escolha = input("\nEscolha uma opção (1-4): ").strip()

            if escolha == '1':
                print("\n--- PROFISSÕES DISPONÍVEIS ---")
                for i, prof in enumerate(profissoes_disponiveis):
                    print(f"[{i+1}] {prof.title()}")
                
                num = int(input("\nDigite o número da profissão: ").strip())
                if 1 <= num <= len(profissoes_disponiveis):
                    prof = profissoes_disponiveis[num - 1]
                    realizar_diagnostico(prof)
                else:
                    print("Número inválido. Tente novamente.")

            elif escolha == '2':
                if modulos_carregados:
                    iniciar_treinamento(modulos_carregados)
                else:
                    print("\nPrimeiro, realize o Diagnóstico (Opção 1).")

            elif escolha == '3':
                exibir_progresso()

            elif escolha == '4':
                print("\nEncerrando o TalentForge. Seu futuro está sendo forjado!")
                time.sleep(1.5)
                break

            else:
                print("Opção inválida. Escolha de 1 a 4.")

        except ValueError:
            print("Entrada inválida. Digite apenas números.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

# Inicia o programa

main()