import streamlit as st

# Define the content for each item
items = [
    {
        "name": "Millet divino 25",
        "description": """
        (sac du quotidien)
        - poche à ordi
        - bonne accessibilité de la poche intérieure
        - 25 litres
        - déperlant (en partie étanche)
        - sangles de compression latérales (pratique pour y accrocher des trucs)
        - filet sur le côté pour gourde
        """,
        "image": "https://www.bfgcdn.com/1500_1500_90/502-6697/millet-divino-25-sac-a-dos-journee.jpg",
        "image2": "https://www.bfgcdn.com/1500_1500_90/502-6697/millet-divino-25-sac-a-dos-journee-detail-11.jpg",
    },
    {
        "name": "The North Face Slackpack 2.0 W",
        "description": """
        (sac de ski)
        - Poche à ordi
        - très bonne accessibilité de la poche intérieure
        - 20 litres
        - deux sangles extérieures permettant d’y accrocher des skis ou autre
        - Compatible avec poche à eau
        """,
        "image": "https://www.bagage24.fr/out/pictures/generated/product/1/768_768_85/81/b4/bc/8adee163dab4fdaf1db1290bf604b2a4_81b4bcd007bf0998d909a108e849a0b4.jpg",
        "image2": "https://www.bagage24.fr/out/pictures/generated/product/4/1500_1500_85/81b4bcd007bf0998d909a108e849a0b4.jpg",
    },
    {
        "name": "Batch Dr. Expedition 40 Duffel Sage",
        "description": """
        (sac de sport)
        - Pas de poche à ordi
        - Très bonne accessibilité de la poche intérieur (type sac de voyage)
        - 40 litres
        - Résistant et imperméable 
        """,
        "image": "https://glisshop-glisshop-fr-storage.omn.proximis.com/Imagestorage/imagesSynchro/735/735/6c52df1381055f045d1d7b7799f357652498dc5e_E24BACHACC420415_BACH0882086_1.jpeg",
        "image2": "https://glisshop-glisshop-fr-storage.omn.proximis.com/Imagestorage/imagesSynchro/735/735/0bddee011ac1205ee800a0501aaf563f0fea0be1_E24BACHACC420415_BACH0882086_4.jpeg",
    },
    {
        "name": "The North Face Base Camp Voyager Duffel 32L",
        "description": """
        (sac de voyage)
        - Poche à ordi
        - Très bonne accessibilité de la poche intérieure (type valise)
        - 32 litres
        - Emplacement bouteille d’eau sur le côté du sac
        """,
        "image": "https://images.snowleader.com/cdn-cgi/image/f=auto,fit=scale-down,q=85/https://images.snowleader.com/media/catalog/product/cache/1/image/0dc2d03fe217f8c83829496872af24a0/T/H/THEN02319_04.jpg",
        "image2": "https://images.snowleader.com/cdn-cgi/image/f=auto,fit=scale-down,q=85/https://images.snowleader.com/media/catalog/product/cache/1/image/0dc2d03fe217f8c83829496872af24a0/T/H/THEN02319_02.jpg",
    },
    {
        "name": "Cotoxi Allpa 28",
        "description": """
        (sac de voyage)
        - poche à ordi
        - 28 litres
        - Ouverture type valise
        - Trois compartiments de rangements avec filets dans la poche principale (comme dans une valise)
        - Poche pour ranger les plus petites affaires
        """,
        "image": "https://www.montanasupplyco.com/cdn/shop/products/1200X1200jpeg-allpa_28_evergreen_front_1_cb0c4689-d0c5-416c-8f53-5ab2d13caeb8_360x.jpg?v=1680798156",
        "image2": "https://www.montanasupplyco.com/cdn/shop/products/1200X1200jpeg-s21_allpa_28L_black_topdownopen-Enhanced_be64fafd-18c4-40b1-ad23-dbc6ce79aa4f_360x.jpg?v=1680798175",
    }
]

# Initialisation de l'état des boutons
if 'show_images' not in st.session_state:
    st.session_state.show_images = [False] * len(items)
if 'detail_view' not in st.session_state:
    st.session_state.detail_view = None

# Image de point d'interrogation
placeholder_image = "https://support.supercell.com/images/Starr-Drop-1.png?v=1706110361"

