# Aula: GitHub – Fluxo Colaborativo e Boas Práticas

## Objetivo da aula

Entender o **GitHub como plataforma**, como ele se conecta ao Git local e como organizar o trabalho em equipe usando **repositórios remotos, branches, pull requests, issues e convenções**. Aqui o Git você já conhece — agora é o modo multiplayer.

---

## O que é GitHub (sem romantizar)

GitHub **não é Git**.

- **Git** → ferramenta de versionamento (local)
- **GitHub** → plataforma que hospeda repositórios Git e adiciona colaboração, revisão, histórico público e automações

Pense assim:

- Git = motor
- GitHub = estrada + regras de trânsito + retrovisor

---

## Repositório remoto

Um **repositório remoto** é uma cópia do projeto hospedada no GitHub.

Normalmente chamado de:

```bash
origin
```

Ver repositórios remotos:

```bash
git remote -v
```

---

## Conectando Git local ao GitHub

Depois de criar um repositório no GitHub:

```bash
git remote add origin https://github.com/usuario/repositorio.git
```

Enviar commits locais:

```bash
git push origin main
```

Buscar atualizações:

```bash
git pull origin main
```

Resumo mental:

- `push` → sobe código
- `pull` → desce código

---

## Clone (começando pelo GitHub)

Clonar um repositório existente:

```bash
git clone https://github.com/usuario/repositorio.git
```

Isso:

- Baixa o código
- Cria o repositório local
- Configura o `origin`

---

## Branch no GitHub (regra de ouro)

❌ Trabalhar direto na `main`

✅ Criar branches para qualquer coisa

Fluxo comum:

```bash
git checkout -b feature/login
git push origin feature/login
```

Cada branch representa:

- Feature
- Correção
- Experimento

---

## Pull Request (PR)

Pull Request é um **pedido de merge**.

Você está dizendo:

> "Ei, fiz isso aqui. Dá uma olhada antes de juntar."

No PR você tem:

- Comparação de código
- Comentários por linha
- Histórico claro
- Discussão técnica (ou filosófica)

PR não é burocracia. É freio.

---

## Fluxo básico com Pull Request

1. Cria branch
2. Commita
3. Push da branch
4. Abre Pull Request
5. Revisão
6. Merge

Simples. Funciona. Evita tragédia.

---

## Merge no GitHub

Tipos comuns:

- **Merge commit** → mantém histórico completo
- **Squash and merge** → vários commits viram um só
- **Rebase and merge** → histórico linear

Para times pequenos: *squash costuma resolver*.

---

## Issues (tarefas e problemas)

Issue é:

- Bug
- Ideia
- Tarefa
- Discussão

Boas issues têm:

- Título claro
- Descrição objetiva
- Critério de aceite

Exemplo:

> Bug: formulário aceita email inválido

---

## Ligando commits e issues

Você pode fechar issues pelo commit ou PR:

```text
fix: valida email no formulário

Closes #12
```

O GitHub faz o resto.

---

## Convenção de commits (padrão que salva tempo)

Formato:

```text
<TIPO>(ESCOPO OPCIONAL): descrição curta
```

Tipos mais usados:

- `feat` → nova funcionalidade
- `fix` → correção de bug
- `docs` → documentação
- `style` → formatação (sem mudar lógica)
- `refactor` → refatoração
- `test` → testes
- `chore` → tarefas internas

Exemplo:

```text
feat(auth): adiciona login com Google
```

Commits claros viram histórico útil. O resto vira ruído.

---

## README.md (cartão de visita)

Todo repositório decente tem um README.

Estrutura mínima:

- O que é o projeto
- Como rodar
- Tecnologias
- Estrutura básica

Se não tem README, ninguém usa. Simples assim.

---

## .gitignore no GitHub

Evita subir lixo:

```text
node_modules/
.env
dist/
```

Arquivo errado no GitHub é erro clássico de iniciante.

---

## Proteção de branch

Configuração comum:

- Bloquear push direto na `main`
- Exigir Pull Request
- Exigir aprovação

Resultado:

- Menos erro
- Mais conversa
- Código melhor

---

## GitHub Actions (visão geral)

Automação integrada ao repositório.

Exemplos:

- Rodar testes
- Verificar build
- Lint automático

Não é magia. É script rodando no push.

---

## Fluxo resumido (cola mental)

1. `clone`
2. `checkout -b`
3. `commit`
4. `push`
5. Pull Request
6. Review
7. Merge

Repete. Em equipe. Sem caos.

---

## Conclusão direta

GitHub não é só hospedar código.

É:

- Histórico
- Revisão
- Organização
- Comunicação técnica

Usar mal vira bagunça. Usar bem vira processo.

