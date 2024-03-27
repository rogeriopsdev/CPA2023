import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px


# Função para mostrar a Página 1
def show_page1():
    # st.markdown("# Página 1 🎈")
    # Configurando layout
    # st.set_page_config(layout="wide")

    # Título principal
    st.markdown("# Docentes Araguatins 2023🎈",
                unsafe_allow_html=True)  # Usando unsafe_allow_html para permitir que o título tenha um tamanho maior

    # Carregando os dados
    #df = pd.read_csv('dados/docentes/araguatins.csv', sep=',')
    df = pd.read_csv('dados/docentes/Docente_2023_Vcom.csv', sep=',')
    local = df["Informe seu Setor de Lotação:"]
    contagem_local = local.value_counts()

    fig_local = px.bar(x=contagem_local.index, y=contagem_local.values, text=contagem_local.values,
                        color_discrete_sequence=['green'])

    fig_local.update_traces(texttemplate='%{text}', textposition='outside')

    st.plotly_chart(fig_local)

    # Barra lateral com link para Docente.py
    st.sidebar.markdown("Clique [aqui](Docente.py) para abrir o arquivo Docente.py.")

    # Lista para armazenar as colunas selecionadas
    colunas_selecionadas = []

    # Botões para cada coluna no sidebar
    for coluna in df.columns:
        # Adicionar checkbox e botão para cada coluna
        checkbox_coluna = st.sidebar.checkbox(coluna)
        if checkbox_coluna:
            colunas_selecionadas.append(coluna)

    # Multiseleção para filtrar dados
    if colunas_selecionadas:
        for coluna in colunas_selecionadas:
            # Filtrar os dados pela coluna selecionada
            dados_filtrados = df[coluna]

            # Exibir DataFrame filtrado com tamanho maior
            st.write(dados_filtrados, height='500')  # Ajustando a altura para aumentar o tamanho do DataFrame

            # Plotar gráfico de dispersão para a coluna selecionada com tamanho maior e cores personalizadas
            fig_dispersao = px.scatter(df, x=coluna, trendline='ols', color_discrete_sequence=['blue'])
            fig_dispersao.update_xaxes(title=coluna)  # Adicionando legenda ao eixo x
            fig_dispersao.update_yaxes(title="Quantidade de docentes")  # Adicionando legenda ao eixo y
            st.plotly_chart(fig_dispersao,
                            use_container_width=True)  # Usando use_container_width para estender o gráfico

            # Calcular a média da coluna selecionada
            media = dados_filtrados.mean()

            # Plotar gráfico de médias para a coluna selecionada com tamanho maior e cores personalizadas
            fig_media = px.bar(x=[coluna], y=[media], text=[f'{media:.2f}'], title=f'Média de {coluna}',
                               color_discrete_sequence=['green'])
            fig_media.update_traces(textposition='outside')
            st.plotly_chart(fig_media, use_container_width=True)  # Usando use_container_width para estender o gráfico

        # Calcular a média das colunas selecionadas
        media_colunas = df[colunas_selecionadas].mean()

        # Calcular a média geral das colunas selecionadas
        media_geral = media_colunas.mean()

        # Plotar gráfico de barras com as médias das colunas selecionadas com cores personalizadas
        fig_media_colunas = px.bar(x=media_colunas.index, y=media_colunas.values,
                                   text=media_colunas.values, labels={'x': 'Coluna', 'y': 'Média'},
                                   title='Média das Colunas Selecionadas', color_discrete_sequence=['red'])
        fig_media_colunas.update_traces(textposition='outside')
        st.plotly_chart(fig_media_colunas,
                        use_container_width=True)  # Usando use_container_width para estender o gráfico

        # Plotar gráfico de barras com a média geral das colunas selecionadas
        fig_media_geral = px.bar(x=['Média Geral'], y=[media_geral],
                                 text=[f'{media_geral:.2f}'], title='Média Geral das Colunas Selecionadas',
                                 color_discrete_sequence=['purple'])
        fig_media_geral.update_traces(textposition='outside')
        st.plotly_chart(fig_media_geral, use_container_width=True)  # Usando use_container_width para estender o gráfico
    else:
        st.sidebar.write("Por favor, selecione uma ou mais colunas.")