# Fonction pour afficher les détails
def show_details(index):
    item = items[index]
    st.write(f"### {item['name']}")
    st.write(item['description'])

# Fonction pour rendre une image cliquable
def clickable_image(image_url, index, hover_image_url):
    st.markdown(
        f"""
        <style>
        .clickable-img-{index} {{
            cursor: pointer;
            transition: all .2s ease-in-out;
        }}
        .clickable-img-{index}:hover {{
            transform: scale(1.1);
            content: url({hover_image_url});
        }}
        </style>
        <img src="{image_url}" class="clickable-img-{index}" id="clickable-img-{index}" onclick="document.getElementById('img-btn-{index}').click()" onmouseover="document.getElementById('clickable-img-{index}').src='{hover_image_url}';" onmouseout="document.getElementById('clickable-img-{index}').src='{image_url}';">
        <input type="button" id="img-btn-{index}" style="display:none;">
        """,
        unsafe_allow_html=True,
    )


# CSS pour l'effet de texte brillant
glowing_text_css = """
    <style>
    @keyframes glowingGold {
        0% { text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #ffd700, 0 0 20px #ffd700, 0 0 25px #ffd700, 0 0 30px #ffd700, 0 0 35px #ffd700; }
        50% { text-shadow: 0 0 5px #fff, 0 0 10px #ffea00, 0 0 15px #ffea00, 0 0 20px #ffea00, 0 0 25px #ffea00, 0 0 30px #ffea00, 0 0 35px #ffea00; }
        100% { text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #ffd700, 0 0 20px #ffd700, 0 0 25px #ffd700, 0 0 30px #ffd700, 0 0 35px #ffd700; }
    }
    .glowing-text-gold {
        font-size: 2.2em;
        color: #000;
        font-weight: bold; /* Gras pour mieux voir le contour */
        text-shadow: 
            -1px -1px 0 #000,  
            1px -1px 0 #000,
            -1px  1px 0 #000,
            1px  1px 0 #000; /* Contour noir autour du texte */
        align-items: center;
        text-align: center;
        animation: glowing 1500ms infinite;
    }
    """

st.write("# Ouvres tes packs étoiles pour choisir ton cadeau !")

st.write("# ")

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    
    # Ajouter le CSS à la page
    st.markdown(glowing_text_css, unsafe_allow_html=True)

    # Utiliser HTML pour ajouter le texte brillant
    st.markdown('<h1 class="glowing-text-violet">    Épic</h1>', unsafe_allow_html=True)
    st.write("")

    # Affichage des icônes
    for i, item in enumerate(items[:-1]):
        if st.session_state.show_images[i]:
            # Image du sac cliquable
            clickable_image(item['image'], i, item['image2'])
            if st.button(f"Voir les détails du {item['name']}", key=f"image_button_{i}"):
                st.session_state.detail_view = i
        else:
            # Image de point d'interrogation cliquable
            clickable_image(placeholder_image, i, placeholder_image)
            if st.button("Ouvrir le pack", key=f"button_{i}", on_click=lambda i=i: st.session_state.update({f"show_images_{i}": True})):
                st.session_state.show_images[i] = True
                st.session_state.detail_view = None
                st.experimental_rerun()
    
    # Utiliser HTML pour ajouter le texte brillant
    st.markdown('<h1 class="glowing-text-gold">    Légendaire</h1>', unsafe_allow_html=True)
    st.write("")

    # Affichage du dernier item
    i = len(items) - 1
    item = items[-1]
    if st.session_state.show_images[i]:
        clickable_image(item['image'], i, item['image2'])
        if st.button(f"Voir les détails du {item['name']}", key=f"image_button_{i}"):
            st.session_state.detail_view = i
    else:
        clickable_image(placeholder_image, i, placeholder_image)
        if st.button("Ouvrir le pack", key=f"button_{i}", on_click=lambda i=i: st.session_state.update({f"show_images_{i}": True})):
            st.session_state.show_images[i] = True
            st.session_state.detail_view = None
            st.experimental_rerun()

with col3:
    st.write(' ')

# Affichage de la page de détails
if st.session_state.detail_view is not None:
    show_details(st.session_state.detail_view)

