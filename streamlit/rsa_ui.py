import streamlit as st
from rsa_algorithm import encrypt, decrypt, generate_keys
import ast

st.set_page_config(page_title="RSA Cryptosystem", layout="wide", page_icon='🔐')

with st.sidebar:
    st.image("https://sectigostore.com/blog/wp-content/uploads/2020/06/how-rsa-works.png")
    st.markdown('# 💬 Encrypt and Decrypt your messages using RSA 🔐')
    st.markdown('''
    ---
    ### 🔮 À Propos

    L'objectif de ce devoir est de réaliser un programme (interactif) implémentant l'algorithme RSA permettant de:

    - Générer les clés RSA (Cryptosystème)
    - Crypter un message d'entrée (Plaintext)
    - Décrypter un message chiffré (Ciphertext)
    ---

    ### 💻 Comment ça marche ?

    1. Enter the text you want to encrypt and click "🔓 Encrypt Message"
    2. A pair of public and private key will be generated
    3. Your plaintext is now in ciphertext
    4. Enter the ciphertext and private key in the "🗝️ Decrypt a ciphertext"
    5. Decrypt your message

    ---
    ''')

    st.markdown('😺 See Project Repository on [GitHub](https://github.com/Hamagistral/decathlon-chatbot)')
    st.markdown('👨‍💻 Made by [EL BELGHITI Hamza](https://www.linkedin.com/in/hamza-elbelghiti/) & EL FARKH Salaheddine')
    st.markdown('---')

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔓 Encrypt your message")
    message = st.text_area('Enter the message you want to encrypt:', '')
    encrypt_btn = st.button('Encrypt Message')

    if encrypt_btn and message:
        public_key, private_key = generate_keys()

        st.session_state['public_key'] = f'🔓 **Public key:** {public_key}'
        st.session_state['private_key'] = f'🗝️ **Private key:** {private_key}'

        st.session_state['encrypted_message'] = f"🗨️ **Encrypted Message:** {encrypt(message, public_key)}"

    # Retrieve the encrypted message from st.session_state
    public_key_info = st.session_state.get('public_key', '🔓 **Public key:**')
    private_key_info = st.session_state.get('private_key', '🗝️ **Private key:**')
    encrypted_message = st.session_state.get('encrypted_message', '🗨️ **Encrypted Message:**')

    col3, col4 = st.columns(2)
    with col3:
        st.info(public_key_info)
    with col4:
        st.info(private_key_info) 
    
    st.error(encrypted_message)
    

with col2:
    st.markdown("### 🗝️ Decrypt a ciphertext")
    decrypt_message = st.text_area('Enter the message you wish to decrypt in a list format ([***, ***, ...]):')
    decrypt_key = st.text_input('Enter the private key in a (d, n) format:')

    decrypt_btn = st.button('Decrypt Message')

    try:
        if decrypt_key:
            privateKey = ast.literal_eval(decrypt_key)

            if decrypt_btn and decrypt_message:
                cipher_message = ast.literal_eval(decrypt_message)

                st.success(f"💬 **Decrypted Message:** {decrypt(cipher_message, privateKey)}")
    except:
        st.warning("⏪ Please enter a valid **private key** in a (d, n) format.")

