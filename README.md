# TalentForge — Simulador de Reskilling Preditivo com IA

![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)
![FIAP](https://img.shields.io/badge/FIAP-Global%20Solution%202025-9C0A2A.svg)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen.svg)

> **Disciplina:** Computational Thinking Using Python  
> **Professor:** Paulo Viniccius Vieira  
> **Turma:** 1TDSPB – 2025  
> **Data da Entrega:** 23/11/2025

### Integrantes
| Nome                          | RM      |
|-------------------------------|---------|
| Andre Sousa Matuda            | 566733  |
| Guilherme Oliveira Feitosa    | 566842  |
| Paulo Henrique Muniz Diedrich | 567618  |

---

## Descrição do Projeto

**TalentForge** é um simulador inteligente de requalificação profissional que ajuda trabalhadores a se prepararem para o futuro do mercado de trabalho, onde a automação e a Inteligência Artificial estão transformando profissões tradicionais.

O sistema oferece:
- Diagnóstico instantâneo do risco de automação da profissão atual
- Recomendações personalizadas de trilhas de capacitação (reskilling)
- Treinamento adaptativo com acompanhamento de progresso em tempo real

**Tudo implementado apenas com estruturas nativas do Python**: dicionários, listas, funções, loops e condicionais — sem bibliotecas externas.

---

## Funcionalidades Implementadas

| Funcionalidade                  | Estrutura Principal                | Descrição |
|----------------------------------|-------------------------------------|---------|
| Diagnóstico de Risco            | Dicionários + `if/elif/else`        | Classifica risco como ALTO, MÉDIO ou BAIXO |
| Iniciar Treinamento Adaptativo  | Listas + `for` + `while` + `append` | Permite marcar módulos como concluídos (S/N) |
| Exibir Progresso                | Listas + `len()` + cálculo de %     | Mostra % de conclusão e módulos pendentes |
| Menu Interativo                 | `while True` + `try/except`         | Interface robusta com tratamento de erros |

---

## Estruturas de Dados Utilizadas

```python
MAPA_DIAGNOSTICO = {                     # Dicionário aninhado (acesso O(1))
    "SUPORTE TECNICO": {
        "risco": 0.65,
        "foco": ["IA Aplicada", "Comunicação Empática", "Gestão de Bots"],
        "soft_skills": ["Pensamento Crítico", "Adaptabilidade"]
    },
    # ... outras profissões
}

modulos_carregados = []   # Lista com módulos recomendados
progresso_modulos = []    # Lista com módulos já concluídos pelo usuário