# Função para mostrar a Página 2
def show_page2():
    # st.markdown("# Página 2 ❄️")
    # Configurando layout
    # st.set_page_config(layout="wide")

    # Título principal
    st.markdown("# Discentes Araguatins 🎈",
                unsafe_allow_html=True)  # Usando unsafe_allow_html para permitir que o título tenha um tamanho maior

    # Carregando os dados
    df = pd.read_csv('dados/discente/discente_2023.csv', sep=',')
    cursos = df["3. Em qual curso está matriculado ( Campus Araguatins )?"]
    contagem_cursos = cursos.value_counts()

    fig_cursos = px.bar(x=contagem_cursos.index, y=contagem_cursos.values, text=contagem_cursos.values,
                        color_discrete_sequence=['green'])

    fig_cursos.update_traces(texttemplate='%{text}', textposition='outside')

    st.plotly_chart(fig_cursos)

    # Barra lateral com link para Docente.py
    st.sidebar.markdown("Clique [aqui](Docente.py) para abrir o arquivo Docente.py.")

    # Lista para armazenar as colunas selecionadas
    colunas_selecionadas = []

    # Botões para cada coluna no sidebar
    for coluna in df.columns:
        # Adicionar checkbox e botão para cada coluna
        checkbox_coluna = st.sidebar.checkbox(coluna)
        if checkbox_coluna:
            colunas_selecionadas.append(coluna)

    # Multiseleção para filtrar dados
    if colunas_selecionadas:
        for coluna in colunas_selecionadas:
            # Filtrar os dados pela coluna selecionada
            dados_filtrados = df[coluna]

            # Exibir DataFrame filtrado com tamanho maior
            st.write(dados_filtrados, height=500)  # Ajustando a altura para aumentar o tamanho do DataFrame

            # Plotar gráfico de dispersão para a coluna selecionada com tamanho maior e cores personalizadas
            fig_dispersao = px.scatter(df, x=coluna, trendline='ols', color_discrete_sequence=['blue'])
            fig_dispersao.update_xaxes(title=coluna)  # Adicionando legenda ao eixo x
            fig_dispersao.update_yaxes(title="Quantidade de docentes")  # Adicionando legenda ao eixo y
            st.plotly_chart(fig_dispersao,
                            use_container_width=True)  # Usando use_container_width para estender o gráfico

            # Calcular a média da coluna selecionada
            media = dados_filtrados.mean()

            # Plotar gráfico de médias para a coluna selecionada com tamanho maior e cores personalizadas
            fig_media = px.bar(x=[coluna], y=[media], text=[f'{media:.2f}'], title=f'Média de {coluna}',
                               color_discrete_sequence=['green'])
            fig_media.update_traces(textposition='outside')
            st.plotly_chart(fig_media, use_container_width=True)  # Usando use_container_width para estender o gráfico

        # Calcular a média das colunas selecionadas
        media_colunas = df[colunas_selecionadas].mean()

        # Calcular a média geral das colunas selecionadas
        media_geral = media_colunas.mean()


        # Plotar gráfico de barras com as médias das colunas selecionadas com cores personalizadas
        fig_media_colunas = px.bar(x=media_colunas.index, y=media_colunas.values,
                                   text=media_colunas.values, labels={'x': 'Coluna', 'y': 'Média'},
                                   title='Média das Colunas Selecionadas', color_discrete_sequence=['red'])
        fig_media_colunas.update_traces(textposition='outside')
        st.plotly_chart(fig_media_colunas,
                        use_container_width=True)  # Usando use_container_width para estender o gráfico

        # Plotar gráfico de barras com a média geral das colunas selecionadas
        fig_media_geral = px.bar(x=['Média Geral'], y=[media_geral],
                                 text=[f'{media_geral:.2f}'], title='Média Geral das Colunas Selecionadas',
                                 color_discrete_sequence=['purple'])
        fig_media_geral.update_traces(textposition='outside')
        st.plotly_chart(fig_media_geral, use_container_width=True)  # Usando use_container_width para estender o gráfico
    else:
        st.sidebar.write("Por favor, selecione uma ou mais colunas.")


