# Portal BioMed — CLAUDE.md

## Visão Geral do Projeto

Blog de saúde e ciência estático (HTML/CSS puro, sem framework nem build system) voltado para o mercado **espanhol**. Todo o conteúdo deve estar em **espanhol de Espanha** (não português, não espanhol latino-americano).

Repositório GitHub: `https://github.com/Uildigital/portalbiomed.git` — branch `main`.

---

## Estrutura de Ficheiros

```
portalbiomed/
├── index.html               ← Homepage (magazine layout)
├── assets/
│   └── css/
│       └── style.css        ← CSS global único (responsivo incluído)
├── posts/                   ← Artigos individuais
│   ├── salud-prostatica.html
│   ├── energia-diaria.html
│   ├── estres-natural.html
│   ├── sueno-y-corazon.html
│   ├── alimentos-insomnio-evitar.html
│   ├── sal-potasio-corazon.html
│   ├── sucos-laxantes-naturales.html
│   ├── alimentos-probioticos-salud.html
│   ├── conciencia-salud-masculina.html
│   └── saude-do-homem-prevencao.html
└── legal/
    ├── privacidad.html
    ├── terminos.html
    └── contacto.html
```

---

## Stack e Convenções

- **HTML/CSS estático** — sem JavaScript, sem bundler, sem npm.
- Fonte: **Inter** (Google Fonts), pesos 400/600/700/800.
- Variáveis CSS definidas em `:root` no `style.css` — usar sempre `var(--primary)`, `var(--secondary)`, etc.
- Imagens: **Picsum Photos** (`https://picsum.photos/seed/{texto}/{largura}/{altura}`). Nunca usar Unsplash (bloqueia hot-linking sem API key). O seed de texto deve ser descritivo (ex: `medical1`, `sleep1`, `men-health1`).

---

## Responsividade (style.css)

Três breakpoints definidos no `style.css`:

| Breakpoint | Uso |
|------------|-----|
| `≤ 900px` | Tablet — hero grid colapsa, footer empilha |
| `≤ 768px` | Mobile — hamburger aparece, nav vira dropdown, grids 1 coluna |
| `≤ 480px` | Small mobile — ajustes finais de tamanho |

**Menu hamburger** — puro CSS (checkbox trick), sem JavaScript:
```html
<input type="checkbox" id="nav-toggle" class="nav-toggle">
<label for="nav-toggle" class="hamburger" aria-label="Menú">
  <span></span><span></span><span></span>
</label>
```
Deve estar em **todos** os ficheiros HTML dentro de `.header__inner`, entre o logo `<a>` e o `<nav>`.

**Cards largos** (flex horizontal com imagem+texto): usar classes `card--wide__inner` e `card--wide__img` para que empilhem em mobile.

---

## Criar um Novo Post

1. Copiar a estrutura de um post existente (ex: `estres-natural.html`).
2. Nomear o ficheiro em espanhol com hífens: `nombre-del-articulo.html`.
3. O `<head>` deve ter:
   - `lang="es"`
   - Link para `../assets/css/style.css`
   - Google Fonts Inter
   - `<style>` inline para estilos específicos do post + media query `@media(max-width:640px)` para qualquer grid 2 colunas
4. O header deve incluir o hamburger (ver acima) e o `<nav>` com os 4 links.
5. Adicionar card de entrada em `index.html` na secção adequada.
6. Fazer commit e push para `main`.

---

## Regras de Conteúdo

- **Idioma**: espanhol de Espanha. Estatísticas e fontes devem ser espanholas/europeias (INE, Ministerio de Sanidad, Sociedad Española de Cardiología, etc.).
- Tom: editorial médico de confiança, baseado em evidências — não sensacionalista.
- Imagens de autores: `https://picsum.photos/seed/doctorN/100/100` (seed `doctor1`, `doctor2`, `doctor3`…).
- CTA principal aponta para `../quiz.html` (página de avaliação).

---

## Git / Deploy

- Trabalhar sempre no branch `main`.
- Commit em português ou espanhol, mensagem clara do que mudou.
- Após qualquer conjunto de alterações, fazer push: `git push origin main`.
- Não há CI/CD — o site é servido diretamente pelo GitHub Pages ou similar.

---

## Encoding

Os ficheiros HTML usam **UTF-8 sem BOM**. Ao escrever ficheiros com PowerShell usar:
```powershell
[System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::UTF8)
```
Nunca `Set-Content -Encoding utf8` (adiciona BOM no PowerShell 5.1).
