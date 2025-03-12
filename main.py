import functions as func
import livros_pd as lv

# pedidos = [
#     "Cem Anos de Solidão - Gabriel García Márquez",
#     # "1984 - George Orwell",
#     # "O Grande Gatsby - F. Scott Fitzgerald",
#     # "Dom Quixote - Miguel de Cervantes",
#     # "Sapiens: Uma Breve História da Humanidade - Yuval Noah Harari"
# ]


#Pegando o caminho do arquivo da lista de livros
file_path = lv.inserirArquivo()
print(file_path)

#Retira aspas do caminho
file_path = lv.tratarArquivo(file_path)

#Verifica se o arquivo existe e retorna a lista de livros
lista = lv.verificarArquivo(file_path)

################################################

driver = func.ininicializarDriver()

func.acessarSite(driver)

# func.logar(driver)

func.carregarTela(driver)

func.adicionarPedidos(lista,driver)

func.finalizarPedido(driver)

func.pagarComPix(driver)

func.gerarQRCode(driver)

func.confirmarPedido(driver)

func.clicarConfirmarPedido(driver)

func.encerrar(driver)