# Função para mostrar a Página 3
def show_page3():
    # Configurando layout
    #st.set_page_config(layout="wide")

    # Título principal
    st.markdown("# Técnicos Administrativos em Educação - Araguatins 🎈",
                unsafe_allow_html=True)  # Usando unsafe_allow_html para permitir que o título tenha um tamanho maior

    # Carregando os dados
    df = pd.read_csv('dados/tae/tae_araguatins.csv', sep=',')

    # Barra lateral com link para Docente.py
    st.sidebar.markdown("Clique [aqui](Docente.py) para abrir o arquivo Docente.py.")

    # Lista para armazenar as colunas selecionadas
    colunas_selecionadas = []

    # Botões para cada coluna no sidebar
    for coluna in df.columns:
        # Adicionar checkbox e botão para cada coluna
        checkbox_coluna = st.sidebar.checkbox(coluna)
        if checkbox_coluna:
            colunas_selecionadas.append(coluna)

    # Multiseleção para filtrar dados
    if colunas_selecionadas:
        for coluna in colunas_selecionadas:
            # Filtrar os dados pela coluna selecionada
            dados_filtrados = df[coluna]

            # Exibir DataFrame filtrado com tamanho maior
            st.write(dados_filtrados, height=500)  # Ajustando a altura para aumentar o tamanho do DataFrame

            # Plotar gráfico de dispersão para a coluna selecionada com tamanho maior e cores personalizadas
            fig_dispersao = px.scatter(df, x=coluna, trendline='ols', color_discrete_sequence=['blue'])
            fig_dispersao.update_xaxes(title=coluna)  # Adicionando legenda ao eixo x
            fig_dispersao.update_yaxes(title="Quantidade de docentes")  # Adicionando legenda ao eixo y
            st.plotly_chart(fig_dispersao,
                            use_container_width=True)  # Usando use_container_width para estender o gráfico

            # Calcular a média da coluna selecionada
            media = dados_filtrados.mean()

            # Plotar gráfico de médias para a coluna selecionada com tamanho maior e cores personalizadas
            fig_media = px.bar(x=[coluna], y=[media], text=[f'{media:.2f}'], title=f'Média de {coluna}',
                               color_discrete_sequence=['green'])
            fig_media.update_traces(textposition='outside')
            st.plotly_chart(fig_media, use_container_width=True)  # Usando use_container_width para estender o gráfico

        # Calcular a média das colunas selecionadas
        media_colunas = df[colunas_selecionadas].mean()

        # Calcular a média geral das colunas selecionadas
        media_geral = media_colunas.mean()

        # Plotar gráfico de barras com as médias das colunas selecionadas com cores personalizadas
        fig_media_colunas = px.bar(x=media_colunas.index, y=media_colunas.values,
                                   text=media_colunas.values, labels={'x': 'Coluna', 'y': 'Média'},
                                   title='Média das Colunas Selecionadas', color_discrete_sequence=['red'])
        fig_media_colunas.update_traces(textposition='outside')
        st.plotly_chart(fig_media_colunas,
                        use_container_width=True)  # Usando use_container_width para estender o gráfico

        # Plotar gráfico de barras com a média geral das colunas selecionadas
        fig_media_geral = px.bar(x=['Média Geral'], y=[media_geral],
                                 text=[f'{media_geral:.2f}'], title='Média Geral das Colunas Selecionadas',
                                 color_discrete_sequence=['purple'])
        fig_media_geral.update_traces(textposition='outside')
        st.plotly_chart(fig_media_geral, use_container_width=True)  # Usando use_container_width para estender o gráfico
    else:
        st.sidebar.write("Por favor, selecione uma ou mais colunas.")


