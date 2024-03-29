from package.app.client.modules.registeremployee.RegisterEmployeeComponent import (
    RegisterEmployeeComponent,
)
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig
from package.app.client.gui.box.Box import Box


class RegisterEmployeeView(metaclass=Singleton):
    def __init__(self):
        self.__component = RegisterEmployeeComponent()
        self.__usernameFieldInput: Gtk.Widget
        self.__fullnameFieldInput: Gtk.Widget
        self.__passwordFieldInput: Gtk.Widget
        self.__salaryFieldInput: Gtk.Widget
        self.__jobLimitFieldInput: Gtk.Widget

    def get(self) -> Gtk.Box:
        mainBox = Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label()
        label.set_markup(toBig("Cadastrar Funcionário"))
        label.set_margin_bottom(30)
        mainBox.pack_start(label, False, False, 0)

        usernameFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        usernameFieldLabel = Gtk.Label()
        usernameFieldInput = Gtk.Entry()
        usernameFieldLabel.set_text("Nome de Usuário *")
        usernameFieldInput.set_margin_top(5)
        usernameFieldInput.set_margin_right(5)
        usernameFieldInput.set_margin_bottom(5)
        usernameFieldInput.set_margin_left(5)
        usernameFieldBox.pack_default(usernameFieldLabel)
        usernameFieldBox.pack_default(usernameFieldInput)

        fullnameFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        fullnameFieldLabel = Gtk.Label()
        fullnameFieldInput = Gtk.Entry()
        fullnameFieldLabel.set_text("Nome Completo *")
        fullnameFieldInput.set_margin_top(5)
        fullnameFieldInput.set_margin_right(5)
        fullnameFieldInput.set_margin_bottom(5)
        fullnameFieldInput.set_margin_left(5)
        fullnameFieldBox.pack_default(fullnameFieldLabel)
        fullnameFieldBox.pack_default(fullnameFieldInput)

        passwordFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        passwordFieldLabel = Gtk.Label()
        passwordFieldInput = Gtk.Entry()
        passwordFieldInput.set_visibility(False)
        passwordFieldLabel.set_text("Senha Funcionário *")
        passwordFieldInput.set_margin_top(5)
        passwordFieldInput.set_margin_right(5)
        passwordFieldInput.set_margin_bottom(5)
        passwordFieldInput.set_margin_left(5)
        passwordFieldBox.pack_default(passwordFieldLabel)
        passwordFieldBox.pack_default(passwordFieldInput)

        salaryFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        salaryFieldLabel = Gtk.Label()
        salaryFieldInput = Gtk.Entry()
        salaryFieldLabel.set_text("Salário Funcionário *")
        salaryFieldInput.set_margin_top(5)
        salaryFieldInput.set_margin_right(5)
        salaryFieldInput.set_margin_bottom(5)
        salaryFieldInput.set_margin_left(5)
        salaryFieldBox.pack_default(salaryFieldLabel)
        salaryFieldBox.pack_default(salaryFieldInput)

        jobLimitFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        jobLimitFieldLabel = Gtk.Label()
        jobLimitFieldInput = Gtk.Entry()
        jobLimitFieldLabel.set_text("Limite de Serviços *")
        jobLimitFieldInput.set_margin_top(5)
        jobLimitFieldInput.set_margin_right(5)
        jobLimitFieldInput.set_margin_bottom(5)
        jobLimitFieldInput.set_margin_left(5)
        jobLimitFieldBox.pack_default(jobLimitFieldLabel)
        jobLimitFieldBox.pack_default(jobLimitFieldInput)

        confirmButton = Gtk.Button(label="Cadastrar")
        confirmButton.set_margin_top(30)
        confirmButton.connect("clicked", self.__onConfirm)

        self.__usernameFieldInput = usernameFieldInput
        self.__fullnameFieldInput = fullnameFieldInput
        self.__passwordFieldInput = passwordFieldInput
        self.__salaryFieldInput = salaryFieldInput
        self.__jobLimitFieldInput = jobLimitFieldInput

        mainBox.pack_start(usernameFieldBox, False, False, 0)
        mainBox.pack_start(fullnameFieldBox, False, False, 0)
        mainBox.pack_start(passwordFieldBox, False, False, 0)
        mainBox.pack_start(salaryFieldBox, False, False, 0)
        mainBox.pack_start(jobLimitFieldBox, False, False, 0)
        mainBox.pack_start(confirmButton, False, False, 0)

        return mainBox

    def __onConfirm(self, _: Gtk.Widget):
        self.__component.getState().addReference("username", self.__usernameFieldInput)
        self.__component.getState().addReference("fullname", self.__fullnameFieldInput)
        self.__component.getState().addReference("password", self.__passwordFieldInput)
        self.__component.getState().addReference("salary", self.__salaryFieldInput)
        self.__component.getState().addReference("limit", self.__jobLimitFieldInput)
        self.__component.requestRegisterEmployee()
