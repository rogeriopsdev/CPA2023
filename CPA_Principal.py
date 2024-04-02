import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px


# Função para mostrar a Página 1
def show_page1():


    # Configurando layout
  #  st.set_page_config(layout="wide")


    # Configurando layout
  #  st.set_page_config(layout="wide")

    # Título principal
    st.markdown("# Docentes Araguatins 2023 🎈🎈", unsafe_allow_html=True)

    # Carregando os dados
    df = pd.read_csv('dados/docentes/Docente_2023_Vcomp.csv', sep=',')

    # Sidebar para seleção de filtros
    st.sidebar.markdown("## Filtros")

    # Filtro por "Informe seu Setor de Lotação"
    filtro_setor = st.sidebar.checkbox("Filtrar por Setor de Lotação")
    if filtro_setor:
        setor_selecionado = st.sidebar.selectbox("Selecione o Setor de Lotação:",
                                                 df["Informe seu Setor de Lotação:"].unique().tolist())
        df_filtrado = df[df["Informe seu Setor de Lotação:"] == setor_selecionado]
    else:
        df_filtrado = df

    # Filtro por "Informe sua Unidade de Lotação"
    filtro_unidade = st.sidebar.checkbox("Filtrar por Unidade de Lotação")
    if filtro_unidade:
        unidade_selecionada = st.sidebar.selectbox("Selecione a Unidade de Lotação:",
                                                   df["Informe seu campus"].unique().tolist())
        df_filtrado = df_filtrado[df_filtrado["Informe seu campus"] == unidade_selecionada]

    # Lista para armazenar as colunas selecionadas
    colunas_selecionadas = []
    st.sidebar.markdown("## Respostas")
    # Botões para cada coluna no sidebar
    for coluna in df_filtrado.columns:
        # Adicionar checkbox e botão para cada coluna
        checkbox_coluna = st.sidebar.checkbox(coluna)
        if checkbox_coluna:
            colunas_selecionadas.append(coluna)

    # Multiseleção para filtrar dados
    if colunas_selecionadas:
        for coluna in colunas_selecionadas:
            # Filtrar os dados pela coluna selecionada
            dados_filtrados = df_filtrado[coluna]

            # Exibir DataFrame filtrado com tamanho maior
            st.write(dados_filtrados, height=500)  # Ajustando a altura para aumentar o tamanho do DataFrame

            try:
                # Plotar gráfico de dispersão para a coluna selecionada com tamanho maior e cores personalizadas
                fig_dispersao = px.scatter(df_filtrado, x=coluna, trendline='ols', color_discrete_sequence=['blue'])
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
                st.plotly_chart(fig_media,
                                use_container_width=True)  # Usando use_container_width para estender o gráfico
            except Exception as e:
                st.write(f"Erro ao gerar gráfico para a coluna {coluna}: {e}")

        # Calcular a média das colunas selecionadas
        media_colunas = df_filtrado[colunas_selecionadas].mean()

        # Calcular a média geral das colunas selecionadas
        media_geral = media_colunas.mean()

        try:
            # Plotar gráfico de barras com as médias das colunas selecionadas com cores personalizadas
            fig_media_colunas = px.bar(x=media_colunas.index, y=media_colunas.values,
                                       text=media_colunas.values, labels={'x': 'Coluna', 'y': 'Média'},
                                       title='Média das Colunas Selecionadas', color_discrete_sequence=['red'])
            fig_media_colunas.update_traces(textposition='outside')
            st.plotly_chart(fig_media_colunas,
                            use_container_width=True)  # Usando use_container_width para estender o gráfico
        except Exception as e:
            st.write(f"Erro ao gerar gráfico de média das colunas selecionadas: {e}")

        try:
            # Plotar gráfico de barras com a média geral das colunas selecionadas
            fig_media_geral = px.bar(x=['Média Geral'], y=[media_geral],
                                     text=[f'{media_geral:.2f}'], title='Média Geral das Colunas Selecionadas',
                                     color_discrete_sequence=['purple'])
            fig_media_geral.update_traces(textposition='outside')
            st.plotly_chart(fig_media_geral,
                            use_container_width=True)  # Usando use_container_width para estender o gráfico
        except Exception as e:
            st.write(f"Erro ao gerar gráfico de média geral das colunas selecionadas: {e}")
    else:
        st.sidebar.write("Por favor, selecione uma ou mais colunas.")


