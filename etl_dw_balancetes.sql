
-- balancetes_banco_central_dw.empresa

\! echo "Carregando dados tabela empresa..."

INSERT INTO balancetes_banco_central_dw.empresa
SELECT DISTINCT cnpj,nome_instituicao
	FROM balancetes_banco_central.balancete_geral_stg
EXCEPT
SELECT cnpj,empresa
	FROM balancetes_banco_central_dw.empresa
ORDER BY 1;

VACUUM ANALYZE balancetes_banco_central_dw.empresa;

----------------------------------------------------------------------------
-- balancetes_banco_central_dw.data

\! echo "Carregando dados tabela data..."

INSERT INTO balancetes_banco_central_dw.data
SELECT DISTINCT data, date_part('week',data), date_part('month',data), date_part('year',data) 
	FROM balancetes_banco_central.balancete_geral_stg
EXCEPT
SELECT date, semana, mes, ano
	FROM balancetes_banco_central_dw.data
ORDER BY 1;

VACUUM ANALYZE balancetes_banco_central_dw.data;

----------------------------------------------------------------------------

-- balancetes_banco_central_dw.nome_conta


\! echo "Carregando dados tabela nome_conta..."

INSERT INTO balancetes_banco_central_dw.nome_conta(conta,nome_conta)
SELECT DISTINCT conta,nome_conta
	FROM balancetes_banco_central.balancete_geral_stg
EXCEPT
SELECT conta,nome_conta
	FROM balancetes_banco_central_dw.nome_conta;

VACUUM ANALYZE balancetes_banco_central_dw.nome_conta;

----------------------------------------------------------------------------

-- balancetes_banco_central_dw.balancete_geral


\! echo "Carregando dados tabela fato balancete_geral..."

COPY (
SELECT d.date, e.cnpj, n.conta_id, f.saldo
	FROM balancetes_banco_central.balancete_geral_stg f
	JOIN balancetes_banco_central_dw.data d ON d.date=f.data
	JOIN balancetes_banco_central_dw.empresa e ON e.cnpj=f.cnpj
	JOIN balancetes_banco_central_dw.nome_conta n ON n.conta=f.conta AND n.nome_conta=f.nome_conta
) to '/home/ubuntu/dump/balancete_geral.txt';

COPY balancetes_banco_central_dw.balancete_geral FROM '/home/ubuntu/dump/balancete_geral.txt';

VACUUM ANALYZE balancetes_banco_central_dw.balancete_geral;