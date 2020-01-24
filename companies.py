### Normaliza nome das empresas
def norm_banks(bankname):
    ### Limpeza
    name = bankname.upper().replace(' (CONGLOMERADO)','')
    name = name.replace('-','').replace(',','')
    name = name.replace('S.A.','').replace('S A','').replace('S/A','').replace('S.A','')
    name = name.replace('LTDA.','').replace('LTDA','')
    name = name.replace('CRÉDITO FINANCIAMENTO E INVESTIMENTO','').replace('CREDITO FINANCIAMENTO E INVESTIMENTO','').replace('CREDITO FINANCIAMENTO E INVESTIMENTOS','')
    name = name.replace('SOCIEDADE DE','')
    name = name.replace('FINANCIADORA','')
    name = name.strip()
    name = ' '.join(name.split())
    name = name.replace('CRÉDITO FINANCIAMENTO E INVESTIMENTO','').replace('CREDITO FINANCIAMENTO E INVESTIMENTO','').replace('CREDITO FINANCIAMENTO E INVESTIMENTOS','').strip()
    
    ### padronizacao
    if name == 'BB':
        name = 'BANCO DO BRASIL'    
    elif 'VIACREDI' in name:
        name = 'VIACREDI'
    elif 'SICOOB' in name:
        name = 'SICOOB'
    elif 'SICREDI' in name:
        name = 'SICREDI'
    elif 'UNIPRIME' in name:
        name = 'UNIPRIME' 
    elif 'UNICRED' in name:
        name = 'UNICRED'
    elif 'CRESOL' in name:
        name = 'CRESOL'
    elif 'ASCOOB' in name:
        name = 'ASCOOB'
    elif 'CREDJUST' in name:
        name = 'CREDJUST'
    elif name.startswith('NU '):
        name = 'NUBANK'
    elif 'XP INVESTIMENTOS' in name:
        name = 'XP INVESTIMENTOS'
    elif name.startswith('COOPERATIVA') and name[-2] == '-':
        name = name[-1]
    else:
        name = name.replace('INTERMEDIUM', 'INTER').replace('BANCO INTER','INTER')
        name = name.replace('PANAMERICANO', 'PAN').replace('BANCO PAN', 'PAN')
        name = name.replace('BONSUCESSO', 'BS2').replace('BANCO BS2', 'BS2').replace('GRUPO BS2 BS2','BS2')
        name = name.replace('CAIXA ECONÔMICA FEDERAL', 'CAIXA ECONOMICA FEDERAL')
        name = name.replace('SANTANDER BANESPA', 'SANTANDER')
        name = name.replace('HSBC BANK BRASIL BANCO MULTIPLO', 'HSBC')
        name = name.replace('BANCO DAYCOVAL','DAYCOVAL')
        name = name.replace('BANCO BMG','BMG')
        name = name.replace('BANCO CITIBANK','CITIBANK')
        name = name.replace('BANCO ORIGINAL','ORIGINAL')
        name = name.replace('PAGSEGURO INTERNET','PAGSEGURO')
        name = name.replace('BANCO BMC','BMC')
        name = name.replace('ABCBRASIL','ABC-BRASIL')
        name = name.replace('BANCO BGN','BGN')
        name = name.replace('BANCO TOPÁZIO','BANCO TOPAZIO')
        name = name.replace('NOVO BANCO CONTINENTAL BANCO MÚLTIPLO','NOVO BANCO CONTINENTAL BANCO MULTIPLO')
        name = name.replace('AGIPLAN FINANCEIRA','AGIPLAN')
        name = name.replace('BANIF INTERNACIONAL DO FUNCHAL (BRASIL) EM LIQUIDAÇÃO ORDINÁRIA','BANIF')
        name = name.replace('BANCO DO ESTADO DO PARÁ','BANCO DO ESTADO DO PARA')
        name = name.replace('BANCO DE TOKYO MITSUBISHI UFJ BRASIL','BANCO DE TOKYOMITSUBISHI UFJ BRASIL')
        name = name.replace('BANCO A J RENNER','BANCO RENNER').replace('BANCO A.J. RENNER','BANCO RENNER')
        name = name.replace('BANCO PORTO REAL DE INVESTIMENTO','BANCO PORTO REAL DE INVESTIMENTOS')
        name = name.replace('BANCO BM&FBOVESPA DE SERVIÇOS DE LIQUIDAÇÃO E CUSTÓDIA','BANCO BM&FBOVESPA').replace('BANCO BM FBOVESPA DE SERVICOS DE LIQUIDACAO E CUSTODIA','BANCO BM&FBOVESPA')
        name = name.replace('BANCO ABN AMRO','ABN AMRO')
        name = name.replace('MÚLTIPLA','MULTIPLA')
        name = name.replace('BANCO DIGIO','DIGIO')
        name = name.replace('BANCO NEON','NEON')
        name = name.replace('BCO ITAUBANK','ITAU')
        name = name.replace('BCO DO BRASIL','BANCO DO BRASIL')
        name = name.replace('BCO BRADESCO','BRADESCO')
        name = name.replace('BCO SANTANDER (BRASIL)','SANTANDER')
        name = name.replace('BCO BS2','BS2')
        name = name.replace('BCO C6','C6 BANK')
        
    if name.endswith(' S'):
        name = name[:-2]
    
    return name