def show_page4():

    # st.set_page_config(layout="wide")

    # Título principal
    st.markdown("# Sociedade Civil - Araguatins 🎈",
                unsafe_allow_html=True)  # Usando unsafe_allow_html para permitir que o título tenha um tamanho maior

    # Carregando os dados
    df = pd.read_csv('dados/soc_civil/Comunidade_araguatins.csv', sep=',')

    # Barra lateral com link para Docente.py
    st.sidebar.markdown("Clique [aqui](Docente.py) para abrir o arquivo Docente.py.")

    # Lista para armazenar as colunas selecionadas
    colunas_selecionadas = []

    # Botões para cada coluna no sidebar
    for coluna in df.columns:
        # Adicionar checkbox e botão para cada coluna
        checkbox_coluna = st.sidebar.checkbox(coluna)
        if checkbox_coluna:
            colunas_selecionadas.append(coluna)

    # Multiseleção para filtrar dados
    if colunas_selecionadas:
        for coluna in colunas_selecionadas:
            # Filtrar os dados pela coluna selecionada
            dados_filtrados = df[coluna]

            # Exibir DataFrame filtrado com tamanho maior
            st.write(dados_filtrados, height=500)  # Ajustando a altura para aumentar o tamanho do DataFrame

            # Plotar gráfico de dispersão para a coluna selecionada com tamanho maior e cores personalizadas
            fig_dispersao = px.scatter(df, x=coluna, trendline='ols', color_discrete_sequence=['blue'])
            fig_dispersao.update_xaxes(title=coluna)  # Adicionando legenda ao eixo x
            fig_dispersao.update_yaxes(title="Quantidade de docentes")  # Adicionando legenda ao eixo y
            st.plotly_chart(fig_dispersao,
                            use_container_width=True)  # Usando use_container_width para estender o gráfico

            # Calcular a média da coluna selecionada
            media = dados_filtrados.mean()

            # Plotar gráfico de médias para a coluna selecionada com tamanho maior e cores personalizadas
            fig_media = px.bar(x=[coluna], y=[media], text=[f'{media:.2f}'], title=f'Média de {coluna}',
                               color_discrete_sequence=['green'])
            fig_media.update_traces(textposition='outside')
            st.plotly_chart(fig_media, use_container_width=True)  # Usando use_container_width para estender o gráfico

        # Calcular a média das colunas selecionadas
        media_colunas = df[colunas_selecionadas].mean()

        # Calcular a média geral das colunas selecionadas
        media_geral = media_colunas.mean()

        # Plotar gráfico de barras com as médias das colunas selecionadas com cores personalizadas
        fig_media_colunas = px.bar(x=media_colunas.index, y=media_colunas.values,
                                   text=media_colunas.values, labels={'x': 'Coluna', 'y': 'Média'},
                                   title='Média das Colunas Selecionadas', color_discrete_sequence=['red'])
        fig_media_colunas.update_traces(textposition='outside')
        st.plotly_chart(fig_media_colunas,
                        use_container_width=True)  # Usando use_container_width para estender o gráfico

        # Plotar gráfico de barras com a média geral das colunas selecionadas
        fig_media_geral = px.bar(x=['Média Geral'], y=[media_geral],
                                 text=[f'{media_geral:.2f}'], title='Média Geral das Colunas Selecionadas',
                                 color_discrete_sequence=['purple'])
        fig_media_geral.update_traces(textposition='outside')
        st.plotly_chart(fig_media_geral, use_container_width=True)  # Usando use_container_width para estender o gráfico
    else:
        st.sidebar.write("Por favor, selecione uma ou mais colunas.")


# Configurando layout
st.set_page_config(layout="wide")

# Título principal
st.sidebar.markdown("# Menu de Navegação 📚", unsafe_allow_html=True)

# Menu para selecionar a página
selected_page = st.sidebar.radio("Selecione a página:", ["Docentes", "Discentes", "Técnico Administrativos em Educação",
                                                         "Sociedade Civil Organizada"])

# Mostrar a página correspondente à opção selecionada
if selected_page == "Docentes":
    show_page1()
elif selected_page == "Discentes":
    show_page2()
elif selected_page == "Técnico Administrativos em Educação":
    show_page3()
elif selected_page == "Sociedade Civil Organizada":
    show_page4()
