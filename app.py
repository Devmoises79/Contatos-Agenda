import streamlit as st

st.set_page_config(page_title="Minha Agenda", page_icon="📒")


# Armazena contatos em memória
if "agenda" not in st.session_state:
    st.session_state.agenda = {}

st.title("📒 Agenda de Contatos")

# Menu lateral
menu = st.sidebar.radio("Navegar", ["Adicionar", "Listar", "Buscar", "Remover"])

if menu == "Adicionar":
    st.subheader("➕ Adicionar Contato")
    nome = st.text_input("Nome")
    telefone = st.text_input("Telefone")
    email = st.text_input("Email")
    
    if st.button("Salvar"):
        if nome and telefone and email:
            st.session_state.agenda[nome] = {"telefone": telefone, "email": email}
            st.success(f"Contato '{nome}' adicionado!")
        else:
            st.warning("Preencha todos os campos.")

elif menu == "Listar":
    st.subheader("📋 Lista de Contatos")
    if st.session_state.agenda:
        for nome, info in st.session_state.agenda.items():
            st.write(f"**{nome}**")
            st.write(f"📞 Telefone: {info['telefone']}")
            st.write(f"📧 Email: {info['email']}")
            st.markdown("---")
    else:
        st.info("Nenhum contato cadastrado.")

elif menu == "Buscar":
    st.subheader("🔎 Buscar Contato")
    busca = st.text_input("Digite o nome do contato")
    if st.button("Buscar"):
        contato = st.session_state.agenda.get(busca)
        if contato:
            st.write(f"📞 Telefone: {contato['telefone']}")
            st.write(f"📧 Email: {contato['email']}")
        else:
            st.warning("Contato não encontrado.")

elif menu == "Remover":
    st.subheader("❌ Remover Contato")
    nome_remover = st.selectbox("Selecione um contato", list(st.session_state.agenda.keys()) if st.session_state.agenda else [""])
    if nome_remover and st.button("Remover"):
        st.session_state.agenda.pop(nome_remover, None)
        st.success(f"Contato '{nome_remover}' removido.")

