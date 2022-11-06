from dataclasses import dataclass
from typing import Dict, Set, Type
from package.app.api.enum.RoleEnum import RoleEnum
from package.app.client.modules.registerjob.RegisterJobView import RegisterJobView
from package.app.client.modules.registervehicle.RegisterVehicleView import (
    RegisterVehicleView,
)
from package.app.client.modules.registeremployee.RegisterEmployeeView import (
    RegisterEmployeeView,
)
from package.app.template.IAppComponent import IAppComponent
from package.app.client.modules.schedulingemployee.EmployeeSchedulingView import EmployeeSchedulingView

@dataclass
class SidebarItem:
    component: Type[IAppComponent]
    roles: Set[RoleEnum]


sidebarItems: Dict[str, SidebarItem] = {
    "Cadastrar Serviço": SidebarItem(
        component=RegisterJobView,
        roles={RoleEnum.GERENTE},
    ),
    "Cadastrar Veículos": SidebarItem(
        component=RegisterVehicleView,
        roles={RoleEnum.GERENTE},
    ),
    "Cadastrar Funcionário": SidebarItem(
        component=RegisterEmployeeView,
        roles={RoleEnum.GERENTE},
    ),
    "Tela Teste Funcionário": SidebarItem(
        component=EmployeeSchedulingView,
        roles={RoleEnum.FUNCIONARIO},
    ),
}
