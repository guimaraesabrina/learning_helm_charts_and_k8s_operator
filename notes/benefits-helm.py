# automatização de deploy: 
    # implementar apps no cluster com apenas um comando 
    # ao invés de aplicar cada YAML manualmente 

# gerenciamento de versões: 
    # o helm garante o monitoramento/gerenciamento/controle das versões de apps 
    # facilita o rollback 

# costumização: 
    # com o uso de *templates*, você pode facilmente personalizar os YAMLS para cada ambiente 
    # prod, staging, dev utilizando valores definidos no values.yaml 
    # isso facilita na hora de personalizar diferentes ambientes 

# reutilização de configs: 
    # você pode criar um package helm para um DB MySQL e reutiliza-lo em outros apps sem precisar criar novos yamls

# comunidade ativa 
    # a comunidade helm disponibiliza vários pacotes prontos

# simplificação de rollbacks 
    # é mais fácil fazer rollback com helm 
    # o helm guarda um histórico dos pacotes aplicados anteriormente 

# gerenciamento de dependencias 
    # você pode criar diversas dependências para seus pacotes 


# charts: significado 
    # charts, em termos de helm significa "coleções"
    # um chart é uma coleção de arquivos YAML que descreve um conjunto de resources de K8s