# Função para mostrar a Página 2
def show_page2():


    # Configurando layout
    #st.set_page_config(layout="wide")

    # Título principal
    st.markdown("# Discentes Araguatins 🎈",
                unsafe_allow_html=True)  # Usando unsafe_allow_html para permitir que o título tenha um tamanho maior

    # Carregando os dados
    df = pd.read_csv('dados/discente/discente_2023.csv', sep=',')

    # Barra lateral com link para Docente.py

    # Lista para armazenar as colunas selecionadas
    colunas_selecionadas = []
    filtro_curso = st.sidebar.selectbox("Selecione o curso:", df[
        "3. Em qual curso está matriculado ( Campus Araguatins )?"].unique().tolist())
    st.sidebar.markdown("## Filtros")
    # Aplicar filtro
    df_filtrado = df[df["3. Em qual curso está matriculado ( Campus Araguatins )?"] == filtro_curso]
    st.sidebar.markdown("## Respostas")
    # Botões para cada coluna no sidebar
    for coluna in df_filtrado.columns:
        # Adicionar checkbox e botão para cada coluna
        checkbox_coluna = st.sidebar.checkbox(coluna)
        if checkbox_coluna:
            colunas_selecionadas.append(coluna)

    # Multiseleção para filtrar dados
    if colunas_selecionadas:
        for coluna in colunas_selecionadas:
            # Filtrar os dados pela coluna selecionada
            dados_filtrados = df_filtrado[coluna]

            # Exibir DataFrame filtrado com tamanho maior
            st.write(dados_filtrados, height=500)  # Ajustando a altura para aumentar o tamanho do DataFrame

            try:
                # Plotar gráfico de dispersão para a coluna selecionada com tamanho maior e cores personalizadas
                fig_dispersao = px.scatter(df_filtrado, x=coluna, trendline='ols', color_discrete_sequence=['blue'])
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
                st.plotly_chart(fig_media,
                                use_container_width=True)  # Usando use_container_width para estender o gráfico
            except Exception as e:
                st.write(f"Erro ao gerar gráfico para a coluna {coluna}: {e}")

        # Calcular a média das colunas selecionadas
        media_colunas = df_filtrado[colunas_selecionadas].mean(axis=0)

        # Calcular a média geral das colunas selecionadas
        media_geral = media_colunas.mean()

        try:
            # Plotar gráfico de barras com as médias das colunas selecionadas com cores personalizadas
            fig_media_colunas = px.bar(x=media_colunas.index, y=media_colunas.values,
                                       text=media_colunas.values, labels={'x': 'Coluna', 'y': 'Média'},
                                       title='Média das Colunas Selecionadas', color_discrete_sequence=['red'])
            fig_media_colunas.update_traces(textposition='outside')
            st.plotly_chart(fig_media_colunas,
                            use_container_width=True)  # Usando use_container_width para estender o gráfico
        except Exception as e:
            st.write(f"Erro ao gerar gráfico de média das colunas selecionadas: {e}")

        try:
            # Plotar gráfico de barras com a média geral das colunas selecionadas
            fig_media_geral = px.bar(x=['Média Geral'], y=[media_geral],
                                     text=[f'{media_geral:.2f}'], title='Média Geral das Colunas Selecionadas',
                                     color_discrete_sequence=['purple'])
            fig_media_geral.update_traces(textposition='outside')
            st.plotly_chart(fig_media_geral,
                            use_container_width=True)  # Usando use_container_width para estender o gráfico
        except Exception as e:
            st.write(f"Erro ao gerar gráfico de média geral das colunas selecionadas: {e}")
    else:
        st.sidebar.write("Por favor, selecione uma ou mais colunas.")


