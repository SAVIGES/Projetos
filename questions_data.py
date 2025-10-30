import pandas as pd

def load_questions():
    return [
        {
            "pergunta": "Em uma situação complicada, o que você faria?",
            "alternativas": [
                "Analisaria com calma os dados e fatos antes de decidir",
                "Buscaria ajuda de outras pessoas para resolver a questão",
                "Tentaria resolver o problema imediatamente com uma solução prática",
                "Focaria em entender as causas lógicas e estruturadas do problema",
                "Exploraria o contexto social ou histórico para encontrar uma solução"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 2},
                {"Enfermagem": 1, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Ao aprender algo novo, qual é sua abordagem principal?",
            "alternativas": [
                "Estudo os números e padrões para entender melhor",
                "Procuro aplicar o conhecimento ajudando outras pessoas",
                "Tento criar algo funcional com o que aprendi",
                "Foco em resolver problemas teóricos e cálculos complexos",
                "Pesquiso o impacto cultural ou social do tema"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Qual tipo de projeto ou tarefa mais te atrai?",
            "alternativas": [
                "Analisar grandes volumes de dados para tirar conclusões",
                "Trabalhar diretamente com pessoas para melhorar sua saúde ou bem-estar",
                "Desenvolver um aplicativo ou sistema para solucionar um problema",
                "Resolver desafios matemáticos ou científicos complexos",
                "Estudar e debater questões históricas ou sociais"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Diante de um desafio técnico ou emocional, qual é sua reação?",
            "alternativas": [
                "Busco dados e evidências para encontrar a melhor solução",
                "Ofereço suporte e empatia para ajudar quem está envolvido",
                "Tento construir uma ferramenta ou sistema para resolver o problema",
                "Analiso o problema de forma lógica e estruturada",
                "Considero as perspectivas humanas e culturais envolvidas"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Qual atividade do dia a dia mais te interessa?",
            "alternativas": [
                "Explorar estatísticas ou prever tendências com informações",
                "Cuidar de alguém que precisa de ajuda ou orientação",
                "Programar ou ajustar algo em um computador ou dispositivo",
                "Resolver quebra-cabeças ou problemas matemáticos",
                "Ler sobre história, cultura ou questões sociais"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Como você prefere trabalhar em um projeto importante?",
            "alternativas": [
                "Sozinho, analisando dados e informações detalhadamente",
                "Em equipe, ajudando e apoiando os outros diretamente",
                "Colaborando para criar algo funcional, como um sistema ou app",
                "De forma independente, resolvendo problemas teóricos complexos",
                "Em grupo, discutindo ideias e contextos culturais ou sociais"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Qual ferramenta ou método você acha mais interessante?",
            "alternativas": [
                "Softwares de análise de dados e estatísticas",
                "Técnicas de cuidado e procedimentos de saúde",
                "Linguagens de programação e desenvolvimento de software",
                "Fórmulas matemáticas e experimentos científicos",
                "Estudos de textos e análises históricas ou sociais"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Ao cometer um erro ou enfrentar uma falha, o que você faz?",
            "alternativas": [
                "Analiso os dados para entender onde errei e corrigir",
                "Peço feedback de outros e tento melhorar com apoio",
                "Reviso o sistema ou código para encontrar e consertar o problema",
                "Refaço os cálculos ou testes para identificar a falha",
                "Reflito sobre o contexto e as consequências humanas do erro"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Se pudesse escolher um tema para pesquisar ou estudar, qual seria?",
            "alternativas": [
                "Tendências e padrões em grandes bases de dados",
                "Métodos para melhorar a saúde e o bem-estar das pessoas",
                "Novas tecnologias para criar sistemas ou aplicativos",
                "Descobertas científicas ou avanços em matemática",
                "Questões sociais, culturais ou históricas da humanidade"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Como você imagina seu futuro profissional?",
            "alternativas": [
                "Trabalhando com análise de dados para tomar decisões importantes",
                "Ajudando pessoas diretamente em hospitais ou comunidades",
                "Desenvolvendo softwares ou tecnologias inovadoras",
                "Contribuindo para avanços científicos ou de engenharia",
                "Atuando em áreas que promovam justiça social ou cultural"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Em uma crise ou emergência, qual seria sua primeira atitude?",
            "alternativas": [
                "Coletar informações para entender a gravidade da situação",
                "Prestar auxílio imediato a quem precisa de ajuda",
                "Criar uma solução rápida para controlar o problema",
                "Planejar uma resposta lógica com base em fatos técnicos",
                "Avaliar o impacto emocional ou social da crise nas pessoas"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Qual ambiente de trabalho você prefere?",
            "alternativas": [
                "Um escritório com computadores e ferramentas de análise",
                "Um hospital ou clínica, cuidando de pessoas",
                "Um espaço de tecnologia, desenvolvendo sistemas ou apps",
                "Um laboratório ou sala de estudo para pesquisas científicas",
                "Um local de debates ou estudos sobre sociedade e cultura"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Como você lida com pressão ou prazos apertados?",
            "alternativas": [
                "Organizo os dados e priorizo as tarefas mais importantes",
                "Mantenho a calma para apoiar quem depende de mim",
                "Trabalho rapidamente para entregar uma solução funcional",
                "Concentro-me em resolver cada etapa de forma lógica",
                "Penso nas consequências humanas e busco equilíbrio"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Que tipo de problema você gosta de resolver?",
            "alternativas": [
                "Problemas que exigem análise de dados e previsão",
                "Problemas de saúde ou bem-estar de outras pessoas",
                "Problemas técnicos em sistemas ou dispositivos",
                "Problemas teóricos que envolvem lógica ou ciência",
                "Problemas sociais ou culturais que afetam comunidades"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Que tipo de leitura ou estudo mais te atrai?",
            "alternativas": [
                "Artigos sobre estatísticas, tecnologia ou dados",
                "Materiais sobre saúde, cuidados e bem-estar",
                "Tutoriais de programação ou tecnologia",
                "Livros de matemática, física ou ciências exatas",
                "Textos sobre história, sociologia ou filosofia"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Como você prefere passar seu tempo livre?",
            "alternativas": [
                "Explorando novas ferramentas de análise ou tecnologia",
                "Ajudando amigos ou familiares com algo que precisam",
                "Criando pequenos projetos ou programando algo novo",
                "Resolvendo quebra-cabeças ou estudando temas científicos",
                "Lendo sobre culturas, história ou assistindo documentários"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Como você reage a novas tecnologias ou inovações?",
            "alternativas": [
                "Analiso como elas podem melhorar a interpretação de dados",
                "Penso em como podem ajudar no cuidado com as pessoas",
                "Quero aprender a usá-las para criar algo novo",
                "Estudo os princípios científicos por trás delas",
                "Reflito sobre o impacto social ou ético que podem causar"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Que tipo de desafio intelectual você prefere?",
            "alternativas": [
                "Decifrar padrões ou prever resultados com dados",
                "Entender as necessidades de outras pessoas e ajudá-las",
                "Resolver falhas em sistemas ou criar algo funcional",
                "Resolver equações ou problemas científicos complexos",
                "Analisar contextos históricos ou sociais para tirar lições"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Como você prefere se comunicar com os outros?",
            "alternativas": [
                "Usando gráficos ou dados para explicar minhas ideias",
                "De forma empática, ouvindo e oferecendo apoio",
                "Explicando soluções técnicas ou funcionais",
                "Apresentando conceitos lógicos ou científicos",
                "Discutindo ideias e valores humanos ou culturais"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Que tipo de evento ou atividade mais te interessa participar?",
            "alternativas": [
                "Conferências sobre tecnologia de dados ou inovação",
                "Campanhas de saúde ou voluntariado em comunidades",
                "Hackathons ou eventos de programação",
                "Feiras de ciências ou competições matemáticas",
                "Debates ou palestras sobre questões sociais e culturais"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Como você avalia o sucesso de um projeto?",
            "alternativas": [
                "Pela precisão dos dados e resultados obtidos",
                "Pelo impacto positivo na vida das pessoas ajudadas",
                "Pela funcionalidade e eficiência do que foi criado",
                "Pela correção técnica ou científica das soluções",
                "Pelo benefício social ou cultural que gerou"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Que tipo de impacto você gostaria de causar no mundo?",
            "alternativas": [
                "Melhorar decisões com base em dados e análises",
                "Ajudar diretamente na saúde e qualidade de vida das pessoas",
                "Criar tecnologias que facilitem a vida cotidiana",
                "Contribuir para descobertas científicas ou técnicas",
                "Promover mudanças sociais ou culturais positivas"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Como você prefere planejar algo importante?",
            "alternativas": [
                "Usando dados e previsões para antecipar resultados",
                "Considerando as necessidades e o bem-estar de todos envolvidos",
                "Desenvolvendo um sistema ou ferramenta para organizar tudo",
                "Baseando-me em lógica e métodos estruturados",
                "Pensando no impacto humano e nas relações interpessoais"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Que tipo de aprendizado mais te motiva?",
            "alternativas": [
                "Aprender a interpretar e usar grandes quantidades de dados",
                "Aprender técnicas para ajudar e cuidar de outras pessoas",
                "Aprender a programar ou construir sistemas digitais",
                "Aprender sobre teorias científicas e cálculos avançados",
                "Aprender sobre a história e o comportamento humano"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Como você define uma boa liderança?",
            "alternativas": [
                "Tomar decisões baseadas em dados e análises sólidas",
                "Cuidar da equipe e garantir o bem-estar de todos",
                "Guiar a equipe na criação de soluções práticas e inovadoras",
                "Resolver problemas complexos com lógica e precisão",
                "Inspirar com valores humanos e compreensão cultural"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
    ]

def ask_questions(questions):
    scores = {}
    for q in questions:
        print("\n" + q["pergunta"])
        for i, alt in enumerate(q["alternativas"], start=1):
            print(f"  {i}. {alt}")
        while True:
            escolha = input("Escolha uma opção (número): ").strip()
            if not escolha.isdigit():
                print("Entrada inválida. Digite o número da opção.")
                continue
            idx = int(escolha) - 1
            if 0 <= idx < len(q["alternativas"]):
                pesos = q["pesos"][idx]
                for materia, peso in pesos.items():
                    scores[materia] = scores.get(materia, 0) + peso
                break
            else:
                print("Opção fora do intervalo. Tente novamente.")
    return scores

def show_results(scores):
    df = pd.DataFrame(list(scores.items()), columns=["Curso/Area", "Score"])
    df = df.sort_values("Score", ascending=False).reset_index(drop=True)
    print("\nResultados (ordenados):")
    print(df.to_string(index=False))
    
    if not df.empty:
        curso_maior_pontuacao = df.iloc[0]["Curso/Area"]
        pontuacao = df.iloc[0]["Score"]
        print(f"\n**Recomendação**: Com base nas suas respostas, você parece ter maior afinidade com **{curso_maior_pontuacao}** (Pontuação: {pontuacao}).")
        print("Isso indica que você pode se sair muito bem nesta área! Explore mais sobre este curso ou itinerário para confirmar seu interesse.")
    else:
        print("\n**Recomendação**: Não foi possível determinar uma área de maior afinidade. Por favor, tente responder às perguntas novamente.")

def main():
    questions = load_questions()
    scores = ask_questions(questions)
    show_results(scores)

if __name__ == "__main__":
    main()