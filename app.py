import streamlit as st

def main():
    st.set_page_config(page_title="Calculateur de Parité de Pouvoir d'Achat (PPA)", page_icon="🌍")

    st.title("🌍 Calculateur de Prix SaaS - PPA")
    st.markdown("""
    Adaptez vos prix en fonction du pouvoir d'achat de chaque pays.
    Ce concept permet de rendre vos produits accessibles mondialement (comme Netflix ou Spotify).
    """)

    # Dictionnaire des coefficients PPA approximatifs (Base USA = 1.0)
    # Ces valeurs sont des estimations pour l'exemple.
    ppp_data = {
        "États-Unis": {"code": "US", "flag": "🇺🇸", "coeff": 1.0},
        "Suisse": {"code": "CH", "flag": "🇨🇭", "coeff": 1.25},
        "Royaume-Uni": {"code": "GB", "flag": "🇬🇧", "coeff": 0.90},
        "Allemagne": {"code": "DE", "flag": "🇩🇪", "coeff": 0.90},
        "France": {"code": "FR", "flag": "🇫🇷", "coeff": 0.85},
        "Belgique": {"code": "BE", "flag": "🇧🇪", "coeff": 0.90},
        "Canada": {"code": "CA", "flag": "🇨🇦", "coeff": 0.95},
        "Australie": {"code": "AU", "flag": "🇦🇺", "coeff": 1.05},
        "Japon": {"code": "JP", "flag": "🇯🇵", "coeff": 0.85},
        "Corée du Sud": {"code": "KR", "flag": "🇰🇷", "coeff": 0.80},
        "Italie": {"code": "IT", "flag": "🇮🇹", "coeff": 0.80},
        "Espagne": {"code": "ES", "flag": "🇪🇸", "coeff": 0.75},
        "Chine": {"code": "CN", "flag": "🇨🇳", "coeff": 0.60},
        "Brésil": {"code": "BR", "flag": "🇧🇷", "coeff": 0.45},
        "Mexique": {"code": "MX", "flag": "🇲🇽", "coeff": 0.45},
        "Russie": {"code": "RU", "flag": "🇷🇺", "coeff": 0.40},
        "Turquie": {"code": "TR", "flag": "🇹🇷", "coeff": 0.35},
        "Inde": {"code": "IN", "flag": "🇮🇳", "coeff": 0.30},
        "Indonésie": {"code": "ID", "flag": "🇮🇩", "coeff": 0.35},
        "Nigeria": {"code": "NG", "flag": "🇳🇬", "coeff": 0.35},
    }

    # Sidebar pour les paramètres
    st.sidebar.header("Paramètres")
    
    # Entrée du prix de base
    base_price = st.sidebar.number_input(
        "Prix de base aux USA ($)", 
        min_value=0.0, 
        value=10.0, 
        step=1.0,
        format="%.2f"
    )

    # Sélection du pays
    country_list = sorted(ppp_data.keys())
    # Mettre USA par défaut si présent, sinon le premier
    default_index = country_list.index("États-Unis") if "États-Unis" in country_list else 0
    
    target_country = st.sidebar.selectbox(
        "Pays cible", 
        country_list, 
        index=default_index
    )

    # Récupération des données du pays sélectionné
    country_info = ppp_data[target_country]
    coeff = country_info["coeff"]
    flag = country_info["flag"]

    # Calcul du prix ajusté
    adjusted_price = base_price * coeff

    # Affichage principal
    st.header(f"Prix recommandé pour {target_country} {flag}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Prix Base (USA)", value=f"${base_price:.2f}")
    
    with col2:
        st.metric(label="Coefficient PPA", value=f"x {coeff}")
        
    with col3:
        st.metric(label="Prix Ajusté", value=f"${adjusted_price:.2f}")

    st.success(f"Le prix recommandé pour un utilisateur en **{target_country}** est de **${adjusted_price:.2f}** (USD).")
    
    # Explication contextuelle
    st.info("""
    **Note :** Ce calcul utilise un coefficient simplifié basé sur la parité de pouvoir d'achat relative aux États-Unis.
    Un coefficient < 1.0 signifie que le pouvoir d'achat est plus faible (prix plus bas recommandé).
    Un coefficient > 1.0 signifie que le coût de la vie est plus élevé (prix potentiellement plus élevé).
    """)

if __name__ == "__main__":
    main()