# Função para mostrar a Página 3
def show_page3():


    # Configurando layout
    #st.set_page_config(layout="wide")

    # Título principal
    st.markdown("# Técnicos Administrativos em Educação Araguatins🎈", unsafe_allow_html=True)

    # Carregando os dados
    df = pd.read_csv('dados/tae/tae_araguatins.csv', sep=',')

    # Barra lateral com link para Docente.py

    # Lista para armazenar as colunas selecionadas
    colunas_selecionadas = []

    # Filtro por "Informe seu setor de lotação"
    filtro_setor = st.sidebar.checkbox("Filtrar por Setor de Lotação")
    if filtro_setor:
        setor_selecionado = st.sidebar.selectbox("Selecione o Setor de Lotação:",
                                                 df["2. Informe seu setor de lotação?"].unique().tolist())
        df_filtrado = df[df["2. Informe seu setor de lotação?"] == setor_selecionado]
    else:
        df_filtrado = df

    # Filtro por "Informe sua Unidade de Lotação"
    filtro_unidade = st.sidebar.checkbox("Filtrar por Unidade de Lotação")
    if filtro_unidade:
        unidade_selecionada = st.sidebar.selectbox("Selecione a Unidade de Lotação:",
                                                   df["1. Informe sua Unidade de Lotação:"].unique().tolist())
        df_filtrado = df_filtrado[df_filtrado["1. Informe sua Unidade de Lotação:"] == unidade_selecionada]

    # Botões para cada coluna no sidebar
    for coluna in df_filtrado.columns:
        # Adicionar checkbox e botão para cada coluna
        checkbox_coluna = st.sidebar.checkbox(coluna)
        if checkbox_coluna:
            colunas_selecionadas.append(coluna)

    # Multiseleção para filtrar dados
    if colunas_selecionadas:
        for coluna in colunas_selecionadas:
            # Filtrar os dados pela coluna selecionada
            dados_filtrados = df_filtrado[coluna]

            # Exibir DataFrame filtrado com tamanho maior
            st.write(dados_filtrados, height=500)  # Ajustando a altura para aumentar o tamanho do DataFrame

            try:
                # Plotar gráfico de dispersão para a coluna selecionada com tamanho maior e cores personalizadas
                fig_dispersao = px.scatter(df_filtrado, x=coluna, trendline='ols', color_discrete_sequence=['blue'])
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
                st.plotly_chart(fig_media,
                                use_container_width=True)  # Usando use_container_width para estender o gráfico
            except Exception as e:
                st.write(f"Erro ao gerar gráfico para a coluna {coluna}: {e}")

        # Calcular a média das colunas selecionadas
        media_colunas = df_filtrado[colunas_selecionadas].mean(axis=0)

        # Calcular a média geral das colunas selecionadas
        media_geral = media_colunas.mean()

        try:
            # Plotar gráfico de barras com as médias das colunas selecionadas com cores personalizadas
            fig_media_colunas = px.bar(x=media_colunas.index, y=media_colunas.values,
                                       text=media_colunas.values, labels={'x': 'Coluna', 'y': 'Média'},
                                       title='Média das Colunas Selecionadas', color_discrete_sequence=['red'])
            fig_media_colunas.update_traces(textposition='outside')
            st.plotly_chart(fig_media_colunas,
                            use_container_width=True)  # Usando use_container_width para estender o gráfico
        except Exception as e:
            st.write(f"Erro ao gerar gráfico de média das colunas selecionadas: {e}")

        try:
            # Plotar gráfico de barras com a média geral das colunas selecionadas
            fig_media_geral = px.bar(x=['Média Geral'], y=[media_geral],
                                     text=[f'{media_geral:.2f}'], title='Média Geral das Colunas Selecionadas',
                                     color_discrete_sequence=['purple'])
            fig_media_geral.update_traces(textposition='outside')
            st.plotly_chart(fig_media_geral,
                            use_container_width=True)  # Usando use_container_width para estender o gráfico
        except Exception as e:
            st.write(f"Erro ao gerar gráfico de média geral das colunas selecionadas: {e}")
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
