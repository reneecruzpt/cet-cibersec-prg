import matplotlib.pyplot as plt
import seaborn as sns

# Dados
categorias = [
    "Usuários de Internet (9 a 17 anos)",
    "Perfil em Redes Sociais (9 a 17 anos)",
    "Perfil em Redes Sociais (15 a 17 anos)"
]
percentuais = [92, 86, 96]

# Configurações de estilo
sns.set(style="whitegrid")

# Criar o gráfico
plt.figure(figsize=(12, 8))
bar_plot = plt.bar(categorias, percentuais, color=sns.color_palette("pastel"))

# Adicionar títulos e rótulos
plt.xlabel('Categoria', fontsize=14, fontweight='bold')
plt.ylabel('Percentual (%)', fontsize=14, fontweight='bold')
plt.title('Uso de Internet e Redes Sociais por Crianças e Adolescentes no Brasil', fontsize=16, fontweight='bold')

# Ajustar os rótulos do eixo x
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

# Adicionar rótulos de valor nas barras
for bar in bar_plot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Adicionar linhas de grade
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Ajustar o layout
plt.tight_layout()

# Exibir o gráfico
plt.show()
