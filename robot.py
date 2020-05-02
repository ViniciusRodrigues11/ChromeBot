# Importe as bibliotecas | Import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Defina seu driver (é com ele que você vai chamar as funções para digitar, click e navegação.)
#Define your driver (it is with it that you will call the functions to type, click and navigate.)
driver = webdriver.Chrome()

# Aqui você direciona pra qual URL o bot deve ir
# Here you direct to which URL the bot should go
driver.get("https://google.com.br")

# Vamos digitar na barra de pesquisa do Google agora, para isso você
# precisa identificar o elemento da página, pode ser pela classe(css)
# pela id do elemento ou pelo xpath. No read.me eu explico como obter o xpath

#Let's type in the Google search bar now, for that you 
#need to identify the page element, it can be by class (css)
#by the element id or xpath. In read.me I explain how to get xpath

elemento = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

# Agora o 'elemento' contém o valor da barra de pesquisa do Google, então vamos digitar nele com o comando send_keys
# Now the 'element' contains the value of the Google search bar, so let's type it in with the command send_keys

elemento.send_keys('Youtube', Keys.ENTER) 
#Keys.Enter simula a tecla Enter do teclado | # Keys.Enter simulates the Enter key on the keyboard


# -------------------------------------------------------------------------------------------------------------------

#Pronto, você aprendeu a usar a navegação basica com Selenium. Parabéns!
#Ready, you learned how to use basic navigation with Selenium. Congratulations!