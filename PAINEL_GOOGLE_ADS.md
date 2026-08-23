# 📊 Como Criar seu Painel de Controle Unificado (Com Contas Separadas)

Como suas 5 contas estão em emails separados, temos um "problema" comum no mundo dos afiliados: se você der acesso de todas as contas para um único email administrador, o Google pode criar um **"Rastro" (Footprint)**. Se uma conta cair por suspensão, ele pode derrubar as outras por tabela.

Para resolver isso, você tem dois caminhos: o **Caminho Ninja (Anti-Bloqueio)** e o **Caminho Padrão (Fácil, mas deixa rastro)**.

---

## 🥷 Caminho 1: O Método Ninja (Google Ads Scripts + Planilha + Looker Studio) -> *Recomendado para Afiliados*

Neste método, as contas não se tocam. Nós usamos um robô interno do Google Ads (um Script) em cada conta para "empurrar" os dados para uma planilha secreta.

1.  **Crie uma Planilha do Google (Google Sheets):**
    *   Crie uma planilha em branco usando um email "limpo".
    *   Clique em "Compartilhar" e coloque "Qualquer pessoa com o link pode Editar" (isso evita que você precise logar os emails lá).
    *   Copie a URL da planilha.
2.  **Rode o Script em Cada Conta do Google Ads:**
    *   Entre na Conta 1 do Google Ads.
    *   No menu lateral esquerdo, vá em **Ferramentas** > **Ações em massa** > **Scripts** (se estiver no layout novo) ou **Ferramentas e Configurações** > **Ações em Massa** > **Scripts** (no antigo).
    *   Crie um script novo e cole o código abaixo.
    *   Substitua o link da planilha no código.
    *   Agende para rodar a cada hora (De hora em hora).
    *   Repita esse processo colando o mesmo script na Conta 2, 3, 4 e 5.
3.  **Ligue no Looker Studio:**
    *   Agora você tem uma única planilha recebendo os cliques, custo e conversões de todas as 5 contas, sem que uma conta saiba da existência da outra.
    *   Basta conectar essa Planilha no **Looker Studio** para criar seus gráficos visuais.

### 📜 Código do Script (Copiar e Colar)
```javascript
// CONFIGURAÇÃO: Insira o URL da sua Planilha do Google aqui
var PLANILHA_URL = 'https://docs.google.com/spreadsheets/d/1uPLYRDRydkUeoNodP8GOZM_xvAw0LBXJaYTsWxY0tEo/edit';
var NOME_DA_ABA = 'GestaoAfiliado'; // Nome da aba na planilha

function main() {
  var spreadsheet = SpreadsheetApp.openByUrl(PLANILHA_URL);
  var sheet = spreadsheet.getSheetByName(NOME_DA_ABA);
  
  // Se a aba não tiver cabeçalho, nós criamos na primeira vez
  if (sheet.getLastRow() == 0) {
    sheet.appendRow(['Data', 'Nome da Conta', 'ID da Conta', 'Campanha', 'Orcamento', 'Target CPA', 'Impressoes', 'Cliques', 'Custo', 'Conversoes', 'CPA Real', 'CPC', '% Topo', '% 1a Posicao']);
  }
  
  var dataHoje = Utilities.formatDate(new Date(), AdWordsApp.currentAccount().getTimeZone(), 'yyyy-MM-dd');
  var nomeConta = AdWordsApp.currentAccount().getName();
  var idConta = AdWordsApp.currentAccount().getCustomerId();
  
  // Puxa os dados das campanhas que estão ativas com dados DESTE MÊS
  var query = 'SELECT segments.date, campaign.name, campaign_budget.amount_micros, campaign.target_cpa.target_cpa_micros, ' +
              'metrics.impressions, metrics.clicks, metrics.cost_micros, ' +
              'metrics.conversions, metrics.cost_per_conversion, metrics.average_cpc, ' +
              'metrics.search_top_impression_share, metrics.search_absolute_top_impression_share ' +
              'FROM campaign WHERE campaign.status = "ENABLED" AND segments.date DURING THIS_MONTH';
              
  var report = AdsApp.report(query);
  var rows = report.rows();
  
  while (rows.hasNext()) {
    var row = rows.next();
    
    // Converte de Micros para Real
    var orcamento = row['campaign_budget.amount_micros'] ? row['campaign_budget.amount_micros'] / 1000000 : 0;
    var targetCpa = row['campaign.target_cpa.target_cpa_micros'] ? row['campaign.target_cpa.target_cpa_micros'] / 1000000 : 0;
    
    var custo = row['metrics.cost_micros'] ? row['metrics.cost_micros'] / 1000000 : 0;
    var cpaReal = row['metrics.cost_per_conversion'] ? row['metrics.cost_per_conversion'] / 1000000 : 0;
    var cpc = row['metrics.average_cpc'] ? row['metrics.average_cpc'] / 1000000 : 0;
    
    // Tratamento das métricas de leilão
    var posTopo = row['metrics.search_top_impression_share'] ? row['metrics.search_top_impression_share'] : 0;
    var posAbsTopo = row['metrics.search_absolute_top_impression_share'] ? row['metrics.search_absolute_top_impression_share'] : 0;
    
    sheet.appendRow([
      row['segments.date'],
      nomeConta,
      idConta,
      row['campaign.name'],
      orcamento,
      targetCpa,
      row['metrics.impressions'],
      row['metrics.clicks'],
      custo,
      row['metrics.conversions'],
      cpaReal,
      cpc,
      posTopo,
      posAbsTopo
    ]);
  }
  
  Logger.log('Dados da conta ' + nomeConta + ' enviados com sucesso!');
}
```

---

## 🔗 Caminho 2: O Método Padrão (Fácil, porém deixa rastro entre as contas)

Se você não se importa de vincular os emails (suas contas são super brancas e não têm risco de bloqueio em cadeia):

1.  Escolha um Email como **"Mestre"**.
2.  Entre em cada um dos 5 emails do Google Ads, vá em Ferramentas > Acesso e Segurança.
3.  Convide o seu Email Mestre com permissão de **"Somente Leitura"**.
4.  Aceite os convites.
5.  Abra o **Looker Studio** com o Email Mestre. Quando você for adicionar a fonte de dados "Google Ads", todas as 5 contas vão aparecer na lista para você selecionar e construir seu painel!
