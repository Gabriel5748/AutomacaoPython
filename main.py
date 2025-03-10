import functions as func

pedidos = [
    "Cem Anos de Solidão - Gabriel García Márquez",
    # "1984 - George Orwell",
    # "O Grande Gatsby - F. Scott Fitzgerald",
    # "Dom Quixote - Miguel de Cervantes",
    # "Sapiens: Uma Breve História da Humanidade - Yuval Noah Harari"
]


driver = func.ininicializarDriver()

func.acessarSite(driver)

func.logar(driver)

func.carregarTela(driver)

func.adicionarPedidos(pedidos,driver)

func.finalizarPedido(driver)

func.pagarComPix(driver)

func.gerarQRCode(driver)

func.encerrar(driver)