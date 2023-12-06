# case_techway


Atualizado email na linha 15 de contato.html
<i class="far fa-envelope mr-2"></i>contato@contato.com.br

<i class="far fa-envelope mr-2"></i>Email: contato@jjinvestimentos.com.br		
Atualizado número de whatsapp na linha 18 de contato.html
<i class="fab fa-whatsapp mr-2"></i>(41) 98433-2211
<i class="fab fa-whatsapp mr-2"></i>+1 (25) 2680 4187
Atualizado número de telefone na linha 21 de contato.html
<i class="fas fa-phone mr-2"></i>(41) 3232-2323


<i class="fas fa-phone mr-2"></i>Telefone: +55 (41) 3223 2112

Alterado linha 4,5,6 e7 do footer.html

<li class="nav-item"><a href="/" class="nav-link px-2 text-body-secondary">Home</a></li>
            <li class="nav-item"><a href="#FIXME" class="nav-link px-2 text-body-secondary">Nossos Serviços</a></li>
            <li class="nav-item"><a href="#FIXME" class="nav-link px-2 text-body-secondary">Contato</a></li>
            <li class="nav-item"><a href="#FIXME" class="nav-link px-2 text-body-secondary">Voltar ao topo</a></li>

Por essas abaixo corrigidas

            <li class="nav-item"><a href="/home" class="nav-link px-2 text-body-secondary">Home</a></li>
            <li class="nav-item"><a href="/services" class="nav-link px-2 text-body-secondary">Nossos Serviços</a></li>
            <li class="nav-item"><a href="/contato" class="nav-link px-2 text-body-secondary">Contato</a></li>
            <li class="nav-item"><a href="#" class="nav-link px-2 text-body-secondary">Voltar ao topo</a></li>
Incluido imagem na linha 7 do header.html
<a class="navbar-brand" href="/"><img src="img/logo.png" alt="Logo"
 <a class="navbar-brand" href="/"><img src="{% static 'page_app/img/logo.png' %}" alt="Logo"



Incluído a linha 15,16 e 17 na página header.html
<li class="nav-item">
 <a class="nav-link active" aria-current="page" href="/home">Home</a>
 </li>
Colocado os links no modo ativo na linha 16 e 22
<a class="nav-link active" href="/contato">Contato</a>
Alterado a imagem na linha 22 da página home.html
<img src="page_app/img/imagem_2.jpg" alt="Imagem da empresa"
            <img src="{% static 'page_app/img/imagem_2.jpg' %}" alt="Imagem da empresa"
Alterado a imagem na linha 39 da página home.html
<img src="page_app/img/imagem_3.jpg" alt="Imagem da empresa"
            <img src="{% static 'page_app/img/imagem_3.jpg' %}" alt="Imagem da empresa"
Alterado a imagem na linha 55 da página home.html
<img src="page_app/img/imagem_1.jpg" alt="Imagem da empresa"
            <img src="{% static 'page_app/img/imagem_1.jpg' %}" alt="Imagem da empresa"
Alterado a imagem na linha 4 da página welcome.html
<img src="img/JJ_investimento.png" alt="imagem grande logo" class="rounded-circle mb-3"
<img src="{% static 'page_app/img/JJ_ivestimento.png' %}" alt="imagem grande logo" class="rounded-circle mb-3"
 Na urls.py incluído na linha 2 e 9, 10,11 e 12 algumas urls faltantes
Linha 2 
from page_app.views import index, contato
from page_app.views import index, contato, footer, header, home, services
linha 9,10,11 e 12
path('footer/', footer),
path('header/', header),
path('home/', home), 
path('services/', services),
na views.py alterado e incluído alguns atalhos faltantes.
Na linha 4 
def index (request):
def home (request):

return render(request, "page_app/partial/contato.html")

def welcome (request):
    return render(request, "page_app/partial/welcome.html")

def footer (request):
    return render(request, "page_app/partial/footer.html")

def header (request):
    return render(request, "page_app/partial/header.html")

def services (request):
    return render(request, "page_app/partial/services.html")

def index (request):
    return render(request,"page_app/global/index.html")

