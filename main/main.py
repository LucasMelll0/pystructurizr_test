from pystructurizr.dsl import Workspace

with Workspace() as workspace:
    with workspace.Model(name='Teste') as model:
        user = model.Person("Cliente")
        user.description = "Pessoa que usa o aplicativo Bizucash, que possui uma conta Bizucash."
        with model.SoftwareSystem("Bizucash") as system:
            mobileApp = system.Container("Aplicativo Móvel",)
            api = system.Container("Api")
            mobileApp.technology = "Flutter"
            mobileApp.description = "Oferece funcionalidades de ver saldo da conta bizucash, e gerar código de resgate"
            api.technology = "C#"
            api.description = "Faz o intermédio entre as aplicações e o banco de dados."

    user.uses(mobileApp, "Vê balanço da conta e gera código de resgate")
    mobileApp.uses(api, "Uses")

workspace.ContainerView(
    system,
    "Sistema",
    "descrição do sistema"
)
