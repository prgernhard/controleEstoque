import datetime

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


from app.models import Produto, Item, Balcao, Safra, Produtos,Servicos



def convert_date(data):
    # replace = data.replace('/', '-')
    date = datetime.datetime.strptime(data, '%d/%m/%Y')
    new_d = datetime.datetime.strftime(date, '%Y-%m-%d')
    return new_d


@login_required(login_url='/admin/login/')
def home(request):
    user = getattr(request, 'user', None)
    itens = Item.objects.all()
    return render(request, 'list.html', {'user':user, 'itens': itens})

@login_required(login_url='/admin/login/')
def lst_safra(request):
    user = getattr(request, 'user', None)
    itens_safra = Safra.objects.all()
    return render(request, 'lst_safra.html', {'user':user, 'itens_safra': itens_safra})

@login_required(login_url='/admin/login/')
def lst_servicos(request):
    user = getattr(request, 'user', None)
    itens_servicos = Servicos.objects.all()
    return render(request, 'lst_servicos.html', {'user':user, 'itens_servicos': itens_servicos})

@login_required(login_url='/admin/login/')
def lst_produtos(request):
    user = getattr(request, 'user', None)
    itens_produtos = Produtos.objects.all()
    return render(request, 'lst_produtos.html', {'user':user, 'itens_produtos': itens_produtos})

@login_required(login_url='/admin/login/')
def add_product(request):
    user = getattr(request, 'user', None)
    if request.method == 'GET':
        return render(request, 'add_produto.html', {'user':user, 'balcoes': Balcao.objects.all()})
    else:
        try:
            produto = Produto(titulo=request.POST['titulo'], sku=request.POST['sku'])
            produto.save()
            item = Item.objects.create(produto=produto, quantidade=request.POST['qtd'],
                                       balcao=Balcao.objects.get(id=request.POST['balcao']))
            item.save()
            messages.success(request, "Produto adicionado com sucesso")
        except:
            messages.error(request, "Houve algum erro")
            return redirect('/add-product')
        return redirect('/')


@login_required(login_url='/admin/login/')
def remove_product(request, id):
    try:
        item = Item.objects.get(id=id)
        produto = item.produto
        produto.delete()
        item.delete()
        messages.success(request, "Produto deletado com sucesso")
        return redirect('/')
    except Item.DoesNotExist:
        messages.error(request, "Houve algum erro")
        return redirect('/')

@login_required(login_url='/admin/login/')
def remove_safra(request, id):
    try:
        safra = Safra.objects.get(id=id)
        safra.delete()
        messages.success(request, "Safra deletado com sucesso")
        return redirect('/lst-safra')
    except Item.DoesNotExist:
        messages.error(request, "Houve algum erro")
        return redirect('/')

@login_required(login_url='/admin/login/')
def remove_servicos(request, id):
    try:
        servicos= Servicos.objects.get(id=id)
        servicos.delete()
        messages.success(request, "Servico deletado com sucesso")
        return redirect('/lst-servicos')
    except Item.DoesNotExist:
        messages.error(request, "Houve algum erro")
        return redirect('/')

@login_required(login_url='/admin/login/')
def remove_produtos(request, id):
    try:
        produtos = Produtos.objects.get(id=id)
        produtos.delete()
        messages.success(request, "Item Produtos deletado com sucesso")
        return redirect('/lst-produtos')
    except Item.DoesNotExist:
        messages.error(request, "Houve algum erro")
        return redirect('/')

def edit_safra(request, id):
    user = getattr(request, 'user', None)
    if request.method == 'GET':
        return render(request, 'edit_safra.html', {'user':user, 'safra': Safra.objects.get(id=id)})
    else:
        try:
            safra = Safra.objects.get(id=id)
            safra.nome = request.POST['nome']
            safra.codigo = request.POST['codigo']
            safra.dtinicio = convert_date(request.POST['dtinicio'])
            safra.dtfim = convert_date(request.POST['dtfim'])
            safra.save()
            messages.success(request, "Safra alterada com sucesso")
        except:
            messages.error(request, "Houve algum erro")
            return redirect('/edit-safra/' + id)
        return redirect('/lst-safra')



def edit_servicos(request, id):
    user = getattr(request, 'user', None)
    if request.method == 'GET':
        return render(request, 'edit_servicos.html', {'user':user, 'servicos': Servicos.objects.get(id=id)})
    else:
        try:
            servicos          = Servicos.objects.get(id=id)
            servicos.nome     = request.POST['nome']
            servicos.dtinicio = convert_date(request.POST['dtinicio'])
            servicos.dtfim    = convert_date(request.POST['dtfim'])
            servicos.produto_id    = request.POST['produto_id']
            servicos.qtdade   = request.POST['qtdade']
            servicos.valor    = request.POST['valor']
            servicos.save()
            messages.success(request, "Servico alterado com sucesso")
        except:
            messages.error(request, "Houve algum erro")
            return redirect('/edit-servicos/' + id)
        return redirect('/lst-servicos')

def edit_produtos(request, id):
    user = getattr(request, 'user', None)
    if request.method == 'GET':
        return render(request, 'edit_produtos.html', {'user':user, 'produtos': Produtos.objects.get(id=id)})
    else:
        try:
            produtos = Produtos.objects.get(id=id)
            produtos.nome = request.POST['nome']

            produtos.save()
            messages.success(request, "Item Produtos editado com sucesso")
        except:
            messages.error(request, "Houve algum erro")
            return redirect('/edit-produtos/' + id)
        return redirect('/lst-produtos')


@login_required(login_url='/admin/login/')
def add_safra(request):
    user = getattr(request, 'user', None)
    if request.method == 'GET':
        return render(request, 'add_safra.html', {'user':user, 'balcoes': Balcao.objects.all()})
    else:
        try:
            safra = Safra(codigo=request.POST['codigo'], nome=request.POST['nome'],
                      dtinicio=request.POST['dtinicio'], dtfim=request.POST['dtfim'])
            safra.save()
            messages.success(request, "Safra adicionado com sucesso")
        except:
            messages.error(request, "Houve algum erro")
            return redirect('/add-safra')
        return redirect('/lst-safra')

@login_required(login_url='/admin/login/')
def add_servicos(request):
    user = getattr(request, 'user', None)
    if request.method == 'GET':
        return render(request, 'add_servicos.html', {'user':user, 'balcoes': Balcao.objects.all()})
    else:
        try:
            servicos = Servicos(nome=request.POST['nome'],produto_id=request.POST['produto_id'],
                       dtinicio=request.POST['dtinicio'], dtfim=request.POST['dtfim'],
                       qtdade=request.POST['qtdade'],valor=request.POST['valor'],)
            servicos.save()
            messages.success(request, "Servico adicionado com sucesso")
        except:
            messages.error(request, "Houve algum erro")
            return redirect('/add-servicos')
        return redirect('/lst-servicos')

@login_required(login_url='/admin/login/')
def add_produtos(request):
    user = getattr(request, 'user', None)
    if request.method == 'GET':
        return render(request, 'add_produtos.html', {'user':user, 'balcoes': Balcao.objects.all()})
    else:
        try:
            produtos = Produtos(nome=request.POST['nome'])
            produtos.save()
            messages.success(request, "Item Produtos adicionado com sucesso")
        except:
            messages.error(request, "Houve algum erro")
            return redirect('/add-safra')
        return redirect('/lst-safra')
@login_required(login_url='/admin/login/')
def log_out(request):
    logout(request)
    return redirect('/')
